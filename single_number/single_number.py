'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    dict = {}

    for i in range(0,len(arr)):
        if arr[i] not in dict:
            dict[arr[i]] = 1
        else:
            dict[arr[i]] = 0

    for i in dict:
        if dict[i] == 1:
            return i
    

            



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")