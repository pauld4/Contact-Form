//============================================================================
// Name        : HelloWorld.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

class BankAccount {
	private:
		double balance = 0.0;
		int accountNumber = 1000;

	public:
		void addFunds(double d) {
			balance += d;
		}

		double getBalance() {
			return balance;
		}
};

void printMenu() {
	cout << "What would you like to do today?" << endl;
	cout << "1 - Withdraw funds" << endl;
	cout << "2 - Deposit funds" << endl;
	cout << "3 - Exit" << endl;
}

int main() {
	int userInput = 0;
	printMenu();
	BankAccount acc1;

	while(userInput != 3) {
		cin >> userInput;

		if(userInput != 3) {
			if(userInput == 1) {
				double withdrawAmount;
				cout << "How much would you like to withdraw?" << endl;
				cout << "Your current balance is: $" << acc1.getBalance() << endl;
				cin >> withdrawAmount;
				if(withdrawAmount > 0) {
					acc1.addFunds(withdrawAmount);
					cout << "You have added " << withdrawAmount << " to your account." << endl << endl;
				} else {
					cout << "Nothing was added to your account." << endl;
				}
			} else if(userInput == 2) {
				//depositFunds();
			}
			printMenu();
		}
	}

	cout << "Thank you for banking with us." << endl;

	return 0;
}
