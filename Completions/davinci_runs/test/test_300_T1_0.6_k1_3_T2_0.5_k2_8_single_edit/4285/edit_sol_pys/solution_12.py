#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

int main() {
    string line;
    string word;
    stringstream ss;
    ifstream inFile;
    inFile.open("test.txt");
    vector<string> vec;
    
    if (inFile.is_open()) {
        while (getline(inFile, line)) {
            ss << line;
            while (ss >> word) {
                vec.push_back(word);
            }
            ss.clear();
        }
    } else {
        cout << "Error opening file." << endl;
    }

    for (auto i : vec) {
        cout << i << endl;
    }

    return 0;
}
