---
title: "Sigil and BookView Research Update"
date: 2015-02-12T10:14:59-05:00
categories:
  - Blog
tags:
  - Announcements
  - Sigil
---

As many Sigil users know, Sigil has a WYSIWYG editor portion. It’s also in my mind substandard. It gets the job done for quick edits but it’s not as full featured as I’d like. Especially when I’m used to using editors like WordPress’s editor.

Back in 2012 I started researching updating the [BookView editor](https://john.nachtimwald.com/2012/03/10/sigil-bookview-changes-preview/). This was a planned feature for the 0.6.0 but was ultimately dropped due to issues unresolvable issues.

Right now Sigil uses a QWebView set to allow editing. This is a very nice feature but requires a lot of Javascript glue to provide things like making selected text bold. Basically, we have a basic editor that gets the job done but isn’t really all that full featured. It’s also very difficult to work with (from a programing standpoint) and for a long time has been stagnant. Most users don’t care because they tend to use CodeView and now that there is a live Preview the use for BookView to see changes is reduced even further. One major issue with BookView is it will change the underlying code which is why Preview was introduced in the the first place.

Now back to 2012. I was researching using [CKEditor](http://ckeditor.com/) or [TinyMCE](http://www.tinymce.com/) as a replacement for QWebView in edit mode. This would put all the editor functionality into these editor packages and reduce the scope of BookView (and it’s Javascript glue) to nearly nothing.

As I said they never made it into any release because they just weren’t working like I needed them to. That’s not to say they aren’t terrific editors and provide all the functionality I wanted. They just didn’t perform like I wanted.

Well, it’s been a few years since then and both projects have matured and greatly improved over that time. So I decided to revisit using them to replace the current BookView. Unfortunately, I ran into the same issue as before. All text is in Javascript which uses a lot of memory and can be very slow to work with. Slow to the point of unusable. Slow to the point of loading the editor can take minutes. Slow to the point of scrolling, and typing can take minutes. I will say they cope much better then they did the last time I looked at them but they still just aren’t going to work for Sigil

This isn’t an issue with the editors themselves. It’s an issue with all text being in Javascript. For a post on a blog or book divided into “short” chapters they work fine and very well. The issue is the amount of text you put into them. Long chapters you start to see the slowdown.

If you were to import a single HTML file and use BookView to put chapter split markers then split, we’ll, the editor just can’t cope. Again it’s because of how Javascript uses strings. These editors and Javascript just can’t deal with multiple Megabytes of text loaded into them.

I know that splitting single files into chapters is a typical use case so I can’t justify an editor that makes that impossible. So for the time being the best option is just to leave BookView as is. Simply because it’s able to cope with a much larger amount of text than these Javascript editors (which are beautiful and so nice to work with). Maybe in a few more years I’ll be able to switch to them for BookView but not right now.