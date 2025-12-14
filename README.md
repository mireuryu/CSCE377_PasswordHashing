# CECE377 – Password Hashing Evaluation

## Overview

This project investigates the security weaknesses of **fast hashing algorithms** when used for password storage. If an attacker gains access to hashed passwords, fast algorithms (such as MD5) allow millions of guesses per second, making large-scale password cracking feasible.

The experiment quantitatively compares **MD5** and **bcrypt** in terms of:

* Hashing time
* Cracking time
* Computational cost

The goal is to demonstrate why modern password hashing schemes provide significantly stronger protection against offline attacks than classical approaches.

---

## Objectives

* Evaluate the security implications of using fast hashing algorithms for password storage
* Compare MD5 and bcrypt under identical attack conditions
* Measure how password strength affects cracking success rates
* Illustrate best practices for secure password storage

---

## System Model

The system assumes a server that stores user passwords using either **MD5** or **bcrypt** as the hashing scheme.

An attacker is assumed to:

* Obtain full access to the hashed password database
* Have complete knowledge of the hashing algorithm in use
* Possess optimized offline cracking tools (e.g., **Hashcat**)
* Face no rate limiting or access restrictions

To avoid ethical concerns, all passwords used in this experiment are **synthetic and not associated with real user accounts**.

---

## Threat Model

Under the threat model, the attacker:

* Has unrestricted access to hashed passwords
* Performs offline attacks without detection or rate limits
* Uses optimized hardware and software to maximize guessing efficiency

The adversary’s objective is to recover as many valid passwords as possible within a given time frame.

---

## Dataset

The experiment uses a dataset of **500,000 passwords** with varying strength levels:

* Very Weak
* Weak
* Average
* Strong
* Very Strong

Each category contains **100,000 passwords**, derived from a public password dataset.

---

## How to Run

### MD5

### 1. Hash the Passwords

Follow the instructions in `md5hash.py` to generate hashed password files for each strength category.

### 2. Perform a Dictionary Attack (MD5)

Use the following Hashcat command to perform a dictionary attack against MD5-hashed passwords:

```bash
hashcat -m 0 <database_folder>/<dataset>.csv attack/<dictionary>.txt
```

### Example Commands (Without Cache)

```bash
hashcat -m 0 md5HashedData/md5_pwlds_very_weak.csv attack/dictionary.txt --potfile-disable
hashcat -m 0 md5HashedData/md5_pwlds_weak.csv attack/dictionary.txt --potfile-disable
hashcat -m 0 md5HashedData/md5_pwlds_average.csv attack/dictionary.txt --potfile-disable
hashcat -m 0 md5HashedData/md5_pwlds_strong.csv attack/dictionary.txt --potfile-disable
hashcat -m 0 md5HashedData/md5_pwlds_very_strong.csv attack/dictionary.txt --potfile-disable
```

### bcrypt

### 1. Hash the Passwords


### 2. Perform a Dictionary Attack (bcrypt)


---

## Appendix

### Appendix A: Password Dataset

* **Source:** PWLDS
* **Description:** Public dataset containing over 10 million passwords, categorized by strength
* **Usage in this Experiment:**

  * 100,000 passwords selected from each strength category
  * Combined into a balanced dataset of 500,000 passwords

---

## License / Disclaimer

This project is for academic and educational use only. Do not use insecure hashing algorithms such as MD5 in production systems.
