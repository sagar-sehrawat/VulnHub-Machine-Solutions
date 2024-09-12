# Drifting Blue 5 - VulnHub Machine Solution

This write-up covers the steps to solve the Drifting Blue 5 machine on VulnHub. It involves Nmap scanning, WordPress exploitation, brute-forcing SSH credentials, steganography, and privilege escalation through cron jobs.

---

## Step 1: Initial Scan with Nmap

Starting with an Nmap scan, I found both SSH and HTTP ports open. On visiting the HTTP service, I saw the default WordPress page with the message 'Just another WordPress site', indicating we're dealing with a WordPress installation.

![Nmap Scan Results](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Drifting%20Blue%20--%205/img/img1.png)

---

## Step 2: Directory Enumeration

Using `gobuster`, I found some interesting WordPress directories.

![Gobuster Results](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Drifting%20Blue%20--%205/img/img2.png)

---

## Step 3: WordPress User Enumeration

Since it's a WordPress site, I ran `wpscan` and found some valid usernames.

![WPScan Results](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Drifting%20Blue%20--%205/img/img3.png)

---

## Step 4: Brute-Forcing SSH

After performing a brute force attack, I was able to crack the password for the user `gill`.

![Brute Force Results](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Drifting%20Blue%20--%205/img/img4.png)

---

## Step 5: Steganography

During site enumeration, I found some pictures, one of which looked odd. I downloaded it and checked it for hidden data using steganography techniques. Luckily, I found the SSH password with Exiftool.

![Steganography Results](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Drifting%20Blue%20--%205/img/img6.png)

---

## Step 6: SSH Login & User Flag

With the credentials, I logged in as `gill` and retrieved the user flag. Additionally, I found a KeePass database file that was password-protected. I used `john` to crack the KeePass password.

![KeePass Crack](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Drifting%20Blue%20--%205/img/img8.png)

---

## Step 7: KeePass Database

Using an online KeePass viewer, I extracted some interesting data resembling usernames and passwords. I copied those details for later use.

![KeePass Data](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Drifting%20Blue%20--%205/img/img9.png)

---

## Step 8: Privilege Escalation via Cron Job

On further inspection of the machine, I found a folder named `keyfolder` and, after running `linpeas`, I discovered a `key.sh` script in the `/root` directory that ran as a cron job. I used `pspy64` to monitor background processes and saw the script being executed regularly.

The folder was owned by `root`, and the information I retrieved from the KeePass database seemed like filenames, not credentials. I tried creating files with these names and after several attempts, I found that creating a file named `fracturedocean` triggered the creation of a `rootcreds.txt` file.

![Pspy64 Monitoring](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Drifting%20Blue%20--%205/img/img10.png)

![Root Creds File](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Drifting%20Blue%20--%205/img/img11.png)

---

## Step 9: Final Flag

Finally, I retrieved the `rootcreds.txt` file, which contained the credentials to access the root account. Using those credentials, I got the final flag!

![Final Flag](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Drifting%20Blue%20--%205/img/img12.png)

---

-Sagar Sehrawat
