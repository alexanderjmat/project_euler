# Largest prime factor
#Problem 3

#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

p3_number = 600851475143
p3_primes = []

for num in list(range(2, p3_number + 1)):
    if p3_number % num == 0:
        for number in list(range(2, num + 1)):
            if 



