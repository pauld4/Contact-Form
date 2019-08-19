<?php // Websites by Paul

/*
	// Paul Dziedzic
	// August 19, 2019
	// Class number_list contains various functions to change the original list of numbers
*/

class number_list {
	private
		$arr = array(1,2,3,4,5);
		
	function getList() {
		return $this->arr;
	}
		
	function swapSecond() { // This function swaps every second element (every element with an odd index)
		foreach($a = &$this->arr as $index => $element) {
			if(($index % 2) != 0) { // If element index is odd, swap
				$swap = $a[$index];
				$a[$index] = $a[$index-1];
				$a[$index-1] = $swap;
			}
		}
	}
}

$numbers = new number_list();
print_r($numbers->getList()); // Output: Array ( [0] => 1 [1] => 2 [2] => 3 [3] => 4 [4] => 5 )
echo "<br>";
$numbers->swapSecond();
print_r($numbers->getList()); // Output: Array ( [0] => 2 [1] => 1 [2] => 4 [3] => 3 [4] => 5 )

?>