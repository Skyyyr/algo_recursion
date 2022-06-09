def factorial(x):
    if x <= 1:
        return 1
    return x * factorial(x - 1)


def palindrome(string, index=0):
    left = string[index]
    right = string[len(string) - 1 - index]
    target_length = (len(string) / 2)
    if index > target_length:
        return False
    elif left == right:
        if index + 1 > target_length:
            return True
        return palindrome(string, index + 1)
    else:
        return False


def bottles(bottle_number):
    finished_message = "Take one down and pass it around, 1 bottle of beer on the wall.\n1 bottle of beer on the " \
                       "wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the " \
                       "wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy " \
                       "some more, 99 bottles of beer on the wall."
    # write your code here!
    output = f"{bottle_number} Bottles of beer on the wall, {bottle_number} bottles of beer on the wall.\nTake one " \
             f"down pass it around, {bottle_number - 1} more on the wall. "
    if bottle_number == 1:
        return print(finished_message)
    print(output)
    bottles(bottle_number - 1)


def roman_num(num, output="", index=0):
    numerals = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'V', 'IV', 'I']
    nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 5, 4, 1]
    current_numeral = numerals[index]
    current_num = nums[index]

    # This is our base case
    if num == 0:
        return output

    if num >= current_num:
        output += current_numeral
        num -= current_num
        index -= 1
    return roman_num(num, output, index + 1)

print(roman_num(99))
