# Drifting Blue 6 - VulnHub Machine Solution

This write-up covers the steps to solve the Drifting Blue 6 machine on VulnHub. The challenge involves directory brute-forcing, zip file password cracking, uploading a reverse shell, and exploiting the Dirty Cow vulnerability to gain root access.

---

## Step 1: Initial Scan with Nmap

Starting with an Nmap scan, only the HTTP port was open, which seemed odd. After checking the `robots.txt` file, I found a mention of a `.zip` file in a directory. A gobuster attempt led me to discover a hidden path `/textpattern`.

![Nmap Scan and Robots.txt](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Drifting%20Blue%20--%206/img/img1.png)

---

## Step 2: Finding a Login Page

In the `/textpattern/textpattern` directory, I found a login page for **Textpattern** CMS. I searched for exploits using `searchsploit`, but none of them were useful in this case.

![Textpattern Login](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Drifting%20Blue%20--%206/img/img2.png)

---

## Step 3: Cracking a Password-Protected Zip File

Using `gobuster`, I discovered a password-protected zip file. To crack it, I used `fcrackzip` (though you can also use `john`), and managed to retrieve the login credentials.

![Zip File Cracked](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Drifting%20Blue%20--%206/img/img3.png)

---

## Step 4: Uploading a PHP Reverse Shell

After logging in and enumerating the site, I found a file upload page. With this, I suspected the existence of a trigger directory for the uploaded files. Using `dirbuster`, I found the path `/textpattern/files/`. I uploaded a PHP reverse shell, set up a listener, and triggered the shell by accessing the file, gaining shell access as the `daemon` user.

![Reverse Shell Obtained](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Drifting%20Blue%20--%206/img/img4.png)

---

## Step 5: Privilege Escalation

Upon further enumeration using `linpeas` and manual inspection, I noticed there were no user accounts. However, I found that the machine was vulnerable to the **Dirty Cow** exploit, which was suggested by `linpeas` as well. The exploit allows the creation of a new user with root privileges. I compiled the Dirty Cow exploit using `gcc` and ran it successfully, which prompted me to set a password for the newly created user.

![Dirty Cow Exploit](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Drifting%20Blue%20--%206/img/img5.png)

---

## Step 6: Gaining Root Access

After successfully running the Dirty Cow exploit, I switched to the newly created user and gained root access.

![Root Access](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Drifting%20Blue%20--%206/img/img6.png)

---

Thanks for following along!

\- **Sagar Sehrawat**
