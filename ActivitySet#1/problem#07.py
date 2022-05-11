# Strings

text = "X-DSPAM-Confidence:    0.8475"

def find_no(text):
    x = text.find(':')
    no = text[x+1:]
    return float(no)

print(find_no(text))