string = "Python is Awesome"
words = string.split()
reversewords = []

for w in words:
    reversewords.append(w[::-1])
reversestring = " ".join(reversewords).lower()

new_string = []

for idx, char in enumerate(string):
    if char.isupper():
        new_string.append(reversestring[idx].upper())
    else:
        new_string.append(reversestring[idx])
new_string = "".join(new_string)        
print(new_string)