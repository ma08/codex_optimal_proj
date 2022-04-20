<?php

$file = 'filetest.txt';
if($handle = fopen($file, 'w')) { //overwrite
	fclose($handle);
}

?>
