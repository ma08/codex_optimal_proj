#!/usr/bin/php
<?php
    if ($argc > 1) {
        $file = file_get_contents($argv[1]);
        $regex = '/<a.*?title="(.*?)">/';
        preg_match_all($regex, $file, $matches);
        $regex = '/<a.*?>(.*?)</';
        preg_match_all($regex, $file, $matches2);
        $i = 0;
        foreach ($matches2[1] as $match) {
            $match = trim(strip_tags($match));
            if ($matches[1][$i])
                echo "$match\t".$matches[1][$i]."\n";
            $i++;
        }
    }
?>
