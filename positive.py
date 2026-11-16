import sys

def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

num = float(sys.argv[1])
print(check_number(num))
