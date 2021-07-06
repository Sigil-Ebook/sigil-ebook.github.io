---
title: "Running PageEdit"
permalink: /pageedit/running-pageedit/
toc: true
toc_sticky: true
---

You can configure Sigil to run PageEdit or use it as a stand-alone application.

### Configure Sigil to run PageEdit

  1. [Download](/pageedit/download/) and install PageEdit.

  2. Open Sigil, and go to __Edit &gt; Preferences &gt; General Settings__. At the very bottom, you should see a box that says "Set your preferred alternative external xhtml editor." (If the option is not present, your Sigil version doesn’t support PageEdit.)

 ![a screenshot of the external editor text box](https://raw.githubusercontent.com/Sigil-Ebook/pageedit-user-guide/master/src/OEBPS/Images/external_editor.png)

  3. Click the Browse button, and locate the PageEdit installation folder.

  4. Select `PageEdit.exe`. You can then click the OK button and get back to Sigil.

  5. Now, at the very top of Sigil, you'll see a little button that looks like a pencil writing on paper that will open up PageEdit. If you haven’t changed the default Sigil keyboard shortcuts, you can also press `F2`.

![a screenshot of the PageEdit toolbar button](https://raw.githubusercontent.com/Sigil-Ebook/pageedit-user-guide/master/src/OEBPS/Images/pe_button.png)

Double-click the .opf file in the Book Browser window _before_ running PageEdit, if you want to edit or preview _all_ XHTML files with PageEdit. Otherwise, you’ll only be able to access the current XHTML file.

__NOTE:__ starting with Sigil v1.6.0, you no longer need to open the opf file before launching PageEdit in order to preview all XHTML files. Launching PageEdit with Sigil's external xhtml editor button will always open PageEdit with _all_ of the epub's resources available. If you wish to only open a single XHTML file with PageEdit in Sigil v1.6.0+, use Sigil's Open With feature.
{: .notice--info}

### Running PageEdit as a stand-alone application

Install PageEdit, and create a Desktop shortcut:

#### Windows

Open the Windows Explorer, locate `PageEdit.exe` in the `C:\Program Files\PageEdit` folder, right-click it, and select `Send to Desktop`.<br/>(You can also [add an app shortcut to the Start menu](https://www.windowscentral.com/add-app-shortcuts-start-menu-manually-windows-10){:target="_blank"})

__NOTE:__ the above is unnecessary if--during the installation--you chose to create a desktop shortcut and add PageEdit to the start menu.
{: .notice--info}

#### Mac

Open a Finder window, locate the PageEdit app in the `Applications` folder, and drag it to the Desktop.

#### Linux

Since most distributions will automatically add a PageEdit shortcut to the desktop environment, you shouldn’t have to manually create one.
