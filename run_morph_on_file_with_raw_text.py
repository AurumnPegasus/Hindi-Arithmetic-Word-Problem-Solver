import os
from argparse import ArgumentParser


def runMorphAnalyzerOnFile(inputFile, outputFile):
    os.system('perl -C ./convertor-indic-1.5.2/convertor_indic.pl -f=text -l=hin -s=utf -t=wx -i=' + os.path.abspath(inputFile) + '>temp.out')
    os.system('python3 tokenizer_for_IL.py --input temp.out --output temp.out.tok')
    inpFD = open('temp.out.tok', 'r', encoding='utf-8')
    #print('Processing File:', inputFile)
    runMorphOnFile(inpFD, outputFile)
    os.system('rm -rf temp.out')
    os.system('rm -rf temp.out.tok')
    #print('DONE')


def runMorphOnFile(inpFD, outFile):
    lines = inpFD.readlines()
    inpFD.close()
    sents = [sent.strip() for sent in lines if sent.strip()]
    for index, sent in enumerate(sents):
        sentenceID = index + 1
        sentenceInConLL = '\n'.join([str(indexToken + 1) + '\t' + token for indexToken, token in enumerate(sent.split())])
        tempFD = open('temp.txt', 'w', encoding='utf-8')
        tempFD.write(sentenceInConLL + '\n')
        tempFD.close()
        tempOut = open('temp2.out', 'a', encoding='utf-8')
        tempOut.write("<Sentence id='" + str(sentenceID) + "'>\n")
        tempOut.close()
        os.system('sh $setu/src/sl/morph/hin/morph_run.sh temp.txt >> temp2.out')
        tempOut = open('temp2.out', 'a', encoding='utf-8')
        tempOut.write('</Sentence>' + '\n\n')
        tempOut.close()
        os.system('perl -C ./convertor-indic-1.5.2/convertor_indic.pl -f=ssf -l=hin -s=wx -t=utf -i=temp2.out >>' + outFile)
        os.system('rm -rf temp.txt')
        os.system('rm -rf temp2.out')


def main():
    parser = ArgumentParser()
    parser.add_argument('--input', dest='inp', help='Enter the input folder path')
    parser.add_argument('--output', dest='out', help='Enter the output folder path')
    args = parser.parse_args()
    runMorphAnalyzerOnFile(args.inp, args.out)


if __name__ == '__main__':
    main()
