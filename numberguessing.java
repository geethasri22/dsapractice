package tiny_projects.number_guessing_game;

import java.util.Scanner;

public class NumberGuessingGame {

  public static void handleEasyChoice(Scanner scan) {
    System.out.println("A random number has been chosen between 1 and 10.");
    System.out.println("You have 3 attempts. Start guessing!");

    int random = (int) (Math.random() * 10) + 1;

    int chances = 3;

    System.out.println();
    System.out.println();

    while (chances > 0) {
      System.out.print("Enter your guess: ");
      int guess = scan.nextInt();

      if (guess == random) {
        System.out.println("Correct!! You guessed it in 3 attempts!");
        return;
      }
      if (guess < random) {
        System.out.println("Too Low! Try again.");
      }
      if (guess > random) {
        System.out.println("Too High! Try again.");
      }

      chances--;
      if (chances == 1) {
        System.out.println();
        System.out.println("This is you last chance!");
        System.out.println();
      }
    }

    System.out.println(
      "Sorry, you’re out of attempts. The number was " + random
    );
  }

  public static void handleMediumChoice() {
    System.out.println("Medium mode coming soon...");
  }

  public static void handleHardChoice() {
    System.out.println("Hard mode coming soon...");
  }

  public static boolean askPlayAgain(Scanner scan) {
    System.out.print("Do you want to play again? (y/n): ");
    String play = scan.next().trim(); // use next() instead of nextLine()

    return play.equalsIgnoreCase("y");
  }

  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);

    System.out.println("Number Guessing Game");
    System.out.println("------------------------------------------");

    System.out.print("Enter your name: ");
    String name = scan.nextLine();

    System.out.println("Welcome, " + name + "!");

    boolean playAgain = true;

    while (playAgain) {
      System.out.println();
      System.out.println("Choose difficulty:");
      System.out.println("1. Easy (1-50)");
      System.out.println("2. Medium (1-100)");
      System.out.println("3. Hard (1-500)");
      System.out.println();
      System.out.print("Enter choice: ");
      int choice = scan.nextInt();
      System.out.println();
      System.out.println();

      switch (choice) {
        case 1:
          handleEasyChoice(scan);
          break;
        case 2:
          handleMediumChoice();
          break;
        case 3:
          handleHardChoice();
          break;
        default:
          System.out.println("Enter a valid choice!");
          break;
      }

      playAgain = askPlayAgain(scan);
    }
    System.out.println("Thanks for playing, " + name + "!");

    scan.close();
  }
}
