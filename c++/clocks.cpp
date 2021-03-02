/*
 * Clocks.cpp
 *
 * Clock application that starts at 0:00:00 and can add an hour, minute, or second to the time.
 * By Paul Dziedzic
 *
 */

#include <iostream>
#include <iomanip>

using namespace std;

//adds an hour to the time
void addHour(int& cTime) {
    cTime = cTime + 3600;
    if(cTime >= 86400) {
        cTime = cTime - 86400;
    }
}

//adds a minute to the time
void addMinute(int& cTime) {
    cTime = cTime + 60;
    if(cTime >= 86400) {
        cTime = cTime - 86400;
    }
}

//adds a second to the time
void addSecond(int& cTime) {
    cTime = cTime + 1;
    if(cTime >= 86400) {
        cTime = cTime - 86400;
    }
}

//prints the time in 12 hour format, with PM/AM
void print12Hour(int cTime) {
    int hour = cTime / 3600;
    int minute = (cTime % 3600) / 60;
    int second = (cTime % 3600) % 60;
    string ampm = (cTime >= (12 * 3600)) ? "PM" : "AM";

    if(hour > 12) {
        hour = hour - 12;
    }

    if(hour == 0) {
        hour = 12;
    }

    cout << setfill('0');
    cout << setw(2) << hour << ":";
    cout << setfill('0');
    cout << setw(2) << minute << ":";
    cout << setfill('0');
    cout << setw(2) << second << " " << ampm;
}

//prints the time in 24 hour format
void print24Hour(int cTime) {
    int hour = cTime / 3600;
    int minute = (cTime % 3600) / 60;
    int second = (cTime % 3600) % 60;

    cout << setfill('0');
    cout << setw(2) << hour << ":";
    cout << setfill('0');
    cout << setw(2) << minute << ":";
    cout << setfill('0');
    cout << setw(2) << second;
}

int main()
{
    int clockTime = 0;
    int userInput = 0;

    while(userInput != 4) {
    	//process user input if requesting to add an hour, minute, or second
    	if(userInput == 1) {
    		addHour(clockTime);
    	} else if(userInput == 2) {
    		addMinute(clockTime);
    	} else if(userInput == 3) {
    		addSecond(clockTime);
    	}
		//print both clocks
		cout << "***************************        ***************************" << endl;
		cout << "*      12-Hour Clock      *        *      24-Hour Clock      *" << endl;
		cout << "*       ";
		print12Hour(clockTime);
		cout << "       *        *        ";
		print24Hour(clockTime);
		cout << "         *" << endl;
		cout << "***************************        ***************************" << endl;
		cout << endl;

		//print menu
		cout << "**************************" << endl;
		cout << "* 1 - Add One Hour       *" << endl;
		cout << "* 2 - Add One Minute     *" << endl;
		cout << "* 3 - Add One Second     *" << endl;
		cout << "* 4 - Exit Program       *" << endl;
		cout << "**************************" << endl;

		//get user input for next selection
		cin >> userInput;
    }

    cout << "Exiting program." << endl;

    return 0;
}
