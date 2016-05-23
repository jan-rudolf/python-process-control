#Python process control for PyWPS

This code is supposed to the ability to create, pause/suspend, resume and kill/terminate processes by Python.

##Installation

1. create **virtualenv**

2. clone project

 `git clone https://github.com/jan-rudolf/python-process-control.git`

3. install requirements

 `pip install -r requirements.txt`

##Run 

Make sure, that two command line windows are opened in the project directory.

###Step 1 in window 1

Make sure, that *output.txt* is an empty file and you are waiting/scanning for whatever new content comes in:

 `rm output.txt 2>/dev/null;touch output.txt;tail -f output.txt`

###Step 2 in window 2

Run `python main.py` and observe the output of the program and the content of file *output.txt* in the window 1.



