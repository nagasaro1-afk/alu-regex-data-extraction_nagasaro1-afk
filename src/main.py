import re
import json

input_path = "../input/raw-text.txt"
output_path = "../output/sample-output.json"
max_size = 50000

email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
card_pattern = r"\b(?:\d[ -]?){13,19}\b"
phone_pattern = r"(?:\+?\d{1,3}[\s.-]?)?(?:\(?\d{2,4}\)?[\s.-]?){1,2}\d{3}[\s.-]?\d{3,4}"
url_pattern = r"https?://[^\s\"'<>]+"


def get_email_type(email):
    email = email.lower()
    if email.endswith("@alumni.alueducation.com"):
        return "ALU alumni email"
    if email.endswith("@si.alueducation.com"):
        return "ALU SI email"
    if email.endswith("@alueducation.com"):
        return "ALU official email"
    return "regular email"


def hide_email(email):
    if "@" not in email:
        return "***"
    parts = email.split("@")
    name = parts[0]
    domain = parts[1]
    if len(name) <= 2:
        hidden = name[0] + "*"
    else:
        hidden = name[0:2] + "*" * (len(name) - 2)
    return hidden + "@" + domain


def check_luhn(number):
    digits = list(number)
    digits.reverse()
    total = 0
    i = 0
    for d in digits:
        d = int(d)
        if i % 2 == 1:
            d = d * 2
            if d > 9:
                d = d - 9
        total = total + d
        i = i + 1
    if total % 10 == 0:
        return True
    else:
        return False


def hide_card(number):
    return "**** **** **** " + number[-4:]


print("Reading input file...")

f = open(input_path, "r", encoding="utf-8")
text = f.read()
f.close()

if len(text) > max_size:
    print("file too big, stopping")
    exit()

lines = text.split("\n")

emails = []
for line in lines:
    found = re.findall(email_pattern, line)
    for e in found:
        emails.append({"masked": hide_email(e), "type": get_email_type(e)})

print("Emails found: " + str(len(emails)))
for e in emails:
    print("  " + e["masked"] + " (" + e["type"] + ")")

cards = []
rejected_cards = 0
for line in lines:
    found = re.findall(card_pattern, line)
    for match in found:
        clean_number = match.replace(" ", "").replace("-", "")
        if len(clean_number) < 13 or len(clean_number) > 19:
            continue
        if check_luhn(clean_number):
            cards.append(hide_card(clean_number))
        else:
            rejected_cards = rejected_cards + 1

print("")
print("Valid cards: " + str(len(cards)) + " (rejected " + str(rejected_cards) + ")")
for c in cards:
    print("  " + c)

phones = []
for line in lines:
    found = re.findall(phone_pattern, line)
    for p in found:
        p = p.strip()
        just_digits = re.sub(r"\D", "", p)
        if len(just_digits) < 7:
            continue
        if p.isdigit() and len(p) > 10:
            continue
        phones.append(p)

print("")
print("Phones found: " + str(len(phones)))
for p in phones:
    print("  " + p)

urls = []
for line in lines:
    found = re.findall(url_pattern, line)
    urls.extend(found)

print("")
print("URLs found: " + str(len(urls)))
for u in urls:
    print("  " + u)
