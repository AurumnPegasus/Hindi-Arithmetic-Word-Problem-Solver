# Hindi Arithmetic Word Problem Solver

## Installation

1. Clone the directory into local machine by doing git clone https://github.com/tejasvicsr1/Hindi-Arithmetic-Word-Problem-Solver.git

2. Download ISC Tokenizer from https://bitbucket.org/iscnlp/tokenizer/src/master/ and install it. Now, copy the isc_tokenizer folder into the same directory as the directory of the Word Problem Solver.

3. Download ISC POS Tagger from https://bitbucket.org/iscnlp/pos-tagger/src/master/ and install it by following instructions in README. Then copy the directory isc_tagger into the same directory as the directory of the Word Problem Solver.

4. Download Hindi Morphanalyzer from https://iiitaphyd-my.sharepoint.com/:u:/g/personal pruthwik_mishra_research_iiit_ac_in/EVdvOPI6vOxBn02Lnuh9Pz4B4dnZJwXNGhsTMAnJN0dXIw?e=IOPU3S and install it by following the  instructions in the README. Copy the script run_morph_on_file_with_raw_text.py and the folder convertor-indic-1.5.2 and morph-hin-le-5.0.5 into the same directory as the directory of the Word Problem Solver.

End of the installtion, your directory should have

- build
- converter-indic-1.5.2
- calculate.py
- dependency_parser.egg-info
- eng-hin_numbers.py
- finalsentenceanalyze.py
- isc_tagger
- isc_tokenizer
- kartakaram.py
- morph-hin-le-5.0.5
- pos-tagger
- pos_tagger.egg-info
- pycache
- requirements.txt
- run_morph_on_file_with_raw_text.py
- setup.cfg
- setup.py
- source.py
- tempfile.txt
- tokenizer_for_IL.py
- verbdocumentation.txt


**This code will work only for Ubuntu 18.04 due to limitations with morph analyser**

The necessary tools are now installed, and the application can now be used.

## Usage Instructions

1. Put the sentences you want to run the Solver on in the list in the script source.py, along with the expected answer if you wish to measure the accuracy.

2. Run the command, while in the current directory
$ python3 equation.py

The Solver will run and display the output and answers accordingly.
Happy solving :)
