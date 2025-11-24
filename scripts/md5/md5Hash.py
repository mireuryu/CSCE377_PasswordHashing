# Mireu Ryu
# takes an unhashed password .csv file as an input,
# outputs a list of MD5 hashed passwords
# (drops strength level from the original .csv file)
# scripts/md5Hash.py
# How to run:
# python scripts/md5Hash.py --in data/<replace with file name>.csv
# EX) python scripts/md5Hash.py --in data/pwlds_weak.csv


import csv, hashlib, argparse, os



def md5_hex(password: str) -> str:
    return hashlib.md5(password.encode('utf-8')).hexdigest()

def process_file(inpath: str, outpath: str):
    read_count = 0
    with open(inpath, newline='', encoding='utf-8') as infile, \
         open(outpath, 'w', newline='', encoding='utf-8') as outfile:

        reader = csv.DictReader(infile)
        if 'Password' not in reader.fieldnames:
            raise ValueError(f"CSV {inpath} must have a 'Password' column")

        # Only write the hashed password
        fieldnames = ['PasswordHash']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            pw = row['Password']
            h = md5_hex(pw)
            writer.writerow({'PasswordHash': h})
            read_count += 1

    print(f"Processed {read_count} rows -> wrote {outpath}")


def main():
    p = argparse.ArgumentParser(description="Compute plain MD5 hashes from CSV")
    p.add_argument('--in', dest='inpath', required=True, help='input CSV path')
    p.add_argument('--out', dest='outpath', default=None, help='output CSV path')
    args = p.parse_args()

    # Folder for output
    out_folder = 'md5HashedData'
    os.makedirs(out_folder, exist_ok=True)

    if args.outpath:
        out = args.outpath
    else:
        base_name = os.path.basename(args.inpath)
        out = os.path.join(out_folder, f"md5_{base_name}")

    if os.path.abspath(out) == os.path.abspath(args.inpath):
        raise SystemExit("Refusing to overwrite input file. Provide --out to specify a different file.")
    
    process_file(args.inpath, out)

if __name__ == '__main__':
    main()

