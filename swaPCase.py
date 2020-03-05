#Programs that read a string from user and 
#turn upper case to lower case and vice versa
#other characters stay the same
def swap_case(s):
    result=''.join([i.lower() if i.isupper() else i.upper() for i in s])
    return result
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
