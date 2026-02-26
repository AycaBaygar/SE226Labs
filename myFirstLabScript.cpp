#include <iostream>
#include <string>

using namespace std;

int main() {
    string name;
    string student_id;

    cout << "What is your name?" << endl;
    cin >> name;

    cout << "Hello " << name << "." << endl;

    cout << "What is your Student ID?" << endl;
    cin >> student_id;

    cout << "Your ID is " << student_id << "." << endl;



    int total_seconds, hours, minutes, seconds, remaining_seconds;

    cout << "Enter total seconds: ";
    cin >> total_seconds;

    hours = total_seconds / 3600;
    remaining_seconds = total_seconds % 3600;
    minutes = remaining_seconds / 60;
    seconds = remaining_seconds % 60;

    cout << total_seconds << " seconds is " << hours << " hours, "
         << minutes << " minutes, and " << seconds << " seconds." << endl;



    double x1, y1, x2, y2, distance;

    cout << "Enter coordinates for the first point:" << endl;
    cout << "x1: "; cin >> x1;
    cout << "y1: "; cin >> y1;

    cout << "Enter coordinates for the second point:" << endl;
    cout << "x2: "; cin >> x2;
    cout << "y2: "; cin >> y2;

    distance = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));

    cout << "Distance = " << distance << endl;



    cout << "*******\n *****\n  ***\n   *" << endl;

    return 0;
}









