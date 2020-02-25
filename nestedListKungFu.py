#Given the names and grades for each student in a Physics class of N students, 
#store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

if __name__ == '__main__':
    marksheet = []
    for a in range(int(input())):
        name = input()
        score = float(input())
        #appending to pre-defined list the input values
        marksheet.append([name, score])
    
    #Find the second largest element by creating
    #a set based on scores, makea list from created set and sort that list
    second_highest = sorted(list(set([score for name, score in marksheet])))[1]
    
    #Print the resulting names of people with similar grades on different lines
    #without showing the grades
    print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))
