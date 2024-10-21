# Clover Writeup

## Initial Recon

Started with a Rustscan and found FTP, SSH, and HTTP services running as normal.

![img 1](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Clover/img/img1.png)

Logged into FTP as `anonymous` and found 3 files, but none of them were useful.

![img 2](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Clover/img/img2.png)

Started some directory busting and found lots of content to work with, including a `phpmyadmin` panel—perhaps we need to perform SQL injection there. There was also a `robots.txt` file but nothing of interest. Additionally, I found a webpage, but nothing was discovered during my enumeration.

![img 4](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Clover/img/img4.png)

In the source code of a page, I saw a comment mentioning a CMS under construction: ColdFusion. This was useful, and after further enumeration, I found its directory `CFIDE`, leading to a login page. The comment also mentioned, "we forgot to disable the login page," which seemed like a hint.

![img 3](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Clover/img/img3.png)

I tried some basic SQL injection, and it worked! I logged in but found nothing significant. There was nothing interesting in the cookies either.

![img 5](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Clover/img/img5.png)

I then captured the login request through Burp Suite and used SQLmap with the static POST request. After some effort, I was able to retrieve the database named `clover`.

![img 6](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Clover/img/img6.png)

After further digging, I found the tables and eventually retrieved user credentials.

![img 7](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Clover/img/img7.png)
![img 8](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Clover/img/img8.png)

## Cracking the Hash

I tried cracking the hash using John and Hashcat but couldn't crack it. After identifying the hash using `hash-identifier`, I discovered it was an MD5 hash for the user `asta`. Using an online tool, I cracked the hash and logged in as `asta`.

![img 9](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Clover/img/img9.png)

## Privilege Escalation

After doing basic enumeration, I found another user, `sword`. I tried importing LinPEAS for automatic enumeration, but since neither curl nor wget was available, I transferred the script using PHP and launched it. I found part of `sword`'s password, but it was incomplete.

![img 10](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Clover/img/img10.png)

Using Python automation for permutations, I generated a wordlist. You can also use Crunch to do this and crack the `sword` password with Hydra. After successfully logging in as `sword` and performing further enumeration with LinPEAS, I found an SUID binary.

![img 11](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Clover/img/img11.png)
![img 12](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Clover/img/img12.png)

The binary was named `daemon`. Initially, I suspected cron jobs were involved, so I used pspy to monitor them, but found nothing.

![img 13](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Clover/img/img13.png)

Next, I focused on the `daemon` binary. I transferred it to my local machine and performed reverse engineering. After some research, I figured out the command I needed to use, which gave me a root shell.

![img 14](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Clover/img/img14.png)

- **Sagar Sehrawat**  
  GitHub: [https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions)
