#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;

int main()
{
    string line;
    ifstream file("example.txt");
    if (file.is_open())
    {
        while (getline(file, line))
        {
            cout << line << '\n';
        }
        file.close();
    }

    else cout << "Unable to open file";

    return 0;
}
