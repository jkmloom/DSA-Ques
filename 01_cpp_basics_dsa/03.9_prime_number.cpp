// Check if a number is prime or not

#include<iostream>

using namespace std;

int main(){
    int in_num;
    bool is_prime = true;

    cout << "Enter a number to check if it's prime:\t";
    cin >> in_num;

    for(int i=2; i < in_num; i++){
        if(in_num % i == 0){ // not a prime number
            is_prime = false;
            break;
        }
    }
    if (is_prime == true){
        cout << "Prime number";
    } else{
        cout << "Not a Prime Number";
    }

    return 0;
}