import subprocess

print('Started...')

try:
    s = subprocess.Popen(["gcc", "hello.c"], shell=True, stderr=subprocess.PIPE) # This Will Compile The 'C' Code and
                                                                                 #  will also return Compile Time Errors.
    compile_result = s.stderr.read().decode("utf-8")                                    
    print('Result =', compile_result)

    if compile_result == '':
        print('Empty String')
        # subprocess.call("./a.exe")
        s2 = subprocess.Popen(['a.exe'], shell=True, stdout=subprocess.PIPE)
        output = s2.stdout.read().decode("utf-8")
        print('Output :', output[3:8], ' ~~~Got!')
    else:
        print('Compile Result Type :',type(compile_result))
        print('Nope')
                                        
    # subprocess.call("./a.exe") # This Will Run The 'C' Code and
                                 #  will also return Output if No Compile Time
                                 #    Error is found.
    
except Exception as e:
    print('Console Error :', e)

finally:
    print('Done...!!')
