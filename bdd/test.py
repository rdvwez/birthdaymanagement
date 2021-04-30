
with open("bdd/bdd.txt", 'r') as data:
    lines = data.readlines()
i = 1
data = []
for line in lines:
    print(line)
    element = line.split(";")
    data.append(element)
    
print(data[0][0])
    # print( lines)
    
    