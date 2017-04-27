import subprocess
proc = subprocess.Popen('lsasdf', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
stdout_value = proc.stdout.read() + proc.stderr.read()

print stdout_value
