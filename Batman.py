import subprocess

subprocess.call([r'C:\Users\Acer\AppData\Local\Programs\Python\Python38-32\TimeCatch.bat'])
with open("Batt.txt") as f:
    line = f.readline()[:5]
    print(line)
