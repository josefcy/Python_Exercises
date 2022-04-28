number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

i = 0
l = len(number_list)
while i < l:
    if number_list[i] > 50:
        del number_list[i]
        l = l-1
    else:
        i = i+1
print(number_list)
