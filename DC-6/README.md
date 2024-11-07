# DC-6 CCTF Writeup

## Nmap Scan

I started with an Nmap scan to identify open ports. The scan revealed that SSH and HTTP were open, with a WordPress instance running on the web server. The domain name was also displayed in the Nmap results.

![Nmap Results](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-6/img/img1.png)


## WordPress Enumeration

After performing enumeration on the WordPress site, I discovered 5 users. I attempted to brute force the passwords but was unsuccessful after trying nearly 30,000 passwords. I then consulted the man page on VulnHub and found a command to create a custom wordlist.

![Wordlist Generation](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-6/img/img2.png)

![Brute Force Attempt](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-6/img/img3.png)

Using this wordlist, I successfully brute-forced the password for the user "mark".

![Mark's Password](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-6/img/img4.png)


## Gaining Access

I logged in as mark but found no plugins or appearances for a reverse shell. I then checked the Activity Monitor for known exploits or vulnerabilities.

![Activity Monitor](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-6/img/img5.png)

I discovered an RCE exploit on ExploitDB.

![ExploitDB](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-6/img/img6.png)

I set up the payload on my local server, made some code edits, and uploaded the site. Within seconds, I obtained a reverse shell.

![Reverse Shell](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-6/img/img7.png)

![Shell Access](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-6/img/img8.png)


## User Enumeration

I established the shell as a regular shell and began enumerating the machine. I found the password for the user "graham" and switched to that account.

![Graham's Password](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-6/img/img9.png)

Using `sudo -l`, I discovered that I could run the `jens/backups.sh` script. I also ran linpeas in parallel, revealing the MySQL user password for WordPress and all user hashes.

![Linpeas Results](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-6/img/img10.png)

![User  Hashes](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-6/img/img11.png)

![MySQL Password](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-6/img/img12.png)


## Privilege Escalation

Focusing on privilege escalation through `backups.sh`, I edited the script and executed it as jens, gaining shell access as jens.

Using `sudo -l`, I found that I could run `nmap` with no password. I utilized this to escalate privileges to root and successfully obtained a root shell.

![Root Shell Access](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-6/img/img13.png)

![Final Shell](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-6/img/img14.png)


## Author

- **Sagar Sehrawat**  
