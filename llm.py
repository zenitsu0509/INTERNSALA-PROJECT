from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.prompts import ChatPromptTemplate
from langchain_huggingface import HuggingFaceEndpoint
from test_extraction import TextExtraction
def generate_response(text):
    textdata = ""
    for i in text:
        textdata += str(i).replace("\n", " ")

    endpoint_url = (
        "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
    )
    llm = HuggingFaceEndpoint(endpoint_url=endpoint_url,api_key = "")

    prompt = f"""
    Extract key information from the following Document and format it as a structured JSON object. Use the given example structure for guidance. Include only the relevant details in the proper JSON format.

    Example Format:
    {{
        "PO Number": "11748477",
        "PO Date": "16-Nov-2024",
        "PO Expiry": "18-Nov-2024",
        "PO Amount": "12602.38",
        "Account Store": "RAI",
        "Account Name": "ResoluteAI Software",
        "Account Delivery Address": "DELHI",
        "Account Billing Address": "BANGALORE",
        "Account GST": "125648W",
        "Account Client Number": "88888",
        "List Items": [
            {{
                "Sr. No.": "1",
                "Description": "NVIDIA",
                "Qty": "12",
                "MRP": "30",
                "Unit Cost": "22.86",
                "Total Value": "288"
            }},
            {{
                "Sr. No.": "2",
                "Description": "LINUX",
                "Qty": "12",
                "MRP": "30",
                "Unit Cost": "22.86",
                "Total Value": "288"
            }}
        ]
    }}

    Format the extracted information from the provided post into this JSON structure and include only valid, extracted details.

    The Post Data you have is: {textdata}                                               
    """
    response = llm.generate(prompts=[prompt])
    return list(list(response)[0])[1][0][0].text
text_extractor = TextExtraction()

pdf_path = "Document Extraction 2.pdf"
pdf_text = text_extractor.extract_pdf_info(pdf_path)
print(generate_response(pdf_text))
