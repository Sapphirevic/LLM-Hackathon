# LLM-Hackathon

# Sales AI Chatbot

Welcome to the Sales AI Chatbot! This chatbot leverages advanced language models to provide insightful answers based on your sales data. It is designed to help you analyze and understand sales trends, performance metrics, and other relevant information.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Conversational Interface**: Engage with the chatbot to ask questions about your sales data.
- **Dynamic Responses**: Receive tailored answers based on the dataset provided.
- **Chat History**: Keep track of your conversation history for reference.

## Technologies Used

- **Python**: Main programming language.
- **Transformers**: For language model integration.
- **LangChain**: For managing conversational retrieval.
- **HuggingFace**: For model assesibility.
- **FAISS**: For efficient similarity search.
- **Pandas**: For data manipulation.

## Getting Started

### Prerequisites

Before running the chatbot, ensure you have the following installed:

- Python 3.11 or higher
- Necessary libraries (install using `pip`):
  ```bash
  pip install transformers langchain gradio faiss-cpu pandas

This model requires a higher GPU for better performance. Try running it in colab with the TGPU enabled.
