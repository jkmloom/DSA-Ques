#include<iostream>

int chcase(char character){
    if (character >= 'a' && character <= 'z'){
        return 1;
    }else if (character >= 'A' && character <= 'Z'){
        return 2;
    }else{
        return 3;
    }
}

int main(){
    char value_in;
    std::cout << "Enter a character:\t";
    std::cin >> value_in;
    std::string char_input_error = "Invalid input! value passed in chcase() should be of character type.";
    
    if (chcase(value_in) == 1){
        std::cout << "Lowercase";
    }else if(chcase(value_in) == 2){
        std::cout << "Uppercase";
    }else{
        std::cout << char_input_error;
    }

    return 0;
}

// Implicit type conversion : the compiler automatically converts a value from one data type to another without needing explicit instructions from the programmer