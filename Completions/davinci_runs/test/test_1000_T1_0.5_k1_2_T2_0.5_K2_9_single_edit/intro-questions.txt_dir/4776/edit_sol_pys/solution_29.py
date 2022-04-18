#include <iostream>
#include <string>


class File
{
public:
	File(string name, int size)
	{
		this->name = name;
		this->size = size;
	}

	string getName()
	{
		return name;
	}

	int getSize()
	{
		return size;
	}

private:
	string name;
	int size;
};

class Node
{
public:
	Node *next;
	File *file;

	Node(File *file)
	{
		this->file = file;
		next = NULL;
	}
};

class LinkedList
{
public:
	Node *head;
	Node *tail;

	LinkedList()
	{
		head = NULL;
		tail = NULL;
	}

	void add(File *file)
	{
		Node *node = new Node(file);

		if (head == NULL)
		{
			head = node;
			tail = node;
		}
		else
		{
			tail->next = node;
			tail = node;
		}
	}

	void print()
	{
		Node *node = head;

		while (node != NULL)
		{
			cout << node->file->getName() << " " << node->file->getSize() << endl;
			node = node->next;
		}
	}
};

using namespace std;

int main()
{
	LinkedList linkedList;

	File *file1 = new File("file1", 100);
	File *file2 = new File("file2", 200);
	File *file3 = new File("file3", 300);

	linkedList.add(file1);
	linkedList.add(file2);
	linkedList.add(file3);

	linkedList.print();
}
