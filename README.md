### Introduction:

*gen-pass* is a very crude random password generator. There is zero security warranty, use at your own risk.

### Current feature set:

1. Password length specification.
2. Ability to in/exclude special characters (punctuations).

### Dependencies:

This script makes use of the following python modules:

1. os
2. random
3. click
4. string
5. time

### Usage:

Parameters supported by this script include:

| Option               | Description                             |
|:---------------------|:----------------------------------------|
| `-P INTEGER`         | Number of passwords to generate. One password by default. |
| `-l INTEGER`         | Password length. Ten characters by default. |
| `-s`                 | Include special characters (punctuations). Excluded by default. |
| `--help`             | Show help message and exit.             |
