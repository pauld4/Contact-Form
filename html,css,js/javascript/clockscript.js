class DemoClock {
	ticks = 0;
	max_ticks = 86400;
	
	getTicks() {
		return this.ticks;
	}
	
	setTicks(t) {
		this.ticks = t;
	}
	
	addTicks(t) {
		this.ticks += t;
		
		if(this.ticks >= this.max_ticks) {
			this.ticks -= this.max_ticks;
		}
		
		if(this.ticks < 0) {
			this.ticks += this.max_ticks;
		}
	}
	
	printTime() {
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

var myClock = new DemoClock();
var timeInterval;

function getLiveTime() {
	var d = new Date();
	var t = 0;
	
	t += d.getHours() * 3600;
	t += d.getMinutes() * 60;
	t += d.getSeconds();
	
	myClock.setTicks(t);
	document.getElementById("clock").innerHTML = myClock.printTime();
}

function resetTime() {
	myClock.setTicks(0);
	document.getElementById("clock").innerHTML = myClock.printTime();
}

function addTime(amount) {
	myClock.addTicks(amount);
	document.getElementById("clock").innerHTML = myClock.printTime();
}

function toggleTime() {
	if(!timeInterval) {
		timeInterval = setInterval(function(){ addTime(1) }, 1000);
		document.getElementById("startTimer").innerHTML = "Stop Time";
	} else {
		clearInterval(timeInterval);
		timeInterval = null;
		document.getElementById("startTimer").innerHTML = "Start Time";
	}
}

function setupClock() {
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
