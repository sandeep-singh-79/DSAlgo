""" 
implementation options:
1. implement the stacks by dividing the array in to two parts
where the first stack goes from 0 to half the array length
2. Use alternate indices to store the elements of the two stacks
for example, stack one elements are stored at indices 0, 2, 4 ...
and stack 2 elements are stored at odd indices - 1, 3, 5 ...
 """

#Function to push an integer into the stack1.
def push1(a,x):
    #code here
    
#Function to push an integer into the stack2.
def push2(a,x):
    #code here
    
#Function to remove an element from top of the stack1.    
def pop1(a):
    #code here
    
#Function to remove an element from top of the stack2.    
def pop2(a):
    #code here
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

top2=101
top1=-1

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arr = list(map(int,input().strip().split()))
        a = [-1 for i in range(101)] # array to be used for the 2 stacks.
        i=0 # curr index
        while i<len(arr):
            if arr[i] == 1:
                if arr[i+1] == 1:
                    push1(a,arr[i+2])
                    i+=1
                else:
                    print(pop1(a),end=" ")
                i+=1
            else:
                if arr[i+1] == 1:
                    push2(a,arr[i+2])
                    i+=1
                else:
                   print(pop2(a),end=" ")
                i+=1
            i+=1
        top2=101
        top1=-1
        print(' ')

# } Driver Code Ends