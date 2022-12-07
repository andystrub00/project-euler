
# Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def is_prime(n):
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if not n % 2 or not n % 3:
        return False
    i = 5
    stop = int(n**0.5)
    while i <= stop:
        if not n % i or not n % (i + 2):
            return False
        i += 6
    return True


if __name__ == "__main__":

    ans_found = True
    while ans_found:
        for i in range(1, 600851475143):
            if 600851475143 % i == 0:
                if is_prime(600851475143//i):
                    print(600851475143//i)
                    ans_found = False
#%%
