import os
import shutil
import pandas as pd
from PIL import Image

if __name__ == "__main__":
    dfdict = {"book": [], "image_file": [], "image_size": []}
    OUTPUTDIR = "allimages"
    for root, _, files in sorted(os.walk(".")):
        for f in sorted(files):
            if "/music_examples/music" in root and f.endswith(".png"):
                path = os.path.join(root, f)
                slugified = path.replace("./", "").replace("/", "-")
                dfdict["book"].append(slugified.split("-")[0])
                dfdict["image_file"].append(f)
                im = Image.open(path)
                dfdict["image_size"].append(im.size)
                if not os.path.exists(OUTPUTDIR):
                    os.mkdir(OUTPUTDIR)
                newpath = os.path.join(OUTPUTDIR, slugified)
                newpath = newpath.replace(".png", ".jpg")
                print(f, im.size)
                im = im.convert("L")
                im.save(newpath)
    df = pd.DataFrame(dfdict)
    df.to_csv("image_summary.csv")