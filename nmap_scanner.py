import subprocess

def nmap():

    target = input("Enter target IP or hostname: ")

    command = ["nmap",target]

    result = subprocess.run(command,capture_output=True,text=True)

    if result.returncode==0:
        print(result.stdout)
    else:
        print("Error:",result.stderr)

print("======================================")
print("        NMAP SCANNER")
print("======================================")

print("Select NMAP Scanning Type:")
print("1. Single IP ie. (192.168.1.10)")
print("2. IP Range ie. (192.168.1.10-20)")
print("3. IP/Subnet ie. (192.168.1.0/24)")
print("4. Distinct IPs ie. (192.168.1.10, 192.168.1.15)")
print("5. Text File ie. (targets.txt)")

ch=int(input("Enter Your Choise:"))

if ch==1:
    print("1. Single IP ie. (192.168.1.10)")
    nmap()

elif ch==2:
    print("2. IP Range ie. (192.168.1.10-20)")
    nmap()

elif ch==3:
    print("3. IP/Subnet ie. (192.168.1.0/24)")
    nmap()

elif ch==4:
    print("4. Distinct IPs ie. (192.168.1.10, 192.168.1.15)")
    nmap()

elif ch==5:
    print("5. Text File ie. (targets.txt)")

    target = input("Enter Target File Name: ")
    
    command = ["nmap","-iL",target]
    
    result = subprocess.run(command,capture_output=True,text=True)
    
    if result.returncode==0:
        print(result.stdout)
    else:
        print("Error:",result.stderr)

print("\nStarting scan...")
print("--------------------------------------")
print("Scan completed.")