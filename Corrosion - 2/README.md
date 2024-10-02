# Corrosion - 2 Writeup

This is a **medium difficulty** machine that involves exploiting a Tomcat server, escalating privileges through SUID binaries, and ultimately gaining root access.

## Enumeration

### Initial Nmap Scan
I started with an Nmap scan and found three open ports: **SSH (22)**, **HTTP (80)**, and **HTTP (8080)**. The HTTP service on port 8080 was running **Tomcat**.

![Nmap Results](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Corrosion%20-%202/img/img1.png)

### User Enumeration
Manually checking the machine, I discovered that there are three users present: `randy` ,`jaye` and `tomcat`.

![User Enumeration](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Corrosion%20-%202/img/img2.png)

## Site Enumeration and Brute-forcing
Next, I enumerated the site and found a **login prompt** at `/manager`. The default credentials didn’t work, so I brute-forced the login and discovered some credentials, but none of them were successful.

![Login Prompt](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Corrosion%20-%202/img/img3.png)

## Directory Brute-forcing
Running `gobuster` revealed an interesting **zip file** that seemed unusual.

![Zip File Found](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Corrosion%20-%202/img/img4.png)

## Cracking the Zip File
I downloaded the file, but it was password protected. Using `fcrackzip` (or `zip2john`), I cracked it and found credentials for `admin` and `manager`. Logging in using these credentials was successful.

![Zip Cracked](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Corrosion%20-%202/img/img5.png)

![Successful Login](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Corrosion%20-%202/img/img6.png)

## Gaining a Reverse Shell
After logging in, I enumerated the site further and found a **Manager Authenticated Upload** feature. This allowed me to upload a shell and get a **Meterpreter session**.

![Uploading Shell](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Corrosion%20-%202/img/img7.png)

![Reverse Shell](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Corrosion%20-%202/img/img8.png)

## Privilege Escalation
I uploaded `linpeas` to the server to check for **SUID binaries**. After exploring a few of them, nothing seemed useful at first.

![Linpeas Output](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Corrosion%20-%202/img/img9.png)

## Switching Users
After some time, I attempted to switch to the `jaye` user using the same password found earlier. It worked!

![Switch to Jaye](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Corrosion%20-%202/img/img10.png)

## Exploring Jaye's Home Directory
In `jaye`’s home directory, I found a folder with an **interesting SUID file**. This file accepts a string and filename as input. By using a simple trick, I passed an empty string to it, which allowed me to read `/etc/shadow`.

![SUID Binary Exploit](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Corrosion%20-%202/img/img11.png)

## Cracking the Hash
I tried to extract the randy hash and successfully cracked it. The password was `07051986randy`. With this, I could escalate to root.

![Hash Cracked](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Corrosion%20-%202/img/img12.png)

## Final Privilege Escalation
Using `sudo -l`, I noticed that I could run `randombase64.py` as root. Searching for more `base64` file in the system, I found it to be a **SUID binary**. After some tinkering, I managed to spawn a root shell by executing os.system('/bin/bash') in file.

![Privilege Escalation](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Corrosion%20-%202/img/img13.png)

## Root Shell
Finally, I gained a root shell!

![Root Shell](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Corrosion%20-%202/img/img14.png)

## Conclusion
This machine involved a mix of **web exploitation, privilege escalation using SUID binaries, and brute-forcing techniques**. The key was to explore various methods and not give up when things seemed stuck.

---

### Author:
- **Sagar Sehrawat**
- [GitHub Profile](https://github.com/sagar-sehrawat)
