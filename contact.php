<?php // Contact Form by Paul Dziedzic

require "config/database.php"; // Load database object to connect to the database
require "objects/contact_obj.php"; // Contact object for creating/loading contacts

$database = new database;
$db = $database->getConnection();

if($_SERVER['REQUEST_METHOD'] == "POST") { // Check for a POST method was sent
	if(isset($_POST['submit_contact'])) { // Check that the submit button was clicked/entered
		empty(trim($_POST['user_name'])) ? $contact_message = "Enter your name." : $user_name = trim($_POST['user_name']); // Validate that all fields that needed to be entered, were entered
		empty(trim($_POST['user_email'])) ? $contact_message = "Enter your email." : $user_email = trim($_POST['user_email']);
		
		$user_message = $_POST['user_message'];
		
		if(empty($contact_message)) { // Continue if no errors
			if(isset($_POST['g-recaptcha-response']) && !empty($_POST['g-recaptcha-response'])) { // Validate the Google CAPTCHA
				$secret = 'key'; // Changed to 'key' for Github
				$verifyResponse = file_get_contents('https://www.google.com/recaptcha/api/siteverify?secret='.$secret.'&response='.$_POST['g-recaptcha-response']);
				$responseData = json_decode($verifyResponse);
				if($responseData->success) { // Continue if CAPTCHA success
					if(strlen($user_name) < 128 && strlen($user_email) < 128 && strlen($user_message) < 128) { // Validate user inputs
						if(filter_var($user_email, FILTER_VALIDATE_EMAIL)) {
							$contact = new contact($db);
							
							if($contact->loadContact($user_email, $user_name)) { // Load the user
								$contact_message = "This email has been submitted already."; // If this email has been found in the database, no email will be sent
							} else {
								$contact->createContact(); // Add email and user's name to database
								
								$headers  = 'MIME-Version: 1.0' . "\r\n"; // Define the headers
								$headers .= 'Content-type: text/html; charset=iso-8859-1' . "\r\n"; // Enable HTML in email
								$headers .= 'From: Paul Dziedzic <paul@websitesbypaul.com>' . "\r\n" . // Display "from" name and address
								'Reply-To: paul@websitesbypaul.com' . "\r\n" . // Set the address to reply to
								'X-Mailer: PHP/' . phpversion(); // Set client used
								
								$addr = "paul@websitesbypaul.com"; // Declare who the email is being sent to
								$sub = "New Contact"; // Declare the subject line in the email
								$msg = "<html><body>"; // Create the text in the email to be displayed
								$msg .= "<p>" . $contact->getName() . " has contacted you. You can contact them back via " . $contact->getEmail() . ".</p>";
								if(!empty($user_message)) { // If a message was written, include that
									$msg .= "<p>A message was included:<br>" . $user_message . "</p>";
								}
								
								$msg .= "</body></html>";
								
								mail($addr,$sub,$msg,$headers); // Send the email
								
								$contact_message = "Thank you for contacting me, " . $contact->getName() . ". You will hear from me within the next 48 hours."; // Display message confirming successful submittion
							}
						} else {
							$contact_message = "Invalid email.";
						}
					} else {
						$contact_message = "Invalid name or email.";
					}
				} else {
					$contact_message = "CAPTCHA verification failed.";
				}
			} else {
				$contact_message = "CAPTCHA verification required.";
			}*/
		}
	}
}

?>

<html>

<head>
	<title>Website Contact Form</title>
	<link rel="icon" href="images/icon.ico" type="image/x-icon">
	
	<!-- Google reCAPTCHA -->
	<script src="https://www.google.com/recaptcha/api.js" async defer></script>
</head>

<body>
	<p>Contact Form</p>
	
	<form action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" method="post">
		<table>
			<tr><td>Name:</td><td><input type="text" name="user_name"></td></tr>
			<tr><td>Email:</td><td><input type="text" name="user_email"></td></tr>
			<tr><td>Message:</td><td><textarea rows="4" cols="50" style="resize:none;" name="user_message"></textarea></td></tr>
		</table>
		<div name="gcap" class="g-recaptcha" data-sitekey="key"></div> <!-- Changed to "key" for Github -->
		<button type="submit" name="submit_contact">Submit</button>
	</form>
	
	<p><?php echo $contact_message; ?></p>
</body>

</html>