<?php

$Date = date("dmY");
$Time = date("H");

$Extension = "jpg";
$FileName = "./Meter Image Uploads/".$Date.' '.$Time. '.' .$Extension;

if ($_SERVER["REQUEST_METHOD"] == "POST"){

  print_r(getallheaders());

  // POST variable contains the data submitted
  print_r($_POST);

  print_r($_POST['UserID']);
  print_r($_POST['Time']);
  print_r($_POST['Date']);

  // FILES variable contains the files submitted
  print_r($_FILES);

	If (file_exists($FileName)){
		print_r('File already exists! Please try a new file.');
	}

	else{ 
		if ($_FILES['fileone']) {
			move_uploaded_file($_FILES["fileone"]["tmp_name"], $FileName);
		}
	}
}
else{
  	echo('Unsuccessful Image Post');
}

?>