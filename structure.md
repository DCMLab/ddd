---
title: Structure
layout: page
published: false

---

The project is structured in three consecutive phases that are marked by a group meeting and the draft of an
intermediate report, documenting the state of the project, encountered obstacles and issues, as well as viable
solutions and avenues to proceed further. The last of these meetings constitutes the basis for the final report.

## Initial phase (3 months)

All textual sources pertinent to the dualism debate will be collected and stored in a central repository (e.g.
GitHub, Open Science Framework). Most texts are readily available through the ​International Music Score
Library Project (IMSLP). The preprocessing steps for subsequent computational analysis comprise page
segmentation, text and image extraction, optical character recognition (OCR), optical music recognition
(OMR), and labeling. Several open access tools will be explored and compared in this phase, e.g. ​Transkribus​,
OCR4all​, ​dhSegment​, ​INCEpTION​, and others.

Apart from text, our sources contain several graphical elements, e.g. diagrams, tables, and musical examples.
Since the project focuses on the textual material, all non-textual elements will be marked up as such and stored
separately for further research. The musical examples, however, will be treated differently and encoded into
machine-readable format of the ​Music Encoding Initiative (MEI). Together, the source images of musical
examples and their encodings will serve as a useful resource for improving optical music recognition (OMR)
tasks. The computational processing and analysis pipeline will be set up and tested using a sub-sample of the
entire dataset, in particular the prefaces and introductions of the texts where the debate mainly takes place.
Finally, a web interface will be created and used to display basic statistics and visualizations extracted from the
data, such as numbers of books, pages, words, and characters, as well as persons, musical concepts, and dates.
At the end of the initial phase, all steps of the pipeline will have been implemented, tested, and evaluated to the
effect that the further progress of the project is guaranteed.

## Main phase (6 months)

### Processing of sources. ​

The improvement of the data quality will be done by manually correcting the OCR
output. The documents will be marked up according to the ​Text Encoding Initiative (TEI) guidelines, in order
to ensure and facilitate their usability for other and future projects. Several textual elements will be annotated
in a combination of manual and automated procedures (e.g. Named Entity Recognition, NER). Specifically,
we will use labels for persons, places, dates, citations, and musical-theoretical concepts (e.g. “Tonica”,
“Accord”) and link them to open data resources such as ​Wikidata​, the ​Virtual International Authority File
(VIAF), and the ​Music Score Ontology ​(MusicOWL).

### Data Analysis. 

The core of the proposed projects is the application of methods from the Digital Humanities
to study the discourse around harmonic dualism in 19th century German music theory. As detailed above
(“Project objectives”) we will study the discursive networks, intertextual relations, and latent topics in our
sources. It is possible for a Master or PhD student to join the team for her or his thesis.

## Final phase (3 months)

The final phase of the project will be dedicated to extensive data curation, ensuring that it conforms to highest
academic standards. The display of the project results on the established platform will be further refined in
order to provide optimal accessibility and dissemination of the project outcomes.

## Envisaged results and outputs

This project will lead to a quantitative reconstruction of the complex author-text networks shaping the
dualism debate and illuminate how empirical methods complement traditional musicological research. In the
spirit of Open Science, the results and data will be made accessible online. The project will produce a detailed
documentation of the experiences, challenges, and problems that arise to be addressed in future research. This
documentation and the computational pipeline will serve as a proof-of-concept for a follow-up grant proposal
that will expand the research initiated here. An expert meeting at the end of the main phase will present the
project to an international audience and explore possible collaborations. At least two open access journal
publications and conference presentations are intended, addressing the musicological as well as technical
aspects of the project.

## Perspectives

Numerous avenues for the continuation of this research are possible. Most promising for follow-up work are
expansions of the source material along several dimensions:

1. Thematic: other 19th-century sources outside the dualism debate
2. Historical: other time periods beyond the 19th century
3. Geographical: other languages and nationalities beyond German
4. Modality: combine the textual analysis with analyses of the musical examples in this study
5. Institutional: broaden the expertise and international collaboration

The large-scale ambition for the future endeavour is to combine take into account as many historical sources
as possible, apply language-agnostic numerical methods (e.g. semantic embeddings), and perform
computational analyses as established in the present project in order to write a comprehensive data-driven
study of the history of music theory using methods of the Digital Humanities.