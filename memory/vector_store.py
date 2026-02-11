import chromadb
import uuid

class VectorStore:

    def __init__(self):
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection(
            name="agent_memory"
        )

    def store_memory(self, text: str):
        self.collection.add(
            documents=[text],
            ids=[str(uuid.uuid4())]
        )

    def retrieve_memory(self, query: str):
        results = self.collection.query(
            query_texts=[query],
            n_results=3
        )
        return results["documents"]

vector_store = VectorStore()
