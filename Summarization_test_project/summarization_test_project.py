
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from abc import ABC, abstractmethod
from heapq import nlargest

stop_words = list(STOP_WORDS)

nlp = spacy.load('en_core_web_sm')

text = "There are broadly two types of extractive summarization tasks depending on what the summarization program focuses on. The first is generic summarization, which focuses on obtaining a generic summary or abstract of the collection (whether documents, or sets of images, or videos, news stories etc.). The second is query relevant summarization, sometimes called query-based summarization, which summarizes objects specific to a query. Summarization systems are able to create both query relevant text summaries and generic machine-generated summaries depending on what the user needs. An example of a summarization problem is document summarization, which attempts to automatically produce an abstract from a given document. Sometimes one might be interested in generating a summary from a single source document, while others can use multiple source documents (for example, a cluster of articles on the same topic). This problem is called multi-document summarization. A related application is summarizing news articles. Imagine a system, which automatically pulls together news articles on a given topic (from the web), and concisely represents the latest news as a summary. Image collection summarization is another application example of automatic summarization. It consists in selecting a representative set of images from a larger set of images. A summary in this context is useful to show the most representative images of results in an image collection exploration system. Video summarization is a related domain, where the system automatically creates a trailer of a long video. This also has applications in consumer or personal videos, where one might want to skip the boring or repetitive actions. Similarly, in surveillance videos, one would want to extract important and suspicious activity, while ignoring all the boring and redundant frames captured."

doc = nlp(text)


class Abs_Class(ABC):

    def __init__(self, doc):
        self.doc = doc
        self.word_frequencies = {}
        self.max_frequency = 0
        self.sentence_tokens = []
        self.sentence_scores = {}
        select_length = 0

from Tokenizer import tokenization

t_s = Tokenizer(doc)
print(t_s.tokenization())

