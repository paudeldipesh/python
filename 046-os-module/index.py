import os

print(os.getcwd())
os.system("ipconfig")

if not os.path.exists("data"):
    os.mkdir("data")

for index in range(0, 10):
    os.mkdir(f"data/{(index+1):02}-day")
    os.rename(f"data/{(index+1):02}-day", f"data/{(index+1):02}-python-course")

folders = os.listdir("data")
print(folders)
