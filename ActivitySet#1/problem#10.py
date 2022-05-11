# Dictionaries

filename = "../dataset/mbox-short.txt"

def get_c(filename):
    c=0
    with open(filename) as f:
        for line in f:
            line = line.rstrip()
            if 'From' in line and 'From:' not in line:
                mail=line.split()
                print(mail[1])
            else:
                continue    
            c += 1
    return c

print(f"There were", {get_c(filename)}, "lines in the file with From as the first word")