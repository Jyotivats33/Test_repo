import pdfplumber
import json
import re
import os

from dotenv import load_dotenv
#from torch._dynamo.polyfills import os

# Load the PDF file
load_dotenv()
print("Starting with regulatory data extraction")
print(os.getenv( "REGULATORY_PDF_PATH"))
pdf_path = os.getenv( "REGULATORY_PDF_PATH")

# Define a list to store extracted rules
rules = []

# Extract text from specific pages (where the rules table is located)
start_page = 165
end_page = 280

with pdfplumber.open(pdf_path) as pdf:
    for page_num in range(start_page - 1, end_page):  # PDF pages are 0-indexed
        text = pdf.pages[page_num].extract_text()
        if text:
            lines = text.split("\n")
            for line in lines:
                # Use regex to find rule number and description
                match = re.match(r"(\d+)\.\s(.+)", line)
                if match:
                    rule_id = int(match.group(1))
                    description = match.group(2)
                    rules.append({
                        "rule_id": rule_id,
                        "description": description,
                        "reporting": "Report as per regulatory guidelines."
                    })

# Convert extracted rules to JSON format
json_output = {"rules": rules}

# Save to a file
with open("loan_rules.json", "w") as json_file:
    json.dump(json_output, json_file, indent=2)

print("Rules extracted and saved to loan_rules.json")
