perl /var/www/html/sampark/system/hin_urd/sampark/bin/sys/common/deletesentencetag.pl $1 | perl /var/www/html/sampark/system/hin_urd/sampark/bin/sys/common/remove_ssf.pl >morph_input

/var/www/html/sampark/system/hin_urd/sampark/bin/sl/morph/hin/morph_hin.exe --logfilepath morph.log --pdgmfilepath /var/www/html/sampark/system/hin_urd/sampark/data_bin/sl/morph/hin/ --uwordpath /var/www/html/sampark/system/hin_urd/sampark/data_bin/sl/morph/hin/dict_final --dictfilepath /var/www/html/sampark/system/hin_urd/sampark/data_bin/sl/morph/hin/dict/  -ULDWH --inputfile morph_input --outputfile morph_output

# uncomment below line if want to print nukta in root word

python /var/www/html/sampark/system/hin_urd/sampark/bin/sl/morph/hin/nukta-adder.py  morph_output | perl /var/www/html/sampark/system/hin_urd/sampark/bin/sys/common/addsentencetag.pl | perl /var/www/html/sampark/system/hin_urd/sampark/bin/sl/morph/hin/adj-gen-1.1/adj_gen.pl

# uncomment below line and comment above line if do not want nukta in root word
#perl /var/www/html/sampark/system/hin_urd/sampark/bin/sys/common/addsentencetag.pl morph_output | perl /var/www/html/sampark/system/hin_urd/sampark/bin/sl/morph/hin/adj-gen-1.1/adj_gen.pl
