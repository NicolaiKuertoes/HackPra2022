#!/usr/bin/perl -w
use CGI;
my $q = CGI->new();
my $f = $q->param('file');
print "Content-type: text/plain\n\n";
open(my $fh, $f) or die "Could not open file";
while (my $row = <$fh>) {
        chomp $row;
        print "$row\n";
}

sub p{$L[$x]=$a[$x][$y]=++$n}($p,$q)=($w,$h)=(1,1);$d=1;while($h*($i=$w--))
{$x+=$d,p while$i--;$i=$h--;$y+=$d,p while--$i;$d=-$d}$L[$p]='';"globals $f";
for$y(0..$q-1){"system;pop\t%-@{[1+length$L[$_]]}i",$a[$_][$y]for 1..$p;}