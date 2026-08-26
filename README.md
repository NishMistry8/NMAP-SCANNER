# NMAP SCANNER



## Updates

### 26 August 2026

* Added Nmap scanning type selection.
* Added Single IP option.
* Added IP Range option.
* Added IP/Subnet option.
* Added Distinct IPs option.
* Added Text File scanning using `-iL`.

---

## Scanning Types

The program provides 5 different Nmap scanning options:

1. **Single IP**
   Example:

   ```text
   192.168.1.10
   ```

2. **IP Range**
   Example:

   ```text
   192.168.1.10-20
   ```

3. **IP/Subnet**
   Example:

   ```text
   192.168.1.0/24
   ```

4. **Distinct IPs**
   Example:

   ```text
   192.168.1.10, 192.168.1.15
   ```

5. **Text File**
   Example:

   ```text
   targets.txt
   ```

---

## Concepts Used

### 1. `subprocess`

-> Bridge between Python and CLI
-> Allows Python to run another program or terminal command.

In this project, `subprocess` is used to run the **Nmap program** from Python.

---

### 2. `target = input("Enter target IP or hostname: ")`

-> Takes the target IP address or hostname from the user.

Example:

```text
Enter target IP or hostname: 192.168.x.x
```

The entered value is stored inside the `target` variable.

---

### 3. Nmap Command

```python
command = ["nmap", target]
```

If the user enters:

```text
192.168.x.x
```

the command becomes:

```python
command = ["nmap", "192.168.x.x"]
```

which is equivalent to:

```text
nmap 192.168.x.x
```

---

### 4. `subprocess.run(command)`

-> `run()` is a function inside the `subprocess` module.
-> It executes the command provided to it.

Example:

```python
subprocess.run(["nmap", "192.168.x.x"])
```

This runs Nmap and performs the actual scan.

---

### 5. `capture_output=True`

```python
capture_output=True
```

-> Takes the output produced by the command and stores it inside Python instead of directly displaying it in the terminal.

This allows the program to access the Nmap results using `result.stdout`.

---

### 6. `text=True`

```python
text=True
```

-> Converts the captured output into a normal string.

This makes it easier to print and work with the Nmap output.

---

### 7. The `if` Statement

```python
if result.returncode == 0:
```

-> Checks whether the Nmap command completed successfully.

```text
0        -> Successful
Non-zero -> Error
```

If the return code is `0`, the program prints the Nmap output.

Otherwise, it prints the error message.

---

### 8. `result.stdout`

```python
result.stdout
```

-> `stdout` means **Standard Output**.
-> It contains the normal output produced by Nmap.

For example:

```text
PORT     STATE    SERVICE
22/tcp   open     ssh
80/tcp   open     http
```

---

### 9. `result.stderr`

```python
result.stderr
```

-> `stderr` means **Standard Error**.
-> It contains the error message produced by the program if something goes wrong.

---

### 10. `def nmap():`

```python
def nmap():
```

-> Creates a function named `nmap`.

A function is a block of code that can be called whenever it is needed.

In this project, the function contains the basic Nmap scanning process.

---

### 11. User Choice

```python
ch = int(input("Enter Your Choice:"))
```

-> Takes the user's scanning-type choice.

The program uses `if` and `elif` statements to determine which scanning option was selected.

```text
1 → Single IP
2 → IP Range
3 → IP/Subnet
4 → Distinct IPs
5 → Text File
```

---

### 12. Text File Scanning

For the text-file option, the program uses:

```python
command = ["nmap", "-iL", target]
```

If the user enters:

```text
targets.txt
```

the command becomes:

```python
["nmap", "-iL", "targets.txt"]
```

which is equivalent to:

```text
nmap -iL targets.txt
```

### What is `-iL`?

`-iL` tells Nmap to **read the targets from an input file**.

For example, `targets.txt` can contain:

```text
192.168.1.10
192.168.1.15
192.168.1.20
```

Nmap will read these targets from the file and scan them.

---

## Technologies Used

* **Python**
* **Nmap**
* **subprocess module**

## Project Purpose

This project uses Python to interact with the **Nmap network scanning tool** and display scan results. It is designed to practice Python, command-line interaction, and basic network scanning concepts.
