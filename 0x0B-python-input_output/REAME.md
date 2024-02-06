0x0B-python-input_output


In Python, file input and output are operations that involve reading from and writing to files. 

To perform file input, you can use the `open()` function to open a file in read mode, like this:

```python
file = open('filename.txt', 'r')
```

To read the contents of the file, you can use methods like `read()`, `readline()`, or `readlines()`.

```python
content = file.read()
```

For file output, you can open a file in write mode and write to it using the `write()` method.

```python
file = open('output.txt', 'w')
file.write('Hello, this is a sample text.')
```

It's important to close the file after you're done with it to free up system resources.

```python
file.close()
```

Alternatively, you can use the `with` statement to automatically close the file after it's done being used.

```python
with open('filename.txt', 'r') as file:
    content = file.read()
```

This is just a basic overview. There are many other operations and modes available for file input and output in Python.


Requirements:

Python Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc.

Python Test Cases
Allowed editors: vi, vim, emacs
All your files should end with a new line
All your test files should be inside a folder tests
All your test files should be text files (extension: .txt)
All your tests should be executed by using this command: python3 -m doctest ./tests/*
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
