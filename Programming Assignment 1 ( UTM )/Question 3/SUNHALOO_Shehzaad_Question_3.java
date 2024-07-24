// import 'InputMismatchException' to handle exceptions
import java.util.InputMismatchException;
// import Scanner Object
import java.util.Scanner;

public class Question3 {

    // as I said, Java / C are similar in terms of memory management
    // I am going to write the functions first, so that it can "find" in
    // in the main program / function
    // even though this is NOT required

    // FUNCTION encrypt(DECLARE text: STRING, DECLARE key: INTEGER)
    public static void encrypt(String text, int key) {

        System.out.println();

        // output the word "Encrypting" in a asthetic manner
        String welcome = "Encrypting";

        // iterate through the word
        for(int i = 0; i < welcome.length(); i++) {

            // output each character / letter in the string
            System.out.print(welcome.charAt(i));
            // this is similar to passing the argument
            // `flush = True` in Python's `print` function
            System.out.flush();
            
            try {
                // sleep the program for 200ms
                // this is equivalent to Python's `time.sleep(0.2)`
                Thread.sleep(200);
            }
            catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        System.out.println("\n");

        // create an array of characters
        // will be used to convert the "string" `text` into an array of characters
        char[] characters = text.toCharArray();

        // create another array to hold the encrypted text
        // this array will be converted to string later
        // takes the size / length of the array `characters`
        char[] encrypted_array = new char[characters.length];

        // populate the array `encrypted_array`
        // with the value from array `characters` with the offset applied
        for(int i = 0; i < characters.length; i++) {
            // adding value with offset APPLIED to new array
            encrypted_array[i] = (char) (characters[i] + key);
        }

        // convert "contents" of array `encrypted_array` to string
        // `new String()` creates another instance of a class string
        String encrypted_text = new String(encrypted_array);

        // output the ecrypted string to user
        System.out.println("Encrypted Text: " + encrypted_text);

        System.out.println("\nASCII Values of '" + text + "' BEFORE Encryption:");

        // outputs the ASCII values of text / string provided by the user
        // these values will be BEFORE the offset has been applied
        for(int i : characters) {
            System.out.printf("%d ", i);
        }

        System.out.println("\n\nASCII Values of '" + text + "' AFTER Encryption:");

        // outputs the ASCII values of text / string provided by the user
        // these values will be AFTER the offset has been applied
        for(int i : characters) {
            // applying offset
            i += key;
            System.out.printf("%d ", i);
        }

        System.out.println("\n");

    }

    // FUNCTION decrypt(DECLARE text: STRING, DECLARE key: INTEGER)
    public static void decrypt(String text, int key) {

        System.out.println();

        // output the word "decrypting" in a asthetic manner
        String welcome = "Decrypting";

        // iterate through the word
        for(int i = 0; i < welcome.length(); i++) {
            System.out.print(welcome.charAt(i));
            // this is similar to passing the argument
            // `flush = True` in Python's `print` function
            System.out.flush();
            
            try {
                // sleep the program for 200ms
                Thread.sleep(200);
            }
            catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        System.out.println("\n");

        // create an array of characters
        // will be used to convert the "string" `text` into an array of characters
        char[] characters = text.toCharArray();

        // create another array to hold the decrypted text
        // we are going to be converting this array to string later
        // this array uses the same length / size as the array `characters`
        char[] decrypted_array = new char[characters.length];

        // populate the array `decrypted_array`
        // with the value from array `characters` with the offset removed
        for(int i = 0; i < characters.length; i++) {
            // adding value with offset REMOVED to new array
            decrypted_array[i] = (char) (characters[i] - key);
        }

        // convert "contents" of array `encrypted_array` to string
        // `new String()` creates another instance of a class string
        String decrypted_text = new String(decrypted_array);

        // output the ecrypted string to user
        System.out.println("Decrypted Text: " + decrypted_text);

        System.out.println("\nASCII Values of '" + text + "' BEFORE Decryption:");

        // outputs the ASCII values of text / string provided by the user
        // these values will be the values that has NOT been decrypted yet
        for(int i : characters) {
            System.out.printf("%d ", i);
        }

        System.out.println("\n\nASCII Values of '" + text + "' AFTER Decryption:");

        // outputs the ASCII values of text / string provided by the user
        // these values will be the values that has been decrypted
        // back to original / original ASCII values
        for(int i : characters) {
            // removing offset
            i -= key;
            System.out.printf("%d ", i);
        }

        System.out.println("\n");

    }

    // FUNCTION choose(DECLARE choice: INTEGER, DECLARE text: STRING, DECLARE key: INTEGER)
    public static void choose(int choice, String text, int key) {

        // user selects to encrypt message
        if(choice == 1) {

            // call encryption function
            encrypt(text, key);

        }
        // user selects to decrypt message
        else if(choice == 2) {

            // call decryption function
            decrypt(text, key);

        }
        // user select to quit the program
        else if(choice == 3) {

            // terminate the program
            System.out.println("\nGoodbye!\n");
            // its Python equivalent is `exit()`
            System.exit(1);

        }
        else {

            System.out.println("\nSomething Went Wrong... Exiting Program\n");
            System.exit(1);

        }

    }

    public static void main(String[] args) {

        // create Scanner Object
        Scanner user_input = new Scanner(System.in);

        // welcoming the user
        System.out.println("\nEncryption / Decryption Program\n");
        
        // exception handling
        try {

            // ask the user for text to encrypt / decrypt
            System.out.print("Please Enter Text to Encrypt / Decrypt: ");
            // DECLARE user_text: STRING
            String user_text = user_input.nextLine();

            // display choices to user
            System.out.println("\nPress '1' To Encrypt");
            System.out.println("Press '2' To Decrypt");
            System.out.println("Press '3' To Exit\n");

            // ask the user if he wants to encrypt or decrypt
            System.out.print("Encrypt or Decrypt ( Please Input Number! ): ");
            // DECLARE choice: INTEGER
            int choice = user_input.nextInt();

            // key will be hardcoded
            // DECLARE key: INTEGER
            int key = 3;

            // initialised string
            String intialised_string = "I L O V E Y O U A N D I M I S S E D Y O U A L O T";

            /*
             * As my program is a bit like the decryption scene from Mr Robot
             * I need to have a variable that will hold the encrypted version of `initialised_string`
             */
            String encrypted_inialised_string = "L#O#R#Y#H#\\#R#X#D#Q#G#L#P#L#V#V#H#G#\\#R#X#D#O#R#W";

            // call function `choose`
            choose(choice, user_text, key);

            // outputs the character '-', 80 times
            System.out.println("-".repeat(80));

            // encrypt the initialised string
            encrypt(intialised_string, key);

            // outputs the character '-', 80 times
            System.out.println("-".repeat(80));

            // decrypt the initialised string
            decrypt(encrypted_inialised_string, key);
            
        }
        // this block of code will only execute when it finds an exception
        // like when user enters string / float values
        catch (InputMismatchException e) {

            System.out.print("\nPlease Enter '1' or '2' only\n\n");

        }
        // this block of code is always executed
        finally {

            // close the Scanner Object
            user_input.close();

        }

    }
}