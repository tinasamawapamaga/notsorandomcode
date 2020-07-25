import textwrap

"""
Program cuts up a paragraph in put into
strings of defined length.
"""

def wrap(string, max_width):
    l= list()
    for i in range(0,len(string),max_width): 
        l.append(string[i:i+max_width])
    return "\n".join(l)
    
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
