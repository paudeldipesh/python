import os
import shutil

shutil.copy("index.py", "main.py")
shutil.copytree("../086-walrus-operator", "previous_lesson")
shutil.move("sample.txt", "text_file/sample.txt")

# os.remove("main.py")
# shutil.rmtree("previous_lesson")
