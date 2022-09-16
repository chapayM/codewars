# Complete the solution so that it returns true if the first argument(string)
# passed in ends with the 2nd argument (also a string).

def string_end_with(string, ending):
    return string[::-1].find(ending[::-1]) == 0

print(string_end_with('abcde', 'cde') == True)
print(string_end_with('abcde', 'abc') == False)
print(string_end_with('abcde', '') == True)
