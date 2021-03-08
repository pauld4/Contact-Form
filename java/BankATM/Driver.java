package account;

import java.util.ArrayList;
import java.util.Scanner;

public class Driver {
	private static ArrayList<Account> accountList = new ArrayList<Account>();
	private static double myWallet = 1000.00; // start user with 1000$ in their pocket
	final static int MAX_ACCOUNTS = 5; // user can only create up to 5 bank accounts

	public static void main(String[] args) {
		Scanner scnr = new Scanner(System.in);
		accountList.add(new Account(1000, 1000.00)); // start user with an account with 1000$
		char userInput = 'a';
		
		while(userInput != 'x') {
			printMenu();
			userInput = scnr.next().charAt(0);
			
			switch(userInput) {
			case '1':
				depositFunds();
				break;
			case '2':
				withdrawFunds();
				break;
			case '3':
				createAccount();
				break;
			case '4':
				closeAccount();
				break;
			case '5':
				printAccounts();
				break;
			case 'x':
				break;
			default:
				System.out.println("Invalid option.");
				break;
			}
		}
		
		System.out.println("Exiting application.");
	}
	
	public static void printMenu() {
		System.out.println("\nSelect Option:\n");
		System.out.println("[1] Deposit Funds");
		System.out.println("[2] Withdraw Funds");
		System.out.println("[3] Create Account");
		System.out.println("[4] Close Account");
		System.out.println("[5] View Accounts");
		System.out.println("[x] Exit System");
		System.out.printf("\nYou have $%.2f in your wallet.\n", myWallet);
		System.out.println("\nEnter a menu selection: ");
	}
	
	public static void printAccounts() {
		for(Account eachAccount: accountList)
			eachAccount.printDetails();
	}
	
	public static void depositFunds() {
		Scanner scnr = new Scanner(System.in);
		char userInput = '1'; // input for which account to deposit to
		double userDeposit = 0;
		int depositAccount = 1000; // default account to deposit to is the first one
		
		System.out.println("How much would you like to deposit? - Enter 0 to cancel");
		userDeposit = scnr.nextDouble();
		if(userDeposit > 0) {
			if(userDeposit <= myWallet) {
				myWallet -= userDeposit;
				accountList.get(0).depositFunds(userDeposit);
				System.out.printf("You have deposited $%.2f. Your balance is now $%.2f.\n", userDeposit, accountList.get(0).getBalance());
			} else {
				System.out.printf("You cannot deposit $%.2f because you only have $%.2f in your wallet.\n", userDeposit, myWallet);
			}
		} else {
			System.out.println("You did not deposit anything.");
		}
	}
	
	public static void withdrawFunds() {
		Scanner scnr = new Scanner(System.in);
		char userInput = '1';
		double userWithdraw = 0;
		int withdrawAccount = 1000; // default account to withdraw from is the first one
		
		System.out.println("How much would you like to withdraw? - Enter 0 to cancel");
		System.out.printf("You have $%.2f in your bank account.\n", accountList.get(0).getBalance());
		userWithdraw = scnr.nextDouble();
		if(userWithdraw > 0) {
			if(userWithdraw <= accountList.get(0).getBalance()) {
				myWallet += userWithdraw;
				accountList.get(0).withdrawFunds(userWithdraw);
				System.out.printf("You have withdrawn $%.2f. Your balance is now $%.2f.\n", userWithdraw, accountList.get(0).getBalance());
			} else {
				System.out.printf("You cannot withdraw $%.2f because you only have $%.2f in your bank account.\n", userWithdraw, accountList.get(0).getBalance());
			}
		} else {
			System.out.println("You did not withdraw anything.");
		}
	}
	
	public static void createAccount() {
		if(accountList.size() < MAX_ACCOUNTS) {
			int accNum = accountList.size() + 1000;
			accountList.add(new Account(accNum, 100.00));
			System.out.printf("New account #%d created.\n", accNum);
		} else {
			System.out.println("You already have the maximum amount of accounts open. Close an account to open a new one.");
		}
	}
	
	public static void closeAccount() {
		System.out.println("Close account option not yet implemented.");
	}

}
