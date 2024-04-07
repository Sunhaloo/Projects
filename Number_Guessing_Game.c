// SIMPLE Number Guessing Game
// AUTHOR: S.Sunhaloo
  // Will prompt the user to enter a number between 1 to 10;
  // Will provide result accordingly

// Include standard input / output header
#include <stdio.h>
// Include standard library header
#include <stdlib.h>
// Include time header / library
#include <time.h>
// Include string header / library
#include <string.h>

// FUNCTION rand_num_generation(DECLARE user_guess: INTEGER)
void rand_num_generation(int user_guess)

{

  // Set seed
    // Will be able to create other random numbers when running program
    // Random Numbers will NOT stay in memory
  srand(time(NULL));

  // DECLARE random_number: INTEGER
    // Need to be 11; if not, will only output random numbers in range of 0 to 9
  int random_number = rand() % 11;

  // Check if user's input is equal to random numbers generated
  if(random_number == user_guess){

    printf("\nYou have guessed the Right Number!\n");

  }
    else if(user_guess < 0 || user_guess > 10){

      printf("\nYou have not entered a number that is in the range!\n");

    }
    else{

      printf("\nYou have not guessed the correct number!\n");
      printf("\nRandom Number was: %d\n", random_number);
      
    }


}

int main()

{

  // DECLARE user_guess: INTEGER
  int user_guess;

  // Ask the user to enter a number from 1 to 10
  printf("\nPlease Enter A Number ( From 0 To 10 ): ");
  scanf("%d", &user_guess);

  // Call the Function `rand_num_generation` to provide result
  rand_num_generation(user_guess);

  printf("\n");

  return 0;

}