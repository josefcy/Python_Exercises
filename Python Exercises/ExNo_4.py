sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
repeat = []
for r in sample_list:
    n = sample_list.count(r)
    if n>1:
        if repeat.count(r) == 0:
            repeat.append(r)
print(repeat)