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
    bool fat = true; // true = 1, and false = 0
    char alpha = 'a';
    
    string str_value = "Namaste"; // std::string
    char word[] = "Anime";

    cout << age << endl;
    cout << grade << endl;
    cout << fat << endl;
    cout << alpha << endl;

    cout << str_value << endl;
    cout << word << endl;
    
    return 0;
}
