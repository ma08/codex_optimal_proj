<?php

$file = fopen("file.txt", "r");

$content = fread($file, filesize("file.txt"));

echo $content;

fclose($file);


?>
