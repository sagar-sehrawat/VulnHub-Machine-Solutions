# Money Box VulnHub Walkthrough

This is a detailed walkthrough of the Money Box VulnHub machine.

---

## Step 1: Finding the Target's IP

We start by finding the IP address of the target machine.

![Image 1](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Money%20Box/img/img1.png)

---

## Step 2: Nmap Scan

After identifying the IP, I performed a quick Nmap scan and found three open ports: FTP, SSH, and HTTP.

![Image 2](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Money%20Box/img/img2.png)

---

## Step 3: Exploring FTP

I noticed that anonymous FTP login is allowed. I logged in and found a `.jpg` file. After downloading it to my system, I used `strings` and `exiftool` but didn't find anything useful, so I kept it for later use.

![Image 3](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Money%20Box/img/img3.png)

---

## Step 4: Investigating the Web Server

The machine is running a web server. After exploring the site, I found something interesting in the source code.

![Image 4](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Money%20Box/img/img4.png)

---

## Step 5: Secret Directory

The source code revealed the name of a secret directory. I navigated to the directory and found a hidden message.

![Image 5](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Money%20Box/img/img5.png)

---

## Step 6: Extracting Data from the Image

The secret message looked like a password key. I used `steghide` to extract hidden data from the image I found earlier. It prompted me for a password, and the key from the secret directory worked. I extracted a `data.txt` file containing a username and the hint that the password is weak.
(Hint : Secret Key 3xtr4ctd4t4 > extractdata)

![Image 6](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Money%20Box/img/img6.png)

---

## Step 7: Brute-Forcing SSH

With the username `renu` and the knowledge that the password is weak, I brute-forced the SSH login and successfully got access.

![Image 7](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Money%20Box/img/img7.png)

---

## Step 8: First Flag

After logging in as `renu`, I obtained the first flag.

![Image 8](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Money%20Box/img/img8.png)

---

## Step 9: Privilege Escalation to Lily

I checked if `renu` could run any `sudo` commands but found no access. I found another user, `lily`, and obtained the second flag from her home directory. I also noticed that her `.ssh` folder was accessible, allowing me to SSH into her account without a password.

![Image 9](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Money%20Box/img/img9.png)

---

## Step 10: Root Access and Final Flag

Once logged in as `lily`, I discovered that she could run `perl` with no password. I exploited this to spawn a root shell and grabbed the final flag.

![Image 10](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Money%20Box/img/img10.png)
![Image 11](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Money%20Box/img/img11.png)

---

Thank you for following along!

- **Sagar Sehrawat**
