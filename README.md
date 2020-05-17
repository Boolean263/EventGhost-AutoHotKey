# EventGhost-AutoHotKey

This program is not very useful on its own. It's a plugin for [EventGhost](http://www.eventghost.net/).  EventGhost is an automation tool for MS Windows which listens for events -- whether user-triggered (like the press of a hotkey) or system events (such as the screensaver activating) -- and runs actions you specify. (It's like [Tasker](http://tasker.dinglisch.net/) for Android, or [Cuttlefish](https://launchpad.net/cuttlefish) for Ubuntu.)

## Description

**I am not the author of this plugin.** I had a nasty proto-plugin in this git space, but then I found that [someone else had already done it better](http://www.eventghost.net/forum/viewtopic.php?f=9&t=5978). They didn't have it in any sort of version control that I can see, so I'm hosting it here so people can find it.

This is a plugin which lets you integrate [AutoHotkey](https://www.autohotkey.com/) into EventGhost.

EventGhost and AutoHotkey are fairly similar on the surface; they both react to events and perform actions. I'm personally partial to EventGhost, because it reacts to more than just hotkeys, and uses Python for user scripting, rather than its own proprietary language like AHK does. But I recently wanted to do someething you'd think would be simple, and [which is simple in AHK](http://xahlee.info/mswin/autohotkey_toggle_maximize_window.html), but is a lot more complex (if possible at all) in EG.

## Installation

Install in the standard EventGhost plugin style. Everything you need is in the box.

## Usage

Here is the list of actions available:

* **AutoHotKey Command** - Runs a one-line ahk command.
* **AutoHotKey Script** - Runs user-entered ahk code.
* **AutoHotKey Files** - Runs an ahk file.
* **[AutoHotKey Message Box](http://www.autohotkey.com/docs/commands/MsgBox.htm)** - Creates an ahk message box. There are several different button styles and each button triggers an event.
* **[AutoHotKey SoundBeep](http://www.autohotkey.com/docs/commands/SoundBeep.htm)** - Emits a tone from the PC speaker.
* **[AutoHotKey Block Input](http://www.autohotkey.com/docs/commands/BlockInput.htm)** - Blocks user input. Freezes the mouse and ignores all keyboard input until the timeout is reached or "BlockInput Off" action is executed. Only works if Eventghost is ran as admin.
* **BlockInput Off** - Gives control back to the user after "Block Input" is executed.
* **[AutoHotKey Click Image](http://www.autohotkey.com/docs/commands/ImageSearch.htm)** - Searches the screen for an image provided by the user. If the image is found the user can choose to have it trigger an event with the coordinates in the payload and/or click the mouse at the coordinates. Window with image must be active.
* **[AutoHotKey Input Box](http://www.autohotkey.com/docs/commands/InputBox.htm)** - Creates an input box the prompts the user. The entered data is set to a variable.

If you want to use `eg.` variables in a script, wrap them in `#` characters, such as: `#eg.variable#`

## Warnings, Problems, and Workarounds

Don't call `ExitApp` from your script, or things will break.

## Author and Acknowledgements

This plugin was created by **Krafty**. The closest it has to an official home page is [this thread in the EventGhost forums](http://www.eventghost.net/forum/viewtopic.php?f=9&t=5978) where they introduced it to the world.

The plugin includes and uses a version of [pyahk](https://bitbucket.org/kitsu/pyahk/src/default/), a python OOP wrapper around AutoHotkey.

pyahk wraps a DLL that includes the AutoHotkey core. This plugin includes the same DLL that Krafty had in their original zip offering. If you prefer to build it from scratch or find a newer version, [this site](https://hotkeyit.github.io/v2/) appears to be the official home page for this offering.

Krafty, if you have a proper site up for this now, reach out to me. I'll either update this repo or remove it and point people your way.
