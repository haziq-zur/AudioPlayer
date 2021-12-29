# AudioPlayer
A simple audio player generated from python codes to play some audio file from a prespecified directory. 

The control include Play, Pause, Stop and Load(user need to load file directory that contain audio file first to populate playlist).

Load button will pop up a dialog box for user to change directory accordingly. For now, only able to load .mp3 file type.

## Audio folder
User can also load from other folder using Load Button.

## Package used
1. pygame (access to mixer class for playing audio file)
2. tkinter (GUI)
3. auto-py-to-exe (compile script to executable)

## Tested Audio file types
1. MP3

## Creating Executables
1. Install Auto Py To Exe (python -m pip install auto-py-to-exe)
2. Compile and packages the script: ../src/interfaces.py
