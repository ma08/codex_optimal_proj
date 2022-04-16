#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char* argv[])
{
	if(argc < 3){
		cout << "please enter two file names" << endl;
		return 1;
	}
	
	ifstream infile1(argv[1]);
	ifstream infile2(argv[2]);
	
	string line1, line2;
	vector<string> lines1, lines2;
	
	while(getline(infile1, line1)){
		lines1.push_back(line1);
	}
	
	while(getline(infile2, line2)){
		lines2.push_back(line2);
	}
	
	if(lines1.size() != lines2.size()){
		cout << "the two files are not the same" << endl;
		return 1;
	}
	
	for(int i = 0; i < lines1.size(); i++){
		if(lines1[i] != lines2[i]){
			cout << "the two files are not the same" << endl;
			return 1;
		}
	}
	
	cout << "the two files are the same" << endl;
	return 0;
}
