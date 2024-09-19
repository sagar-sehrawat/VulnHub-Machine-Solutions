# VulnHub Machine Walkthrough: FunBox

This is a step-by-step walkthrough for the "FunBox" VulnHub machine.

## 1. Nmap Scan

Performed an Nmap scan and found the following open ports: FTP, SSH, HTTP, and MySQL. Also identified the domain name.

![img1](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/FunBox/img/img1.png)

## 2. Website Enumeration

Visited the site and used Gobuster to identify that it was running WordPress. Quickly performed a WPScan and found two users: `admin` and `joe`.

![img2](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/FunBox/img/img2.png)

## 3. Brute Force Attack

Brute-forced the user `joe` across WordPress, FTP, and SSH. Found that all passwords were the same.

![img3](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/FunBox/img/img3.png)

## 4. FTP and SSH Access

Logged in via FTP and found nothing special. Then, logged in via SSH and encountered a restricted shell (`rbash`). After breaking out of the restricted shell, discovered an interesting message in `joe`'s home directory:

Hi Joe, please tell funny the backupscript is done.

![img4](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/FunBox/img/img4.png)

## 5. Enumerating Cron Jobs

Run `pspy64` to monitor cron jobs and noticed that both `funny` and `root` were running cron jobs.

## 6. Reverse Shell via Cron Job

Injected a reverse shell into the cron job executed by `funny`.

![img5](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/FunBox/img/img5.png)

After waiting 1-2 minutes for the cron job to run, successfully obtained a shell as the `funny` user.

![img6](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/FunBox/img/img6.png)

## 7. Root Shell

After several attempts, managed to get a root shell because the root cron job was executed after `funny`.

![img7](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/FunBox/img/img7.png)

- Sagar Sehrawat

