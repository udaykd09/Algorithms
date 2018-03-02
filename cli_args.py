#!/usr/bin/python

import sys, getopt

def main():
    ifile = ''
    ofile = ''
    print sys.argv
    args = sys.argv[1:]
    try:
        opts, args = getopt.getopt(args, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print ('Usage : cli_args.py -i <input_file> -o <output_file>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('Usage : cli_args.py -i <input_file> -o <output_file>')
            sys.exit()
        elif opt in ('-i', '--ifile'):
            ifile = arg
        elif opt in ('-o', '--ofile'):
            ofile = arg

    print "Input file %s" % ifile
    print "Output file %s" % ofile

if __name__ == '__main__':
    main()