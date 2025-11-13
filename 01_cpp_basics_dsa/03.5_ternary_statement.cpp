// 03.5_ternary_statement.cpp
// Just how Unary means 1, and Binary means 2, Ternary means 3

#include<iostream>

int main(){
    // for simple conditional satement
    int n;
    std::cout << "Enter a number:\t";
    std::cin >> n;
    
    // ternary statement
    std::cout << (n >= 0 ? "धनात्मक संख्या" : "ऋणात्मक संख्या") << " | ";
    std::cout << (n >= 0 ? "Positive Number" : "Negative Number") << std::endl;
    
    return 0;
}