# llama_index Readme

This repository contains code that utilizes the llama_index library for building and querying a vector store index. The index is designed to handle document retrieval based on vector representations of textual data.

## Prerequisites

Make sure you have the necessary dependencies installed. You can install them using the following:

```bash
pip install llama_index
```

## Getting Started

### 1. Setting up the Environment

Ensure that the required environment variable `OPENAI_API_KEY` is set. This key is necessary for the proper functioning of the code. If it is not set, the script will raise an exception, prompting you to set the key.

### 2. Loading and Indexing Documents

If the storage directory (`starter2/storage`) does not exist, the script proceeds with the following steps:

- **Loading Documents:** The code uses the `SimpleDirectoryReader` class from llama_index to load documents from the specified data directory (`starter2/data`).

- **Indexing Documents:** It creates a vector store index (`VectorStoreIndex`) from the loaded documents. With chunk size 512, which creates multiple embeddings with given chunk size.

- **Storing the Index:** The index is then persisted to the specified storage directory (`starter2/storage`) using the storage context.

### 3. Querying the Index

If the storage directory exists, the script loads the index from storage and prepares it for querying.

- **Query Engine:** The script creates a query engine from the loaded index using the `as_query_engine` method.

- **Querying the Index:** Finally, the script performs a sample query ("when did modi became prime minister of india") using the query engine and prints the response.

## Running the Code

Execute the script to run the code:

```bash
python3 starter2/starter2.py
```

Ensure that you have set the `OPENAI_API_KEY` environment variable before running the script.

Feel free to customize the data directory (`starter2/data`) and storage directory (`starter2/storage`) according to your requirements.