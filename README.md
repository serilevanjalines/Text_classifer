# Text Classifier - Entity Extraction for Communication Analysis

Natural Language Processing tool that extracts sender and receiver information from unstructured text queries using spaCy NER (Named Entity Recognition).

## Features
- **Name extraction**: Identifies PERSON entities using spaCy's pre-trained model
- **Email extraction**: Regex-based pattern matching for email addresses
- **Phone extraction**: Detects 10-digit phone numbers
- **Smart mapping**: Associates extracted emails/phones with closest detected names by position
- **JSON output**: Structured data format for easy integration

## Tech Stack
- Python
- spaCy (en_core_web_sm)
- Regex for pattern matching

## Use Case
Built for communication monitoring systems (like SIH 2025 project) to parse natural language queries and extract structured contact information for sender-receiver identification.

## Example Input/Output
**Input Query:**
"Give me details regarding the communication between Ram and Prasanna in the email prasana@gmail.com and ra@gmail.com about burglary."

text

**Output:**
```json
{
    "sender_name": "Ram",
    "sender_email": "ra@gmail.com",
    "sender_number": null,
    "receiver_name": "Prasanna",
    "receiver_email": "prasana@gmail.com",
    "receiver_number": null
}
