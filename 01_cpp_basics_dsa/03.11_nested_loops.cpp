// printnig * pattern using nested for loop
#include<iostream>

using namespace std;

int main(){
    int x, y;
    cout << "Enter the nmber of row:\t";
    cin >> x;
    cout << "Enter the number of columns:\t";
    cin >> y;

    for(int i = 1; i <= x; i++){
        for(int j = 1; j <= y; j++){
            cout << "* ";
        }
        cout << endl;
    }

    return 0;
}