from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

pdf_path = Path("Reynaldo_AI_Brain_v2.pdf")

if not pdf_path.exists():
    raise FileNotFoundError(
        f"Could not find: {pdf_path.resolve()}"
    )

print("Uploading AI Brain...")

with pdf_path.open("rb") as file:
    uploaded_file = client.files.create(
        file=file,
        purpose="assistants",
    )

print(f"Uploaded file: {uploaded_file.id}")

print("Creating vector store...")

vector_store = client.vector_stores.create(
    name="Reynaldo Portfolio AI Brain"
)

print(f"Vector store: {vector_store.id}")

print("Indexing AI Brain...")

vector_file = client.vector_stores.files.create_and_poll(
    vector_store_id=vector_store.id,
    file_id=uploaded_file.id,
)

print(f"File status: {vector_file.status}")

if vector_file.status != "completed":
    raise RuntimeError(
        f"Vector store indexing failed: "
        f"{vector_file.status}"
    )

print()
print("=" * 60)
print("AI BRAIN READY")
print("=" * 60)
print(f"VECTOR_STORE_ID={vector_store.id}")
print(f"FILE_ID={uploaded_file.id}")
print("=" * 60)