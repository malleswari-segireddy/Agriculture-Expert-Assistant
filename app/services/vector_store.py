import faiss
import pickle


def save_faiss_index(index, file_path):
    faiss.write_index(index, file_path)


def load_faiss_index(file_path):
    return faiss.read_index(file_path)
