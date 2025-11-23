// print factorial of a number N

#include<iostream>

using namespace std;

int main(){
    int fact = 1;
    int N;
    cout << "Enter a number:\t";
    cin >> N;

    for(int i = 1; i <= N; i++){
        fact = fact * i;
    }
    cout << "Factorial : " << fact;

    return 0;
}