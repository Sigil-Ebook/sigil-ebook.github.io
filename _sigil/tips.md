---
title: "Sigil Tips and Troubleshooting"
permalink: /sigil/tips/
toc: true
toc_sticky: true
---


## General Platform-agnostic stuff

### Yes Book View is really gone

We told everybody we were going to do it. It's been discussed forever in the Sigil support forums at [Mobileread](https://www.mobileread.com/forums/forumdisplay.php?f=203), it was in the [0.9.14 release notes](https://github.com/Sigil-Ebook/Sigil/releases/tag/0.9.14) (the last version to support WYSIWYG editing), in the 0.9.15 beta version's release notes, and in this very wiki. For those who don't think they'll be able to live without it, we created a new external application called PageEdit that can do many of the things that Book View could accomplish. But instead of being a part of Sigil, it's an external application that can be launched via Sigil's Open With feature, or by assigning it to Sigil's new "External HTML Editor" button. Check out the PageEdit repo for its [latest releases](https://github.com/Sigil-Ebook/PageEdit/releases).

The decision to remove Book View (WYSIWYG editing) from Sigil is final. If PageEdit does not suit your needs for WYSIWYG editing, you're more than welcome to continue using any older version of Sigil that still works the way you prefer. None of the previous downloads will be removed. So we've not taken anything from anyone, we've simply moved on.

Please do not create new issues in Sigil's issue database bemoaning the loss of Book View/WYSIWYG. Those discussions have been over since June of 2019. All new issues trying to extend that discussion will be closed with a link to this Wiki article. (last updated on Feb 15, 2021)

### Qt5.12.4 bug that affects Sigil

There's a [particularly nasty bug](https://bugreports.qt.io/browse/QTBUG-76588) in the newly released Qt5.12.4 (and 5.13.1) that will affect Sigil (and probably other projects as well) across all 3 platforms. Floating dialogs that are closed with the title-bar 'X' button may crash the next time that particular dialog is re-opened. The new floating Inspector Widget in Sigil 0.9.15+ is a prime candidate. The official Sigil installer for Windows and MacOS won't be using these versions so you should be OK unless you build your own Sigil on either of those platforms. If you do, don't use Qt5.12.4 or Qt5.13.1. If your Linux distro has updated to either of these versions of Qt, you may may experience some crashing. We apologize for this. A questionable "fix" that wasn't well tested should have never made into a Qt LTS version in the first place!

### Sigil moving to QtWebEngine

Sigil 0.9.14 will mark the last version that uses QtWebKit, and will be the last version to support editing in BookView.

Soon after our upcoming Sigil 0.9.14 release we will release the QtWebEngine version of Sigil as a beta along side a beta of a new program called PageEdit that will do much of what BookView did via Sigil's "Open-With" feature but will run on QtWebEngine.

The official 32-bit Windows installer for Sigil will also be on the chopping block very, very soon (but will be included for the Sigil 0.9.14 release). We're not going to be removing the ability for Sigil to be _built_ as a 32-bit application on Windows, but we won't be providing official 32-bit Windows installers after 0.9.14 (or maybe the next version after that) any more.

For Linux packagers, the current "master" branch of Sigil will be moved to a "webkit" branch while the development branch "engine" will become the new master. This will be taking place sometime after the Sigil 0.9.14 release. Please adjust accordingly.

### If you're here because...

Sigil v0.9.13 (or higher) is crashing, won't run correctly, or won't start _at all_, please see the below message. In short, your preference INI files from Sigil 0.9.11/12 are not compatible with Sigil 0.9.13+. If you have backups of your preferences from Sigil v0.9.10 or earlier, you can restore those. Otherwise ... you need to delete Sigil's preference INI files, let Sigil recreate default ones when it next starts, and then reconfigure your preferences from Sigil's normal interface. We apologize for any inconvenience.

For those who don't know where their preference files are; you can always get to them by clicking the "Open Preferences Location" button at the bottom of Sigil's Preferences dialog (Edit->Preferences). If you can't launch Sigil, however you can find them at:

[Windows Directions](#locating-your-sigil-preferences-folder-on-windows)<br/>
[Linux Directions](#opening-sigils-preference-folder-on-linux)

The four INI files are what needs to be restored from Sigil-0.9.10 (or earlier) backups, or deleted if you don't have backups. Any temporary lock files corresponding to those INI files should deleted regardless. You can also safely restore your plugins, plugin_prefs (and any dictionary) folders if you don't want to reinstall/reconfigure them all. It's only the INI files that are at issue here.

### Versions 0.9.11 and 0.9.12 of Sigil are very buggy.

Please don't use them. If you have good backups of your Sigil 0.9.10 (or earlier) preferences, roll back to Sigil 0.9.10 and restore your backed up preferences. If you don't have backups of your Sigil 0.9.10 (or earlier) preferences, roll back to Sigil 0.9.10 anyway and recreate your preferences as best you can from within Sigil's UI. Those preferences will be usable with Sigil v0.9.13 (and higher) when it is released.

### Other Platform-agnostic Tips

When you fire up Sigil for the very first time:

- navigate to the new General Preferences and select the default
epub version you plan to work with (epub 2 or epub3) so that new
empty ebooks start with the correct code.
- if you plan to work with epub3 epubs, you should change your
PreserveEntities setting to use ONLY NUMERIC entities.
For example use &amp;\#160; for non-breaking spaces and etc.
- We strongly recommend enabling Mend On Open in your settings
for best performance with Sigil.


## Mac Tips and Troubleshooting

The latest version of Sigil requires macOS 10.12 or higher. macOS upgrades are available for free directly from Apple.


### Need to Install ActiveState's Active TCL

Per the recommendation of www.python.org (see <https://www.python.org/download/mac/tcltk/>), due to bugs and the age of Apple's internal Tcl library, you should also download and install ActiveState's ActiveTcl Community Edition. To get the latest bug fixes, Sigil-0.x.x's embedded Python has been linked with the very latest version of Tcl 8.6.x.x

We may *not* redistribute this Package with Sigil due to ActiveState's binary non-redistribution policy.

So please, if you have not already done so download and install this version of ActiveState's Active Tcl Community Edition, until we get a chance to do our own build of Tcl from source for future releases. ActiveState is a primary contributor to www.python.org and a respected and trusted source for python and tcl/tk related binaries on both Windows and Mac.

See: <http://www.activestate.com/activetcl/downloads>
Version: 8.6.4.1 or later 8.6.X release


### New Release File Format starting with Sigil-0.9.18

For macOS we have moved to a new release file format.  Instead of .dmg files, the releases will use "xz" compression of a standard BSD tar archive of the application to create .txz files (aka .tar.xz files).

The reason for this change is because xz compression is just that much better than the zlib -9 compression used in dmg.  This means much smaller and much faster downloads and more space for backups, and other things.

For example, here are the file sizes of the current release files in both formats:

     87312287  3 Sep 11:32 PageEdit-0.9.5-Mac-Package.dmg

     56781604  3 Sep 11:32 PageEdit.app-0.9.5-Mac.txz

for a savings of over 30 meg, and

     127709658  3 Sep 11:22 Sigil-0.9.18-Mac-Package.dmg

     78071020  3 Sep 11:22 Sigil.app-0.9.18-Mac.txz

for a savings of about 50 meg.

So combined for the two downloads (PageEdit and Sigil), people are saving over 80 megs on downloads per release.


### How to uncompress .tar.xz, or .txz files

If you are on macOS 10.15 Catalina or newer, simply double-click the .txz file and macOS's built-in Archive Utility will automatically uncompress the file and leave you with a new Sigil.app, which you can drag to your /Applications folder (or wherever you want). 

If you are on an older macOS, the easiest path is to install a good gui decompressor program that actually knows how to handle .xz files (and almost all other types of archive files).  One the oldest and best out there is called "The Unarchiver", which is free from the macOS App store:

[The Unarchiver](https://apps.apple.com/us/app/the-unarchiver/id425424353?mt=12){: .btn .btn--success}

Alternatively, modern macOS versions can do the decompression with nothing additional needed via the Terminal.app and the command line as follows:
   
1. move the Sigil.app-0.9.18-Mac.txz file to your Desktop
2. open Terminal.app, and type the following commands:

~~~
cd ~/Desktop
tar -xvf ./Sigil.app-0.9.18-Mac.txz
exit
~~~

A list of all of the pieces that make up Sigil should appear as they are unpacked.  Once this completes and you close Terminal.app, you should see the new "Sigil.app" on your Desktop ready to be dragged to your /Applications folder (or wherever you want).


## Windows Tips

The latest version of Sigil requires Windows 7 sp1 or higher.

If your current version of Sigil is 0.9.6 or earlier, it's recommended (but not required) that you uninstall that version before installing the newer version. Some compiled Python files have had their file extentions changed (as well as the change to Python 3.5, 3.7, and 3.8). As a result, there will be a lot of extraneous files left lying around if you just install the new over the old. It won't cause any functionality problems, but if disk space is at a premium, you may want to clean things up a bit. You can do this by uninstalling Sigil at any time (even after 0.9.10 is installed) and reinstalling. Doing so won't affect your any of your preferences, plugins, keyboard shortcuts, clips, saved searches, etc.


### Locating your Sigil Preferences Folder on Windows

You can open your Sigil preferences folder by clicking the "Open Preferences Location" button at the bottom of Sigil's Preferences dialog (Edit->Preferences). If you can't launch Sigil, however, Windows 7 and Windows 10 users should be able to open their Sigil's preference folder by entering %localappdata%\sigil-ebook\sigil in the Windows 7 Start->Run dialog (or type the same in the Windows 10 Cortana/search box and open the folder that appears in the results).


## Linux Users
There are currently no official binary releases available for Linux on the Sigil Release page. Please check with your favorite distro's software repositories to see if they have Sigil for installation via your OS's package management system. If not, there are build instructions for compiling Sigil yourself in the source archive's docs directory: https://github.com/Sigil-Ebook/Sigil/tree/master/docs.

### lxml 4.4.0
Avoid updating to lxml 4.4.0 until we work out some compatibility issues with our sigil_bs4 module. Downgrade to lxml 4.3.4 in the meantime.  **EDIT: this one has been fixed in the latest [github master branch](https://github.com/Sigil-Ebook/Sigil/commit/aa4f6549554fb99ad062ce501afe23c51530cbf5). That fix will be included in Sigil 0.9.17 (it can also be safely backported to earlier Sigil versions).**

### If You Notice HTML Entities Being Doubled In Your EPUB's HTML

There's a bug in libxml2-2.9.3 and 2.9.4(ish) that affects how QtWebKit renders html entities. Which means Sigil is affected on systems which use those versions. The problem was resolved in libxml2-2.9.5.

To quickly tell if your system is affected:

Type a visible html entity (like \&copy\;) into Sigil's Code View (epub2). If it appears twice in Sigil's Preview or Book View, then you have the buggy version of libxml2.

I've released a makeself Linux-only "updater" that installs a patched version of libxml2 into an existing Sigil installation to work around the issue.

**NOTE:** At no time will your system version of libxml2 be altered/affected by this update.

[Download the installer](https://github.com/Sigil-Ebook/sigil-libxml2-updater/releases) (make sure it's executable bit is set) and use:

`sudo ./sigil_libxml2_update.run`

to install.

You'll have the option to bail out if you get cold feet.

See the installer's [Github README](https://github.com/Sigil-Ebook/sigil-libxml2-updater) for more options/explanations.

### Crashes on KDE Desktops when reordering files in Sigil's Book Browser.

Reordering files (via drag and drop) in Sigil's Book Browser has been known to cause issues (including crashes) on distros that use the KDE desktop environment. It has been discussed in [Sigil's user forums on MobileRead](https://www.mobileread.com/forums/showthread.php?t=289977) and bug reports have been filed with [KDE](https://bugs.kde.org/show_bug.cgi?id=399989) and [Qt](https://bugreports.qt.io/browse/QTBUG-63546). It appears that [a fix is in the works](https://phabricator.kde.org/D16305) from the folks at KDE, but in the meantime, there is a workaround.

Just add the following line to Sigil's launch script (typically $$install_prefix$$/bin/sigil) somewhere near the beginning:

`XDG_CURRENT_DESKTOP=XFCE`

This will allow Sigil to bypass KDE's Qt platform integration plugin (which is where the issue seems to manifest).

### Opening Sigil's Preference Folder on Linux

You can open your Sigil preferences folder by clicking the "Open Preferences Location" button at the bottom of Sigil's Preferences dialog (Edit->Preferences). If you can't launch Sigil, however, the Sigil preferences folder can be found at ~/.local/share/sigil-ebook/sigil. You'll have to have configured your system file-browser to show hidden folders/files to be able to see the .local folder in your home directory.