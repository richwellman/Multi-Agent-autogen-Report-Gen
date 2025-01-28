from openai import AzureOpenAI
import config

az_openai_endpoint = config.az_openai_endpoint
az_open_ai_key = config.az_open_ai_key
az_open_ai_model = config.az_open_ai_model
az_deployment_name = config.az_deployment_name
az_openai_api_version = config.az_openai_api_version


client = AzureOpenAI(
    api_key=az_open_ai_key,
    api_version=az_openai_api_version,
    azure_endpoint=f"https://{az_openai_endpoint}.openai.azure.com/",
)

# A utlitity function to delete all files in the current working directory, except the files that are required to run the multi agent system
for _file in client.files.list(purpose="assistants_output"):
    # print(_file.filename)
    print(f"deleting File {_file.filename} ....")
    client.files.delete(_file.id)


