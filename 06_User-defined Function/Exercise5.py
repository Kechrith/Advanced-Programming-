"""
(Twin  primes)  Twin  primes  are  a  pair  of  prime  numbers  that  differ  by  2.  For  example,  3  and  5  are 
twin primes, 5 and 7 are twin primes, and 11 and 13 are twin primes.  
Create a function called is_prime that checks whether a given number is a prime or not. Then, create 
another  function  called  generate_twin_primes  that  returns  all  the  twin  primes  less  than  1200.  
Write a test program that displays all twin primes less than 1200.
"""

# Function to check if number is prime
def is_prime(n):
    if n < 2:
        return False
    
    # Check for from 2 to n-1
    for i in range(2, n):

        #if divisible, not prime 
        if n % i == 0:
            return False
        
    #if no divisors, it is prime
    return True

# Function to generate twin primes less than 1200
def generate_twin_primes():

    # Loop through numbers
    for i in range(3, 1200):
        if is_prime(i) and is_prime(i + 2):
            print(i, i + 2)

# Call function
print("Twin primes less than 1200:")
generate_twin_primes()
