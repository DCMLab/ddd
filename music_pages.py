import os
import xml.etree.ElementTree as etree

root, sources, files = next(os.walk("."))

for source in sources:
    path = source + f"/{source}"
    pages = os.listdir(path + "/page/")
    for page in pages:
        with open(path + "/page/" + page) as f:
            lines = f.read()
            if "MusicRegion" in lines:
                pass 
            elif "$$MUSIC$$" in lines:
                pass
            elif "GraphicRegion" in lines:
                pass
            elif "$$GRAPHIC$$" in lines:
                pass
            else:
                # remove xmls
                os.remove(path + "/page/" + page)
    
    # remove jpgs
    pages = os.listdir(path + "/page/")
    for page in pages:
        fname, ext = page.split(".")
        img = fname + ".jpg"
        if img not in os.listdir(path):
            os.remove(path + "/" + img)
