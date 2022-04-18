#include <iostream>
#include <fstream>
using namespace std;
int main()
{
	ifstream fin;
	fin.open("file.txt");
	string str;
	while(!fin.eof())
	{
		getline(fin,str);
		cout<<str<<endl;
	}
	fin.close();
	return 0;
}
