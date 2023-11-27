def concat(arr):
    result = ""
    for item in arr:
        result += item
    return result


string_array = ["Johnny", "DeeDee", "Joey", "Marky"]
result_string = concat(string_array)


print(result_string)