// Loops are used to repeat a part of code/program

#include<iostream>

using namespace std;

int main(){
    // int count = 1;

    // while(count <= 5){
    //     cout << count << " ";
    //     count++;
    // }
    // cout << endl;

    int number, count = 1;
    cout << "Enter an integer value:\t";
    cin >> number;

    while(count <= number){
        cout << count << " ";
        count++;
    }

    return 0;
}