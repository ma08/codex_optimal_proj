<?php
$file = fopen("newfile.txt", "a");
echo fwrite($file, "Hello World. Testing!");
fclose($file);
?>
