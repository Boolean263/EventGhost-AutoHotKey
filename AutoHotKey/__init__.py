# -*- coding: utf-8 -*-
#
# This file is a plugin for EventGhost.
# Copyright © 2005-2016 EventGhost Project <http://www.eventghost.org/>
#
# EventGhost is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 2 of the License, or (at your option)
# any later version.
#
# EventGhost is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along
# with EventGhost. If not, see <http://www.gnu.org/licenses/>.

"""<md>
Plugin to allow you to call [AutoHotkey](https://www.autohotkey.com/)
scripts from EventGhost.

This plugin is currently very simplistic. It only provides an action to run
an AHK script string.

Don't call `ExitApp` in your script or things will break.

Requires the AutoHotkey DLL available [here](https://hotkeyit.github.io/v2/).
"""

import eg

from os.path import abspath, join, dirname
import ctypes
from eg.WinApi.Dynamic import (
    CDLL, FreeLibrary,
)

eg.RegisterPlugin(
    name = "AutoHotKey",
    author = (
        "Boolean263",
    ),
    version = "0.0.1",
    url = 'https://github.com/Boolean263/EventGhost-AutoHotKey',
    guid = "{79a26d8f-c41f-45a0-aa44-401dacdc85a3}",
    description = __doc__,
    icon = (
        "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAACQ1BMVEXQKZ8AIQEAN"
        "gIAPgEARQEASwMATAAATAEAUwAAVQIAVgICWgIKVwoMWQwAXwIMWwsAYAIEYAQFYA"
        "QNXg4AaAEGZgYHZgcAaQEAagEJbAgKbQkAcgAAcwAAcwEMcgsNcwwDeAMDegMDewM"
        "DfAMGfAYPeQ4Qeg8RfBASfREHgwYHhAcHhQcKhApHbEYIhQdIbkcVghYWgxcWhBgX"
        "hBgYhBkLiwoahRschR0LjAoLjQsMjQsehh8OjQ4MjgshhiEjhyMmiCUniScPkw4Pl"
        "A4qiikSlRIQlg8siysQlw8vjC4wjC8zjTEzjTITnBIWmxU4jjYTnRI5jzcTnxIUnx"
        "MUnxQZnxgmmyYWpBYXpRZHk0UXphZIk0YYpxcvni8YqBcYqBgcqRsarBkbrRobrho"
        "crxserx4csBsfsR8dsh0esh1emVwesx0esx4fsx4fsx9fml0dtR8gtCAgtCEetiAh"
        "tSIhtSMitSMitSQitiQjtiQjtiUityNOpk4ltycmtycntygntykotyksuSwsuS0tu"
        "S4uuS4vuS4yuzI0uzM0uzRBtkFQsVA3vDY5vTg6vTl4p3g+vz0/vz5AwD9EwUNFwU"
        "RSvFJGwkVIwkdLw0lMw0pNw0t+tH6DtINrwmtdyVtfyV10xHRny2ZrzGmBx4GzurO"
        "qyaqL14mizqKsy6yszKytz628zbyq1aqZ3Jip1qmx1LGb3Zqi26HH0se02rTS1dLL"
        "5cvU5NTo6Ojn6+fm8ub29vb39/f6+/r4/Pj6/Pr8/vz////NPAtZAAAAAXRSTlMAQ"
        "ObYZgAAAAFiS0dEAIgFHUgAAAAJcEhZcwAAHtkAAB7ZAa73TPwAAAEbSURBVBjTAR"
        "AB7/4AAC9vW1FMSkdBPzs2MzETAAAtsbCimpSSjomFgXp2cmcPAGqtpp+Xko6IhYF"
        "wdnJubCgAWaGemL2niISAnb+LbmxmJgBPmZaRwKiEf3muwF1rZl8fAEuTkYzAqH95"
        "dazAUmReVBoASZCNhsCpeXRys8BVXFNIFgBEjYd7wLa1ub7AwE5TRj0SAECHg3PAw"
        "MC3tLi7RUY6LgsAPoJ+lcCrVmBjr7o8OSsjCAA3fXigwJxpY1qqvCwqIx0GADR3dK"
        "PAm2NYUKXAJCMcGAQAMnRxirJ8WFBDj6QgGxcQAwAwcW1oYlhNQzgpIhsXDgoCAA1"
        "laGFXTUI1KSEbFA4JBQEAAAwnJR4ZFRELCAcEAwIBAMGmYsJ/6n6hAAAAAElFTkSu"
        "QmCC"
    ),
)

class AutoHotKey(eg.PluginBase):
    """\
    Documentation for this class.
    """

    _default_dll = abspath(join(dirname(__file__), "AutoHotkey.dll"))

    def __init__(self):
        self.AddEvents()
        self.AddAction(AhkScript)

    def Configure(self, dll=""):
        if not dll:
            dll = self._default_dll
        panel = eg.ConfigPanel()
        dllPathCtrl = panel.FileBrowseButton(dll)

        sizer = wx.GridBagSizer(5, 5)
        sizer.AddMany([
            (panel.StaticText("Path to AutoHotkey.dll"), (0, 0), (1, 1), wx.ALIGN_CENTER_VERTICAL),
            (dllPathCtrl, (0, 1), (1, 1), wx.EXPAND),
        ])
        sizer.AddGrowableCol(1)
        panel.sizer.Add(sizer, 1, wx.EXPAND)
        while panel.Affirmed():
            panel.SetResult(dllPathCtrl.GetValue() or self._default_dll)

    def __start__(self, dll=None):
        if not dll:
            dll = self._default_dll
        self.dll = CDLL(dll)
        self.handle = self.dll.ahktextdll("","","")

    def __stop__(self):
        self.dll.ahkterminate()
        FreeLibrary(self.dll._handle)
        self.handle = None
        self.dll = None

    def runScript(self, scriptStr="", interp=False):
        scriptStr = str(scriptStr) # The DLL doesn't like unicode?
        if interp:
            scriptStr = eg.ParseString(scriptStr)
        self.dll.ahkExec(scriptStr)

class AhkScript(eg.ActionBase):
    name = "Run AutoHotKey Script"
    description = "Run the text as a AutoHotKey script."

    def __call__(self, scriptStr, interp=False):
        self.plugin.runScript(scriptStr, interp)

    def Configure(self,
            scriptStr="",
            interp=False,
    ):
        panel = eg.ConfigPanel()
        editTextCtrl = panel.TextCtrl("\n\n\n", style=wx.TE_MULTILINE)
        height = editTextCtrl.GetBestSize()[1]
        editTextCtrl.ChangeValue(scriptStr or "")
        editTextCtrl.SetMinSize((-1, height))
        interpCtrl = panel.CheckBox(interp, "Parse script for EventGhost variables")

        sizer = wx.GridBagSizer(5, 5)
        expand = wx.EXPAND
        align = wx.ALIGN_CENTER_VERTICAL
        sizer.AddMany([
            (panel.StaticText("Script"), (0, 0), (1, 1), align),
            (editTextCtrl, (0, 1), (1, 1), expand),
            (interpCtrl, (1, 1), (1, 1), expand),
        ])
        sizer.AddGrowableCol(1)
        panel.sizer.Add(sizer, 1, expand)

        while panel.Affirmed():
            panel.SetResult(
                    editTextCtrl.GetValue() or "",
                    interpCtrl.GetValue()
            )



#
# Editor modelines  -  https://www.wireshark.org/tools/modelines.html
#
# Local variables:
# c-basic-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# coding: utf-8
# End:
#
# vi: set shiftwidth=4 tabstop=4 expandtab fileencoding=utf-8:
# :indentSize=4:tabSize=4:noTabs=true:coding=utf-8:
#
