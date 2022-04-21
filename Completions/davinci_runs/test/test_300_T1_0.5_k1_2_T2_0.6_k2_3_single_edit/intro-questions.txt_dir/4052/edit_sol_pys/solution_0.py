<?php

$file = fopen("file.txt", "r") or die("Unable to open file!");

$data = fread($file,filesize("file.txt"));

echo $data;

$file = fopen("file.txt", "w") or die("Unable to open file!");

$txt = "Rohan\n";
fwrite($file, $txt);
$txt = "Sanket\n";
fwrite($file, $txt);

fclose($file);

?>
