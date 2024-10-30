# DC-4 VulnHub Walkthrough

## 1. Initial Nmap Scan
I started by scanning the machine using Nmap and found that SSH and HTTP (Nginx) were running. 

## 2. Enumerating the Website
After visiting the site, I found a login form. There wasn't anything interesting in the source code or directories, though I did discover some PHP files like `command.php`.

I tried default usernames such as `admin` and `root`, and got a hit with the username `admin`.

![Login Page](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-4/img/img1.png)
![Login Success](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-4/img/img2.png)

## 3. Exploiting `command.php`
The site was running the default command execution via the `command.php` script. I captured the request in Burp Suite and manipulated it, confirming that command injection was possible.

![Command Injection](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-4/img/img3.png)

## 4. Getting a Shell
I used a Python one-liner reverse shell command and injected it through `command.php`. This gave me a shell as the `www-data` user.

![Reverse Shell](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-4/img/img4.png)

## 5. Finding SSH Credentials for `jim`
During enumeration, I found three users. In `jim`'s backup files, I discovered a password list. I used this to brute-force the SSH login for `jim` and successfully got access to his account.

![SSH Brute Force](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-4/img/img5.png)
![Successful SSH Login](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-4/img/img6.png)

## 6. Discovering Credentials for `charles`
In `jim`'s directory, I found a mail file. After checking `/var/mail`, I discovered a password for the `charles` user.

![Mail File](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-4/img/img7.png)
![Password for charles](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-4/img/img8.png)

## 7. Privilege Escalation to Root
I logged in as `charles` and checked his `sudo` privileges using `sudo -l`. I found that he could run the binary `/usr/bin/teehee` as `root` without a password.

After doing some research on GTFOBins, I found that this binary could be exploited to overwrite files. I used it to overwrite `/etc/passwd` with a root user and gained a root shell.

![Overwriting /etc/passwd](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-4/img/img9.png)
![Root Shell](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-4/img/img10.png)

## 8. Root Access
Finally, I got root access!

![Root Access](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-4/img/img11.png)

---

**GitHub:** [Sagar Sehrawat]
