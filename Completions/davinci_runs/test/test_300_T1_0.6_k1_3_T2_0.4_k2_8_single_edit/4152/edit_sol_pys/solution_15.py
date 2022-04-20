#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ofstream out("myfile.txt");
    if (out.is_open())
    {
        out << "Hello World!" << endl;
        out.close();
    }
    else
    {
        cout << "Cannot open file for writing." << endl;
    }

    ifstream in("myfile.txt");
    if (in.is_open())
    {
        string line;
        while (getline(in, line))
        {
            cout << line << endl;
        }
        in.close();
    }
    else
    {
        cout << "Cannot open file for reading." << endl;
    }

    return 0;
}
