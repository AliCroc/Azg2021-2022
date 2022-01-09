# imports
import math, itertools

# helping functions and variables, not important

global partial_list
partial_list = []

def get_sum_terms(numbers, target, partial=[]):
    s = sum(partial)
    if s == target: 
        partial_list.append(partial)
    if s >= target:
        return
    
    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        get_sum_terms(remaining, target, partial + [n])


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
    result_message = ""
    if a == 0:
        return "\"a\" argument cannot be equal 0! Please input correct quadratic equasion"
    
    delta = b ** 2 - 4 * a * c
    sqrt_delta = math.sqrt(my_abs(delta))

    if delta > 0: 
        result_message = f'x1 = {(-b + sqrt_delta)/(2 * a)} x2 = {(-b - sqrt_delta)/(2 * a)}'
      
    elif delta == 0: 
        result_message = f'x = {-b / (2 * a)}'
      
    else:
        result_message = f'Delta is smaller than 0 and we are not operating on complex numbers so there are NO results'

    return result_message + "\t"

def is_prime(number):
    if number in {0, 1}:
        return False
    for divisor in range(2, number): 
    # variable "number" will not be tested here, as its value is not included in range returned by function range(2, number)
        if number % divisor == 0:
            return False
    return True

def is_lucky(serial_number):
    if len(serial_number) != 6:
        print(f'Serial number is invalid\nLength of serial number is not equal 6 but {len(serial_number)} and/or bad input')
        return False
    dsn = [int(digit) for digit in serial_number] # dsn is short for digitalized serial number list
    if dsn[0] + dsn[1] + dsn[2] == dsn[3] + dsn[4] + dsn[5]:
        return True
    return False


def calculate_amount_of_lucky_tickets():
    # there are total of 900000 combinations of 6-digit numbers, including "000000"
    # sum of 3 digit number has a range between 0 and 27
    # for a ticket to be lucky we need two 3-digit numbers which sum of digits is the same
    # function will calculate all possible combinations of getting a values in range [0, 27] then get all combinations of lucky 6-digit serial numbers
    
    lucky_ticket_serial_number_count = 2 # this includes "000000" and "999999" which values (0 nad 27) will be excluded in further calculations
    list_of_combinations_indexed_by_value = [0] * 27
    # can be 27, here first and last are excluded
    three_digit_combinations = 998 # excluding '000' and '999'

    for value in range(1, three_digit_combinations + 1):
        digit_sum = 0
        while (value != 0):
            digit_sum += int(value % 10)
            value = int(value/10)
        list_of_combinations_indexed_by_value[digit_sum] += 1
    for value_index in range(1, 27):
        # kombinacja z powtórzeniami
        combination_result = int(math.factorial(int(list_of_combinations_indexed_by_value[value_index]+1))/(2*math.factorial(list_of_combinations_indexed_by_value[value_index]-1)))
        lucky_ticket_serial_number_count += combination_result
    return lucky_ticket_serial_number_count


def generate_n_lucky_tickets(n): # generate first n 6-digits lucky tickets, max value is 27128
    if n > calculate_amount_of_lucky_tickets():
        print("Maximum number of lucky tickets to print exceeted")
        return
    if n == 0: 
        return []
    if n == 1:
        return ["000000"]
    lucky_ticket_list = ["000000"]
    n -= 1
    i = 1
    counter = 0
    while counter < n:
        partial_list.clear()
        get_sum_terms(list(range(1, 10)), i)
        combination_list = [a for a in partial_list if len(a) <= 3]
        for comb in combination_list:
            temp_result = []
            final_list = []
            if len(comb) == 1:
                temp_result = list(set(list(itertools.product(f'{comb[0]}00', repeat=3)))) # function that gives all possible combinations on string
            elif len(comb) == 2:
                temp_result = list(set(list(itertools.product(f'{comb[0]}{comb[1]}0', repeat=3))))
            else:
                temp_result = list(set(list(itertools.product(f'{comb[0]}{comb[1]}{comb[2]}', repeat=3))))
            # print("products", temp_result)
            for r in temp_result:
                for t in temp_result:
                    # print(sum([int(elem1) for elem1 in r]), sum([int(elem2) for elem2 in t]), r, t, r+t)
                    if sum([int(elem1) for elem1 in r]) != sum([int(elem2) for elem2 in t]):
                        continue
                    final_list.append("".join(r + t))
                final_list.append("".join(r + r))
            for result in list(set(final_list)):
                lucky_ticket_list.append(result)
                counter += 1
                if counter >= n:
                    break
            if counter >= n:
                    break
        i += 1
    return sorted(lucky_ticket_list)
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

print(solve_equasion(1, 5, 4), solve_equasion(4, 4, 1), solve_equasion(2, 1, 1))

print(is_prime(1), is_prime(5), is_prime(1024), is_prime(97))

print(is_lucky("123123"), is_lucky("111222"), is_lucky("000001"))

print(generate_n_lucky_tickets(10))

print(calculate_amount_of_lucky_tickets())

#
