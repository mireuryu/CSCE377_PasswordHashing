# Alaa Ismail
# Extracts only the bcrypt hashes from the output of bcryptHash.py to use 
# in the dictionary attack
# scripts/bcryptExtractHash.py
# How to run:
# python3 scripts/bcryptExtractHash.py hashed.csv
# EX) python3 scripts/bcryptExtractHash.py hashed_weak.csv

import pandas as pd
import glob
import os

folder = "../../data"

files = glob.glob(os.path.join(folder, "*.csv"))

for f in files:
    df = pd.read_csv(f)

    # extract the 3rd column (index 2)
    hash_col = df.iloc[:, 2]

    # build output filename
    base = os.path.basename(f)              
    name, ext = os.path.splitext(base)     
    out_file = os.path.join(folder, f"{name}_hashOnly.csv")

    # save the third column as a new CSV
    hash_col.to_csv(out_file, index=False, header=["bcrypt_hash"])

    print(f"Created: {out_file}")
