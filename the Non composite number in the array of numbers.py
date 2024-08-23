def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def find_non_composite_numbers(arr):
    non_composite_nums = [num for num in arr if is_prime(num)]
    return non_composite_nums
array_of_elements = [26, 28, 47, 26, 43, 51, 29]
prime_numbers_in_array_elements = find_non_composite_numbers(array_of_elements)
print("Prime numbers in Array elements =", prime_numbers_in_array_elements)
