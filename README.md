# CLI Utility in Python

[![Lint Code Base](https://github.com/pacroy/python-cli-utils/actions/workflows/linter.yml/badge.svg)](https://github.com/pacroy/python-cli-utils/actions/workflows/linter.yml) [![Check Markdown links](https://github.com/pacroy/python-cli-utils/actions/workflows/check-md-links.yml/badge.svg)](https://github.com/pacroy/python-cli-utils/actions/workflows/check-md-links.yml)

CLI utility scripts written in Python

## gitscan

Print Git status of all subdirectoies. Use `--help` to see usage.

```text
 ./gitscan.py -d ~/tmp
Repository              Branch                  Status
notgit                  n/a                     not a git repository
master                  master                  clean
branchstale             main                    clean, -1
longbranch              this-is-a-very-long-... clean
branch                  newbranch               clean, +1
this_is_a_very_long_... n/a                     not a git repository
dirty-staged            main                    dirty
dirty-unstaged          main                    dirty
tmp2                    n/a                     not a git repository
```