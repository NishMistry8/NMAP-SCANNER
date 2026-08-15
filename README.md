======================================
         NMAP SCANNER
======================================

1. subprocess
-> bridge btw python and CLI
-> allows Python to run another program or terminal command

2. target = input("Enter target IP or hostname: ")
-> Ex: Enter target IP or hostname: 192.168.x.x

3.  Nmap command ie. command = ["nmap", target]
-> command = ["nmap", "192.168.x.x"] -> nmap 192.168.x.x

4. subprocess.run(command)
-> run() is a function inside the subprocess module
-> Run this terminal program ie subprocess.run(["nmap", "192.168.x.x"])

5. capture_output=True
-> Take the output produced by the command and store it inside Python instead of directly to the terminal

6. text=True
-> Python converts the captured output into a normal string

7. The 'if' statement
-> IF the return code is 0, THEN print the Nmap output
ie 0 -> successful & non-zero -> error

8. result.stdout
-> stdout = Standard Output
-> The normal output produced by Nmap

9. result.stderr
-> stderr = Standard Error
-> he error message produced by the program



