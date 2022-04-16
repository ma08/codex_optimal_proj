#!/usr/bin/perl

use strict;
use warnings;
use File::Basename;
use Getopt::Long;

my $usage = "

Synopsis:

perl file.pl -i <inputfile> -o <outputfile>

Description:

This script is used to parse the output file from the
mapping.pl script. It will output a file containing
the read name and the number of times that read maps
to a reference genome.

Options:

-i|--input			Input file
-o|--output			Output file

";

my ($input, $output);

GetOptions(
	'i|input=s' => \$input,
	'o|output=s' => \$output,
);

die $usage unless ($input && $output);

open(my $in, "<", $input) or die "Could not open $input\n";
open(my $out, ">", $output) or die "Could not open $output\n";

my $count = 0;
my $seq = "";
my $read = "";

while (my $line = <$in>) {
	chomp($line);
	if ($line =~ /^@/) {
		$read = $line;
		$count = 0;
	} elsif ($line =~ /^[A-Z]/) {
		$seq = $line;
	} elsif ($line =~ /^\+/) {
		$count++;
		if ($count == 1) {
			print $out "$read\t$seq\t$count\n";
		}
	}
}

close($in);
close($out);
