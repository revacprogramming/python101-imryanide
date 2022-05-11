# Files



filename = "mbox-short.txt"

def get_avg(filename):
    c = 0
    total = 0
    with open(filename) as f:
        for line in f:
            if line.startswith("X-DSPAM-Confidence:"):
                c +=1
                indx = line.find(':')
                total += float(line[indx+1:])
    return total/c

print(f"Average spam confidence: {get_avg(filename)}")
