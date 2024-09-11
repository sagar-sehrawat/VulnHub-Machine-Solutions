# Drifting Blues 4

## Scanning and Initial Findings

Start with an Nmap scan and find the open ports: FTP (21), SSH (22), and HTTP (80).

![Nmap Scan](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Drifting%20Blue%20--%204/img/img1.png)

## Web Page Analysis

In the webpage source code, I found a nested Base64 encoded string. After decoding it multiple times, I reached a final decoder that revealed a TXT file location.

![Base64 Decoding](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Drifting%20Blue%20--%204/img/img2.png)

Inside the TXT file, there was a lot of Brainfuck code.

![Brainfuck Code](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Drifting%20Blue%20--%204/img/img3.png)

## QR Code and Usernames

After decoding the Brainfuck code, I found the location of an image containing a QR code. Scanning the QR code revealed some usernames.

![QR Code](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Drifting%20Blue%20--%204/img/img4.png)

## Brute Forcing FTP

I started with brute-forcing the FTP credentials. I found a valid user `hubert`.

![FTP Brute Force](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Drifting%20Blue%20--%204/img/img5.png)

The FTP directory for `hubert` had an empty `.ssh` folder, so I uploaded a custom-generated public key and the corresponding private key.

![SSH Directory](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Drifting%20Blue%20--%204/img/img6.png)

## Gaining User Access

After uploading the public key and setting the correct permissions, I logged in as `hubert` and retrieved the user flag.

![User Flag](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Drifting%20Blue%20--%204/img/img7.png)

## Privilege Escalation

Using linpeas and manual enumeration, I found a SUID binary named `getinfo`.

![SUID Binary](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Drifting%20Blue%20--%204/img/img8.png)

The binary read the `ip` file in the `/tmp` directory. I created a script in `/tmp`, made it executable, and modified the `PATH` to run my script instead. This allowed me to gain root access.

![Root Access](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/Drifting%20Blue%20--%204/img/img9.png)
