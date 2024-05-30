from google.cloud import language_v1
from google.oauth2 import service_account
credentials = service_account.Credentials.from_service_account_file('path/to/credentials.json')
client = language_v1.LanguageServiceClient(credentials=credentials)