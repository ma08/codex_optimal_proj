


#%%
import os
import sys


#%%
def read_input(file):
    """
    file: input file
    return: input array
    """
    with open(file) as f:
        # content = f.readlines()
        content = f.read().splitlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    return content


#%%
def write_output(file, array):
    """
    file: output file
    array: list of results
    """
    with open(file, 'w') as f:
        for item in array:
            f.write("%s\n" % item)


#%%

def main():
    if len(sys.argv) != 3:
        print("Correct usage: wordCount.py <input text file> <output file>")
        exit()
    textFname = sys.argv[1]
    outputFname = sys.argv[2]
    if not os.path.exists(textFname):
        print("text file input %s doesn't exist! Exiting" % textFname)
        exit()
    # write your code here
    input_array = read_input(textFname)
    print(input_array)
    # call the function to get the word count
    output_array = [1, 2, 3]
    # write output to file
    write_output(outputFname, output_array)


#%%
if __name__ == '__main__':
    main()

#%%
