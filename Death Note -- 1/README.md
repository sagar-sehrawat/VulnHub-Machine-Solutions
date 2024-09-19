# VulnHub Machine Walkthrough: Deathnote -- 1

This document provides a step-by-step walkthrough for the "Deathnote -- 1" VulnHub machine.

## 1. Nmap Scan

Performed an Nmap scan to identify open ports. Found SSH and HTTP services running.

![img1](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Death%20Note%20--%201/img/img1.png)

## 2. Initial Exploration

Visited the website using the domain name and discovered a hint page suggesting the presence of `notes.txt` and checking its source code.

![img2](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Death%20Note%20--%201/img/img2.png)

Enumerated paths and discovered `notes.txt` and `user.txt` files.

![img3](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Death%20Note%20--%201/img/img3.png)
![img4](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Death%20Note%20--%201/img/img4.png)

## 3. Robots.txt and IP Access

Discovered `robots.txt` using Gobuster but it wasn't accessible via the domain. Accessed it through the IP.
![img5](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Death%20Note%20--%201/img/img5.png)

## 4. Image Analysis

Downloaded the image and found that it was not an actual image file. It contained hints about the username in `user.txt` and potential password in `notes.txt`.

![img6](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Death%20Note%20--%201/img/img6.png)

## 5. SSH Brute Force

Used Hydra to perform a brute-force attack on SSH and found valid credentials.

![img7](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Death%20Note%20--%201/img/img7.png)

## 6. Decoding Brainfuck Code

The `user.txt` file contained Brainfuck code. Decoded it to find hints about another user, Kira.

![img8](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Death%20Note%20--%201/img/img8.png)

## 7. Accessing Kira’s Account

Found that Kira was another user. Checked the `.ssh` folder and managed to log in as Kira without a password. The file's data, base64 decoded, provided hints to check `/opt` and `/var`.

![img9](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Death%20Note%20--%201/img/img9.png)

## 8. Finding Root Credentials

In `/opt`, found a file that was actually a text file disguised as a WAV file. This file contained the password needed to escalate privileges to root.

![img10](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Death%20Note%20--%201/img/img10.png)

## Conclusion

This walkthrough covers the steps to compromise the "Deathnote -- 1" VulnHub machine, including enumeration, file discovery, and privilege escalation techniques.

- Sagar Sehrawat


