#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

int main()
{
    string filename = "stats.txt"; // assign string to filename
    ifstream input;
    input.open(filename); // open file

    if (input.fail()) // if file doesn't open
    {
        cout << "There was an error opening the file " << filename << endl;
        exit(1);
    }

    while (input) // while file is open
    {
        string line; // string to hold line
        getline(input, line, ':'); // get line with : as delimiter

        int population; // int to hold population
        input >> population; // get population

        input >> ws; // ignore whitespace

        if (!input) // if input is false
        {
            break; // break out of loop
        }

        cout << "'" << line << "'" // print line
             << " -- '" << population << "'" << endl; // print population
    }

    input.close(); // close file

    return 0;
}
