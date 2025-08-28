import ollama
import numpy as np
import faiss
import hidden_key as hk

EMBEDDING_MODEL = hk.EMBEDDING_MODEL
FAISS_INDEX = hk.FAISS_INDEX


def update_today_index(log_texts, tday_faiss="index_today.faiss"):
    embeddings = EMBEDDING_MODEL.encode(log_texts)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    faiss.write_index(index, tday_faiss)


def update_index(new_logs):
    vectors = EMBEDDING_MODEL.encode(new_logs)
    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(np.array(vectors))
    faiss.write_index(index, FAISS_INDEX)


def summarize_logs(log_texts, model="llama3"):
    prompt = f"以下のログを日本語で要約してください:\n{log_texts}"
    response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]


def log_data(logs):
    return [log["text"] for log in logs]


def summarize_recent(model="llama3"):
    index = faiss.read_index("index_latest.faiss")
    query = EMBEDDING_MODEL.encode(["最近のログを要約してください"])
    D, I = index.search(np.array(query, dtype="float32"), k=20)
    relevant_logs = [log_data[i] for i in I[0]]
    prompt = "以下のログを日本語で要約してください:\n" + "\n".join(relevant_logs)
    response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]
