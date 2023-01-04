import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

assistant_id = '5963c60b-6a6f-4548-b6dc-292105a12dfe'

authenticator = IAMAuthenticator('{apikey}')
assistant = AssistantV2(
    version='2021-06-14',
    authenticator = authenticator
)

assistant.set_service_url('{url}')

response = assistant.message(
    assistant_id='{assistant_id}',
    session_id='{session_id}',
    input={
        'message_type': 'text',
        'text': 'Hello'
    }
).get_result()

print(json.dumps(response, indent=2))