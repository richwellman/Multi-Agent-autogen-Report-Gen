from openai import AzureOpenAI
import config

az_openai_endpoint = config.az_openai_endpoint
az_open_ai_key = config.az_open_ai_key
az_open_ai_model = config.az_open_ai_model
az_deployment_name = config.az_deployment_name
az_openai_api_version = config.az_openai_api_version

# A utility function to download the Report Document created by the multi agent system
# it takes the file name as an argument and downloads the file to the current working directory
def download_document(file_name):

    client = AzureOpenAI(
    api_key=az_open_ai_key,  
    api_version=az_openai_api_version,
    azure_endpoint = f"https://{az_openai_endpoint}.openai.azure.com/"
    )
    for _file in client.files.list():
        # print(_file.filename)
        if _file.filename == file_name:
            doc_data = client.files.content(_file.id)
            doc_data_bytes = doc_data.read()
            with open("./report.docx", "wb") as file:
                file.write(doc_data_bytes)
                break

def download_document_from_id(file_id):
    client = AzureOpenAI(
    api_key=az_open_ai_key,  
    api_version=az_openai_api_version,
    azure_endpoint = f"https://{az_openai_endpoint}.openai.azure.com/"
    )
    doc_data = client.files.content(file_id)
    doc_data_bytes = doc_data.read()
    with open("./report.docx", "wb") as file:
        file.write(doc_data_bytes)


if __name__ == "__main__":
    # download_document("/mnt/data/Vanarsdel_Monthly_Business_Insights_Report_July_2024.docx")
    download_document_from_id("assistant-Hu7jQT7KDqDKZQpNupNiyVss")
