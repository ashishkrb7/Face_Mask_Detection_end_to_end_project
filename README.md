# Face mask detection application
[![MIT License](https://img.shields.io/github/license/ashishcssom/Face_mask_detection.svg?style=flat-square)](https://github.com/ashishcssom/Face_mask_detection/blob/master/LICENSE)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555)](https://www.linkedin.com/in/ashishk766/)

## Demo

<img src="./log/DemoImage.png">

## Project description
[Dataset](https://drive.google.com/drive/folders/1QI_O0soGWn0jzm6mFKnhVh4OkKCb-_Nn?usp=sharing)

## Directory structure
```
D:.
│   app.py
│   Aptfile
│   config.py
│   Engine.py
│   LICENSE
│   MainAPI.bat
│   Procfile
│   README.md
│   requirements.txt
│   runtime.txt
│
├───dataset
│   ├───without_mask
│   │       Snapshot.png
│   │
│   └───with_mask
│           Snapshot (1).png     
│
├───log
│       DemoImage.png
│       MainAPIlog.log
│
├───models
│       deploy.prototxt
│       model
│       res10_300x300_ssd_iter_140000.caffemodel
│
├───notebook
│       ModelTester.ipynb
│       ModelTrainer.ipynb
│
├───static
│   ├───downloads
│   │       Snapshot.png
│   │
│   └───uploads
│           Snapshot.png
│
└───templates
        index.html
        WebSnapshot.html
```

## Instruction to install the application in local machine

1. Install Anaconda from this link https://www.anaconda.com/products/individual#windows and follow the steps mentioned in following link
https://docs.anaconda.com/anaconda/install/windows/

2. After Anaconda installation, go to search and run Anaconda Prompt and create virtual environment using following commands.

`conda create -n FaceDetect python=3.7 anaconda`

`conda activate FaceDetect`

3. Run Anaconda prompt and change the drive to the location of manual folder and run command `pip install -r requirements.txt`. This will install all the packages require for model execution.
    - (base) C:\Users\imash>conda activate FaceDetect
    - (FaceDetect) C:\Users\imash>
    - (FaceDetect) C:\Users\imash>pip install -r requirements.txt 
4. MainAPI.bat is Batch file for easy start of server and it can be used as schedular. In this file modify the line number 5 and 6 for the location of activate.bat  in base and python.exe in virtual environment. To run the server in your local, just hit MainAPI.bat file.
```
@echo off
SET LOGFILE="%~dp0\log\MainAPIlog.log"
(echo====================================================================================================== >> %LOGFILE%)
(echo Script Start Running at - ^ %date% %time% >> %LOGFILE%)
call "C:\ProgramData\Anaconda3\Scripts\activate.bat"
"C:\Users\imash\.conda\envs\FaceDetection\python.exe" "%~dp0\app.py"
(echo Script Successfully Executed at - ^ %date% %time% >> %LOGFILE%)
(echo====================================================================================================== >> %LOGFILE%)
pause
```

## Application deployment in Heroku

<!-- 1. Procfile — This specifies the commands to be executed by Heroku’s server by the app on startup.
2. requirements.txt — This contains the list of modules in your virtual environment it can be gotten by executing in your terminal .
3. runtime.txt — Used to specify the python version to be run of the server -->

## Credit
[PyImageSearch](https://www.pyimagesearch.com/)
[Chandrika deb github link](https://github.com/chandrikadeb7)

## License
```
MIT License

Copyright (c) 2020 Ashish Kumar
```

