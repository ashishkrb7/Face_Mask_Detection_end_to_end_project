@echo off
SET LOGFILE="%~dp0\log\MainAPIlog.log"
(echo====================================================================================================== >> %LOGFILE%)
(echo Script Start Running at - ^ %date% %time% >> %LOGFILE%)
call "C:\ProgramData\Anaconda3\Scripts\activate.bat"
"C:\Users\imash\.conda\envs\FaceDetection\python.exe" "%~dp0\app.py"
(echo Script Successfully Executed at - ^ %date% %time% >> %LOGFILE%)
(echo====================================================================================================== >> %LOGFILE%)
pause
