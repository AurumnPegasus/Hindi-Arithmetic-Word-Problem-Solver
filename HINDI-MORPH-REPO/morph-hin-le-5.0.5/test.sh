echo "Testing Installation"
echo "--------------------"
echo "--------------------"
sh morph_run.sh tests/morph_test.in > test.out
sh morph_run.sh tests/exception_words_test.in > test1.out
diff tests/morph_test.out test.out > output.tmp
diff tests/exception_words_test.out test1.out > output1.tmp
if [ -s output.tmp ] && [ -s output1.tmp ]; then
echo "Installation Unsuccessful"
echo "This version of morph analyzer is tested on fc8-32bit, fc-14-32bit & 64bit, fc-16-32bit, fc-21-64bit, ubuntu-12.04-32bit & 64bit, ubuntu-14.04-64bit, Centos-6.6-32bit & 64bit, Centos-7-64bit";
else
echo " morph hindi version 5.0.4 installed successfully."
fi ;

