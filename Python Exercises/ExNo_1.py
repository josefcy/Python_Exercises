string = "Python is Awesome"
words = string.split()
reversewords = []

for w in words:
    reversewords.append(w[::-1])
reversestring = " ".join(reversewords)

print(reversestring)