<?php
$file = 'test.txt';
$file_handle = fopen($file, 'w');
fwrite($file_handle, 'Hello World');
fclose($file_handle);
?>
