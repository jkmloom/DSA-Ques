// do-while loop

#include<iostream>

using namespace std;

int main(){
    int n = 10;
    int i = 1;

    do{
        cout << "Line executed " << i << " times" << endl;
        i++;
    } while(i <= n);

    return 0;
}