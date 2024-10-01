# create a function to display the 2D-List
def display_2D(the_list: list):
    # NOTE: assuming  that all cols are of the same size

    rows_length = len(the_list)
    cols_length = len(the_list[0])

    # actual printing algorithm
    for i in range(rows_length):
        # uncomment the line below to be able to add blank space between rows
        # print()
        for j in range(cols_length):
            # output the value at that index in a grid like pattern
            print(f"{the_list[i][j]}", end="\t")
        print()


# function to initially create and populate 2D-List with '0'
def create_aparments(rows: int = 12, cols: int = 12) -> list:
    # create a 2D-List
    # create the outer 1D-List
    outer_list = []
    for i in range(rows):
        # create the inner 1D-List(s)
        inner_row_list = []
        for j in range(cols):
            # populate the array with '0'
            inner_row_list.append(0)
        # add the inner 1D-List to the outer 1D-List
        outer_list.append(inner_row_list)

    # return the 2D-List to the main program
    return outer_list


# create a function to populate the "initial" noise level for 100 appartments
def populate_noise_level(appartments: list):
    # import the `randint` function from the random module
    from random import randint
    # NOTE: assuming  that all cols are of the same size

    rows_length = len(appartments)
    cols_length = len(appartments[0])

    # WARNING: we only need to populate the 10 by 10 matrix
    # for i in range(rows_length + 2):
    for i in range(1, 11):
        # for j in range(cols_length + 2):
        for j in range(1, 11):
            '''
            change the value at each index of the 10 by 10 matrix
            to add / change the initial '0' to a "noise level"
            '''
            appartments[i][j] = randint(0, 10)


# function to find the sum of "surrounding" noise level
def sum_noise_level(appartments: list) -> list:
    # create a 2D-List
    outer_sum_noise = []
    for i in range(10):
        inner_sum_noise = []
        for j in range(10):
            # populate the 2D-List with '0'
            inner_sum_noise.append(0)
        # combine the inner 1D-List with outer 1D-List
        outer_sum_noise.append(inner_sum_noise)

    # start finding the sum of surrounding of appartment

    # NOTE: Explanation why we created 12 by 12 originally instead of 10 by 10

    '''
    as we are required to calculate the surrounding "noise level"
    we are going to need a way so that we don't get 'Out of Bounds' error

    KEY:
        x = target
        z = surrounding of the target

    example of 'Out of Bounds' error:

        x   z
        z   z

        hence, in this case we are going to have z + z + z
        but how we are going to find z + z + z

    THUS!!!

    create a bigger 2D-List, fill everything with '0's after that we are going to be able to have something like this:

        0   0   0
        0   x   z
        0   z   z

        therefore, we are going to have 0 + 0 + 0 + 0 + z + 0 + z + z

    because this will work even when we are going to have:

        z   z   z
        z   x   z
        z   z   z

        in this case we will be having: z + z + z + z + z + z + z + z
    '''

    # we are gong to start in the "middle" index of each "appartment"
    # in addition, only using the "inner" 10 by 10 array
    for i in range(1, 11):
        for j in range(1, 11):
            # create a variable that will hold the current noise level
            current_noise = 0

            # calculate the sum of surrounding noise
            current_noise += appartments[i - 1][j - 1]
            current_noise += appartments[i - 1][j]
            current_noise += appartments[i - 1][j + 1]
            current_noise += appartments[i][j - 1]
            current_noise += appartments[i][j + 1]
            current_noise += appartments[i + 1][j - 1]
            current_noise += appartments[i + 1][j]
            current_noise += appartments[i + 1][j + 1]

            # append the value to the respective index in the newly created list `outer_sum_noise`
            # again the list `outer_sum_noise` is only a 10 by 10
            # therefore we need to remove 1 index from both `i` and `j`
            # hence, the will both start at 0 and end at 11
            outer_sum_noise[i - 1][j - 1] = current_noise

    # return the array to the main program
    return outer_sum_noise


# create a function that will be able to flag each apartment at noisy or not
def flag_noisy(list_noise_level: list, threshold: int):

    # the lecturer did not say create another array
    # BUT I WANT TO, THIS IS MY KEYBOARD, COMPUTER, BRAIN, CODE!!!
    # I DO WHATEVER THE FUCK I WANT ( BAD )
    noisy_or_not = [[0 for y in range(10)] for x in range(10)]

    # we don't need to calculate the length of this 2D-List
    # because we already know that its going to be a 10 by 10 grid
    for i in range(10):
        for j in range(10):
            # check if noise level exceed threshold
            if list_noise_level[i][j] > threshold:
                # at this point, flag as noisy in the newly created 2D-List `noisy_or_not`
                noisy_or_not[i][j] = 1
            # if the appartment is not noisy
            else:
                noisy_or_not[i][j] = 0

    # return `noisy_or_not` to the main program
    return noisy_or_not

def main():
    # exception handling
    try:
        # create the 12 by 12 initial matrix
        appartments = create_aparments()
        
        # populate the 2D-List with the their respective noise levels
        populate_noise_level(appartments)

        # cacluate sum of surrounding noise level ( into a new 2D-List )
        sum_noise_level_list = sum_noise_level(appartments)

        # ask the user to enter the noise level threshold
        user_threshold = int(input("\nPlease Enter Noise Threshold Level: "))

        # check that the user value is in range
        while user_threshold < 0 or user_threshold > 100:
            # ==> user did not enter correct level
            print("\nNoise Threshold: 0 to 100")
            # prompt the user again
            user_threshold = int(input("\nPlease Enter Noise Threshold Level: "))

        # call the function that will flag each appartment at noisy or not
        # noisy = 1
        # not noisy = 0

        appartment_noisiness = flag_noisy(sum_noise_level_list, user_threshold)

        # WARNING: For Testing Purposes

        print("\nInitial Noise Level\n")
        
        # call the function to display the 2D-List
        display_2D(appartments)

        print('-'*50)

        print("\nSum of Noise Level\n")

        display_2D(sum_noise_level_list)

        print('-'*50)

        print("\nNoisy / Not Noisy Appartment\n")

        display_2D(appartment_noisiness)

    # if the user does not enter an interger value
    except ValueError as e:
        print(f"\nError: {e}")


# run the main program
if __name__ == '__main__':
    main()
