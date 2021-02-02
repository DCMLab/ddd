Pipeline
========

Upload document to collection
-----------------------------

- Open Transkribus
- Switch to collection "CROSS2021 - Dualism"
- Click on "Document..."
- Select "Import document to server..."
- Select "Extract and upload images from pdf"
- Specify file location
- Click on "Upload"
- Wait until file has been processed on server (you can check by clicking on the "Jobs" icon, the cup)
- Double-click on document in list to open it
- Go to "Overview"
- Click on "Show Document Manager"
- Select pages to be deleted and click on "Delete"

Layout Analysis
---------------

Automated
.........

- Click on "Tools"
- Select Method "CITlab Advanced"
- Keep presettings in "Configure..."
	- Neural Net: "Preset"
	- Text Orientation: "Default"
	- Use Separators: "Default"
- Select "Pages (XXX-XXX)" (all pages)
- Check "Find Text Regions"
- Check "Find Lines in Text Regions"
- Click "=> Run"

Segmentation Correction (manually)
..................................

- select source
- select page

- automatic page segmentation (Transkribus)
    - if completely fails, do everything manually instead of correcting proposal
    - draw baselines
    - merge to paragraphs
- manual page segmentation (incl. deletion of redundant segments)

Type assignment
...............

- element type assignment
    - TextRegion
    - Music 
    - Table 
    - Graphic 
    - List 
- structure type assignment (for TextRegions)
    - paragraph
    - paragraph-continued
    - page-number 
    - footnote
    - footnote-continued
    - header
    - heading
- structure type assignment (for other element types)
    - float
    - foat-continued

Line segmentation
-----------------

- line segmentation (automatic)
- merging of lines 

- check again 

Transcription 
-------------

- automatic OCR (Transkribus)
- correction/transcription
    - incl. application of guidelines (punctuation etc.)
- insert **inline placeholders**
    - $$MUSIC (Notenbeispiel inline)
    - $$MATH  (Formel, Brüche, etc.)
    - $$ANALYSIS (harmonische Stufensymbole, Funktionssymbole, falls sie sich nicht in Transkribus direkt transkribieren lassen)
- textual markup (boldface, emphasis, italic...)

Placeholder replacement
-----------------------

- manually insert music encoding, math expressions, etc.

Annotation 
----------

- tbc