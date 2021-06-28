---
title: "Download Sigil"
permalink: /sigil/download/
installer_version: "1.6.0"
guide_version: "2021.05.27"
---

[Latest Windows x64 download](https://github.com/Sigil-Ebook/Sigil/releases/download/{{ page.installer_version }}/Sigil-{{ page.installer_version }}-Windows-x64-Setup.exe){: .btn .btn--success}<br/>[Latest MacOS download](https://github.com/Sigil-Ebook/Sigil/releases/download/{{ page.installer_version }}/Sigil.app-{{ page.installer_version }}-Mac.txz){: .btn .btn--success}

Past and present installers are always available under [releases](https://github.com/Sigil-Ebook/Sigil/releases) at the main code hosting location. The latest release will be on top. You can see what's changed between releases by looking at the [ChangeLog](https://github.com/Sigil-Ebook/Sigil/blob/master/ChangeLog.txt).

<div markdown="1">
Note that Sigil currently provides Windows installers for x86 and x64 and will only work on Windows 7 or newer. Mac OS X binaries are typically one version behind the current release. This means that today 10.10 is the current release so it should run on the 10.9 (with the latest updates installed). However, this is subject to change and this information is not always current. Especially for OS X. This is an at best support for older versions of Windows and OS X.

All releases also have CHECKSUM.sha256 file which includes sha256 check sums of the file posted. This will let you know if you have a bad download or if a build has been tampered with.

Going forward release announcements will include the sha256 checksum of the checksum file itself so you can verify that it hasn't been tampered with either.
</div>
{: .notice--info}

<div markdown="1">
Finally, the OS X .app file (not the .dmg) is signed before release. You can use the code sign command line tool (I don't know of another way) to verify the application. There will be a lot of output but you're looking for my signature saying I  (Kevin, the project maintainer built this binary). From a terminal run:

~~~
codesign -dvvv Sigil.app
~~~

There will be a lot of output but you should look for the following: Authority=Developer ID Application: Kevin Hendricks (2SMCVQU3CJ)
</div>
{: .notice--info}

### Source
Sigil's source code can be found on [GitHub](https://github.com/Sigil-Ebook/Sigil). Sigil is open source and licensed under the [GPLv3](http://www.gnu.org/copyleft/gpl.html). We're very opens to contributions and that's how the project keeps itself running. Feel free to discuss ideas using the issue tracker before issuing pull requests.

Starting with Sigil v0.9.9, the Git tags and source archives used for Sigil releases are signed with Doug Massay's PGP Key. His public key can be found and retrieved from any public key server. The fingerprint for his public key is:

~~~
B5A5 6206 AB0F BC1A 24EF AB8A A166 D29A 8FCD AC63
~~~

### Issue Tracker
The issue tracker is for development issues that are actively being worked. It is not a user support system. It is meant solely for development and for developer to developer communication. If you need help then head over to the [Support Page](../support).

Feature requests opened on the issue tracker will be closed if there isn't anyone willing to implement the requested feature. Only items being worked will be left open.

### Sigil On Linux
Sigil **will** run on Linux. We try to maintain compatibility with Linux mainly because it's easy to with Sigil supporting both OS X and Windows and it uses a number of technologies that already support Linux. That said, there is currently no official Sigil binary package for Linux.

If you're looking to use Sigil on Linux, you can always build it from source. The docs directory in  [Sigil's Github repository](https://github.com/Sigil-Ebook/Sigil/tree/master/docs) has instructions that can guide you in that endeavor. You can also look to see if Sigil is available in the official repositories for your flavor of Linux.
