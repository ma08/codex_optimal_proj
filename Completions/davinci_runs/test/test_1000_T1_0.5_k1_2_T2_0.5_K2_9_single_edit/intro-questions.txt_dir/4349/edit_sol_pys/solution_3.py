#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
using namespace std;

int main(){
	string str;
	ifstream file1;
	ofstream file2;
	file1.open("input.txt");
	file2.open("output.txt");
	if(file1.is_open()){
		while(getline(file1,str)){
			file2 << str << endl;
		}
	}
	else{
		cout << "Unable to open file";
		exit(1);
	}
	file1.close();
	file2.close();
	return 0;
}
