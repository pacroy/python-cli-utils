#!/usr/bin/env python
# Rearrange PDF pages scanned from non-duplex scanner
import os, sys, getopt
import PyPDF2

# Terminal color class
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_usage(script_name):
    print(f"usage: python {script_name} pdf_file")
    print()
    print("Reaarange duplex PDF document scanned from your simplex scanner.")
    print()
    print("arguments:")
    print("  pdf_file : PDF file to rearrange pages")
    print("options:")
    print("  -h, --help                 : Print this usage string")

def print_error(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# Process CLI arguments and options
def process_argv(argv):
    script_name = argv[0]

    try:
        opts, args = getopt.getopt(argv[1:], "h", ["help"])
    except getopt.GetoptError as err:
        print_error(f"Error: {err}")
        print_usage(script_name)
        sys.exit(90)

    if len(args) > 0:
        pdf_file = args[0]
    else:
        pdf_file = ""

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print_usage(script_name)
            sys.exit()

    if not pdf_file:
        print_error(f"Error: Missing mandatory argument: pdf_file")
        print_usage(script_name)
        sys.exit(91)
    if not os.path.exists(pdf_file):
        print_error(f"Error: File '{pdf_file}' does not exist.")
        sys.exit(92)

    return script_name, pdf_file

def validate_pdf_pages(pdf_file):
    pdfFile = open(pdf_file, "rb")
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    totalPages = pdfReader.numPages
    if totalPages < 4:
        print_error(f"Error: PDF file must have at least 4 pages")
        sys.exit(93)
    if totalPages % 2 != 0:
        print_error(f"Error: PDF file does not have even number of pages")
        sys.exit(94)

def main(argv):
    _, pdf_file = process_argv(argv)
    validate_pdf_pages(pdf_file)

if __name__ == "__main__":
    main(sys.argv)
