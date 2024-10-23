# VulnHub DC-2 Walkthrough

## Initial Enumeration

### Nmap Scan
I started by running an Nmap scan, which revealed that HTTP and SSH were open on the target machine. After some more enumeration, I found that the site was running WordPress.

### Discovery of Flag 1
By exploring the WordPress site further, I discovered **Flag 1**, along with a hint to use `cewl` for password generation.

![Flag 1](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-2/img/img1.png)
![Flag 1 - Hints](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-2/img/img3.png)

## WordPress Users Enumeration

Next, I used `wpscan` to enumerate users and discovered three usernames. I then tried password cracking and found valid passwords for two users: **Jerry** and **Tom**.

![wpscan Results](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-2/img/img2.png)
![Password Cracking](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-2/img/img4.png)
![Login Credentials](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-2/img/img5.png)

## Gaining Access

### Logging in as Jerry
I logged into the WordPress site as **Jerry** and found **Flag 2**. After further enumeration, I was unable to obtain a reverse shell from the website, so I attempted to SSH into the machine with Jerry's and Tom's credentials.
![jerry](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-2/img/img7.png)

### SSH Access as Tom
Tom's credentials worked for SSH, but I was greeted with a restricted shell. I investigated the shell and discovered that I could run `vi` from within the restricted shell, which allowed me to read **Flag 3**. The hint in Flag 3 suggested using `su`.

![SSH as Tom](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-2/img/img7.png)

## Breaking Out of Restricted Shell

### Vi Shell Escape
Using the known technique of breaking out of restricted shells with `vi`, I was able to escape to a normal bash shell and read **Flag 4**.

![Flag 4](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-2/img/img9.png)
![Shell Escape](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-2/img/img8.png)

## Privilege Escalation

### Linpeas Enumeration
Running `linpeas` revealed some SQL credentials for the WordPress database, but they were not particularly useful. I then remembered the hint about using `su`, and I successfully switched to **Jerry**'s account using the WordPress password.

### Sudo Privileges as Jerry
Once logged in as Jerry, I checked my sudo privileges and found that I could run `git` as root. Using this, I escalated my privileges to root and captured the final flag.

![Root Access](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-2/img/img10.png)
![Privilege Escalation](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-2/img/img11.png)
![Final Flag](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-2/img/img12.png)


### Author
**Sagar Sehrawat**
