import os.path

# Basic RAG with simple document, showing loading, indexing, storage and query phases

from llama_index.core import ( VectorStoreIndex,
                               SimpleDirectoryReader,
                               StorageContext,
                               load_index_from_storage,)
import logging
import sys

# logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
# logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))


# pre check
openai_key = os.getenv("OPENAI_API_KEY")
if not openai_key:
    raise Exception("Please set OPENAI_API_KEY to proceed.")
# check if storage exists
PERSIST_DIR = "starter1/storage"
DATA_DIR = "starter1/data"
if not os.path.exists(PERSIST_DIR):
    # 1. loading
    documents = SimpleDirectoryReader(DATA_DIR).load_data()
    # 2. indexing
    index = VectorStoreIndex.from_documents(documents)
    # 3. storage
    index.storage_context.persist(persist_dir=PERSIST_DIR)
else:
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)

# 4. query the index now.
query_engine = index.as_query_engine()
response = query_engine.query("when did modi became prime minister of india")
print(response)