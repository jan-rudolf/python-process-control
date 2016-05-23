#Python process control for PyWPS

This code is supposed to demonstrate the ability to create, pause/suspend, resume and kill/terminate processes by Python.

The program runs simple process of writing lines of numbers into file *output.txt* (lines of *main.py* 6-12). During short time intervals, the program pause the process printing numbers into the file for 20 seconds (lines 36-38 in *main.py*). After 20 seconds process continues to printing lines into the file for next 20 seconds, then is forced to terminate (lines 36-42).  

##Installation

1. create **virtualenv**

2. clone project

 `git clone https://github.com/jan-rudolf/python-process-control.git`

3. install requirements

 `pip install -r requirements.txt`

##Run 

Make sure, that two command line windows are opened in the project directory.

###Step 1 in window 1

Make sure, that *output.txt* is an empty file and you are waiting/scanning for whatever new content comes in, everytime before step 2:

 `rm output.txt 2>/dev/null;touch output.txt;tail -f output.txt`

###Step 2 in window 2

Run `python main.py` and observe the output of the program and the content of the file *output.txt* in the window 1.



