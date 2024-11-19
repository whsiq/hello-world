def is_prime(number):
    if number == 0 or number == 1:
        return False
    factors = [1, number]
    for i in range(3, number - 1):
        if (number % i == 0):
            factors.append(i)
    if (len(factors) > 2):
        return False
    return True