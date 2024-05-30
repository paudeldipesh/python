import os

files = os.listdir("cluttered_folder")
for index, file in enumerate(files):
    os.rename(f"cluttered_folder/{file}", f"cluttered_folder/{index}.png")
