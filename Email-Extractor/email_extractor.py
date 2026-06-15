import re

# Read file
with open("input.txt", "r") as file:
    text = file.read()

# Find emails using regex
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

# Save emails
with open("extracted_emails.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")

# Display emails
print("Extracted Emails:\n")

for email in emails:
    print(email)

print("\nEmails saved successfully!")
