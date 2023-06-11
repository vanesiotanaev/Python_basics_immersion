# Write a function that takes an integer as input, and returns
# the number of bitsthat are equal to one in the binary representation of that number.
# You can guarantee that input is non-negative.

# Example: The binary representation of 1234 is 10011010010,
# so the function should return 5 in this case

def count_bits(decimal_value):
    BINARY_DIVIDER = 2

    count = 0
    binary_value = ''

    while decimal_value > 0:

        if decimal_value % BINARY_DIVIDER == 1:
            count += 1

        binary_value += str(decimal_value % BINARY_DIVIDER)
        decimal_value = decimal_value // BINARY_DIVIDER
        
    return count

print(count_bits(1234))