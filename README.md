[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0) 
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-blue.svg)](http://creativecommons.org/licenses/by-sa/4.0/)

# Smaller Basic

A simple Python interpreter using ANTLR4 as a parser generator for a version of Microsoft's Small Basic language renamed "Smaller Basic."

## Starting point working locally

**Create and start a new virtual environment**

`source create_venv.sh venv` 

**Start current virtual environment**

`source venv/bin/activate`

**Deactivate the current virtual environment**

`deactivate`

## Run interpreter

In development phase the following command will re-generate the grammar related files from scratch. 
Note that, again for the development phase, the file must be contained in the `source_code` folder.

`smallbasic <name>.sb`


### Generate grammar

`antlr4 -Dlanguage=Python3 -visitor src/grammar/SmallerBasic.g4`

- **Requirements**: the same or greater java version used to compile the antlr4 jar. (in my case **java-18-openjdk-amd64**)  

- Change version of java: `update-alternatives --config java`.

- `antlr4` is an alias generated by the `create_venv.sh` file.

### Run main

`python3 -m src.main source_code/test.sb`


### Run the `main.py` file of the `<x>` package 

`python3 -m src.<x>.main`




