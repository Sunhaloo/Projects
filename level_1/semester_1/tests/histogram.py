def main():
    # import the `randint()` function from the random module
    from random import randint
    # create a 1D-Array to hold the generated random numbers
    random_numbers_range = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # increment the counter ---> based upon random number generated
    for i in range(100):
        # create the random number
        random_number = randint(0, 99)
        # populate the array
        random_numbers_range[(random_number  -1)// 10] += 1
        # NOTE: why `(random_number - 1)`? Just trace the function when
        # `random_number = 20`; you will see why we added that `- 1`

    # create and populate the "histogram" with zeros
    histogram = []
    for i in range(10):
        # create a 1D-array that will act the each row of a 2D-list
        row =[]
        for j in range(10):
            # append '0' to that 1D-list
            row.append(0)
        # append that "row" to the outer list
        histogram.append(row)

    # start writing to the "histogram" / 2D-list
    for i in range(len(random_numbers_range)):
        # add numbers such as 10, 20, 30, ..., 90
        for j in range(0, random_numbers_range[i] // 10 + 1):
            '''
            for the histogram, we have flipped the array 90 degrees?
            Basically the row has becomes the columns and the columns have become the rows
            '''
            # [9-j] ==> find the specific position ( "row-wise" )
            histogram[9 - j][i] = (j + 1) * 10
        '''
        if "number" does not finish with 0 like 10, 90 etc
        if instead the "number" is like 37, 23, 99
        the 30, 20, 90 part will be taken care by the above "part"
        but for the 7, 3, 9 that remains, this is where the modulus comes into play
        '''
        histogram[9 - j][i] = random_numbers_range[i] % 10

    # output the histogram
    for i in range(10):
        for j in range(10):
            '''
            if we output like `histogram[j][i]`
            ==> we are going to get all the values starting from the last column
            example:
                0 0 6 10
                0 0 0 10
                0 0 0 8
            hence, we print it out normally
            '''
            print(f"{histogram[i][j]}\t\t", end="")
        print()

    print('-'*150)

    # optionally output the total number count
    for i in random_numbers_range:
        # simply display the values of the 1D-array
        print(f"{i}\t\t", end="")
    print()
    
    print('-'*150)

    # output the ranges below each "columns"
    # for 0 to 100, output the numbers in step of 10
    for i in range(0, 100, 10):
        print(f"{i}-{i + 10}\t\t", end="")


if __name__ == '__main__':
    main()
