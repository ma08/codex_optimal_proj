#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main(){
    string str;
    ifstream inFile;
    inFile.open("test.txt");
    while(!inFile.eof()){
        getline(inFile,str);
        cout<<str<<endl;
    }
    inFile.close();
    return 0;
}
