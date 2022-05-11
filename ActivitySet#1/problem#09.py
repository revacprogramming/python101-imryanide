# Lists

filename = "romeo.txt"

def get_words(filename):
    l=[]
    with open(filename) as f:
        for line in f:
            sentence = line.rstrip().split()
            for word in sentence:
                if word not in l:
                    l.append(word)
    l.sort()
    return l

print(get_words(filename))