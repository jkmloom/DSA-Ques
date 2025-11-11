// even/odd number

#include<iostream>

using namespace std;

int main(){
    int number;
    cout << "Enter a number:\t";
    cin >> number;

    if (number%2 == 0){
        cout << number << " is an EVEN number..!";
    }else{
        cout << number << " is an ODD number..!";
    }

    return 0;
}