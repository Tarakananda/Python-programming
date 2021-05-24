#Read different types of data from standard input, process them as shown in output format and print the answer to standard output.


#Input format:
#First line contains integer N.
#Second line contains string S.

#Output format:
#First line should contain N x 2.
#Second line should contain the same string S.

#Constraints:
    #0<=N<=10
    #0<=S<=15

 #where S length of string S
 
 
number=int(input())

string=input()

if number > 0:

    if len(string) > 0:

        print(number * 2)

print(string)

