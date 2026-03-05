n = int(input("Please enter a positive integer greater than 1: "))

steps = 0

while n != 1:
    print(n, end=" -> ")
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    steps += 1

print(1)
print("Total steps:", steps)




while True:
    n = int(input("Please enter a number between 10 and 100: "))
    if 10 <= n <= 100:
        break
    print("Invalid input.", end=" ")

fizz_count = 0
buzz_count = 0
fizzbuzz_count = 0

for i in range(1, n + 1):
    if i % 7 == 0:
        print(f"({i} is skipped)")
        continue

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        fizzbuzz_count += 1
    elif i % 3 == 0:
        print("Fizz")
        fizz_count += 1
    elif i % 5 == 0:
        print("Buzz")
        buzz_count += 1
    else:
        print(i)

print("--- Summary ---")
print("Fizz count :", fizz_count)
print("Buzz count :", buzz_count)
print("FizzBuzz count:", fizzbuzz_count)






n = int(input("Please enter a number between 3 and 9: "))

while n < 3 or n > 9:
    n = int(input("Invalid input. Please enter a number between 3 and 9: "))

for i in range(1, 2 * n):
    if i <= n:
        print("*" * i)
    else:
        print("*" * (2 * n - i))