def check_if_in_range(number, range):
    if number>=range[0] and number<=range[1]:
        return True
    else:
        return False

print(check_if_in_range(4,(1,4)))