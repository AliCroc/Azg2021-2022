
# imports


# helping variables / functions

hex_list =  ["A", "B", "C", "D", "E", "F"]

# task functions

def as_binary(n):
    return "{0:b}".format(int(n))

    # previous solution:
    # result = ""
    # while n > 0:
    #     m = n % 2
    #     n = n // 2
    #     result = str(m) + result
    # return result


def as_hex(n):
    result = ""
    while n > 0:
        m = n % 16
        n = n // 16
        if m >= 10:
            result = hex_list[m-10] + result
        else:
            result = str(m) + result
    return result

# test zone

print(as_binary(7))
print(as_hex(111), as_hex(255))