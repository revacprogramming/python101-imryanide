# Tuples


import re
filename = "../dataset/mbox-short.txt"

# d = dict()


# def getmail(filename):
#     with open(filename) as f:
#         for lines in f:
#             word = lines.rstrip().split()
#             if 'From' in word and 'From:' not in word:
#                 email = word[1]
#                 d[email] = d.get(email, 0) + 1

#     cnt = 0
#     mail = None

#     for email, count in d.items():
#         if count > cnt:
#             cnt = count
#             mail = email

#     return mail, cnt


# x, y = getmail(filename)
# print(x, y)


fhandle = open(filename, 'r')
hours = []
count = dict()
for line in fhandle:
    if line.startswith('From '):
        time = re.findall(r"[\d]+:[\d]+:[\d]+", line)
        print(time[0][:2])
