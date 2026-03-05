#include <iostream>
using namespace std;

int main() {


    int n;
    cout << "Please enter a positive integer greater than 1: ";
    cin >> n;

    int steps = 0;

    while (n != 1) {
        cout << n << " -> ";
        if (n % 2 == 0) {
            n = n / 2;
        } else {
            n = 3 * n + 1;
        }
        steps++;
    }

    cout << 1 << endl;
    cout << "Total steps: " << steps << endl;







    while (true) {
        cout << "Please enter a number between 10 and 100: ";
        cin >> n;
        if (n >= 10 && n <= 100) {
            break;
        }
        cout << "Invalid input. ";
    }

    int fizz_count = 0;
    int buzz_count = 0;
    int fizzbuzz_count = 0;

    for (int i = 1; i <= n; i++) {
        if (i % 7 == 0) {
            cout << "(" << i << " is skipped)\n";
            continue;
        }

        if (i % 3 == 0 && i % 5 == 0) {
            cout << "FizzBuzz\n";
            fizzbuzz_count++;
        } else if (i % 3 == 0) {
            cout << "Fizz\n";
            fizz_count++;
        } else if (i % 5 == 0) {
            cout << "Buzz\n";
            buzz_count++;
        } else {
            cout << i << "\n";
        }
    }

    cout << "--- Summary ---\n";
    cout << "Fizz count : " << fizz_count << "\n";
    cout << "Buzz count : " << buzz_count << "\n";
    cout << "FizzBuzz count: " << fizzbuzz_count << "\n";






    cout << "Please enter a number between 3 and 9: ";
    cin >> n;

    while (n < 3 || n > 9) {
        cout << "Invalid input. Please enter a number between 3 and 9: ";
        cin >> n;
    }

    for (int i = 1; i < 2 * n; i++) {
        int k;
        if (i <= n) {
            k = i;
        } else {
            k = 2 * n - i;
        }

        for (int j = 0; j < k; j++) {
            cout << "*";
        }
        cout << "\n";
    }

    return 0;
}
