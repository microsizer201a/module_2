numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = list()
not_primes = list()
is_prime = True
for i in numbers:
    for j in range(2, len(numbers) - 1):
        if i % j == 0:
            if i != j:
                is_prime = False
                break
            if i == j:
                is_prime = True
                break
    if i == 1:
        continue
    if is_prime == True:
            primes.append(i)
    if is_prime == False:
            not_primes.append(i)
print("Primes:", primes)
print("Not primes:", not_primes)