Pipeline
========

Preprocessing
-------------

- select source
- select page

Page segmentation 
-----------------

- automatic page segmentation (Transkribus)
    - if completely fails, do everything manually instead of correcting proposal
    - draw baselines
    - merge to paragraphs
- manual page segmentation (incl. deletion of redundant segments)

Type assignment
---------------

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