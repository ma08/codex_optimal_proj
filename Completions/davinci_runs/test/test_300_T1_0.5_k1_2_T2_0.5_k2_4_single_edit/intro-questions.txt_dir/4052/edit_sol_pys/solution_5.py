<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
	<div>
		<?php
			$file = fopen("testfile.txt", "r") or die("Unable to open file!");
			echo fread($file, filesize("testfile.txt"));
			fclose($file);
		?>
	</div>
</body>
</html>
