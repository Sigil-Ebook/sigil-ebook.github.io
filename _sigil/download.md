---
title: "Download Sigil"
permalink: /sigil/download/
---

{% include remote_versions.html %}
[Latest Windows x64 download](https://github.com/Sigil-Ebook/Sigil/releases/download/{{ sigil_ver }}/Sigil-{{ sigil_ver }}-Windows-x64-Setup.exe){: .btn .btn--success}<br/>[Latest MacOS (Intel) download](https://github.com/Sigil-Ebook/Sigil/releases/download/{{ sigil_ver }}/Sigil.app-{{ sigil_ver }}-Mac-x86_64.txz){: .btn .btn--success}<br/>[Latest MacOS (Arm64) download](https://github.com/Sigil-Ebook/Sigil/releases/download/{{ sigil_ver }}/Sigil.app-{{ sigil_ver }}-Mac-arm64.txz){: .btn .btn--success}<br/>[Latest Linux AppImage Download](https://github.com/Sigil-Ebook/Sigil/releases/download/{{ sigil_ver }}/Sigil-{{ sigil_ver }}-x86_64.AppImage){: .btn .btn--success}

Past and present installers are always available under [releases](https://github.com/Sigil-Ebook/Sigil/releases) at the main code hosting location. The latest release will be on top. You can see what's changed between releases by looking at the [ChangeLog](https://github.com/Sigil-Ebook/Sigil/blob/master/ChangeLog.txt).

### Checksum verification
<div markdown="1">
All releases also have a CHECKSUM.sha256.txt file which includes sha256 check sums of the file posted. This will let you know if you have a bad download or if a build has been tampered with. Going forward release announcements will include the sha256 checksum of the checksum file itself so you can verify that it hasn't been tampered with either.
</div>
{: .notice--info}

### Sigil on Windows
<div markdown="1">
Sigil currently provides a Windows installer for x64 and will only work on Windows 10 (1809) or newer.

The latest Sigil versions are also typically available via the [winget (Windows 10+)](https://winstall.app/apps/Sigil-Ebook.Sigil), [Chocolatey (Windows 10+)](https://community.chocolatey.org/packages/Sigil), and [Npackd](https://npackd.appspot.com/p?q=sigil) Windows package managers within a week of our releases (often sooner). There are no "scary" Microsoft warnings about unknown publishers if you install Sigil via one of these package managers. Those Windows package managers download their unpatched Sigil installers directly from our release posts. So while I'm not officially endorsing the use of these package managers, I feel there's value (and no risk) in utilizing them to manage your Sigil installation/updates.
</div>
{: .notice--info}

### Sigil on Mac
<div markdown="1">
Sigil currently runs on macOS 11 Big Sur and newer. 

Whether a macOS version can run Sigil depends primarily on whether it is supported by the Qt libraries used to build Sigil. Currently, Sigil is built using Qt6.5.x, which requires macOS 11. Therefore Sigil requires macOS 11 or newer.

In addition, the macOS .app file (not the .txz) is signed before release. You can use the code sign command line tool to verify the application. Open a terminal and run:

~~~
codesign -dvvv Sigil.app
~~~

There will be a lot of output. Look for the following, which tells you that Kevin Hendricks, the project maintainer, built this binary: Authority=Developer ID Application: Kevin Hendricks (2SMCVQU3CJ)
</div>
{: .notice--info}

### Sigil on Linux
<div markdown="1">
Sigil **will** run on Linux. We try to maintain compatibility with Linux mainly because it's easy to with Sigil supporting both Mac and Windows and it uses a number of technologies that already support Linux. That said, there is currently no official Sigil binary package for Linux.

If you're looking to use Sigil on Linux, you can always build it from source. The docs directory in  [Sigil's Github repository](https://github.com/Sigil-Ebook/Sigil/tree/master/docs) has instructions that can guide you in that endeavor. You can also look to see if Sigil is available in the official repositories for your flavor of Linux.

An up-to-date version of Sigil is available via flatpak on Flathub. So if your distro can use Flatpak, you can always use [Sigil that way](https://flathub.org/apps/details/com.sigil_ebook.Sigil) if your distro's Sigil package seems to be lagging too far behind.
</div>
{: .notice--info}

### Package Versions of Sigil
[![Packaging status](https://repology.org/badge/vertical-allrepos/sigil.svg)](https://repology.org/project/sigil/versions)
