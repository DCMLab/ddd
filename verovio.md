---
title: Verovio JS Toolkit
layout: page
published: true
nav_order: 6
---

<head>
    <title>Verovio Hello World! example</title>
    <!--/////////////////////-->
    <!-- The Verovio toolkit -->
    <!--/////////////////////-->
    <script src="https://www.verovio.org/javascript/develop/verovio-toolkit.js" type="text/javascript" ></script>
    <!--////////////////////-->
    <!-- We also use jQuery -->
    <!--////////////////////-->
    <script src="https://code.jquery.com/jquery-3.1.1.min.js" type="text/javascript" ></script>
</head>
<body>
    <h2>Hi this is a test</h2>
    <!--//////////////////////////////////////////////-->
    <!-- The div where we are going to insert the SVG -->
    <!--//////////////////////////////////////////////-->
    <div id="svg_output"/>
    <script type="text/javascript">
        ///////////////////////////
        /* Create the vrvToolkit */
        ///////////////////////////
        var vrvToolkit = new verovio.toolkit();
        ////////////////////////////////////
        /* Load the file using a HTTP GET */
        ////////////////////////////////////
        $.ajax({
            url: "https://raw.githubusercontent.com/DCMLab/ddd/tei-publisher/meil-files/RIE1880-0017-02.mei"
            , dataType: "text"
            , success: function(data) {
                var svg = vrvToolkit.renderData(data, {});
                $("#svg_output").html(svg);
            }
        });
    </script>
</body>