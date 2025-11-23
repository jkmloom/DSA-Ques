// Lecture 3: Assignment
// Sum of all numbers from 1 to N which are divisible by 3

#include<iostream>

using namespace std;

int main(){
    int N;
    int sum = 0;
    int divNum = 3;

    cout << "Enter a number:\t";
    cin >> N;

    cout << "Numbers divisible by " << divNum << " are: ";
    for(int i; i <= N; i++){
        if (i % divNum == 0){
            cout << i << " ";
            sum += i;
        }
    }
    cout << endl;
    cout << "Sum = " << sum;

    return 0;
}