import subprocess


res = subprocess.call(["ls","-l"],shell=True)
print(res)

subprocess.call("ls -l",shell=True)
