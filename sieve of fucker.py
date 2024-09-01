# create a main function
def main():
    # import the `math.sqrt()` function from math module
    from math import sqrt
    # NOTE: this will import `sqrt()` ONLY; in addition no need to do `math.sqrt()`

    # exception handling
    try:

        # ask the user to enter a number
        n = int(input("\nPlease Enter A Value for 'n': "))

        # create an array / list to hold the prime numbers
        # NOTE: I call it arrays... its not arrays
        '''
        if you use Java, you will know that we have Primitive Data Types
        and also Object Data Types
        Example of Primitive Data Types:
            - int
            - char
            - float
            - double
        Example of Object Data Types:
            - String
            - Integer
        Now, "arrays" are primitive ( in the case of Java ---> don't know for other )
        and "list" are "objects"
        Therefore, you can do thing such as creating an array that looks like this:
            array = ["hello", True, 4, "world", 69.69]
        >Reason why list are not arrays
        '''
        # populate the array with list comprehension
        # starting from '2' because '0' and '1' will always be not prime
        prime_numbers = [x for x in range(2, n+1)]

        # iterate from 2 to square root of `n`
        # NOTE: check the algorithm to find the explanation
        for i in range(2, int(sqrt(n) + 1)):
            # NOTE: type "casted" square root as it is a float value
            # iterate from ($i^{2}$) to (n + 1) ==> kinda like length of array
            for j in range(i*i, n+1, i):
                # move in step of `i`
                # mark the value at `prime_numbers[j - 2]` to None or some character
                # NOTE: will explain why steps of `i` and `prime_numbers[j - 2]`
                prime_numbers[j - 2] = None

        '''
        The mistake that I was doing it iterating from 2 to square root of `n`
        This is wrong because when it will find values such as 2, 3, 5 which
        are themselves of multiples of 2, 3 and 5 ( and so on ) respectively

        Hence, we need to iterate from the power of `i`; for example:
            i = 2
            i*i = 4
            OR
            i = 3
            i*i = 9
            ...
        Therefore, it will start "removing" / "iterating" from 4 and miss the '2'
        Now, this is the reason that we move in step of `i`.
        Because we don't want this:
            for j in range(i*i, n+1):
                print(j)
            OUTPUT:
                4, 5, 6, ... n + 1
        Thus, we need to step in `i`
        ---
        Now why `prime_numbers[j - 2]`?
        Simple, how does arrays working in most programming languages like:
            - Python
            - Java
            - Rust
            - Go
            - C ( the greatest of all time ---> if you can do it in C; you can do it everywhere )
        >There are programming languages that do not start with 0
        >Like:
        >- Lua ( why! why do you not start at 0... self-plug: https://github.com/Sunhaloo )
        >- MatLab ( if you consider that a programming language )
        ---
        List / Arrays starts with the value '0'
        Therefore if we are starting `i = 2` then the index will start at '2' ( instead of '0' )
        '''

        # remove all none values
        prime_numbers = [x for x in prime_numbers if x is not None]

        '''
        Similar to `range(len(array))`; we can simply to `array`
        Its like we are doing something like:
            for index, value in enumerate(prime_numbers):
                print(f"Index = {index} | Value: {value}")
        '''

        # output the array
        # print(prime_numbers)

        # output the numbers in a file
        # 'x' mode; create the file if it has not been created
        with open("output.txt", 'x') as file:
            
            # output the contents of array to the file
            for index, value in enumerate(prime_numbers):
                # in this format
                file.write(f"Index = {index} | Value: {value}\n")

    # if user does not input integer numbers
    except ValueError:
        print("\nPlease Enter Integer Numbers Only!!!\n")

'''
    NOTE: no need to add this
    you have simply wrote
    `main()` at the bottom of the file
'''

# runs this file
if __name__ == '__main__':
    # runs the main function
    main()
