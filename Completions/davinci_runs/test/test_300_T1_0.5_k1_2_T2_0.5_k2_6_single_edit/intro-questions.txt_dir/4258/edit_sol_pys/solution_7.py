#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main(){

   ifstream inputFile;
   string name;
   int age;

   inputFile.open("file.txt");
   if(!inputFile){
      cout << "Error opening file" << endl;
      return 0;
   }

   while(inputFile >> name >> age){
      cout << name << " " << age << endl;
   }

   inputFile.close();

   return 0;
}
