import spacy
import re
import json

nlp = spacy.load("en_core_web_sm")

query = "Give me details regarding the communication between Ram and Prasanna in the email prasana@gmail.com and ra@gmail.comWhatsApp about burglary."


doc = nlp(query)
names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]


email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
phone_pattern = r"\b\d{10}\b"

emails = re.findall(email_pattern, query)
phones = re.findall(phone_pattern, query)


sender_name = names[0] if len(names) > 0 else None
receiver_name = names[1] if len(names) > 1 else None


sender_email = emails[0] if len(emails) > 0 else None
receiver_email = emails[1] if len(emails) > 1 else None

sender_number = phones[0] if len(phones) > 0 else None
receiver_number = phones[1] if len(phones) > 1 else None


result = {
    "sender_name": sender_name,
    "sender_email": sender_email,
    "sender_number": sender_number,
    "receiver_name": receiver_name,
    "receiver_email": receiver_email,
    "receiver_number": receiver_number
}

# Print in nice JSON format
print(json.dumps(result, indent=4))

