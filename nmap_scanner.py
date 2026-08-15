import subprocess

print("======================================")
print("        NMAP SCANNER")
print("======================================")

target = input("Enter target IP or hostname: ")

print("\nStarting scan...")
print("--------------------------------------")

command = ["nmap", target]

result = subprocess.run(command,capture_output=True,text=True)

if result.returncode == 0:
    print(result.stdout)
else:
    print("Error:")
    print(result.stderr)

print("--------------------------------------")
print("Scan completed.")