import json
import gzip
import pandas as pd

from langchain_core.documents import Document

from langchain_community.document_loaders import (
    PyPDFLoader
)


def load_faq_data():

    docs = []

    with open(
        "data/faq/train.json",
        "r",
        encoding="utf-8"
    ) as f:

        for line in f:

            item = json.loads(line)

            docs.append(
                Document(
                    page_content=f"""
                    Question: {item['question']}
                    Answer: {item['answer']}
                    """,
                    metadata={
                        "source": "faq"
                    }
                )
            )

    return docs


def load_pdf_data():

    loader = PyPDFLoader(
        "data/pdfs/employee_handbook_print_1.pdf"
    )

    return loader.load()


def load_product_data():

    df = pd.read_csv(
        "data/csv/amazon-products.csv"
    )

    df = df.head(1000)

    docs = []

    for _, row in df.iterrows():

        docs.append(
            Document(
                page_content=str(row.to_dict()),
                metadata={
                    "source": "products"
                }
            )
        )

    return docs


def load_support_data():

    df = pd.read_csv(
        "data/csv/Bitext_Sample_Customer_Support_Training_Dataset_27K_responses-v11.csv"
    )

    df = df.head(3000)

    docs = []

    for _, row in df.iterrows():

        docs.append(
            Document(
                page_content=str(row.to_dict()),
                metadata={
                    "source": "support"
                }
            )
        )

    return docs


def load_qa_data():

    docs = []

    with gzip.open(
        "data/qa/amazon-qa.jsonl.gz",
        "rt",
        encoding="utf-8"
    ) as f:

        for i, line in enumerate(f):

            if i >= 2000:
                break

            item = json.loads(line)

            docs.append(
                Document(
                    page_content=str(item),
                    metadata={
                        "source": "amazon_qa"
                    }
                )
            )

    return docs