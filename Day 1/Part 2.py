with open('data', 'r') as data_file:
    data = data_file.read().splitlines()

list_one = []
list_two = []
total = 0

for line in data:
    list_one.append(int(line.split("  ")[0]))
    list_two.append(int(line.split("  ")[1]))

for num in list_one:
    total += num * list_two.count(num)

print(total)