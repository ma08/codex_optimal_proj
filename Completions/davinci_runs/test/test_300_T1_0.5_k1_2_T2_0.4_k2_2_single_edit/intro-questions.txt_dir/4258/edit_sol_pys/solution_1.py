#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    ifstream input("input.txt");
    ofstream output("output.txt");

    if (input.is_open() && output.is_open())
    {
        string line;
        vector<string> lines;
        while (getline(input, line))
        {
            lines.push_back(line);
        }
        sort(lines.begin(), lines.end());
        for (string s : lines)
        {
            output << s << endl;
        }
    }
    else
    {
        cout << "Error opening file" << endl;
    }
    input.close();
    output.close();
}
