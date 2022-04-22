#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	char filename[] = "test.txt";
	ofstream outfile;
	outfile.open(filename);

	string s = "Hello world!\n";
	s += "This is a test file.\n";
	outfile << s;
	outfile.close();

	ifstream infile;
	infile.open(filename);
	while(!infile.eof())
	{
		string line;
		getline(infile, line);
		cout << line << endl;
	}
	infile.close();

	vector<int> v;
	v.push_back(100);
	v.push_back(200);
	v.push_back(300);

	outfile.open(filename);
	for(int i = 0; i < v.size(); i++)
	{
		outfile << v[i] << endl;
	}
	outfile.close();

	infile.open(filename);
	while(!infile.eof())
	{
		int i;
		infile >> i;
		cout << i << endl;
	}
	infile.close();
}
