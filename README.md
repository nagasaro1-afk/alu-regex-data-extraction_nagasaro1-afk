# Data Extraction & Secure Validation Assignment

Name: Nicia Greta Agasaro
GitHub: nagasaro1-afk

## What this is

Regex assignment that pulls structured data out of raw/messy text (like
what you'd get back from an external API or a scraped support ticket)
and doesnt blindly trust the text it's given.

Extracts 4 things:
- Emails (with extra checks for ALU emails)
- Credit card numbers
- Phone numbers
- URLs

## Folder structure

alu-regex-data-extraction_nagasaro1-afk/
- input/raw-text.txt
- src/main.py
- output/sample-output.json
- README.md

## How to run it

Needs Python 3, no extra libraries, just re and json which are both built in.

cd src
python3 main.py

Reads input/raw-text.txt, prints a summary in the terminal, and saves
the full result to output/sample-output.json.

## How the regex works

Emails - EMAIL_REGEX matches name@domain.tld. get_email_type() checks
alumni/si endings before the plain alueducation.com check, since those
addresses technically also end in alueducation.com.

Credit cards - CARD_REGEX grabs 13-19 digit runs, spaced, dashed or
squished together, then check_luhn() runs the actual luhn checksum.
Failed ones get dropped completely, not kept as invalid.

Phone numbers - PHONE_REGEX covers a few common formats. long
unformatted digit strings get skipped since those are more likely a
stray card number.

URLs - URL_REGEX only matches http or https links.

## Security stuff

Every line gets checked against bad_stuff before any extraction
happens. If a line matches something sketchy the whole line gets
skipped.

max_size stops the regex from running on a huge file.

Emails and card numbers are masked everywhere, console and json.
Phone numbers and urls arent masked since theyre not sensitive the
same way.

## Known limits

Luhn check confirms structure, not that a card is real or active.
Phone regex doesnt catch every format, just the ones i tested.
The bad_stuff list is basic, its showing the idea not a full
production sanitizer.
