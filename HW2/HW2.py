# Problem 2
def sum_list(num_list):
    return sum(num_list)

print("#2")
x = sum_list([1, 2, 3, 4, 5])
print(x)
print(" ")


# Problem 3
def multiply_list(num_list):
    result = 1
    for num in num_list:
        result *= num
    return result

print("#3")
x = multiply_list([1, 2, 3, 4, 5])
print(x)
print(" ")


# Problem 4
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

print("#4")
x = factorial_recursive(5)
print(x)
print(" ")


# Problem 6
def is_palindrome(s):
    s_cleaned = str(s).lower().replace(" ", "")
    return s_cleaned == s_cleaned[::-1]

print("#6")
x = is_palindrome("Racecar")
print(x)
print(" " * 20)


# Problem 8
def unshared_elements(list1, list2):
    return list(set(list1) ^ set(list2))

print("#8")
x = unshared_elements([1, 2, 3, 4], [3, 4, 5, 6])
print(x)
print(" ")


# Problem 9
def folded_paper_thickness(n):
    thickness_mm = 0.1 * (2 ** n)
    return f"{thickness_mm} mm"

print("#9")
x = [folded_paper_thickness(folds) for folds in [1, 5, 10]]
print(x)
print(" ")


# Problem 11
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("#11")
x = is_prime(17)
print(x)