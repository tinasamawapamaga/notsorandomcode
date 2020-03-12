def split_and_join(line):
    # write your code here
    form=line.split(" ")
    return "-".join(form)
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
