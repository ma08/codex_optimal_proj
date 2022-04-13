<?php
$file = fopen("newfile.txt", "w") or die("Unable to open file!");
echo fwrite($file, "Hello World. Testing!");
fclose($file);
?>
