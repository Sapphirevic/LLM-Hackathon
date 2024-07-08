from pymongo import MongoClient
import pandas as pd
from transformers import AutoModelForCausalLM, AutoTokenizer

client = MongoClient("mongodb://localhost:27017/")
db = client["sales_database"]
collection = db["retail_data"]

# Load the data into a pandas DataFrame
data = pd.DataFrame(list(collection.find()))

data["Period"] = pd.to_datetime(data["Period"])


# Load model and tokenizer
model_name = "gpt-3.5-turbo"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)


# Define the prompt template
def generate_prompt(query, context):
    prompt = f"""
    You are a market performance expert. Based on the context provided, answer the following query. If you don't know the answer to any question truthfully say so and do not hallucinate.:
    Query: {query}
    Context: {context}
    """
    return prompt


def get_best_performing_brand(city):
    df = data[data["City"] == city]
    best_brand = df.groupby("Brand")["Sales_Volume(KG_LTRS)"].sum().idxmax()
    return best_brand


def get_sales_trends(quarter):
    df = data[data["Period"].dt.to_period("Q") == quarter]
    top_brands = df.groupby("Brand")["Sales_Volume(KG_LTRS)"].sum().nlargest(5)
    return top_brands


def compare_brand_performance(brand_a, brand_b):
    df_a = (
        data[data["Brand"] == brand_a]
        .groupby(["City", data["Period"].dt.to_period("Q")])["Sales_Volume(KG_LTRS)"]
        .sum()
    )
    df_b = (
        data[data["Brand"] == brand_b]
        .groupby(["City", data["Period"].dt.to_period("Q")])["Sales_Volume(KG_LTRS)"]
        .sum()
    )
    comparison = pd.DataFrame({"Brand A": df_a, "Brand B": df_b})
    return comparison


def get_market_size(quarter):
    df = data[data["Period"].dt.to_period("Q") == quarter]
    market_size = df["Sales_Value"].sum()
    return market_size


def get_chatbot_response(query):
    context = ""  # Extract relevant context from your dataset
    if "best performing brand" in query:
        city = query.split("in")[-1].strip()
        result = get_best_performing_brand(city)
        context = f"The best performing brand in {city} is {result}."
    elif "top-performing brands" in query:
        quarter = query.split("in the last quarter")[-1].strip()
        result = get_sales_trends(quarter)
        context = f"The top-performing brands in the last quarter are {result}."
    elif "performance of" in query:
        brands = query.split("compared to")
        brand_a = brands[0].split("performance of")[-1].strip()
        brand_b = brands[1].strip()
        result = compare_brand_performance(brand_a, brand_b)
        context = (
            f"Comparison of performance between {brand_a} and {brand_b}: {result}."
        )
    elif "market size" in query:
        quarter = query.split("in each quarter")[-1].strip()
        result = get_market_size(quarter)
        context = f"The market size in each quarter is {result}."

    prompt = generate_prompt(query, context)
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=100)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return response
