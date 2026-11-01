def count_digits(n):
    c = []
    for i in n:
        c.append(i)
    if(len(c)==0):
        return 0
    else:
        c.pop()
        return 1 + count_digits(c)
# digit = input()
# print(count_digits(digit))

def power(base, exponent):
    if(exponent == 0):
        return 1
    else:
        return base * power(base, exponent-1)

# print(power(2,10), power(5,0))

def is_palindrome(text):
    # n_txt = text
    if(len(text) <= 1):
        return True
    if(text[0] == text[-1]):
        return is_palindrome(text[1:len(text)-1])
    else:
        return False
# print(is_palindrome('racecar'),is_palindrome('level'),is_palindrome('python'))