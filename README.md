# CLI Utility in Python

[![Lint Code Base](https://github.com/pacroy/python-cli-utils/actions/workflows/linter.yml/badge.svg)](https://github.com/pacroy/python-cli-utils/actions/workflows/linter.yml)
[![Check Markdown links](https://github.com/pacroy/python-cli-utils/actions/workflows/check-md-links.yml/badge.svg)](https://github.com/pacroy/python-cli-utils/actions/workflows/check-md-links.yml)
[![Test CLI](https://github.com/pacroy/python-cli-utils/actions/workflows/test.yml/badge.svg)](https://github.com/pacroy/python-cli-utils/actions/workflows/test.yml)

CLI utility scripts written in Python

## gitscan

Print Git status of all subdirectoies. Use `--help` to see usage.

```console
$ ./gitscan.py ~/tmp
Repository              Branch                  Status
notgit                  n/a                     not a git repository
branchstale             main                    clean
branch                  newbranch               clean
this_is_a_very_long_... n/a                     not a git repository
dirty-staged            main                    dirty
dirty-unstaged          main                    dirty
tmp2                    n/a                     not a git repository
```