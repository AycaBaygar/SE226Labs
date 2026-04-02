#soru1
def factorial(x):
    """Calculates the factorial of x recursively."""
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)


#soru2
term_calc = lambda x, n: (x ** n) / factorial(n)


def exp_x(x, n):
    """Calculates the summation of the e^x series for n terms."""
    total = 0
    for i in range(n):

        total += term_calc(x, i)
    return total



try:
    user_x = float(input("Enter the value of x: "))
    user_n = int(input("Enter the number of terms (n): "))
    print(f"e^{user_x} (first {user_n} terms): {exp_x(user_x, user_n)}")
except Exception as e:
    print("Error:", e)

#soru3
total_s = 0


def solve_series(n):
    """
    Docstring:
    This function calculates the series Sn = 1 - 1/2 + 1/3 - 1/4 ... recursively.
    Logic: The function iterates backwards from n down to 1.
    Sign Handling: Uses the formula (-1)^(n+1) so that even terms are negative
    and odd terms are positive.
    """
    global total_s
    if n < 1:
        return


    term = ((-1) ** (n + 1)) / n
    total_s += term


    solve_series(n - 1)


n_val = int(input("\nEnter n for question 3: "))
solve_series(n_val)
print(f"Series Sum (S_{n_val}): {total_s}")