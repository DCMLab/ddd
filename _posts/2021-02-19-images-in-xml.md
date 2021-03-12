---
layout: post
title:  "The <graphic> element"
date:   2021-03-11 20:52 +0100
category: tei-publisher
---

#### Representing graphics/images with TEI

The ```<graphic>``` element indicates the existence of a graphic or image embedded in the text. It has a **@url** attribute that specifies the URL from where the media can be obtained.
The ```<figure>```element can be used to contain images, captions and text. <br>
**Example:**
```
<figure>
	<graphic url="https://dcmlab.github.io/ddd/music-pictures/RIE1880-0017-01.png" width="300px"/>
	<figDesc>Riemann 1880-0017-01</figDesc>
</figure>
```
**How to add a graphic to be rendered in the viewer:**
1. Upload the image to the appropriate project's folder
2. Embbed the image in the XML file within a ```<graphic>``` element. The ```<figure>``` element is optional but has the advantage to contain other useful elements like an image title and/or description. 
    - the **@url** attribute should be like so: _https://dcmlab.github.io/ddd/FOLDER_NAME/FILE_NAME_
3. It is possible to add a custon **@height** and **@width** attribute spcific to that image. The title could also be included in the @title attribute, although not directly displayed. 
4. The ODD's graphic model is what define the ```<graphic>``` elements' behaviour. 

#### Note
- Because I am testing this site locally, the **@url** to the picture is through Github for now so it will work on other local environments: _https://raw.githubusercontent.com/DCMLab/ddd/tei-publisher/music-pictures/RIE1880-0017-01.png_
- The size and behaviour of images can be modified through the ODD.

#### The viewer

<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, minimum-scale=1, initial-scale=1, user-scalable=yes" />
    <title>pb-view Demo</title>
    <script src="https://unpkg.com/@webcomponents/webcomponentsjs@2.4.3/webcomponents-loader.js"></script>
    <script type="module" src="https://unpkg.com/@teipublisher/pb-components@latest/dist/pb-components-bundle.js">
    </script>
    <style>
        pb-page {
            position: relative;
        }
        pb-view {
            margin: 0 auto;
        }
        #view1 {
            overflow: auto;
            display: flex;
            justify-content: center;
            max-height: calc(100vh - 100px);
        }
        @media (min-width: 769px) {
            pb-view {
                max-width: 60vw;
            }
        }
        pb-navigation[direction="forward"] {
            float: right;
            color: green;
        }
        /* Color of navigation */
        paper-fab{
            background: lightsteelblue;
        }
        paper-fab:hover{
            background: steelblue;
        }
        </style>
</head>
<body>
    <pb-page endpoint="https://teipublisher.com/exist/apps/tei-publisher" emit="kant" class="embedded">
        <!-- Load document -->
        <pb-document id="doc1" path="playground/die_natur_der_harmonik.xml" odd="melinda-dodis"></pb-document>
        <!-- Navigate to next page // not in footer not to mess with site's footer, before pb-view to be on top // -->
        <pb-navigation direction="forward" keyboard="right">
            <paper-fab icon="icons:chevron-right"></paper-fab>
        </pb-navigation>
        <!-- Navigate to previous page -->
        <pb-navigation direction="backward" keyboard="left">
            <paper-fab icon="icons:chevron-left"></paper-fab>
        </pb-navigation>
        <pb-view src="doc1" xpath="//teiHeader/fileDesc/titleStmt/title">
            <pb-param name="header" value="short"></pb-param>
        </pb-view>
        <pb-view class="transcription" src="doc1" view="page"></pb-view>
    </pb-page>
</body>