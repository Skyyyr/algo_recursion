def factorial(x):
    if x <= 1:
        return 1
    return x * factorial(x - 1)


def palindrome(string, index=0):
    left = string[index]
    right = string[len(string) - 1 - index]
	print(left, right, )
    if left == right and index >= len(string) / 2:
        return True
    elif left == right:
        return palindrome(string, index + 1)
    else:
        return False


# def palindrome(string, index=0):
#     left = string[index]
#     right = string[len(string) - 1 - index]
#
#     if left == right:
# 		if index == (len(string) / 2):
# 			return True
# 		else:
# 			palindrome(string, index + 1)
# 	else:
# 		return False


def bottles(num):
    pass


def roman_num(num):
    pass


# print(factorial(5))
print(palindrome("palap"))
