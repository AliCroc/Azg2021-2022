# function declarations

def my_max(number_a, number_b): #returns greatest value out of 2 integers
    if number_a > number_b:
        return number_a
    return number_b

def my_max3(number_a, number_b, number_c):  # returns greatest value out of 3 integers
    if number_a < number_b:
        if number_b < number_c:
            return number_c
        else:
            return number_b
    else:
        if number_a < number_c:
            return number_c
        else:
            return number_a

def minmax(list_of_int):  # returns tuple of minimum and maximum value from list of integers
    length = len(list_of_int)
    int_current = 0
 
    while int_current < length - 1:
        if (list_of_int[int_current] > list_of_int[int_current + 1]):
            value_temp = list_of_int[int_current]
            list_of_int[int_current] = list_of_int[int_current + 1]
            list_of_int[int_current + 1] = value_temp
            int_current = -1
        int_current += 1
    return (list_of_int[0], list_of_int[-1])

def sweap(list_of_int): # returns a list in with first and last integers have swapped places
    int_a = list_of_int[0]
    int_b = list_of_int[-1]
    list_of_int[0] = int_b
    list_of_int[-1] = int_a
    return list_of_int

def my_abs(value):
    if value < 0:
        value = -value
    return value

def fib(integer): # return fibonacci value at given index
    if integer in {0, 1}:
        return integer
    return fib(integer - 1) + fib(integer - 2)

def filter_nums(list_of_nums): # return all numbers indivisible by 3 
    return [a for a in list_of_nums if a%3 != 0]

def generate_evens(value_start, value_end):
    if value_start % 2 != 0:
        value_start += 1
    return [a for a in range(value_start, value_end, 2)]

def compute(nums, value_power_to, value_modulo):
    return [a ** value_power_to % value_modulo for a in nums]


def solve_equasion(a = 0, b = 0, c = 0):
    if a != 0:
        



#


# test area

print(my_max(10, 20))
print(my_max3(10, 20, 100))
print(minmax([10, 1, 22, 19, 30]))
print(sweap([5, 9, 1, 2, 3, 4, 0]))
print(my_abs(10), my_abs(-10))
print(fib(0), fib(1), fib(2), fib(7))
print(filter_nums([1, 8, 7, 10, 9, 6, 3]))
print(generate_evens(1, 12))
print(compute([1, 2, 3], 10, 7))
print("empty")
print("empty")
print("empty")
print("empty")
print("empty")
#
