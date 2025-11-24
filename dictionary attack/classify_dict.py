import re

weak_file = open("weak_100k.txt", "w")
moderate_file = open("moderate_100k.txt", "w")

weak_count = moderate_count = strong_count = 0
LIMIT = 100000  # 100k per category

def classify(password):
  length = len(password)
  has_lower = re.search(r"[a-z]", password) is not None
  has_upper = re.search(r"[A-Z]", password) is not None
  has_digit = re.search(r"[0-9]", password) is not None
  has_symbol = re.search(r"[^A-Za-z0-9]", password) is not None

  # Weak
  if length < 8:
    return "weak"
  if (has_lower or has_upper) and not has_digit and not has_symbol:
    return "weak"
  if has_digit and not has_lower and not has_upper and not has_symbol:
    return "weak"

  # Strong
  if length >= 12 and has_lower and has_upper and has_digit and has_symbol:
    return "strong"

  # Moderate (everything else)
  return "moderate"


with open("dictionary_1M.txt", "r", errors="ignore") as f:
  for line in f:
    pw = line.strip()

    if not pw:
        continue

    category = classify(pw)

    if category == "weak" and weak_count < LIMIT:
      weak_file.write(pw + "\n")
      weak_count += 1

    elif category == "moderate" and moderate_count < LIMIT:
      moderate_file.write(pw + "\n")
      moderate_count += 1

    # Stop early if we have all three files full
    if weak_count >= LIMIT and moderate_count >= LIMIT:
      break

weak_file.close()
moderate_file.close()

print("Done!")
print("Weak:", weak_count)
print("Moderate:", moderate_count)