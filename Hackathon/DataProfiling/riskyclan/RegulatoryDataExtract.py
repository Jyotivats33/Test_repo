
import fitz
import re
import tempfile
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain_community.document_loaders import DirectoryLoader

from DataProfiling.riskyclan.RuleCreation import loginOpenAI

def clean_filename(filename): # will be needed for chroma database collection creation
    new_filename = re.sub(r'\s\(\d+\)', '', filename)
    return new_filename

def regulatoryDataExtraction(filepath):
    print("Reading Regulatory pdf")
    print(filepath)
# doc = fitz.open ("../../FR_Y-14Q20240331_i.pdf")
  #  text = ""
   # for page in doc:
      #  text += page.get_text()
    # print(text[1:10])
    document =  load_pdfs_from_folder(filepath)
    print("document created....going to create chunks")

    chunks = split_document(document, 400, 10)
    print(f"Total chunks : {len(chunks)}")
    print("First chunk:")
    print(chunks[0].page_content)
    print("123rd chunk:")
    print(chunks[122].page_content)
    print("last chunk:")
    print(chunks[2216].page_content)



def load_pdfs_from_folder(folder_path):
    # Load all PDF files from the folder
    loader = DirectoryLoader(folder_path, glob="*.pdf", loader_cls=PyPDFLoader)

    # Load documents
    documents = loader.load()

    return documents


# def createTempDoc(filepath) :
#     try:
#
#         input_file = filepath.read()
#         temp_file = tempfile.NamedTemporaryFile(delete=False)
#         temp_file.write(input_file)
#         temp_file.close()
#
#         # load PDF document
#         loader = PyPDFLoader(temp_file.name)
#         documents = loader.load()
#
#         return documents
#
#     finally:
#         # Ensure the temporary file is deleted when we're done with it
#         os.unlink(temp_file.name)
#
#     #response = loginOpenAI(text)

def split_document(document, chunk_size, chunk_overlap)  -> object:
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size,
                                                   chunk_overlap=chunk_overlap,
                                                   length_function=len,
                                                   separators=["\n\n", "\n", " "])
    return text_splitter.split_documents(document)
