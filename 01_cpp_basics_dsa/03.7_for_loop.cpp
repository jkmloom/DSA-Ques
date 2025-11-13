#include<iostream>

using namespace std;

int main(){
    // for(int i = 1; i <= 10; i++){
    //     cout << i << " ";
    // }
    // cout << endl;

    // -----------------------

    // sum of numbers from 1 to n
    int sum = 0;
    int n;
    
    cout << "Enter trhe value of n:\t";
    cin >> n;

    for(int i = 1; i <= n; i++){
        sum += i;
    }

    cout << "Sum = " << sum << endl;
    return 0;
}