<?php
require_once("lib/config.php");
require_once("lib/funcs.php");
require_once("lib/file.php");

$file = new File();
$file->create("teste.txt", "teste");

?>
