# CECE377_PasswordHashing

Password based authentication continues to be widely used because it is simple and easy to deploy. However, many security breaches have shown that passwords are often poorly protected. When attackers gain access to a password database, they can attempt to crack passwords offline without any restrictions, making weak hashing schemes ineffective. Older hashing algorithms, such as MD5, were designed to be fast. As a result, they offer little resistance against brute force and dictionary attacks. Advanced schemes, such as bcrypt, are specifically designed for stronger password protection and include features that intentionally slow down the hashing process. This increases the cracking effort required by attackers while keeping authentication practical for real users. 

The main problem addressed in this project is the weakness of fast hashing algorithms that are used for password storage. If an attacker obtains hashed passwords, fast algorithms allow millions of guesses per second, making password cracking practical and efficient. 
The objective of this experiment is to quantitatively compare MD5 and bcrypt in terms of security and usability. The focus of the experiment is highlighting differences in hashing time, cracking time, and computational resources, which affect offline attacks. By analyzing these factors, the experiment aims to prove why modern password hashing schemes provide stronger protection than classical approaches.
The system model assumes that a server stores user passwords using either MD5 or bcrypt as the hashing scheme. An attacker is assumed to have obtained access to the hashed password database and to possess necessary hardware and offline cracking tools, such as Hashcat. The system model implements the following security requirements: hash and crack passwords that are not associated with real user accounts. The password dataset is compiled of 500K passwords of varying strength levels as given in Appendix A. 
Under the threat model, attackers are assumed to have full access to the hashed passwords, complete knowledge of the hashing algorithm in use, and the ability to perform offline attacks without rate limits. Additionally, attackers are assumed to use optimized cracking software and hardware to maximize guessing efficiency. The main and usual goal of the adversary is to obtain as many correct password-guesses as possible.

**How to Run:**
Follow instructions in md5hash.py to hash all the data, and perform a dictionary attack on hashed files via commands below.
MD5 Dictionary Attack
Command: 
hashcat -m 0 <database folder>/<dataset>.csv attack/<dictionary>.txt 

Ex) run without cache

hashcat -m 0 md5HashedData/md5_pwlds_very_weak.csv attack/dictionary.txt --potfile-disable
hashcat -m 0 md5HashedData/md5_pwlds_weak.csv attack/dictionary.txt --potfile-disable
hashcat -m 0 md5HashedData/md5_pwlds_average.csv attack/dictionary.txt --potfile-disable
hashcat -m 0 md5HashedData/md5_pwlds_strong.csv attack/dictionary.txt --potfile-disable
hashcat -m 0 md5HashedData/md5_pwlds_very_strong.csv attack/dictionary.txt --potfile-disable



**Appendix**
This section provides supporting materials used in the conduct of this experiment.
Appendix A: Password Dataset
Password Dataset
Source: PWLDS
Description: public dataset of over 10 million passwords, with assigned strength levels: very weak, weak, average, strong, very strong.
Use: derived 100K passwords from each strength level to compile a comprehensive and scaled dataset of 500K passwords of varying strength levels
