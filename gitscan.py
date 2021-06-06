#!/usr/bin/env python
# Scan each directory for Git status
# References:
# - [shell - How to execute a program or call a system command from Python - Stack Overflow](https://stackoverflow.com/questions/89228/how-to-execute-a-program-or-call-a-system-command-from-python)
# - [python - Convert bytes to a string - Stack Overflow](https://stackoverflow.com/questions/606191/convert-bytes-to-a-string)
# - [python - How to check if the string is empty? - Stack Overflow](https://stackoverflow.com/questions/9573244/how-to-check-if-the-string-is-empty)
# - [python - How do I read the first line of a string? - Stack Overflow](https://stackoverflow.com/questions/11833266/how-do-i-read-the-first-line-of-a-string)
# - [python - Printing Lists as Tabular Data - Stack Overflow](https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data)
# - [printing - How to print to stderr in Python? - Stack Overflow](https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python)
import os, sys, getopt, subprocess, re

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

def print_usage():
    print("Usage:")
    print("  python3 gitscan.py [-a] directory")
    print()
    print("Arguments:")
    print("  directory : Specify a directory to scan. Omit to scan the current directory.")
    print("Options:")
    print("  -h, --help                 : Print this usage string.")
    print("  -a, --show-all             : Print all directories. Omit to print only unclean ones.")

def format_column_text(text, length):
    if len(text) > length:
        return text[0:length-3] + "..."
    else:
        return text

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hd:b:a", ["help", "directory=", "show-all", "default-branch="])
    except getopt.GetoptError as err:
        eprint(f"Error: {err}")
        print_usage()
        sys.exit(90)

    if len(args) > 0:
        directory = args[0]
    else:
        directory = ""
    show_all = False
    default_branch = "main"

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print_usage()
            sys.exit()
        elif opt in ("-a", "--show-all"):
            show_all = True
    
    if not directory:
        directory = os.getcwd()
    if not os.path.exists(directory):
        eprint(f"Error: Directory '{directory}' does not exist.")
        sys.exit(92)

    branchRegex = re.compile(r"On branch (.+)\n")
    cleanRegex = re.compile(r"nothing to commit")
    notGitRegex = re.compile(r"not a git repository")
    uptodateRegex = re.compile(r"Your branch is up to date with '.+/.+'")
    outofsyncRegex = re.compile(r"Your branch is (behind|ahead of) '.+/.+' by (\d+) commit")

    directories = os.listdir(directory)
    if len(directories) == 0:
        print("No repository found.")
        return

    print(bcolors.HEADER + "Repository".ljust(23) + "\t" + "Branch".ljust(23) + "\t" + "Status" + bcolors.ENDC)
    for item in directories:
        abspath = os.path.join(directory, item)
        if os.path.isdir(abspath):
            os.chdir(abspath)
            result = subprocess.run(["git", "status"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout = result.stdout.decode("utf-8")
            stderr = result.stderr.decode("utf-8")
            
            result_line = format_column_text(item, 23).ljust(23)
            result_bad = False

            if stderr:
                result_bad = True
                stderr_1stline = stderr.partition('\n')[0]
                notGitMatchObject = notGitRegex.search(stderr_1stline)
                result_line += f"\t{'n/a'.ljust(23)}"
                if notGitMatchObject is not None:
                    result_line += f"\t{bcolors.FAIL}{notGitMatchObject.group()}{bcolors.ENDC}"
                else:
                    result_line += f"\t{bcolors.FAIL}{stderr_1stline}{bcolors.ENDC}"
            else:
                branch = branchRegex.findall(stdout)[0]
                branch_print = format_column_text(branch, 23).ljust(23)

                if uptodateRegex.search(stdout) is not None:
                    result_line += f"\t{bcolors.OKGREEN}{branch_print}{bcolors.ENDC}"
                elif outofsyncRegex.search(stdout) is not None:
                    result_bad = True
                    result_line += f"\t{bcolors.WARNING}{branch_print}{bcolors.ENDC}"
                else:
                    result_line += f"\t{branch_print}"

                if cleanRegex.search(stdout) is None:
                    result_bad = True
                    result_line += f"\t{bcolors.WARNING}dirty{bcolors.ENDC}"
                else:
                    result_line += f"\t{bcolors.OKGREEN}clean{bcolors.ENDC}"

            if show_all or result_bad:
                print(result_line)


if __name__ == "__main__":
    main(sys.argv[1:])
