#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

int main()
{
    string filename = "stats.txt";
    ifstream input;
    input.open(filename);

    if (input.fail())
    {
        cout << "There was an error opening the file " << filename << endl;
        exit(1);
    }

    while (input)
    {
        string line;
        getline(input, line, ':');

        int population;
        input >> population;

        input >> ws;

        if (!input)
        {
            break;
        }

        cout << "'" << line << "'" << " -- '" << population << "'" << endl;
    }

    input.close();

    return 0;
}
