with open('data', 'r') as data_file:
    data = data_file.read().splitlines()

list_one = []
list_two = []
total_distance = 0

for line in data:
    list_one.append(int(line.split("  ")[0]))
    list_two.append(int(line.split("  ")[1]))

list_one.sort()
list_two.sort()


for i in range(len(list_one)):
    print(list_two[i] - list_one[i])
    total_distance += abs(list_two[i] - list_one[i])


print(total_distance)
