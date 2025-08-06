#Prime number checker

def is_prime(num):
    for x in range(2, num):
        if num % x == 0:
            return False
    return True
            

print(is_prime(7))

