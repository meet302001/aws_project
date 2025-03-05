import streamlit as st
import requests
import json

def call_lambda_api(blog_topic):
    url = "https://gjf2pperx6.execute-api.us-east-1.amazonaws.com/dev/blog-generation"  # Replace with your API Gateway endpoint
    headers = {"Content-Type": "application/json"}
    payload = json.dumps({"blog_topic": blog_topic})

    try:
        response = requests.post(url, headers=headers, data=payload)
        if response.status_code == 200:
            try:
                return response.json()  # Ensure valid JSON response
            except json.JSONDecodeError:
                return {"error": "Invalid JSON response from server", "raw_response": response.text}
        else:
            return {"error": f"Failed with status code {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}

# Streamlit UI
st.title("AI Blog Generator using AWS Bedrock & Lambda")

blog_topic = st.text_input("Enter Blog Topic:")

if st.button("Generate Blog"):
    if blog_topic.strip():
        response = call_lambda_api(blog_topic)
        st.json(response)  # Show API response
    else:
        st.error("Please enter a blog topic!")
