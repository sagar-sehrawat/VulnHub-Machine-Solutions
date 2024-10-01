# Pylington Machine - Walkthrough

## 1. Initial Enumeration with Nmap
Started with an nmap scan and found the following open ports:

- **22** - SSH
- **80** - HTTP

Additionally, there were some disallowed entries in the `robots.txt` file.

![Nmap Scan](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Pylington/img/img1.png)

## 2. Website Analysis and Login
After visiting the website, a login page was discovered. Tried some basic credentials such as `admin:admin` but they didn’t work. Next, `robots.txt` was checked, and a hidden entry was found, revealing valid login credentials.

![Login Page](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Pylington/img/img2.png)

## 3. Python IDE Exploitation
The application turned out to be a restricted Python IDE that blocks some commands like `import` `os` and `open`. However, hex-encoded `exec` payloads worked, allowing us to execute commands. Initially, I thought of retrieving the SSH private key, but `/home/py` did not have an `.ssh` directory.

![Restricted IDE](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Pylington/img/img3.png)

## 4. Reverse Shell Payload
I crafted a reverse shell payload using standard input and embedded it into the IDE’s program section. This successfully spawned a reverse shell.

![Reverse Shell Payload](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Pylington/img/img4.png)
![Reverse Shell Obtained](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Pylington/img/img5.png)

## 5. Typing Game Analysis
Upon exploring the user’s home directory, I found a `typing.cc` file and a corresponding binary named `typing`. The binary asked for a specific sentence to be entered. By typing the correct text, it revealed the contents of `password.txt` from the same directory.

![Typing Game](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Pylington/img/img6.png)

## 6. Backup Directory Exploitation
The home directory also contained a `secret_stuff` directory, which had a `backup` program. It allowed appending text to any file in `/srv/backups` directory. I initially considered using this to spawn a shell, so I used `pspy64` to monitor cron jobs but found nothing unusual. 

I then decided to overwrite `/etc/sudoers` to grant `ALL=NOPASSWORD: ALL` privileges to the user.

## 7. Privilege Escalation and Root Access
After successfully overwriting `/etc/sudoers`, I switched to the root user and obtained the root flag.

![Root Flag](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Pylington/img/img7.png)

---

- Sagar Sehrawat
