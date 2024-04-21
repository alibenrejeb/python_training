import os.path

filename = os.path.join("data", "file.txt")

# if not os.path.exists("config"):
#     os.mkdir("config")
# os.rmdir("config")
# os.remove(filename)

print("Filename: " + filename)
try:
    f = open(filename, "r")
except FileNotFoundError:
    print(f"The file {filename} is not found")
else:
    for line in f:
        print(line, end="")
    f.close()
