# Drifting Blue - 2 | VulnHub Walkthrough

## Introduction
This walkthrough demonstrates how I exploited the Drifting Blue - 2 machine from VulnHub. Basic scanning revealed several services running, and I proceeded step-by-step to gain root access. Let's dive in!

---

## Step 1: Nmap Scan

I started with a basic Nmap scan and discovered the following open ports:

- FTP (21)
- SSH (22)
- HTTP (80)

FTP allowed **anonymous login**, and upon logging in, I found an image file but no further clues.

![Image 1](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Drifting%20Blue%20--%202/img/img1.png)

---

## Step 2: Website Enumeration

Next, I checked the website but found nothing interesting in the source code or any login page. So, I used **Gobuster** to enumerate directories. This revealed a `/blog/` directory.

Running **Gobuster** inside the `/blog/` directory, I found a WordPress installation and a link in the source code that revealed a domain name.

![Image 2](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Drifting%20Blue%20--%202/img/img2.png)
![Image 3](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Drifting%20Blue%20--%202/img/img3.png)

---

## Step 3: WordPress User Enumeration

Since the site was running WordPress, I performed a **WordPress scan** using `wpscan` and luckily found a valid username.

![Image 4](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Drifting%20Blue%20--%202/img/img4.png)

---

## Step 4: WordPress Login Brute Force

With the username in hand, I attempted to brute-force the password using `wpscan`. After several attempts, I successfully logged in.

![Image 5](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Drifting%20Blue%20--%202/img/img5.png)

---

## Step 5: Reverse Shell via WordPress

After logging in, I checked for vulnerable parameters to spawn a reverse shell. I inserted a **PHP reverse shell** into the `404.php` template and triggered it by visiting:
(Triggered url : "http://driftingbblues.box/blog/wp-content/themes/twentytwentyone/404.php")

![Image 6](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Drifting%20Blue%20--%202/img/img6.png)

I set up my listener and successfully got a shell as `daemon`.

![Image 7](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Drifting%20Blue%20--%202/img/img7.png)

---

## Step 6: Privilege Escalation

After some enumeration, I discovered a user named **freddie** and found their SSH private key.

![Image 8](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Drifting%20Blue%20--%202/img/img8.png)

I successfully logged in via SSH as `freddie`.

---

## Step 7: Root Access

Running `sudo -l` revealed that I could run **nmap** without a password. I exploited this to spawn a root shell:


