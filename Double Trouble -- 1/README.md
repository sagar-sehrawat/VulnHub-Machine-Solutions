# Double Trouble: 1 - VulnHub Walkthrough

This is a detailed walkthrough of the Double Trouble: 1 machine from VulnHub.

## Initial Enumeration

### Nmap Scan
Started with an initial Nmap scan and found two open ports: **SSH (22)** and **HTTP (80)**.

![Nmap Scan](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Double%20Trouble%20--%201/img/img1.png)

### Gobuster Scan
After discovering HTTP, I ran a **Gobuster** scan to look for hidden directories. Gobuster found several directories, and one of them, `/secret`, contained an image file.

![Gobuster Scan](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Double%20Trouble%20--%201/img/img2.png)

## Steganography on Image
I found an image in the `/secret` directory, so I used **stegseek** to perform steganography and retrieve hidden credentials from the image.

![Stegseek on Image](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Double%20Trouble%20--%201/img/img3.png)

## Logging into the Website
Using the credentials obtained, I logged into the website. After enumerating the site, I found no signs of a file upload feature that could allow a reverse shell.

![Login and Site Enumeration](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Double%20Trouble%20--%201/img/img4.png)

## Exploiting qdPM Version 9.1
Since the website was running **qdPM 9.1**, I researched known vulnerabilities for this version and found a Remote Code Execution (RCE) vulnerability. I set up a listener to catch the reverse shell.

![RCE Exploitation](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Double%20Trouble%20--%201/img/img5.png)
![Listener Setup](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Double%20Trouble%20--%201/img/img6.png)

## Privilege Escalation
After getting a shell as the `daemon` user, I further enumerated the box. I noticed there was no typical user, which led me to think it might be vulnerable to **Dirty COW**. However, running `sudo -l` revealed that the `www-data` user could execute `awk` without a password.

Using this, I spawned a root shell and successfully rooted the box.

![Root Shell](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Double%20Trouble%20--%201/img/img7.png)

- Sagar Sehrawat
