
import sys 
  
def main(): 
    key = sys.stdin.readline() 
    key_table = build_key_table(key) 
    plaintext = sys.stdin.readline() 
    ciphertext = encrypt(key_table, plaintext) 
    print(ciphertext) 
  
def build_key_table(key): 
    key_table = [[None for _ in range(5)] for _ in range(5)] 
    key_set = set() 
    row = 0 
    col = 0 
  
    for char in key: 
        if char == ' ': 
            continue 
        if char == 'q': 
            continue 
        if char in key_set: 
            continue 
        key_set.add(char) 
        key_table[row][col] = char 
        col += 1 
        if col == 5: 
            row += 1 
            col = 0 
  
    for char in 'abcdefghiklmnoprstuvwxyz': 
        if char in key_set: 
            continue 
        key_set.add(char) 
        key_table[row][col] = char 
        col += 1 
        if col == 5: 
            row += 1 
            col = 0 
  
    return key_table 
  
if __name__ == '__main__': 
    main() 
