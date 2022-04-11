---
title: Sigil Qt6 - Plugin PySide6 Migration
date: 2022-03-11T21:57:56Z
categories:
  - Blog
tags:
  - Sigil
  - Announcements
header:
  show_overlay_excerpt: false
  tagline: ""
  overlay_image: /assets/images/coding-1920.jpg
  overlay_filter: 0.5
---

You may or may not know that Sigil is planning to move from Qt5 to Qt6 in a near-future release. This will effect plugins that currently utilize PyQt5 for their GUI interfaces. Note that plugins that use tkinter, or don't use a GUI interface will be unaffected by this change.


__For all plugin devs whose plugins will be affected:__

For reasons that are not really up for debate, Sigil has chosen to move to PySide6 for its preferred Python wrapper to Qt in the bundled Python that comes with the Windows and macOS Sigil packages.

![Plugin Changes](/assets/images/changes.jpg)

In order to maintain compatibility with older versions of Sigil (Qt5/PyQt5) and newer versions of Sigil (Qt6/PySide6), I've come up with a compatibility module that can be included in your plugin to make things easier. If you don't update your plugin, you and your users will still have the option of using an external Python with PyQt5 installed for your plugin. No one will be left completely out in the cold. You can also use your own homegrown solution to remain compatible with Sigil-Qt5 and Sigil-Qt6. There are less differences than you would think between PyQt5 and PySide6. And where there are differences, I've coded some helper utilities in the plugin_utils module to facilitate things.

The [plugin_utils](https://github.com/dougmassay/sigil-plugin-utils/blob/main/plugin_utils.py) module can be found in my [personal github repository for it](https://github.com/dougmassay/sigil-plugin-utils).

I use the module extensively in my own [TagMechanic plugin](https://github.com/dougmassay/tagmechanic-sigil-plugin) (which has been updated to work with PyQt5 and PySide6), so feel free to use it as an example.

I've also made a [Sigil Qt Plugin template](https://github.com/dougmassay/sigil-qtplugin-template/releases/latest) that makes use of the plugin_utils module so that is another resource for plugin devs to modify their Gui Qt plugins. It's full of comments in the code to explain what is happening.

Our own EPUB3 reader plugins have also been updated. That code is available for your perusal.

And of course myself and Kevin will be able to offer advice to those plugin devs who may run into trouble accommodating the upcoming changes.

Checkout the [discussion thread about it](https://www.mobileread.com/forums/showthread.php?t=346162) at Mobileread to stay abreast of the situation.


