# EvilBox -- One Writeup

## Enumeration

1. **Finding the IP Address**

   ![Finding IP](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/EvilBox%20--one/img/img1.png)

   We started by identifying the IP address of the target machine.

2. **Nmap Scan**

   ![Nmap Scan](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/EvilBox%20--one/img/img2.png)

   We performed an Nmap scan to enumerate open ports and services. This scan reveals that the machine is running SSH and HTTP. We used `-sC` and `-sV` for basic script scanning and version detection.

3. **Initial Web Enumeration**

   ![Apache Default Page](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/EvilBox%20--one/img/img3.png)

   The web server displayed the Apache default page. The source code review yielded no useful information.

4. **Nikto Scan**

   ![Nikto Scan](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/EvilBox%20--one/img/img4.png)

   Running a Nikto scan revealed a `/secret` directory.

5. **Directory Brute Forcing**

   ![Gobuster](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/EvilBox%20--one/img/img6.png)

   We used Gobuster to explore directories and found `robots.txt`.

   ![robots.txt](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/EvilBox%20--one/img/img5.png)

   The `robots.txt` file reveal a username. Concurrently, Hydra was used to brute-force SSH credentials.

6. **Exploring `/secret` Directory**

   ![Gobuster Secret Directory](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/EvilBox%20--one/img/img7.png)

   Gobuster revealed an `evil.php` file within the `/secret` directory.

   ![File Analysis](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/EvilBox%20--one/img/img8.png)

   This file appeared to be vulnerable to Local File Inclusion (LFI) or Remote Code Execution (RCE). Using `ffuf`, we confirmed it was indeed vulnerable.

7. **Viewing `/etc/passwd`**

   ![Viewing /etc/passwd](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/EvilBox%20--one/img/img9.png)

   We accessed the `/etc/passwd` file, which indicated potential for command execution but initially didn’t provide further access.

## Exploitation

1. **Finding SSH Keys**

   ![SSH Key](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/EvilBox%20--one/img/img10.png)

   We found an SSH private key in one of the user directories. However, it was password-protected.

2. **Cracking the SSH Key Password**

   ![Cracking SSH Key Password](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/EvilBox%20--one/img/img11.png)

   Using `ssh2john`, we cracked the password for the SSH key.

   ![Cracked Password](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/EvilBox%20--one/img/img12.png)

3. **SSH Login and User Flag**

   Successfully logging in via SSH, we obtained the user flag. We proceeded to escalate privileges.

4. **Privilege Escalation**

   ![LinPEAS Results](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/EvilBox%20--one/img/img13.png)

   Using LinPEAS, we identified that the `/etc/passwd` file had write permissions.

   ![Editing /etc/passwd](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/EvilBox%20--one/img/img14.png)

   Attempts to set a custom root password in `/etc/passwd` were unsuccessful.

   ![Adding a New User](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/EvilBox%20--one/img/img15.png)

   We then added a new user with root privileges and a custom password hash. 

   ![Final Steps](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/EvilBox%20--one/img/img16.png)

   This allowed us to escalate to root and gain full access.

## Conclusion

Thank you for following this writeup. I hope it provides valuable insights into the exploitation process.

- **Sagar Sehrawat**
