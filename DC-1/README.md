# DC-1 Write-up

## Nmap Scan
The initial **Nmap** scan revealed the following open ports: SSH, HTTP, and RPCBind. The target was identified as a Drupal site, which was interesting due to the presence of several directories indicated by Nmap.

![Image 1](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-1/img/img1.png)

## robots.txt
Upon inspecting the `robots.txt` file, I found a list of disallowed directories. After visiting `UPGRADE.txt`, I was able to identify the Drupal version being used.

![Image 2](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-1/img/img2.png)

### Note
At this point, there were two possible approaches to exploit the system: 
1. Using a reverse shell directly via Metasploit.
2. Utilizing a Python script to exploit the add admin user vulnerability.

I opted for the Metasploit method, which I will demonstrate below.

![Image 3](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-1/img/img3.png)

### Getting the Meterpreter Shell
After executing the Metasploit exploit, I successfully obtained a Meterpreter shell.

![Image 4](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-1/img/img4.png)

### Finding Flags
I located **flag4** in the home directory and **flag1** in the web directory files.

![Image 5](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-1/img/img5.png)
![Image 6](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-1/img/img6.png)

### Database Access
During my exploration, I discovered SQL database files. After some digging, I found the database user and password, allowing me to log in.

![Image 7](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-1/img/img7.png)
![Image 8](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-1/img/img8.png)

### Flag Enumeration
After some enumeration within the database, I found **flag3** located in the nodes.

![Image 9](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-1/img/img9.png)

### User Credentials
I also retrieved the user **Fred**’s password hash. However, it’s important to note that this hash is for Drupal login, not for SSH. I considered cracking it.

![Image 10](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-1/img/img10.png)
![Image 11](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-1/img/img11.png)

### Finding SUID Binaries
After searching for SUID binaries, I discovered the `find` binary, which I could utilize. Using this binary, I managed to view files in the root directory and got final flag.

![Image 12](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-1/img/img12.png)
![Image 13](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/DC-1/img/img13.png)

---

- **Sagar Sehrawat**  
