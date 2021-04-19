def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Tests
print(is_prime(2147483647))
print(is_prime(4))
print(is_prime(5))
print(is_prime(6))
print(is_prime(7))
print(is_prime(8))
print(is_prime(9))
print(is_prime(10))
print(is_prime(121))
print(is_prime(122))
print(is_prime(7919))
print(is_prime(-10))
print(is_prime(0))
print(is_prime(1))
print(is_prime(2))
