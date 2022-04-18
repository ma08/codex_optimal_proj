
import sys 
def main(): 
  
    # Get the total number of arguements 
    total = len(sys.argv) 
  
    # Get the arguments list 
    cmdargs = str(sys.argv) 
  
    # Print it 
    print ("The total numbers of args passed to the script: %d " % total) 
    print ("Args list: %s " % cmdargs) 
  
    # Check for the arguements passed 
    if total == 2: 
        print ("The script is called: %s" % str(sys.argv[0])) 
        print ("The first arg is: %s" % str(sys.argv[1])) 
    elif total > 2: 
        print ("The script is called: %s" % str(sys.argv[0])) 
        print ("The first arg is: %s" % str(sys.argv[1])) 
        print ("Number of arguments passed: %d" % total) 
  
# Call the main method 
if __name__ == "__main__": 
    main() 
