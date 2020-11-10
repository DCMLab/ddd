---
title: Scope
layout: page
published: true
order: 1

---

## General context

Music theory is one of the oldest academic disciplines of Western culture (Christensen,
2002), being numbered among the seven liberal arts in antiquity, and with traditions dating back at least to the
teachings of Pythagoras (c. 570-510 BC) about harmonic ratios. Over the centuries, Western
music-theoretical writings have encompassed a wide range of topics such as musical scales, tuning,
consonance and dissonance, meter and rhythm, musical form, voice leading and counterpoint, and many
more. These texts comprise a diverse range of formats, such as theoretical treatises, composition manuals,
lexica, textbooks and others. Many of these sources are characterized by recurring concepts like "tone",
"chord", "scale", "key", "harmony", "melody", etc. but the precise definitions of these concepts as well as their
derivation from first principles is at times subject of heated debate.

## The present project

​The proposed project ​Digitizing the Dualism Debate: A Case Study in the Computational
Analysis of Historical Music Theory Sources applies modern methods from the Digital Humanities to the study
of one of the central debates in German 19th century music theory, the so-called "dualism debate". Focusing
on this particular dispute as a case study allows to approach the project under a "mixed methods" paradigm
(Johnson et al., 2007), combining "close" and "distant reading" (Moretti, 2013) techniques. The project will
thus serve to build methodological bridges between the humanities and the sciences. It will demonstrate the
benefits of the methodological approach for music theory and musicology, as well as providing a
proof-of-concept for future studies building on this project.

## The Dualism Debate

​The debate around harmonic dualism was triggered in reaction to Moritz
Hauptmann's ​The Nature of Harmony and Meter (1853) and Arthur v. Oettingen's ​Harmoniesystem in dualer
Entwicklung ​(1866). Numerous music theorists, mostly based in Leipzig, Germany, subsequently either
attacked, or defended and elaborated the systematization of the major-minor tonal system as laid out by the
"dualists". In a nutshell, the debate between the monist and the dualist schools of thought concerns the relation
between the major and the minor triads, scales, and keys (Snyder, 1980). More specifically, the discussion
revolves around whether the minor triad is a mere derivative of the major triad (e.g. by means of chromatic
alteration of its third, the monist position) or whether it can be derived from first principles on its own right
(e.g. by postulating the existence of an undertone series, the dualist position). In this debate, the probably most
prominent figure and most ardent advocate of harmonic dualism is Hugo Riemann (1849-1919). For him,
harmonic dualism is "the assumption of a twofold (dual) basis of harmony, that of the major consonance [from
the main tone upwards] and that of the minor consonance [from the main tone downwards]" (Riemann, 1900,
273). The justifications for this position in his manifold writings is an intricate melange of physical,
psychoacoustical, and philosophical arguments (Rehding, 2003). The authors that partake in this debate do not
mince their words when expressing their criticism of other texts and do not hesitate to accuse an opponent of
ignorance, incompetence, or even ill will. These harsh criticisms mostly appear in the prefaces and
introductions of the texts. For this reason and in alignment with the overall mixed-methods approach, those
parts of the texts will also undergo a close-reading analysis.

## Goals

This project does not aim at resolving the dualism debate in the sense of providing qualitative or
quantitative arguments for either side. Rather, it strives to reconstruct and critically evaluate the discursive
relations within this debate by using the combined power of qualitative-historical and quantitative-numerical
methods. We will address the following project objectives:

1. **Revealing and analyzing discursive networks.** We will study the discourse structure of the dualism
   debate by analyzing the relations between the authors and their texts as agents in complex networks. This
   will allow us to address important musicological and historical questions: How do the different actors in
   the debate relate and refer to each other? To which earlier music theorists do they explicitly refer as
   authoritative figures? Is the centrality of Hugo Riemann's work reflected in network structures that do not
   rely on the sheer volume of his writings (Rehding, 2003)? In order to study these and related questions, we
   will apply modern network modeling techniques (Bavaud, et al. 2015; Ceré & Bavaud, 2019) to the texts
   extracted from the music theory sources.
2. **Clustering and classification of texts.** We will study whether the information contained in the texts
   themselves (Cocco, & Bavaud, 2015; Bavaud, 2020) allows to draw inferences on the respective role that
   the text plays in the dualism debate. We will investigate whether it is possible to classify authors and/or
   texts as being either monist or dualist. This can be achieved by applying clustering and classification
   techniques to the resources in vector-embedding spaces of the texts (Bavaud, 2011). We are expecting that
   such an approach will lead to a more fine-grained view than the monist-dualist dichotomy, and will show
   where authors are located on a spectrum between these poles.
3. **Finding latent topics in the sources.** ​In order to reveal latent themes in the discourse about harmonic
   dualism, we will employ the established method of topic modeling to our sources (Blei, 2012; Moss, 2019;
   Lieck et al. in review). We will model textual similarity to obtain a quantitative notion of textual distance
   based on those topics and on correspondence analysis (Cocco & Bavaud, 2015).

The above mentioned research objectives will be realized by establishing a proof-of-concept implementation
of a computational pipeline that applies methods from the Digital Humanities to the analysis of music-theoretical texts. 
This pipeline, which reflects the initial, main, and final phases of the project, can be summarized as:

[Preprocessing] → [Analysis] → [Dissemination]

## Main contributions

The main contribution of the proposed project consists in an empirical reconstruction
of the discursive structure of the dualism debate. The project will lead to a publicly-available online resource
that displays the results of the research project and provides access to the data for subsequent research.
      
## Previous work

​While digital musicology has increasingly produced digital editions of scores, letters, and
libretti (Pugin, 2005; Neuwirth & Rohrmeier, 2016), previous decades have only seen a relatively small
number of editorial efforts to digitize and make available large portions of music theory resources. Most of
these approaches aim at providing easier scholarly access to the primary resources in the form of scanned pages
(images) of the original material.[^1] A few digital editions exist, covering different languages and historical
periods.[^2] However, when it comes to digital editions and large-scale online scholarly access, the extensive
body of 19th century sources, in particular German sources, has surprisingly not yet been digitized. While the
aforementioned projects do provide open access to digital editions of the sources, they have remained virtually
unexplored and not analyzed in depth using sophisticated methods from corpus studies, natural language
processing, and the Digital Humanities in general. The present project thus closes an important gap in the
research landscape by concentrating on a somewhat underrepresented historical period and by applying
numerical techniques that are in principle extensible to the existing digital resources.

[^1]: E.g., the collection of music-theoretical and musicological writings in the archives of the 
      [*Bayrische Staatsbibliothek*](​https://www.digitale-sammlungen.de/index.html?c=sammlung&projekt=1199864125​).

[^2]: E.g., several projects at Indiana University: 
      [​Thesaurus Musicarum Latinarum](http://www.chmtl.indiana.edu/tml/​) ​(3rd-17th c.);
      [​Saggi Musicali Italiani](​http://www.chmtl.indiana.edu/smi/​) (15th-19th c.),
      [Texts on Music in English](http://www.chmtl.indiana.edu/tme/) ​(14th-17th c.​),
      [Traités français sur la musique](http://www.chmtl.indiana.edu/tfm/​) (14th-19th c.) 
      and the [​Thesaurus Musicarum Italicarum](https://euromusicology.cs.uu.nl/​) (18th c.) at Utrecht University.