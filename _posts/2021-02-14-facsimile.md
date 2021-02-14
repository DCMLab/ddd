---
layout: post
title:  "Displaying a facsimile"
date:   2021-02-14 20:35 +0100
---

For Tei Publisher to be able to display a facsimile, the template used needs to have a `<pb-facsimile>` component.
It is possible to copy and modify a preexisting one on the tei publisher app or to create a new one. 

### Alignment between text and images

The XML document is divided by page breaks with the `<pb>` element. Each element has a *@facs* attrbute that refers to the xml:id of the specific image and a *@n* attribute with page number. 
TEI also support embeded transcription in images, but I am not sure yet if the opposite is possible. 
[E-editiones workshop 2/3](https://www.youtube.com/watch?v=5qu94bhftpk&t=3548s) explains how to display facimile -with the ODD- that are all `<graphic>` within a `facsimile` element, without any pagination.
The TEI documentation [section 11.1](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/PH.html#PHFAX) was also helpful. 

I am looking into how to do it when working with files that have `<pb>` elements for pagination and a more copmlex XML structure to store images. But I couldn't do it so far and ran into a few questions:
- how and where are the images stored? As in do they need to be uploaded somewehre or embeded into the XML before being able to display them with the `<pb-facsimile>` element?
- how to do with the ODD to get to the images when they are not all stored within the same xml element?

The template file is the HTML that would be directly written in a post to add all the pb elements: `<pb-view>`, `<pb-facsimile>`, etc... And can be directly modified on it. 
The ODD need to be on TEI Publisher.

Related notes on the ODD:
- need to find how to select the zones that are set in Transkribus from the ODD to style them (page number, titles, footnotes etc...) 
- why is no use allowed to modify the ODD andt template files directly in TEI publisher playground? 

