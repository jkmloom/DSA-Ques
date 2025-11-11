// conditional statements
// Voting eligibility

#include<iostream>

using namespace std;

int main(){
    int age;
    char nation, permition = 'y';

    cout << "Are you Indian? (y/n):\t";
    cin >> nation;

    if (nation == permition){
        cout << "Enter your age:\t";
        cin >> age;

        if (age > 0 && age < 150){
            if (age >= 18){
                cout << "Go and vote!";
            }else{
                cout << "You are younger than the legal voting age in India.";
            }
        }else{
            cout << "Invalid age..!";
        }
    }else{
        cout << "You need to be Indian to vote in India";
    }

    return 0;
}