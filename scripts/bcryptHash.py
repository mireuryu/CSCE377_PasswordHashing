#!/usr/bin/env python3
"""
bcrypt_hash.py
<<<<<<< HEAD
=======

Usage:
  python bcrypt_hash.py --input passwords.txt --output hashed.csv --rounds 12 --workers 4 --include-plaintext

Produces CSV: password,bcrypt_hash,rounds,time_ms
"""
import argparse
import csv
import time
from functools import partial
from concurrent.futures import ProcessPoolExecutor, as_completed
import bcrypt

def hash_one(password: str, rounds: int, measure_time: bool = True, include_plain: bool = True):
    pw_bytes = password.encode('utf-8', errors='ignore')
    start = time.perf_counter() if measure_time else None
    salt = bcrypt.gensalt(rounds=rounds)
    bhash = bcrypt.hashpw(pw_bytes, salt)
    end = time.perf_counter() if measure_time else None
    time_ms = (end - start) * 1000 if measure_time else None
    return {
        "password": password if include_plain else "",
        "bcrypt_hash": bhash.decode('utf-8'),
        "rounds": rounds,
        "time_ms": round(time_ms, 3) if time_ms is not None else ""
    }

def process_file(input_path, output_path, rounds, workers, include_plain):
    with open(input_path, 'r', encoding='utf-8', errors='ignore') as f:
        passwords = [line.rstrip('\n') for line in f if line.strip() != ""]
    # Use ProcessPoolExecutor for CPU-bound hashing
    results = []
    if workers and workers > 1:
        with ProcessPoolExecutor(max_workers=workers) as ex:
            futures = [ex.submit(hash_one, pw, rounds, True, include_plain) for pw in passwords]
            for future in as_completed(futures):
                results.append(future.result())
    else:
        # sequential
        for pw in passwords:
            results.append(hash_one(pw, rounds, True, include_plain))

    # write CSV
    fieldnames = ["password", "bcrypt_hash", "rounds", "time_ms"]
    with open(output_path, 'w', newline='', encoding='utf-8') as csvf:
        writer = csv.DictWriter(csvf, fieldnames=fieldnames)
        writer.writeheader()
        for r in results:
            writer.writerow({
                "password": r["password"],
                "bcrypt_hash": r["bcrypt_hash"],
                "rounds": r["rounds"],
                "time_ms": r["time_ms"]
            })
    print(f"Hashed {len(results)} passwords -> {output_path}")

def main():
    ap = argparse.ArgumentParser(description="Hash passwords with bcrypt and save CSV.")
    ap.add_argument('--input', '-i', required=True, help='Input file (one password per line)')
    ap.add_argument('--output', '-o', required=True, help='Output CSV path')
    ap.add_argument('--rounds', '-r', type=int, default=12, help='bcrypt cost factor (default 12)')
    ap.add_argument('--workers', '-w', type=int, default=1, help='Number of parallel worker processes (default 1)')
    ap.add_argument('--include-plaintext', action='store_true', help='Include plaintext in output CSV (use only for lab data)')
    args = ap.parse_args()

    if args.include_plaintext is False:
        # rename to match variable used below
        include_plain = False
    else:
        include_plain = True

    process_file(args.input, args.output, args.rounds, args.workers, include_plain)

if __name__ == "__main__":
    main()
>>>>>>> 7d436099e9d605f43f2fdd9e330d359e7502549a

Usage:
  python bcrypt_hash.py --input passwords.csv --output hashed.csv --rounds 10 --workers 4 --include-plaintext

Input CSV must contain: password, strength
Output CSV: password, strength, bcrypt_hash,rounds,time_ms
"""
import argparse
import csv
import time
from concurrent.futures import ProcessPoolExecutor
import bcrypt # FIX THIS

def hash_one(row, rounds: int, include_plain: bool):
    """
    row: dictionary with keys {password, strength}

    Returns a dictionary with hashing results
    """
    password = row["Password"]
    strength= row["Strength_Level"]

    pw_bytes = password.encode('utf-8', errors='ignore')
    start = time.perf_counter()
    
    salt = bcrypt.gensalt(rounds=rounds)
    bhash = bcrypt.hashpw(pw_bytes, salt)

    end = time.perf_counter()
    time_ms = round((end - start) * 1000, 3)

    return {
        "password": password if include_plain else "",
        "strength": strength,
        "bcrypt_hash": bhash.decode('utf-8'),
        "rounds": rounds,
        "time_ms": time_ms
    }

def hash_one_wrapper(args):
    row, rounds, include_plain = args
    return hash_one(row, rounds, include_plain)

def process_file(input_path, output_path, rounds, workers, include_plain):
    # Read CSV input
    with open(input_path, 'r', encoding='utf-8', errors='ignore') as f:
        reader = csv.DictReader(f)
        rows = list(reader)# preserve ordering
    
    # Hash in parallel or sequential
    results = []
    if workers > 1:
        with ProcessPoolExecutor(max_workers=workers) as ex:
            results = list(
                ex.map (
                    hash_one_wrapper,
                    [(r, rounds, include_plain) for r in rows]
                )
            )
    else:
        results = [hash_one(r, rounds, include_plain) for r in rows]

    # Write output CSV
    fieldnames = ["password", "strength", "bcrypt_hash", "rounds", "time_ms"]
    with open(output_path, 'w', newline='', encoding='utf-8') as csvf:
        writer = csv.DictWriter(csvf, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print(f"Hashed {len(results)} passwords -> {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Hash passwords with bcrypt and save CSV.")
    parser.add_argument('--input', '-i', required=True)
    parser.add_argument('--output', '-o', required=True)
    parser.add_argument('--rounds', '-r', type=int, default=10)
    parser.add_argument('--workers', '-w', type=int, default=1)
    parser.add_argument('--include-plaintext', action='store_true')
    args = parser.parse_args()

    process_file(
        args.input, 
        args.output, 
        args.rounds, 
        args.workers, 
        args.include_plaintext)

if __name__ == "__main__":
    main()