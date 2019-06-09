def length(x):
    count = 0
    for i in x:
        count += 1

    return count


s = "hello world"

#2) Reverse String
def string_reverse(string):
    """

    :type string: object
    """
    n = length(string) - 1
    print(n)
    str2 = ""
    while n >= 0:
        str2 = str2 + string[n]

        n -= 1

    return str2

#1) Reverse String
def string_reverse_second(s):
    str2 = s.split()
    str3 = ""
    for i in str2:
        str3 += i[::-1] + " "
    return str3
    # string reverse using indices method


def str_reverse_indices(s):
    s = s[::-1]
    return s


s = "hello world"
print(s.split(" "))
s1 = "deep learn"
print(s[8])
print(string_reverse(s))
print(str_reverse_indices(s))

print(string_reverse(s1))
print(str_reverse_indices(s1))
print(string_reverse_second(s))
