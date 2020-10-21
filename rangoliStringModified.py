"""Tin Le 20/10/2020
This program is a personal modification to the 
alphabet rangoli challenge from Hackerank. 
The passing function is this one:

def print_rangoli(size):
    # your code goes here
    myStr = 'abcdefghijklmnopqrstuvwxyz'[0:size]
    
    for i in range(size-1, -size, -1):
        x = abs(i)
        line = myStr[size:x:-1]+myStr[x:size]
        print ("--"*x+ '-'.join(line)+"--"*x)
      
However, I modified it to take in 2 additional parameters:
-The original material fabric/string.
-The outer wrapping, fabric, which is taken as the 
first two characters of an input string.
This program then can print fun and creative patterns
that are not limited to just the alphabet and '--' as
the connecting components. 
There might be some printing errors that have not been resolved 
between the size and the length of original string, so the output might not always 
be symmetrical. 
"""

        
def print_rangoli_fun(size,sentence,pattern):
    # your code goes here
    #myStr = 'abcdefghijklmnopqrstuvwxyz'[0:size]
    string = sentence[0:size]

    for i in range(size-1, -size, -1):
        x = abs(i)
        line = string[size:x:-1]+string[x:size]
        print (pattern*x+ '-'.join(line)+pattern*x)

if __name__ == '__main__':
    n = int(input())
    m = input("Enter your rangoli material: ")
    o = input("Enter your rangoli wrapping:\nPlease limit to two characters")[:2]
    print_rangoli_fun(n,m,o)
