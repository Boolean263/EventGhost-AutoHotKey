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

## Warnings, Problems, and Workarounds

Don't call `ExitApp` from your script, or things will break.

## Author and Acknowledgements

This plugin was created by **Krafty**. The closest it has to an official home page is [this thread in the EventGhost forums](http://www.eventghost.net/forum/viewtopic.php?f=9&t=5978) where they introduced it to the world.

The plugin includes and uses a version of [pyahk](https://bitbucket.org/kitsu/pyahk/src/default/), a python OOP wrapper around AutoHotkey.

pyahk wraps a DLL that includes the AutoHotkey core. This plugin includes the same DLL that Krafty had in their original zip offering. If you prefer to build it from scratch or find a newer version, [this site](https://hotkeyit.github.io/v2/) appears to be the official home page for this offering.

Krafty, if you have a proper site up for this now, reach out to me. I'll either update this repo or remove it and point people your way.
