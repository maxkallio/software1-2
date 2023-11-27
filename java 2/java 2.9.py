def even(arr):
    return [num for num in arr if num % 2 == 0]


number_array = [2, 7, 4]
even_numbers = even(number_array)


print("Original array:", number_array)
print("Even numbers array:", even_numbers)