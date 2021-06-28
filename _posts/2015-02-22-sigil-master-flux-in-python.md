---
title: "Sigil Master Flux In Python"
date: 2015-02-22T19:40:27-05:00
categories:
  - Blog
tags:
  - Announcements
  - Sigil
---

Right now Sigil master is in a state of flux. Many components are being removed and replaced. Python 3 is going to be a hard dependency (it will be embedded by default). Right now Python 3 and a few packages are required to be installed on your system to build and run Sigil. Specifically:

*   Python3.4+
*   lxml
*   six

I haven’t gotten around to researching and bundling all of this yet and as primary development happens on OS X these things are easy enough for me (and Kevin) to just not worry about at this moment. Anyone building from master themselves will need to deal with this though.

Already Tidy has been removed and replaced with a new parser, Gumbo+BS4. FlightCrew has been removed (if you want it see if someone is willing to make it into a plugin). Boost will be going next.

Gumbo+BS4(Beautiful Soup)+lxml all mean we will be able to support epub3. Not to mention even running some of the code in Python it’s a lot faster than the current solution (tidy and Xerceres). These are also easier to use.

As for FlgihtCrew, validation isn’t going away. We’re just going to build in a non-schema validating validator. Meaning if you want true schema validation to the letter of the epub spec then use a plugin. I added a specific plugin type in a previous release for this very reason. The validation we have in mind is simple stuff like is the HTML well formed. Also, by utilizing Python we’ll be able to (hopefully) have Javascript and CSS validation as well.

Basically FlightCrew wasn’t up to the task. Being written in C++ all the prebuilt libraries for validating things like CSS and Javascript being written in Python meant I’d have to write my own C++ version. There really wasn’t any sense in reinventing something that is already available…

One last thing. The Gumbo parser and BS4 are forks we’re including directly. In Gumbo’s case both the main person (Google employee) and the Github employee who forked it (there are two competing Gumbos’ right now. Don’t want our epub 3 changes. So there will probably be three versions of Gumbo as each diverges to meet the specific needs of each project. Right now we’re pretty close to the Github one but that will probably change in the future and we’ll probably rename and maintain ours as part of Sigil.

As for BS4 there are patches we need that have been waiting in never never land for years. calibre for example uses a modifed BS4 with a lot of the same patches because while they’ve been submitted upstream they’ve never even been looked at let along included…

So right now Sigil built directly from the master git repo (which we don’t recommend unless you’re developing directly for it) is in a major state of flux so we can finally get the structural changes to support not just epub 3 for to fix long standing issues.

One issue the new parser should fix is the fact that ebooks that were created using epubmerge often lose whole parts of the book due to file name conflicts due to the use of sub directories.

At this point I’m not willing to commit to saying exactly what the next release will bring other than underlying structural changes. Chances are Sigil itself from a user perspective will remain and function exactly the same when 0.9.0 (a long way off from now) as 0.8.x. But underneath a lot will have changed.