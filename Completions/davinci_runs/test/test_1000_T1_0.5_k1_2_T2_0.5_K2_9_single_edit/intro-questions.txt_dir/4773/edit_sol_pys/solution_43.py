

import sys
import math

# This solution is a little tricky.
# We can't use any of the standard compression algorithms (LZW, Huffman, etc.)
# because we don't know what the input will be.

So instead, we need to come up with a way to compress the input and still be able
to decode it.

The key insight is that we can use a "macro" to reduce the size of a sequence of
moves that is repeated.

So, we can build a "macro" by starting with the first move, and then continuing
to add moves until we find a repeated sequence.

We then replace the repeated sequence with a 'M' and continue to build the macro.

We repeat this process until we have built a macro that covers the entire input.

We then compare the size of the original input to the size of the macro and
return the smaller one.

def compress(s):
  """Compress the input string using a macro.

  Args:
    s: The string to compress.

  Returns:
    The compressed string.
  """
  # If the string is empty, return it.
  if s == '':
    return s
  
  # If the string has less than 2 moves, return it.
  if len(s) < 2:
    return s
  
  # The compressed string.
  compressed = ''
  
  # The macro string.
  macro = ''
  
  # The current index in the input string.
  index = 0
  
  # The length of the input string.
  length = len(s)
  
  # While there are still moves in the input string.
  while index < length:
    # Get the next move.
    move = s[index]
    
    # If the macro is empty, add the move to the macro.
    if macro == '':
      macro += move
    # Otherwise, if the move is the same as the last move in the macro,
    # add the move to the macro.
    elif move == macro[-1]:
      macro += move
    # Otherwise, if the move is different from the last move in the macro,
    # look for a repeated sequence in the input string.
    else:
      # The length of the repeated sequence.
      repeat_length = 2
      
      # While the repeated sequence is less than the length of the macro,
      # and the repeated sequence is at the end of the input string.
      while repeat_length <= len(macro) and s.endswith(macro[-repeat_length:]):
        # If the repeated sequence is the same length as the macro,
        # we have found a repeated sequence.
        if repeat_length == len(macro):
          # Remove the repeated sequence from the input string.
          s = s[:-repeat_length]
          
          # Add the macro to the compressed string.
          compressed += 'M'
          
          # Reset the macro.
          macro = ''
          
          # Reset the index.
          index = 0
          
          # Reset the length of the input string.
          length = len(s)
          
          # Break out of the loop.
          break
        # Otherwise, increase the length of the repeated sequence.
        else:
          repeat_length += 1
      
      # If we found a repeated sequence, add the move to the macro.
      if repeat_length <= len(macro):
        macro += move
      # Otherwise, add the macro to the compressed string,
      # and add the move to the macro.
      else:
        compressed += macro
        macro = move
    
    # Increase the index.
    index += 1
  
  # If the input string is not empty, add the macro to the compressed string.
  if s != '':
    compressed += macro
  
  # Return the compressed string.
  return compressed

def main():
  # Read the input string.
  s = sys.stdin.readline().strip()
  
  # Compress the input string.
  compressed = compress(s)
  
  # Print the size of the smaller string.
  print min(len(s), len(compressed))

if __name__ == '__main__':
  main()
