import random
import time
import os

try:
    os.remove("file2.txt")
    os.remove("newFile2_1.txt")
    os.remove("newFile2_2.txt")
    os.remove("newFile2_3.txt")
except:
    print("No files deleted")

inFile = "file2.txt"
size = 1000000

with open(inFile, "a") as file:
    for i in range(size):
        file.write(f"{random.randint(0,32767)}\n") # 32767 is the max value in the bash $RANDOM, a signed 15-bit int


# Read the entire contents of file1.txt into memory, then process each row
start = time.time()
with open(inFile, "r") as file:
    array = file.readlines()
    with open("newFile2_1.txt", "w") as output:
        for i in range(len(array)):
            out = array[i] * 2
            output.write(str(int(array[i]) * 2) + "\n")
end = time.time()
print(f"{end-start:.4f} seconds: Time to read into memory then process each row")

# Read one row of file1.txt at a time and process it.
start = time.time()
with open(inFile, "r") as file:
    with open("newFile2_2.txt", "w") as output:
         while True:
            line = file.readline()
            if not line:
                break
            out = int(line)
            output.write(str(out * 2) + "\n")
end = time.time()
print(f"{end-start:.4f} seconds: Time to read one row at a time then process")

# Split file1.txt into 2 parts and read each part into memory separately
start = time.time()
with open(inFile, "r") as file:
    array1 = []
    array2 = []
    for i in range(round(size / 2)):
        line = file.readline()
        if not line:
            break
        out = int(line)
        array1.append(out)
    j = round(size / 2)
    for j in range(size):
        line = file.readline()
        if not line:
            break
        out = int(line)
        array2.append(out)
    with open("newFile2_3.txt", "w") as output:
        for i in range(len(array1)):
            out = array1[i] * 2
            output.write(str(int(array2[i]) * 2) + "\n")
        for i in range(len(array1)):
            out = array2[i] * 2
            output.write(str(int(array2[i]) * 2) + "\n")
end = time.time()
print(f"{end-start:.4f} seconds: Time to split into two parts and read each into memory seperately")