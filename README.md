# EventGhost-AutoHotKey

This program is not very useful on its own. It's a plugin for [EventGhost](http://www.eventghost.net/).  EventGhost is an automation tool for MS Windows which listens for events -- whether user-triggered (like the press of a hotkey) or system events (such as the screensaver activating) -- and runs actions you specify. (It's like [Tasker](http://tasker.dinglisch.net/) for Android, or [Cuttlefish](https://launchpad.net/cuttlefish) for Ubuntu.)

## Description

This is a very simplistic plugin which lets you run [AutoHotkey](https://www.autohotkey.com/) script text as an EventGhost action.

EventGhost and AutoHotkey are fairly similar on the surface; they both react to events and perform actions. I'm personally partial to EventGhost, because it reacts to more than just hotkeys, and uses Python for user scripting, rather than its own proprietary language like AHK does. But I recently wanted to do someething you'd think would be simple, and [which is simple in AHK](http://xahlee.info/mswin/autohotkey_toggle_maximize_window.html), but is a lot more complex (if possible at all) in EG.

## Disclaimer

I know very little about AHK. There are probably some things I do here which aren't recommended. I make no guarantees that this will do what you need it to do. (But I'll happily accept pull requests!)

## Installation

This plugin requires an AutoHotkey DLL in order to work. This doesn't seem to come with a standard installation of AutoHotkey, so you'll need to download it from [here](https://hotkeyit.github.io/v2/). (The one I use is the Win32w DLL.)

Apart from that, installation is in the standard EventGhost plugin style. When you add the plugin, it'll prompt you for the path of the DLL.

## Usage

There is currently a single action you can add to your EventGhost tree, called "Run AutoHotKey Script." Type or paste the script text into the Script text box, and optionally click Test to see if it does what you expect.

There's an option to parse the script for EventGhost variables. If you check this, any `{`/`}` characters you put in your script which *aren't* wrapping an EventGhost value must be doubled up.

## Warnings, Problems, and Workarounds

Don't call `ExitApp` from your script, or things will break.

*(Once I learn more about AHK, I may add checks for commands like that which may breeak things and remove them.)*

In some circumstances, attempts to use this plugin will cause a popup window to appear which just says "RegClass" in it. (A surefire way to make this happen is to disable and re-enable the plugin.) Once you see that, the plugin isn't going to work any more until you exit and restart EventGhost.

*(If anyone knows what's causing that and how I can prevent it, let me know.)*

## Other Resources

* [pyahk](https://bitbucket.org/kitsu/pyahk/src/default/), a python OOP wrapper around AutoHotkey. This plugin doesn't use it, but got some inspiration from it.
* [This simple AutoHotkey tutorial](http://xahlee.info/mswin/autohotkey.html) which is where I found the script I originally wanted to recreate in EventGhost.
* And of course, [the official AutoHotkey website](https://www.autohotkey.com/).

