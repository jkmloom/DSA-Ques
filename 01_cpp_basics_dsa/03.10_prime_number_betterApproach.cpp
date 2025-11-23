// check prime number (better approach than 03.9)

#include<iostream>

using namespace std;

int main(){
    // check prime numbers using their factors
    int inNum;
    bool isPrime = true;

    cout << "Enter a number:\t";
    cin >> inNum;

    for(int i=2; i*i <= inNum; i++){
        if(inNum % i == 0){
            isPrime = false;
            break;
        }
    }

    if(isPrime == true){
        cout << "Prime Number";
    } else{
        cout << "Composite Number";
    }

    return 0;
}