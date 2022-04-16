import sys
import os
import csv
import numpy as np
import matplotlib.pyplot as plt


# ===============================================
# ==============  HELPER FUNCTIONS  =============
# ===============================================

def get_file_path():
    """
    This function will return the file path of the file the user wants to open.
    """
    # Check if file path is provided as argument
    if len(sys.argv) == 1:
        # If not, ask user for file path
        file_path = input("Please enter the file path: ")
        if not os.path.isfile(file_path):
            print("File does not exist.")
            sys.exit(1)
    else:
        # If so, check if file exists
        file_path = sys.argv[1]
        if not os.path.isfile(file_path):
            print("File does not exist.")
            sys.exit(1)
    return file_path


def check_file_header(file_path):
    """
    This function checks if the file has a header.
    """
    # Open csv file
    with open(file_path, "r") as csv_file:
        # Read first line
        first_line = csv_file.readline()
        # Check if first line contains a number
        if first_line.split(",")[0].isdigit():
            return False
        else:
            return True


def read_csv_file(file_path, has_header):
    """
    This function reads the csv file and returns the data in a numpy array.
    """
    # Open csv file
    with open(file_path, "r") as csv_file:
        # Read csv file
        csv_reader = csv.reader(csv_file, delimiter=",")
        # Create list of data
        data_list = []
        for row in csv_reader:
            data_list.append(row)
    # Convert list to numpy array
    data_array = np.array(data_list)
    # Check if file has header
    if has_header:
        # If so, remove header
        data_array = np.delete(data_array, 0, axis=0)
    # Convert all data to float
    data_array = data_array.astype(float)
    return data_array


# ===============================================
# ==============  DATA ANALYSIS  ================
# ===============================================

def analyze_data(data_array):
    """
    This function returns the mean, standard deviation and correlation coefficient.
    """
    # Calculate mean
    mean = np.mean(data_array, axis=0)
    # Calculate standard deviation
    std = np.std(data_array, axis=0)
    # Calculate correlation coefficient
    corrcoeff = np.corrcoef(data_array, rowvar=False)
    return mean, std, corrcoeff


# ===============================================
# ==============  DATA PLOTTING  ================
# ===============================================

def plot_data(data_array):
    """
    This function plots the data.
    """
    # Create figure
    fig = plt.figure()
    # Create plot
    ax = fig.add_subplot(111)
    # Plot data
    ax.plot(data_array[:, 0], data_array[:, 1], "o")
    # Show plot
    plt.show()



def main():
    # Get file path
    file_path = get_file_path()
    # Check if file has header
    has_header = check_file_header(file_path)
    # Read csv file
    data_array = read_csv_file(file_path, has_header)
    # Analyze data
    mean, std, corrcoeff = analyze_data(data_array)
    # Print results
    print("Mean: {}".format(mean))
    print("Standard deviation: {}".format(std))
    print("Correlation coefficient: {}".format(corrcoeff))
    # Plot data
    plot_data(data_array)


if __name__ == "__main__":
    main()
