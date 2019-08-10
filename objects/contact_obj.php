<?php

class contact {
	private
		$contact_id,
		$email,
		$name,
		
		$table_name = "contacts",
		$conn;
		
	function __construct($database) {
		$this->conn = $database;
	}
	
	function loadContact($email, $name) {
		$stmt = $this->conn->prepare("SELECT * FROM " . $this->table_name . " WHERE email = ?");
		$stmt->bindParam(1, $email, PDO::PARAM_STR);
		$stmt->execute();
		
		if($stmt->rowCount() > 0) {
			$row = $stmt->fetch();
			$this->contact_id = $row['contact_id'];
			$this->email = $row['email'];
			$this->name = $row['name'];
			return true;
		}
		
		$this->email = $email;
		$this->name = $name;
		return false;
	}
	
	function createContact() {
		$stmt = $this->conn->prepare("INSERT INTO " . $this->table_name . " (email, name) VALUES (?,?)");
		$stmt->bindParam(1, $this->email, PDO::PARAM_STR);
		$stmt->bindParam(2, $this->name, PDO::PARAM_STR);
		$stmt->execute();
	}
	
	function getEmail() {
		return $this->email;
	}
	
	function getName() {
		return $this->name;
	}
}

?>