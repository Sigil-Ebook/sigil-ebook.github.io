---
title: "Download Sigil"
permalink: /sigil/download/
---

{% include remote_versions.html %}
[Latest Windows x64 download](https://github.com/Sigil-Ebook/Sigil/releases/download/{{ sigil_ver }}/Sigil-{{ sigil_ver }}-Windows-x64-Setup.exe){: .btn .btn--success}<br/>[Latest MacOS download](https://github.com/Sigil-Ebook/Sigil/releases/download/{{ sigil_ver }}/Sigil.app-{{ sigil_ver }}-Mac.txz){: .btn .btn--success}<br/>[Latest CHECKSUMS file](https://github.com/Sigil-Ebook/Sigil/releases/download/{{ sigil_ver }}/Sigil-{{ sigil_ver }}-CHECKSUMS.sha256.txt){: .btn .btn--success}

Past and present installers are always available under [releases](https://github.com/Sigil-Ebook/Sigil/releases) at the main code hosting location. The latest release will be on top. You can see what's changed between releases by looking at the [ChangeLog](https://github.com/Sigil-Ebook/Sigil/blob/master/ChangeLog.txt).

### Checksum verification
<div markdown="1">
All releases also have a CHECKSUM.sha256.txt file which includes sha256 check sums of the file posted. This will let you know if you have a bad download or if a build has been tampered with. Going forward release announcements will include the sha256 checksum of the checksum file itself so you can verify that it hasn't been tampered with either.
</div>
{: .notice--info}

### Sigil On Windows
<div markdown="1">
Note that Sigil currently provides Windows installers for x86 and x64 and will only work on Windows 7 or newer.
</div>
{: .notice--info}

### Sigil on Mac OS
<div markdown="1">
Mac OS X binaries are typically one version behind the current release. This means that today 10.10 is the current release so it should run on the 10.9 (with the latest updates installed). However, this is subject to change and this information is not always current. Especially for OS X. This is an at best support for older versions of Windows and OS X.

Finally, the OS X .app file (not the .txz) is signed before release. You can use the code sign command line tool (I don't know of another way) to verify the application. There will be a lot of output but you're looking for my signature saying I  (Kevin, the project maintainer built this binary). From a terminal run:

~~~
codesign -dvvv Sigil.app
~~~

There will be a lot of output but you should look for the following: Authority=Developer ID Application: Kevin Hendricks (2SMCVQU3CJ)
</div>
{: .notice--info}

### Sigil On Linux
<div markdown="1">
Sigil **will** run on Linux. We try to maintain compatibility with Linux mainly because it's easy to with Sigil supporting both OS X and Windows and it uses a number of technologies that already support Linux. That said, there is currently no official Sigil binary package for Linux.

If you're looking to use Sigil on Linux, you can always build it from source. The docs directory in  [Sigil's Github repository](https://github.com/Sigil-Ebook/Sigil/tree/master/docs) has instructions that can guide you in that endeavor. You can also look to see if Sigil is available in the official repositories for your flavor of Linux.
</div>
{: .notice--info}
