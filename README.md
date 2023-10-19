# Auto
## Introduction:
Many people are using program to play games automatically. I am also striving to develop a program that can automatically play the dancing game I used to enjoy during my childhood. In this game, players need to press the arrow keys at specific intervals. Once all the arrows have been pressed, players must press the space or control key to obtain a score at a specific location.

## Implementation method
In my automated program, I mainly rely on the Python library OpenCV. The program follows this logic: Upon execution, it continuously captures screenshots. By using OpenCV, the captured screenshots are compared with the prepared arrow images. If a match is found, indicating the presence of an arrow, the program proceeds to press the corresponding key.
