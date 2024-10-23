def check_positive(num):
    if num<0:
        raise ValueError("Neg Number not allowed")
    return True

check_positive(1)
check_positive(-5)
