#  Write a python script to
# Form a list of K random numbers within a limit N where K and N are set by the user. Minimum value of K should be 10.
# Define a function (or two functions) to return the composite numbers and prime numbers of this list as two separate lists.
# Determine the square of all prime numbers and square root of all composite numbers
# Plot both prime numbers Vs their squares and composites Vs their square roots on the same figure object as scatterplots. ( two different subplots on the same figure object)

import random
import math
import matplotlib.pyplot as plt

# Step 1: User input for K and N, with K having a minimum value of 10
K = int(input("Enter the number of random values (K), at least 10: "))
while K < 10:
    K = int(input("K should be at least 10. Enter again: "))
N = int(input("Enter the upper limit for random values (N): "))

# Generate K random numbers within the limit N
random_numbers = [random.randint(1, N) for _ in range(K)]
print("Random numbers:", random_numbers)

# Step 2: Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Step 3: Separate prime and composite numbers
def get_prime_and_composite(numbers):
    primes = [num for num in numbers if is_prime(num)]
    composites = [num for num in numbers if num > 1 and not is_prime(num)]
    return primes, composites

primes, composites = get_prime_and_composite(random_numbers)
print("Primes:", primes)
print("Composites:", composites)

# Step 4: Calculate the square of primes and the square root of composites
prime_squares = [p ** 2 for p in primes]
composite_sqrt = [math.sqrt(c) for c in composites]

# Step 5: Plot the data
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Plot primes vs their squares
ax1.scatter(primes, prime_squares, color="blue", label="Prime Squares")
ax1.set_title("Prime Numbers vs Their Squares")
ax1.set_xlabel("Prime Numbers")
ax1.set_ylabel("Square of Prime Numbers")
ax1.legend()

# Plot composites vs their square roots
ax2.scatter(composites, composite_sqrt, color="green", label="Composite Square Roots")
ax2.set_title("Composite Numbers vs Their Square Roots")
ax2.set_xlabel("Composite Numbers")
ax2.set_ylabel("Square Root of Composite Numbers")
ax2.legend()

# Show plot
plt.tight_layout()
plt.show()
