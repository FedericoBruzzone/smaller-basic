# Smaller Basic

A Python interpreter using ANTLR4 as a parser generator for a version of Microsoft's Small Basic language renamed "Smaller Basic."

## Examples of source code

Location of this source code: `source_code/source.sb`.

```python
Sub x_as_int
    If (x = "1") Then x = 1 EndIf
    If (x = "2") Then x = 2 EndIf
    If (x = "3") Then x = 3 EndIf
    If (x = "4") Then x = 4 EndIf
    If (x = "5") Then x = 5 EndIf
    If (x = "6") Then x = 6 EndIf
    If (x = "7") Then x = 7 EndIf
    If (x = "8") Then x = 8 EndIf
    If (x = "9") Then x = 9 EndIf
EndSub

Sub main
    While (true)
        IO.WriteLine("Enter a number from 0 to 9: ")
        x = IO.ReadLine()
        x_as_int()

        IO.WriteLine("Enter your name: ")
        name = IO.ReadLine()

        For i = 0 To x Step 2
            IO.WriteLine("Hello " + name)
        EndFor
    EndWhile
EndSub

main()
```


<details>
  <summary>AST</summary>

  ![ast](https://github.com/mapio-teaching/LET23-Bruzzone-Federico/blob/main/img_readme/ast-source.png)
</details>

The output of this source code is:

```bash
+---------------------------------------+
| ----- Run source_code/source.sb ----- |
+---------------------------------------+

Enter a number from 0 to 9:
|> 8
Enter your name:
|> Federico
Hello Federico
Hello Federico
Hello Federico
Hello Federico
```

<details>
  <summary><b>Example using Library, Array and Goto statements</b> [source_code/first_prog.sb] </summary>

  ```python
Sub init_value_as_int
    If (init_value = "1") Then init_value = 1 EndIf
    If (init_value = "2") Then init_value = 2 EndIf
    If (init_value = "3") Then init_value = 3 EndIf
    If (init_value = "4") Then init_value = 4 EndIf
    If (init_value = "5") Then init_value = 5 EndIf
    If (init_value = "6") Then init_value = 6 EndIf
    If (init_value = "7") Then init_value = 7 EndIf
    If (init_value = "8") Then init_value = 8 EndIf
    If (init_value = "9") Then init_value = 9 EndIf
EndSub

Sub ArrayInit
    For i = 0 To 3
        For j = 0 To 3
            my_vec[i][j] = init_value
        EndFor
    EndFor
EndSub

Sub ArrayIncrement
    For i = 0 To 3
        For j = 0 To 3
            my_vec[i][j] = my_vec[i][j] + 1
        EndFor
    EndFor
EndSub

Sub Main
    my_vec[2][2] = 0
    IO.WriteLine(my_vec)

    count = 0
    LabelFor5:
    IO.WriteLine(count)

    IO.WriteLine("Enter the value with which you want to initialize the array: ")
    init_value = IO.ReadLine()
    If (String.Length(init_value) > 1) Then
        IO.WriteLine("You entered more than one character. Only the first character will be used.")
        init_value = String.Substr(init_value, 0, 1)
    EndIf
    init_value_as_int()

    ArrayInit()
    IO.WriteLine(my_vec)

    ArrayIncrement()
    IO.WriteLine(my_vec)

    count = count + 1
    If (count < 5) Then
        Goto LabelFor5
    EndIf

    Goto End

    While (my_vec[2][2] < 10)
        ArrayIncrement()
        IO.WriteLine(my_vec)
    EndWhile
EndSub

Main()

End:
    IO.WriteLine("End of program.")
  ```
</details>

<details>
  <summary><b>Example using nested Goto</b> [source_code/second_prog.sb]</summary>

  ```python
  a = 1

Loop1:
    IO.WriteLine("Loop1")

    Loop2:
        IO.WriteLine("Loop2")
        a = a + 1
        If (a < 10) Then
            Goto Loop2
        EndIf

    IO.WriteLine(a)
    a = a + Math.Sqrt(a)
    IO.WriteLine(a)

    If (a > 100) Then
        Goto End
    EndIf

Goto Loop1


End:
    IO.WriteLine("End")
  ```
</details>

Parsing errors and warnings are displayed as follows:

![warning_error](https://github.com/mapio-teaching/LET23-Bruzzone-Federico/blob/main/img_readme/warning_error.png)

## Project directory structure

```
.
├── source_code
│   ├── ...
└── src
    ├── abstract_syntax_tree
    │   ├── ...
    ├── error
    │   ├── ...
    ├── grammar
    │   ├── SmallerBasic.g4
    │   └── ...
    ├── interpreter
    │   ├── dispatch_table.py
    │   ├── global_memory.py
    │   ├── interpreter.py
    │   └── library
    │       └── ...
    ├── main.py
    └── utils
        └── ...
```

### Overview

- `source_code`: This directory contains the source code files of SmallerBasic programming language.

- `src`: The main source code directory containing various subdirectories and files related to the interpreter and language implementation.

    - `abstract_syntax_tree`: This directory hold files related to constructing and manipulating the abstract syntax tree.

    - `error`: This directory there are files related to error handling and reporting within the interpreter.

    - `grammar`: This directory contain the grammar definition files, such as `SmallerBasic.g4`, which define the syntax and structure of the SmallerBasic language using ANTLR grammar notation.

    - `interpreter`: This is a crucial directory containing the implementation of the interpreter for the SmallerBasic language.

        - `dispatch_table.py`: This file contains the implementation of a dispatch table used for efficiently executing different language constructs.

        - `global_memory.py`: This file contains the code related to managing the global memory and variables within the interpreter.

        - `interpreter.py`: This is the main interpreter implementation that executes SmallerBasic programs by traversing the abstract syntax tree and performing actions based on the language constructs.

        - `library`: This directory contain the library files that provide built-in functions or utilities for SmallerBasic programs, for example `IO`, `Math` and `String` libraries.

- `main.py`: This is the entry point of your interpreter, where execution starts when running the interpreter.

- `utils`: This directory could hold utility files that are used throughout the project, for example the metaclass that colors prints.

## Starting point working locally

**Create and start a new virtual environment**

`source create_venv.sh venv`

**Start current virtual environment**

`source venv/bin/activate`

**Deactivate the current virtual environment**

`deactivate`

## Usage

```
Usage: smallbasic [OPTION] [FILE]
Run Smaller Basic program

Options:
  -h      display this help and exit
  -g      generate grammar
  -gas    generate grammar and run all files in source_code folder
  -as     run all files in source_code folder
```

## Interpreter

### Run a file

`smallbasic <file>.sb`

For example, you can ri-generate the grammar and run a file in `source_code` directory in the following way:

`smallbasic -g source_code/source.sb`

### Generate grammar

`antlr4 -Dlanguage=Python3 -visitor src/grammar/SmallerBasic.g4`

- **Requirements**: the same or greater java version used to compile the antlr4 jar. (in our case **java-18-openjdk-amd64**)

- Change version of java: `update-alternatives --config java`.

- `antlr4` is an alias generated by the `create_venv.sh` file.

### Run a file using `python3` interpreter

`python3 -m src.main source_code/<file>.sb`

## Contact

If you have any questions or suggestions regarding this repository, please don't hesitate to reach out. You can contact us via the GitHub repository or through the following channels:
- Email: [federico.bruzzone.i@gmail.com] or [federico.bruzzone@studenti.unimi.it]
