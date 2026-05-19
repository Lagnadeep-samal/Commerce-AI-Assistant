from tqdm import tqdm

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_huggingface import (
    HuggingFaceEmbeddings
)

from langchain_community.vectorstores import FAISS

from src.loaders import (
    load_faq_data,
    load_pdf_data,
    load_product_data,
    load_support_data,
    load_qa_data
)

faq_docs = load_faq_data()
pdf_docs = load_pdf_data()
products_docs = load_product_data()
support_docs = load_support_data()
qa_docs = load_qa_data()

all_docs = (
    faq_docs
    + pdf_docs
    + products_docs
    + support_docs
    + qa_docs
)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)

split_docs = splitter.split_documents(all_docs)

embedding = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

batch_size = 100

for i in tqdm(
    range(0, len(split_docs), batch_size)
):

    batch = split_docs[i:i+batch_size]

    if i == 0:

        db = FAISS.from_documents(
            batch,
            embedding
        )

    else:

        db.add_documents(batch)


db.save_local("vectordb")

print("Vector DB Created")