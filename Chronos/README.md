# Chronos VulnHub Walkthrough

This is a walkthrough for the Chronos machine on VulnHub

## Step 1: Initial Enumeration with Nmap

Started with an `nmap` scan and found three open ports: `22` (SSH), `80` (HTTP), and `8000` (an HTTP service running on a Node.js framework).

![Image 1](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Chronos/img/img1.png)

---

## Step 2: Analyzing the HTTP Service

After visiting the website on port `8000`, I found a basic site with no forms or interactive elements. However, by examining its JavaScript code, I noticed a request being sent for date and time using a `format` query parameter.

![Image 2](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Chronos/img/img2.png)

---

## Step 3: Investigating the Query Parameter

I intercepted the request with Burp Suite and discovered that the `format` parameter accepts a Base58-encoded string. Initially, I suspected that it might be a Server-Side Template Injection (SSTI) or command injection vulnerability. It turned out to be a command injection vulnerability with Base58 encoding, so I crafted a reverse shell payload encoded in Base58.

![Image 3](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Chronos/img/img3.png)

---

## Step 4: Executing the Payload

By sending the payload to the vulnerable URL, I was able to gain a reverse shell as the `www-data` user.

![Image 4](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Chronos/img/img4.png)  
![Image 5](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Chronos/img/img5.png)

---

## Step 5: Further Enumeration with LinPEAS

After basic enumeration with LinPEAS, I found multiple directories named `chronos` and `chronos-v2`. It seemed like another npm server was running locally on `127.0.0.1`.

![Image 6](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Chronos/img/img6.png)

---

## Step 6: Exploiting Local NPM Server

After enumerating the code, I found a vulnerable version of `express-fileupload` with known Remote Code Execution (RCE) vulnerabilities.

![Image 7](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Chronos/img/img7.png)

---

## Step 7: Gaining a Higher Privileged Shell

I set up a script on the victim machine and managed to get a reverse shell as `imera`.

![Image 8](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Chronos/img/img8.png)

---

## Step 8: Privilege Escalation to Root

Using `sudo -l`, I found that `imera` can run `npm` and `node` with `NOPASSWORD`. As expected, I used `node` for privilege escalation and gained a root shell.

![Image 9](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Chronos/img/img9.png)  
![Image 10](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Chronos/img/img10.png)

---

**- Sagar Sehrawat**  

