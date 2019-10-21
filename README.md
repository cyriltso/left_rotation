# Left Rank algorithm

### 1. Introduction

Repository that contains the Python file for the Left Rotation algorithm from HackerRank.

More information regarding the Left Rotation algorithm here : https://www.hackerrank.com/challenges/array-left-rotation/problem.

This algorithm allows the user to shift the positions of the elements inside of a string.

This algorithm will be able to be executed through the Terminal or through the use of Docker.

It's recommended to upload the entire repository from this GitHub page before proceeding to the next steps.

### 2. How to run the algorithm with the Terminal ?

To run the algorithm, you must go to your terminal and use the following command below :

**python -m input_string number_of_left_rotation**

Parameters :
-  input_string; type = string : the string for which we want to left rotate its elements.
-  number_of_left_rotation; type = int : number of left rotate we want to do.

### 3. How to run the algorithm with Docker ?

To run the algorithm with Docker, there are few steps to follow :

1.  Launch the Terminal on your computer.
2.  You have to locate on your directory that contains the Python script and the Dockerfile (a succession of instructions on which a Docker image is built and ran on).
3.  Use this command to build the image of the Python script : **docker build -t left_rotate .**
4.  Once the image is built, use this command to run the image that will launch the script : **docker run -it --rm left_rotate input_string number_of_left_rotation**. 

**left_rotate** will act as the image that contains **main.py** and **LeftRotate.py**. 

For example, if I want to left rotate elements by 2 in the string "abcdefg", you will have to write this command : **docker run -it --rm left_rotate abcdefg 2**, the output will be 'cdefgab'.

### 4. Contents of the repository

-  LeftRotation.py : Python file that contains the code to do the left rotation.
-  main.py : Python file that allows to run the left rotation from the terminal.
-  Dockerfile : A text file that contains all the instructions to execute while building the image of an application.
