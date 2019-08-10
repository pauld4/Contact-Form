<?php

class database {
	private 
		$host = "localhost",
		$db_name,
		$username,
		$password;
		
	public $conn;
	
	function getConnection(){
		$this->conn = null;
		
		try {
			$this->conn = new PDO("mysql:host=" . $this->host . ";dbname=" . $this->db_name, $this->username, $this->password);
			$this->conn->exec("set names utf8");
		} catch(PDOException $exception) {
			echo "Connection error: " . $exception->getMessage();
		}

		return $this->conn;
	}
}

?>