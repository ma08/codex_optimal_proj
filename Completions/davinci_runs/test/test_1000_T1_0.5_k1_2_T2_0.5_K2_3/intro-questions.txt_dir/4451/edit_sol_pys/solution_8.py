#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

int main()
{
    string filename = "stats.txt"; //set filename to stats.txt
    ifstream input;
    input.open(filename); //open file

    if (input.fail()) //if fail to open file, print error message
    {
        cout << "There was an error opening the file " << filename << endl;
        exit(1); //exit program
    }

    while (input) //while input is open
    {
        string line; //create string line
        getline(input, line, ':'); //getline from input file

        int population; //create integer population
        input >> population; //set population to the input

        input >> ws; //set whitespace

        if (!input) //if input fails to open
        {
            break; //break out of loop
        }

        cout << "'" << line << "'" //print line
             << " -- '" << population << "'" << endl; //print population
    }

    input.close(); //close input

    return 0; //return 0
}
