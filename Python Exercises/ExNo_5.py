ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
print(ascii_dict.items())
rmap = {}
for k,v in ascii_dict.items():
    rmap[v] = k
print(rmap)