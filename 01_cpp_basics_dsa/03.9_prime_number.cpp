// Check if a number is prime or not

#include<iostream>

using namespace std;

int main(){
    int n;
    bool is_prime;
    
    while (true){
        cout << "Enter a number:\t";
        cin >> n;
        
        for (int i = 2; i <= n-1; i++){
            if(n%i == 0){
                is_prime = 0;
                break;
            } else{
                is_prime = 1;
            }
        }

        if(is_prime == true){
            cout << "Prime Number" << endl;
        } else{
            cout << "Not a Prime Number" << endl;
        }
    }
    return 0;
}