from google.cloud  import dialogflow_v2 as dialogflow

def detect_intent(session_id, message):

    project_id = "documentchatbotv1"
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.types.TextInput(text=message, language_code="en")
    query_input = dialogflow.types.QueryInput(text=text_input)

    response = session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result.fulfillment_text
