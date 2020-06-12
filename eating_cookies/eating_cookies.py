'''
Input: an integer
Returns: an integer
'''

def get_factorial(n):
    count = n
    factorial = 1

    for i in range(0,n):
        factorial *= count
        count -= 1

    return factorial

def eating_cookies(n):
    # Your code here
    # print(get_factorial(n),get_factorial(3), get_factorial(n-3))
    # return (get_factorial(n)/(get_factorial(3) * get_factorial(n-3))) 
    cookies = n
    ways = 0

    if cookies == 0:
        return ways
    
    if n % 3 != 0:
        ways += int(n/3)
        print("hi",ways, n%3)
    else:
        ways += int(n/3) + 1
    
    if n % 2 == 0:
        ways += int(n/2)
    else:
        ways += int(n/2) + 1
    
    ways += n

    eating_cookies(cookies - 1)


    
if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 4

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

