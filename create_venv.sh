#!/bin/bash

venv_dir="$1"
python3 -m venv "$venv_dir"
echo "Virtual environment created at $venv_dir"

activate_script=""
if [[ $OSTYPE == "msys" || $OSTYPE == "cygwin" || $OSTYPE == "win32" ]]; then
    activate_script="$venv_dir/Scripts/activate"
else
    activate_script="$venv_dir/bin/activate"
fi
source "$1/bin/activate"

# export ANTLR4_JAR=$HOME/Documents/smaller-basic/jars/antlr-4.12.0-complete.jar
export ANTLR4_JAR=./jars/antlr-4.12.0-complete.jar
alias antlr4='java -jar $ANTLR4_JAR'
alias grun='java org.antlr.v4.gui.TestRig'

smallbasic_run_all () {
    antlr4 -Dlanguage=Python3 -visitor src/grammar/SmallerBasic.g4; 
    for file in source_code/*.sb; do
        echo "Running $file"
        file=${file#source_code/}
        smallbasic "$file"
        echo ""
    done
}

smallbasic() {
    if [[ $1 == "-h" ]]; then
        echo "Usage: smallbasic [OPTION] [FILE]"
        echo "Run Smaller Basic program"
        echo ""
        echo "Options:"
        echo "  -h      display this help and exit"
        echo "  -g      generate grammar"
        echo "  -ga     generate grammar and run all files in source_code folder"
        echo "  -a      run all files in source_code folder"
        echo ""
    elif [[ $1 == "-g" ]]; then
        antlr4 -Dlanguage=Python3 -visitor src/grammar/SmallerBasic.g4; 
        if [[ $2 ]]; then
            python3 -m src.main source_code/"$2"
        fi
    elif [[ $1 == "-ga" ]]; then
        antlr4 -Dlanguage=Python3 -visitor src/grammar/SmallerBasic.g4; 
        smallbasic_run_all
    elif [[ $1 == "-a" ]]; then
        smallbasic_run_all
    else
        python3 -m src.main source_code/"$1"
    fi
}

pip install -e .

pip -V
