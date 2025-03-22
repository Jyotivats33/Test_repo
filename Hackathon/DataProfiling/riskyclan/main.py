import os

from dotenv import load_dotenv

from DataProfiling.riskyclan.RegulatoryDataExtract import regulatoryDataExtraction
load_dotenv()
print("Starting with regulatory data extraction")
print(os.getenv( "REGULATORY_PDF_PATH"))
regulatoryDataExtraction(os.getenv( "REGULATORY_PDF_PATH"))
