#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

int main(){
	//create a file
	ofstream myfile;
	myfile.open("file.txt");
	myfile<<"this is a file\n"
		<<"this is a file\n"
		<<"this is a file\n"
		<<"this is a file\n"
		<<"this is a file\n"
		<<"this is a file\n"
		<<"this is a file\n"
		<<"this is a file\n"
		<<"this is a file\n"
		<<"this is a file\n"
		<<"this is a file\n"
		<<"this is a file\n"
		<<"this is a file\n"
		<<"this is a file\n";
	myfile<<"this is a file\n";
	myfile.close();

	//read a file
	ifstream myfile2;
	myfile2.open("file.txt");
	string line;
	if(myfile2.is_open()){
		while(getline(myfile2,line)){
			cout<<line<<"\n";
		}
	}
	myfile2.close();

	//create a file
	ofstream myfile3;
	myfile3.open("file2.txt");
	myfile3<<"this is a file\n"
		<<"this is a file\n"
		<<"this is a file\n"
		<<"this is a file\n"
		<<"this is a file\n"
		<<"this is a file\n"
		<<"this is a file\n"
		<<"this is a file\n"
		<<"this is a file\n"
		<<"this is a file\n"
		<<"this is a file\n"
		<<"this is a file\n"
		<<"this is a file\n"
		<<"this is a file\n";
	myfile3.close();

	//read a file
	ifstream myfile4;
	myfile4.open("file2.txt");
	if(myfile4.is_open()){
		string line;
		stringstream ss;
		while(getline(myfile4,line)){
			ss<<line;
		}
		string token;
		while(getline(ss,token,' ')){
			cout<<token<<"\n";
		}
	}
	myfile4.close();
}
