// Lecture 1 was all theory hence, in the "cpp_basics" directory the file's naming is starting from '2'

#include<iostream>
using namespace std;

// starting function
int starter(){
    cout << "Namaste Duniya" << endl;
    cout << "@jkmloom" << endl;

    return 0;
}


// main function
int main(int argc, char const *argv[])
{
    // called the stater function
    starter();

    int age = 25;
    float grade = 9.7;
    bool is_fat = true; // true = 1, and false = 0
    char alpha = 'a';
    double price = 19827.8364;
    
    string str_value = "Namaste"; // std::string
    char word[] = "Anime";

    cout << age << " | " << sizeof(age) << " byte/s" << endl;
    cout << grade << " | " << sizeof(grade) << " byte/s" << endl;
    cout << is_fat << " | " << sizeof(is_fat) << " byte/s" << endl;
    cout << alpha << " | " << sizeof(alpha) << " byte/s" << endl;
    cout << price << " | " << sizeof(price) << " byte/s" << endl;

    cout << str_value << " | " << sizeof(str_value) << " byte/s" << endl;
    cout << word << " | " << sizeof(word) << "byte/s" << endl;

    return 0;
}
