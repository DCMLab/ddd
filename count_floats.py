from lxml import etree 
import glob
import re

# Read all TEI xmls
files = glob.glob("./data/**/*tei.xml", recursive=True)

# parse xmls
docs = [ etree.parse(f) for f in files ]

# define namespace
ns = {'tei':'http://www.tei-c.org/ns/1.0'}

if __name__=="__main__":

    ## Count placeholders

    mus = []
    for f in files:
        with open(f) as file:
            mus.append(len(re.findall("\$\$MUSIC", file.read())))

    gra = []
    for f in files:
        with open(f) as file:
            gra.append(len(re.findall("\$\$GRAPHIC", file.read())))

    ## Count floats
    music_examples = sum([ docs[i].xpath("count(.//tei:zone[@rendition='Music'])", namespaces=ns) for i in range(len(files)) ]) + sum(mus)
    graphic_examples = sum([ docs[i].xpath("count(.//tei:zone[@rendition='Graphic'])", namespaces=ns) for i in range(len(files)) ]) + sum(gra)
    tables = sum([ docs[i].xpath("count(.//tei:zone[@rendition='Table'])", namespaces=ns) for i in range(len(files)) ])

    print("Musics:  ", music_examples)
    print("Graphics:  ", graphic_examples)
    print("Tables:  ", tables)
