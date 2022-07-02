# Regular Expressions
# https://www.py4e.com/lessons/regex
import re
f = open("../dataset/regex_sum_1543941.txt")

s = 0
for line in f:
    w = re.findall(r"\d+", line)
    if w:
        for i in w:
            s = s+int(i)
print(s)
