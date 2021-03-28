---
layout: default
title:  Transcription 1
author: Hauptmann
parent: Transcriptions
---

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