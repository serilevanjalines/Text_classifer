import spacy
import re
import json

nlp = spacy.load("en_core_web_sm")

query = "Give me details regarding the communication between Ram and Prasanna in the email prasana@gmail.com and ra@gmail.com WhatsApp about burglary."

doc = nlp(query)

# Extract names with their start positions
names = [(ent.text, ent.start_char) for ent in doc.ents if ent.label_ == "PERSON"]

# Extract emails with their positions
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails = [(m.group(), m.start()) for m in re.finditer(email_pattern, query)]

# Extract phones with positions
phone_pattern = r"\b\d{10}\b"
phones = [(m.group(), m.start()) for m in re.finditer(phone_pattern, query)]

# Function to find closest entity
def closest(target_pos, entities):
    if not entities:
        return None
    return min(entities, key=lambda x: abs(x[1] - target_pos))[0]

# Assign sender = first name, receiver = second name
sender_name = names[0][0] if len(names) > 0 else None
receiver_name = names[1][0] if len(names) > 1 else None

sender_email = closest(names[0][1], emails) if names else None
receiver_email = closest(names[1][1], emails) if len(names) > 1 else None

sender_number = closest(names[0][1], phones) if names else None
receiver_number = closest(names[1][1], phones) if len(names) > 1 else None

result = {
    "sender_name": sender_name,
    "sender_email": sender_email,
    "sender_number": sender_number,
    "receiver_name": receiver_name,
    "receiver_email": receiver_email,
    "receiver_number": receiver_number
}

print(json.dumps(result, indent=4))
