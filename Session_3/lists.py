# Store multiple data points, can take different data shapes
students = ["Marina", "Donna", "Isabela"]
#print (students)
#print(type(students))
students.append("Kirby") #mutates the list and adds to the end of the existing list we mentioned
print(students)
# students.count("Kirby")
# students.remove("Kirby")
# print(students)

# List operations

# Index - location starts from 0
numbers = [1, 2,3,4]
# print(numbers)
numbers[1] = numbers[1] + 1
print(numbers[0:2])

# list of lists
mysterious_letter = ['d']
letters = ['a', 'b', 'c']
# letters.append(mysterious_letter)
letters.extend(mysterious_letter)
print(letters)