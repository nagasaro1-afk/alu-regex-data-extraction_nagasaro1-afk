import re
import json

input_path = "../input/raw-text.txt"
output_path = "../output/sample-output.json"
max_size = 50000

print("Reading input file...")

f = open(input_path, "r", encoding="utf-8")
text = f.read()
f.close()

if len(text) > max_size:
    print("file too big, stopping")
    exit()

lines = text.split("\n")

print("Done reading, got " + str(len(lines)) + " lines")
