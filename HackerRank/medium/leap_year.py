def is_leap(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    elif year % 4 == 0:
        return True
    else:
        return False


r = int(input("Enter the year"))
# print(r)
n = is_leap(r)
print(n)
