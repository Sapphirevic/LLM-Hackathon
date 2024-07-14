# from dotenv import load_dotenv
# import os
# import pandas as pd
# from pymongo import MongoClient
# from flask import Flask, request, jsonify
# import openai
# from langchain.chains import LLMChain
# from langchain_community.llms import OpenAI
# from openai.types.chat import ChatCompletionMessage
# from langchain.prompts import PromptTemplate
# from langchain.chat_models import ChatOpenAI
# from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate
# from langchain.memory import MongoDBChatMessageHistory
# from langchain.chains import LLMChain
# from langchain.schema import BaseMessage

# # Load environment variables from the .env file
# # env_path = 'C:/Users/2024/llm/LLM-Hackathon/src/.env'
# # load_dotenv(dotenv_path=env_path)
# openai_api_key = 

# # Initialize the ChatOpenAI model
# model = ChatOpenAI(
#     api_key="openai_api_key",
#     temperature=0.2,
#     model='gpt-3.5-turbo'
# )

# # Create the chat prompt template
# prompt = ChatPromptTemplate.from_messages([
#     ("system", """You are a sales analyst assistant. Provide accurate answers based on the {context} provided. 
#     If you don't know the answer to any question, truthfully say so and do not make up information."""),
#     MessagesPlaceholder(variable_name="chat_history"),
#     HumanMessagePromptTemplate.from_template("{input}")
# ])

# # Create the LLMChain
# chain = LLMChain(llm=model, prompt=prompt)

# # Initialize MongoDB chat message history
# def get_chat_history(session_id: str) -> MongoDBChatMessageHistory:
#     return MongoDBChatMessageHistory(
#         session_id=session_id,
#         connection_string="mongodb://localhost:27017",
#         database_name="History",
#         collection_name="chat_history"
#     )

# # Function to fetch context from MongoDB
# def fetch_context_from_mongodb():
#     client = MongoClient("mongodb://localhost:27017")
#     db = client["sales_database"]
#     collection = db["retail_data"]
    
#     # Fetch the most recent document as an example
#     # You may want to adjust this query based on your needs
#     document = collection.find_one(sort=[('_id', -1)])
    
#     if document:
#         context = f"""
#         Period: {document['Period']}
#         City: {document['City']}
#         Channel: {document['Channel']}
#         Category: {document['Category']}
#         Segment: {document['Segment']}
#         Manufacturer: {document['Manufacturer']}
#         Brand: {document['Brand']}
#         Item Name: {document['Item Name']}
#         Pack Size: {document['Pack_Size']}
#         Packaging: {document['Packaging']}
#         Unit Price: {document['Unit_Price']}
#         Sales Volume (KG/LTRS): {document['Sales_Volume(KG_LTRS)']}
#         Sales Value: {document['Sales_Value']}
#         """
#         return context
#     else:
#         return "No data available in the database."

# # Main conversation loop
# def chat_bot():
#     session_id = "terminal_session"  # You can generate a unique ID if needed
#     chat_history = get_chat_history(session_id)

#     print("Welcome to the Sales Analyst Assistant. Type 'exit' to end the conversation.")
    
#     while True:
#         user_input = input("\nYou: ")
#         if user_input.lower() == 'exit':
#             print("Thank you for using the Sales Analyst Assistant. Goodbye!")
#             break
        
#         context = fetch_context_from_mongodb()
        
#         response = chain.run(
#             context=context,
#             chat_history=chat_history.messages,
#             input=user_input
#         )
        
#         print(f"\nAssistant: {response}")
        
#         # Add the interaction to chat history
#         chat_history.add_user_message(user_input)
#         chat_history.add_ai_message(response)

# if __name__ == "__main__":
#     chat_bot()