from datetime import datetime


def current_time():

    return str(datetime.now())


def format_docs(docs):

    return "\n\n".join(
        [doc.page_content for doc in docs]
    )


def clean_text(text):

    return text.strip()


def print_separator():

    print("=" * 50)