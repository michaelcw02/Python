import string
import random
import argparse
import os
import shutil

parser = argparse.ArgumentParser()

parser.add_argument("-n", "--number", type=int, help="The number of files to make")
args = parser.parse_args()

number = args.number

path = "08-ExerciseRandomFiles/"
name = "archive-"

# make some new files....
for i in range(0, number):
    ext = "." + random.choice(string.ascii_lowercase) + random.choice(string.ascii_lowercase) + random.choice(string.ascii_lowercase)
    fullname = path + name + str(i) + ext
    file = open(fullname, "w")
    print(fullname)


for root, dirs, files in os.walk(path):
    for file in files:
        splitted = file.split(".")
        if not os.path.exists(path + splitted[1]):
            os.makedirs(path + splitted[1])
        shutil.move(path + file, path + splitted[1] + "/" + file)

print ('done')