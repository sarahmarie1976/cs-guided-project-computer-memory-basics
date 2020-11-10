"""
"In order to store strings in memory, each character in the string must be encoded so that it can be stored as binary.
ASCII is one example of a character set. Each character in ASCII can be represented by 7 bits (although they are commonly
stored as 8 bits). Given that, what is the maximum number of characters that could be in the ASCII set?"


A - 128
B - 72
C - 64
D - 140


Answer is:

A - 128

2   * 2     (this is includes 1 and 2 bits for the amount of 2's used) 
4   * 2     (3rd time using it)
8   * 2     (4th time using it)
16  * 2     (5th time using it)
32  * 2     (6th time using it)
64  * 2     (7th time using it)
128 * 2     (8th time using it)    
256   = total ASCII  

"""