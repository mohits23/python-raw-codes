@echo off
time /t | clip 
powershell -command "Get-Clipboard" > C:\Users\Acer\AppData\Local\Programs\Python\Python38-32\Batt.txt 
cls
exit
