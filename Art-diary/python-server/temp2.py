import os

path = r"C:\Users\Iris Nguyen\Documents\Portfolio_projects\Art-diary\python-server"

with open(os.path.join(path, "file.txt"), "w+") as f:
    line = f.read()
    print(line)
    content = "123\n456\n789"
    f.seek(0)
    f.write(content)
    f.truncate()