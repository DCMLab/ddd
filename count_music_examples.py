import os

PATH = "data/"

dirs = os.listdir(PATH)

if __name__ == "__main__":
    allmusic = PATH + "all_music_examples/"

    if not os.path.exists(allmusic):
        os.makedirs(allmusic)
        print(f"Created directors: {PATH + allmusic}")
    
    N = 0
    for dir in dirs:
        if os.path.isdir(PATH + dir):
            print(dir)
            try: 
                current_path = PATH + dir + "/music_examples/music"
                for file in os.listdir(current_path):
                    if file.endswith(".png"):
                        N +=1
                        print("\t", file)
                        os.system(f"cp -r {current_path} {allmusic + dir}")
            except:
                print(f"!!!: No music examples for {dir}")
    print(f"There are {N} music examples.")