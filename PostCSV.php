<?php

if ($_SERVER["REQUEST_METHOD"] == "POST"){

  print_r(getallheaders());

  // POST variable contains the data submitted
  print_r($_POST);

  // FILES variable contains the files submitted
  print_r($_FILES);

 	if ($_FILES['filetwo']){
	move_uploaded_file($_FILES["filetwo"]["tmp_name"], './Meter Image Timestamps/Meter Image Data.csv');
	}
} 

else{
  	echo('Unsuccessful CSV Post');
}

?>