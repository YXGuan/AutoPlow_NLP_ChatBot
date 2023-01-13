import json
from ibm_watson import AssistantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# api keys are stored in .gitignore

authenticator = IAMAuthenticator('{apikey}')
assistant = AssistantV1(
    version='2021-06-14',
    authenticator = authenticator
)

assistant.set_service_url('{url}')

response = assistant.message(
    workspace_id='{workspace_id}',
    input={
        'text': 'Hello'
    }
).get_result()

print(json.dumps(response, indent=2))