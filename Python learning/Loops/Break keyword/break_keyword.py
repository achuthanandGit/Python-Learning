count = 0

while True:  # this condition cannot possibly be false
    print(count)
    count += 1
    if count >= 5:
        break           # exit loop if count >= 5


zoo = ["lion", 'tiger', 'elephant', 'rabbit']
while True:                         # this condition cannot possibly be false
    animal = zoo.pop()       # extract one element from the list end
    print(animal)
    if 'elephant' is animal:
        break           # exit loop

print(zoo)
