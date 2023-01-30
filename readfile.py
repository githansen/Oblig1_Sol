
def filters(t):
    ut = ''
    for i in t:
        if i in '1234567890':
            ut+= i
    return ut

file_list = open("testfil.txt", "r").readlines()

filtered_list = [filters(i) for i in file_list]
sum = 0
for i in filtered_list:
    sum += int(i)
print(sum)
