def addition(func):
    def wrapper(*args, **kwargs):
        total_sum = func(*args, **kwargs)
        return total_sum

    return wrapper


@addition
def total(num):
    total_sum = sum(num)
    return total_sum


result = total([1, 2, 3])
print(result)
