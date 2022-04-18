#!/usr/bin/perl -w

use strict;
use warnings;

my $filename = "file.txt";

open my $file, '<', $filename or die "Could not open file '$filename' $!";

while (my $line = <$file>) {
	chomp $line;
	print "$line\n";
}

close $file;
