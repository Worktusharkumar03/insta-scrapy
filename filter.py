# Filter Module
# Filters transcripts by keyword or language

from langdetect import detect

def filter_transcript(text, keywords=None, language=None):
    if language and detect(text) != language:
        return False
    if keywords:
        if not any(kw.lower() in text.lower() for kw in keywords):
            return False
    return True

# Example usage:
# filter_transcript('This is a wildlife video', keywords=['wildlife'], language='en')
