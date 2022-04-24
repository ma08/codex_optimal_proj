#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main(){
	vector<string> v;
	ifstream file("file.txt");
	string line;
	while(getline(file, line)){
		v.push_back(line);
	}
	for(int i = 0; i < v.size(); i++){
		cout<<v[i]<<endl;
	}
	return 0;
}
