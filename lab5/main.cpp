#include <iostream>

using namespace std;


double solveSeriesRecursive(int n) {

    if (n == 1) {
        return 1.0;
    }


    double term;
    if (n % 2 == 0) {
        term = -1.0 / n;
    } else {
        term = 1.0 / n;
    }


    return term + solveSeriesRecursive(n - 1);
}

int main() {
    int n;
    cout << "Question 4 - Enter the value of n: ";
    cin >> n;

    if (n <= 0) {
        cout << "Please enter a positive integer." << endl;
    } else {
        double result = solveSeriesRecursive(n);
        cout << "Series Sum (S_" << n << "): " << result << endl;
    }

    return 0;
}