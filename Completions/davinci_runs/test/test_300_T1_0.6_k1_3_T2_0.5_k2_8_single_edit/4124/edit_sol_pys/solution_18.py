#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <sstream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int main(){
	int num_vertices, num_edges;
	vector<int> adj_list;
	vector<int>::iterator it;

	string line;
	ifstream inFile;
	inFile.open("graph.txt");
	if(inFile.is_open()){
		//get the number of vertices and edges
		getline(inFile, line);
		stringstream ss(line);
		ss >> num_vertices >> num_edges;

		//put all the edges in the adjacency list
		while(getline(inFile, line)){
			stringstream ss(line);
			int a, b, weight;
			ss >> a >> b >> weight;
			adj_list.push_back(a);
			adj_list.push_back(b);
			adj_list.push_back(weight);
		}
	}
	else{
		cout << "Error: Cannot open file" << endl;
		exit(1);
	}
	inFile.close();

	//print out the adjacency list
	for(it = adj_list.begin(); it != adj_list.end(); it++){
		cout << *it << " ";
	}
	cout << endl;

	return 0;
}
