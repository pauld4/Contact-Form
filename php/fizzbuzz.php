<?php 

/*
	// Paul Dziedzic
	// fizzbuzz.php
	// August 16, 2019
	// Based on the FizzBuzz example on http://wiki.c2.com/?FizzBuzzTest
	// This uses classes to create a number object, "fuzz"
	// A fuzz is created when a new list is generated
	// Generate any amount of lists with any amount of fuzz
*/

class fuzz {
	private
		$val;
	
	function __construct($number) {
		$this->val = $number;
	}
	
	function getFuzz() {
		if( ($this->val % 3 == 0) && ($this->val % 5 == 0) ) {
			return "FizzBuzz";
		} elseif($this->val % 3 == 0) {
			return "Fizz";
		} elseif($this->val % 5 == 0) {
			return "Buzz";
		} else {
			return $this->val;
		}
	}
	
	function getVal() {
		return $this->val;
	}
}

// Fuzz list object generates and stores the fuzz values
class fuzz_list {
	private
		$min,
		$max,
		
		$fuzz;
	
	function __construct($minimum,$maximum) {
		$this->editFuzz($minimum,$maximum);		
		$this->loadFuzz();
	}
	
	function loadFuzz() {
		for($i = $this->min;$i < $this->max;$i++) {
			$this->fuzz[] = new fuzz($i);
		}
	}
	
	function editFuzz($minimum,$maximum) { // Set or reset the values
		$this->min = $minimum;
		$this->max = $maximum;
	}
	
	function getFuzz() {
		return $this->fuzz;
	}
	
	function fuzzCount() {
		return count($this->fuzz);
	}
}

// Create the fuzz list here
// This can be put in a loop to generate more lists, and more fuzz

$fuzzies = new fuzz_list(5,25);
?>

<html>

<head>
	<title>FizzBuzz</title>
</head>

<body>
	<p><?php echo $fuzzies->fuzzCount(); ?> numbers were generated.</p>
		
	<p>
		<?php foreach($fuzzies->getFuzz() as $fuzz): ?> <!-- Get the list of fuzz using getFuzz function, and print its fuzz value -->
			<?php echo $fuzz->getFuzz(); ?><br>
		<? endforeach; ?>
	</p>
</body>

</html>
