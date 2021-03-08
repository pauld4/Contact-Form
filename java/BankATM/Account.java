package account;

public class Account {
	private int id;
	private double balance;
	
	Account(int i, double amt) {
		id = i;
		balance = amt;
	}
	
	public int getAccountId() {return id;}
	public double getBalance() {return balance;}
	
	public void printDetails() {
		System.out.printf("Account ID: %d, Balance: %f \n", id, balance);
	}
	
	public void depositFunds(double amt) {
		balance += amt;
	}
	
	public void withdrawFunds(double amt) {
		balance -= amt;
	}
}
