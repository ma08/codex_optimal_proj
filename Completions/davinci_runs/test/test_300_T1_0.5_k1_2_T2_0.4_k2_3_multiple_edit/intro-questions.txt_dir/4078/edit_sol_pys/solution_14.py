#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int main()
{
    string line, word;
    ifstream myfile("test.txt");

    vector<string> words;

    while (myfile >> word)
    {
        words.push_back(word);
    }

    for (int i = 0; i < words.size(); i++)
    {
        cout << words[i] << endl;
    }

    return 0;
}
