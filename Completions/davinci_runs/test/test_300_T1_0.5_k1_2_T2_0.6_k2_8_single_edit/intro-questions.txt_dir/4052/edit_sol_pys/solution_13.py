<?php

class File {

	public static function read($file) {
		if(!file_exists($file)) {
			return false;
		}
		$h = fopen($file, 'r');
		$contents = fread($h, filesize($file));
		fclose($h);
		return $contents;
	}

	public static function write($file, $content) {
		$h = fopen($file, 'w');
		fwrite($h, $content);
		fclose($h);
	}

	public static function append($file, $content) {
		$h = fopen($file, 'a');
		fwrite($h, $content);
		fclose($h);
	}
}
