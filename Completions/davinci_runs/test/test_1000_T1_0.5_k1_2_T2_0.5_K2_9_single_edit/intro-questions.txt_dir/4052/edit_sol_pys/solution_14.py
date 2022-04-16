<?php

$file = fopen('data.txt', 'r');

$data = fread($file, filesize('data.txt'));

echo $data;

fclose($file);

?>
