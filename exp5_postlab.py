# -----------------a------------------------
numbers = (3, 5, 6, 7, 6, 9, 10, 6, 5, 6)
element = 6
count = numbers.count(element)
print(f"{element} occurs {count} times in the tuple.")



# -----------------b------------------------
numbers = (3, 5, 6, 7, 9, 10)
element = 6

if element in numbers:
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does not exist in the tuple.")



# -----------------c------------------------
t = ('H', 'e', 'l', 'l', 'o')
result = ''.join(t)
print("String is:", result)



# -----------------d------------------------
numbers = (5, 2, 9, 1, 7, 3)
maximum = max(numbers)
minimum = min(numbers)
print("Maximum element:", maximum)
print("Minimum element:", minimum)



# -----------------e------------------------
words = ("Python", "is", "fun")
result = " ".join(words)
print("Single string is:", result)



# -----------------f------------------------
numbers = (5, 2, 9, 1, 7, 3)
sorted_tuple = tuple(sorted(numbers))
print("Sorted tuple is:", sorted_tuple)



# -----------------g------------------------
numbers = (10, 20, 30, 40, 50)
first = numbers[0]
last = numbers[-1]
print("First element:", first)
print("Last element:", last)
