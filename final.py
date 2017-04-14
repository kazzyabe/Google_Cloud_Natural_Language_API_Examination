# NEED to install the library
# pip install --upgrade google-cloud-language
from google.cloud import language
from glob import glob

def load_file_names(directory):
    """
    Load files' path with fila names ending with .txt
    """
    path = directory + '/*.txt'
    return glob(path)

def sentiment_text(result, text):
    """
    Detects sentiment in the text.
    Modified code at https://cloud.google.com/natural-language/docs/reference/libraries
    need to install 'Google Cloud SDK' and authenticate by typing the following command:
    gcloud auth application-default login
    """
    language_client = language.Client()

    f = open(text, 'r')
    analizee = f.read()
    f.close()
    # result.write(analizee)
    result.write(text + '\n')
    # Instantiates a plain text document.
    document = language_client.document_from_text(analizee)

    # Detects sentiment in the document. You can also analyze HTML with:
    #   document.doc_type == language.Document.HTML
    sentiment = document.analyze_sentiment().sentiment

    result.write('Score: {}\n'.format(sentiment.score))
    result.write('Magnitude: {}\n'.format(sentiment.magnitude))

# def sentiment_text(text):
#     """Detects sentiment in the text."""
#     language_client = language.Client()

#     # Instantiates a plain text document.
#     document = language_client.document_from_text(text)

#     # Detects sentiment in the document. You can also analyze HTML with:
#     #   document.doc_type == language.Document.HTML
#     sentiment = document.analyze_sentiment().sentiment

#     print('Score: {}'.format(sentiment.score))
#     print('Magnitude: {}'.format(sentiment.magnitude))

def analysis(directory):
    """
    Run sentiment analysis feature of Cloud Natural Language API on files under 'directory'

    Output: print the file name, the document score, and the magnitude for each file in the directory
    """
    lists_of_texts = load_file_names(directory)
    f = open('result.txt', 'w')
    for text in lists_of_texts:
        # result.write(text + '\n')
        sentiment_text(f, text)

