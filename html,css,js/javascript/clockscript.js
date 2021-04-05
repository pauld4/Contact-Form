class DemoClock {
	ticks = 0; // ticks represents the seconds; 3600 ticks is 3600 seconds, or 1 hour
	max_ticks = 86400; // number of seconds in a day
	
	getTicks() {
		return this.ticks;
	}
	
	setTicks(t) { // set ticks is used for getting the current time
		this.ticks = t;
	}
	
	addTicks(t) { // add ticks is used for adding hours, minutes, or seconds to the time
		this.ticks += t;
		
		if(this.ticks >= this.max_ticks) { // if the ticks is more than a day or less than 0, then convert to appropriate time
			this.ticks -= this.max_ticks;
		}
		
		if(this.ticks < 0) {
			this.ticks += this.max_ticks;
		}
	}
	
	printTime() { // converts the ticks to a readable format (hh:mm:ss)
		var t = this.ticks;
		
		var h = Math.floor(t / 3600);
		var m = Math.floor((t % 3600) / 60);
		var s = Math.floor((t % 3600) % 60);
		var mid = "AM";
		
		if(h > 11) {
			mid = "PM";
		}
		
		if(h == 0) {
			h = 12;
		}
		
		if(h > 12) {
			h -= 12;
		}
		
		if(m < 10) {
			m = "0" + m;
		}
		
		if(s < 10) {
			s = "0" + s;
		}
		
		var time_str = h + ":" + m + ":" + s + " " + mid;
		return time_str;
	}
}

var myClock = new DemoClock(); // create a new clock object
var timeInterval; // variable to store the status of the interval for incrementing the time each second

function getLiveTime() { // get the current time and convert it to ticks
	var d = new Date();
	var t = 0;
	
	t += d.getHours() * 3600;
	t += d.getMinutes() * 60;
	t += d.getSeconds();
	
	myClock.setTicks(t);
	document.getElementById("clock").innerHTML = myClock.printTime();
}

function resetTime() { // set the clock to 0 ticks, or 12AM
	myClock.setTicks(0);
	document.getElementById("clock").innerHTML = myClock.printTime();
}

function addTime(amount) { // used for adding/subtracting the hours, minutes, and seconds
	myClock.addTicks(amount);
	document.getElementById("clock").innerHTML = myClock.printTime();
}

function toggleTime() { // toggles the start/stop of the incrementing
	if(!timeInterval) {
		timeInterval = setInterval(function(){ addTime(1) }, 1000);
		document.getElementById("startTimer").innerHTML = "Stop Time";
	} else {
		clearInterval(timeInterval);
		timeInterval = null;
		document.getElementById("startTimer").innerHTML = "Start Time";
	}
}

function setupClock() { // sets up the clock GUI for the HTML tag; returns the string
	var str = "";
	
	str += "<div id='clock'></div>";
	str += "<br>";
	str += "<div id='time_panel'>";
	str += "<button onclick='getLiveTime()'>Get Live Time</button><br>";
	str += "<button onclick='resetTime()'>Reset</button><br>";
	str += "<button id='startTimer' onclick='toggleTime()'>Start Time</button><br>";
	str += "Hours: <button onclick='addTime(-3600)'>-</button> <button onclick='addTime(3600)'>+</button><br>";
	str += "Minutes: <button onclick='addTime(-60)'>-</button> <button onclick='addTime(60)'>+</button><br>";
	str += "Seconds: <button onclick='addTime(-1)'>-</button> <button onclick='addTime(1)'>+</button>";
	str += "</div>";

	return str;
}
