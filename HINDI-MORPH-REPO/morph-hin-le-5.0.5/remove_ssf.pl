#!usr/bin/perl

$_prev=1;
while(<>)
{
	if($_=~m/^0\t/)
	{
		$_prev=2;
		next;
	}
	elsif($_=~/^\t\)\)/ and $_prev=~/^\t\)\)/)
	{
		$_prev="\t))";
		next;
	}
	else
	{
		$_prev="$_";
		print "$_";
	}
}
