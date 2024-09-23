def read_key_file() -> list:
    # create a list to hold the "key values"
    key_list = []
    # open the file for read
    key_file = open('key.txt', 'r')
    
    '''
    after opening the file
    we need to read each line of the file
    and then add that value to our array `key_list`
    '''

    # NOTE: we are using `.extend` function because it will not create a 2D-List
    for line in key_file:
        # "add" that value into the array
        key_list.extend(line.split())

    # close the file
    key_file.close()

    # return the list to the main program
    return key_list


def main():
    # call the function to get the "values" from the key file
    key_values = read_key_file()

    # open the actual text file
    text_file = open('text.txt', 'r')
    # open the file that we are going to be creating to write the cipher text
    encrypted_file = open('encryption.txt', 'w')
    # open the file that we are going to be creating to write the plain text
    decrypted_file = open('decryption.txt', 'w')

    # Encrypting
    # for every line in the `text.txt` file
    for line in text_file:
        # create a variable that will hold the current line
        # this current line will be list
        current_line = line.strip().split()

        # for each word in the that "current line"
        for word in current_line:

            # check if that "word" is found in the `key_values` list
            if word in key_values:
                # find the index of the current word
                index_word = key_values.index(word)
                # find the cipher character
                cipher_character = key_values[index_word + 1]
                # write the the encrypted file
                encrypted_file.write(f"{cipher_character} ")

            # if the "word" is NOT found in the key file
            else:
                '''
                this is NOT required at all
                why? because we have create the `text.txt` and also `key.txt` file
                hence, how can we don't have a "word" that does not correspond to a specific
                cipher character
                '''
                # write a blank space
                encrypted_file.write(f" ")

        # change the line in the "encrypted" file
        encrypted_file.write("\n")

    # Decrypting
    # NOTE: here instead of opening the encrypted file for writing, we open for reading
    encrypted_file = open('encryption.txt', 'r')

    # for every line in the `encryption.txt` file
    for line in encrypted_file:
        # create a variable that will hold the current line
        # this current line will be list
        current_line = line.strip().split()

        # for each character in the that "current line"
        for ch in current_line:

            # check if that "character" is found in the `key_values` list
            if ch in key_values:
                # find the index of the current character
                index_word = key_values.index(ch)
                # find the "plain text" character
                plain_character = key_values[index_word - 1]
                # write the the encrypted file
                decrypted_file.write(f"{plain_character} ")

            # if the "character" is NOT found in the key file
            else:
                '''
                this is NOT required at all
                why? because we have create the `text.txt` and also `key.txt` file
                hence, how can we don't have a "character" that does not correspond to a specific
                "plain text" character
                '''
                decrypted_file.write(f" ")

        # change the line in the "decrypted" file
        decrypted_file.write("\n")

    # close the files
    text_file.close()
    encrypted_file.close()
    decrypted_file.close()

# run the main function
if __name__ == '__main__':
    main()
