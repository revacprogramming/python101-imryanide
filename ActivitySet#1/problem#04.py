# Conditional Execution

score = input("Enter Score: ")
s = float(score)

def grade(s):
    if(s > 0 and s < 1):
        if(s >= 0.9):
            print("A")
        elif(s >= 0.8):
            print("B")
        elif(s >= 0.7):
            print("C")
        elif(s >= 0.6):
            print("D")
        else:
            print("F")
    else:
        print("Error. Enter a value between 0 and 1 only")

grade(s)