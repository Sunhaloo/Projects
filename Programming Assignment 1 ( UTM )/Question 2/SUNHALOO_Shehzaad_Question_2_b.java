// Question 2 - Part (b)
// Author: S.Sunhaloo
// Date: 31 May @ 9:20

public class SUNHALOO_Shehzaad_Question_2_b {
    public static void main(String[] args) {

        // DECLARE ch_output: INTEGER
            // hold the number of character to print
        int ch_output = 3;
        // DECLARE N: INTEGER
            // hold the original amount of lines to print
        int N = ch_output;

        // number of lines to print / output
        for(int i = 0; i < N; i ++){
            // move it to the other side
            for(int x = 0; x < i; x++){
                // as we are using print function, the <Space> character will be on the same line
                /* 
                    in addition, we are using the same amount / same number of iteration / loop
                    ==> same number of <Space> output the same as `ch_output`
                */
                System.out.print(" ");
            }

            // number of character to output ---> in single line
            for(int j = 0; j < ch_output; j++){
                // output the character '*'
                System.out.print("*");
            }

            // decrement the number of character to print / output by 1
            ch_output -= 1;
            // add a println function to change the line ---> else will print in the same line as using print function
            System.out.println();
        }

    }
}
