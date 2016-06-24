#Script to calculate differences along the first column of a csv file.
#Prints to derivative.txt
#csv filename given at command line.

use strict;
use warnings;

defined($ARGV[0]) or die;

open(my $file_handle_in, '<', $ARGV[0]) or die "can't open file";
open(my $file_handle_out, '>', "derivative.txt");

my @positions = ();
my @linearray;

while (my $line = <$file_handle_in>) {
  @linearray = split(",",$line);
  push(@positions,$linearray[0]);
}

my $difference;

for my $i (2..scalar(@positions)-1) {
  $difference = abs($positions[$i]-$positions[$i-1]);
  print $file_handle_out "$difference\n";
}
