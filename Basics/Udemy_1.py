a = "1"
b = 2
print(int(a) + b)  # typecast to integer

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
##########  0    1    2    3    4    5    6    7    8    9

print(letters[1])  # list indexing

print(letters[-3])  # negative indexing
# note: positive index starts with 0->towards right, negative index starts with -1 towards <- left
print(letters[3:6])  # slicing, default step size is 1


print(letters[-3:])  # when no value is specified it means all
print(letters[:-1])
print(letters[::3])
print(letters[::])

print(letters[2:8:3])  # The complete syntax of list slicing is [start(inclusive):end(exclusive):step]

my_range = range(1, 21)  # range(start (inclusive), stop (exclusive), step size)
print(list(my_range))

# write table of 17 till 10times
my_table = range(17, 171, 17)  # range(start (inclusive), stop (exclusive), step size)
print(list(my_table))
next(yes)
