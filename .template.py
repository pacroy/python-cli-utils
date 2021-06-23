#!/usr/bin/env python
# Python CLI template
import os, sys, getopt

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
    print(f"usage: python {script_name} [-a] [directory]")
    print()
    print("Do something script")
    print()
    print("arguments:")
    print("  directory : Specify a directory. Omit to use the current directory.")
    print("options:")
    print("  -h, --help                 : Print this usage string")
    print("  -a, --show-all             : Show all information")

def print_error(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# Process CLI arguments and options
def process_argv(argv):
    script_name = argv[0]

    try:
        opts, args = getopt.getopt(argv[1:], "hd:b:a", ["help", "directory=", "show-all", "default-branch="])
    except getopt.GetoptError as err:
        print_error(f"Error: {err}")
        print_usage(script_name)
        sys.exit(90)

    if len(args) > 0:
        directory = args[0]
    else:
        directory = ""
    show_all = False

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print_usage(script_name)
            sys.exit()
        elif opt in ("-a", "--show-all"):
            show_all = True

    if not directory:
        directory = os.getcwd()
    if not os.path.exists(directory):
        print_error(f"Error: Directory '{directory}' does not exist.")
        sys.exit(91)

    return script_name, show_all, directory

def main(argv):
    script_name, show_all, directory = process_argv(argv)
    print(f"script   : {script_name}")
    print(f"show-all : {show_all}")
    print(f"directory: {directory}")

if __name__ == "__main__":
    main(sys.argv)
