#include<iostream>
#include<typeinfo>

using namespace std;


int main(int argc, char const *argv[])
{
    // type casting: converting data types
    // 1. type conversion (implicit process: compiler auto-do it)
    float grade = 'A';
    int value = grade; // ASCII for 'A' is 65
    cout << value << endl;
    cout << typeid(value).name(); // i stands for integer

    // 2. type casting (explicit process: have to be done manually)
    

    return 0;
}
