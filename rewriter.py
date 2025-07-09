# Rewriter Module
# Uses open-source LLMs via Hugging Face Transformers

from transformers import pipeline

def rewrite_text(text, model_name='mistralai/Mistral-7B-Instruct-v0.2'):
    summarizer = pipeline('summarization', model=model_name)
    summary = summarizer(text, max_length=100, min_length=20, do_sample=False)
    return summary[0]['summary_text']

# Example usage:
# rewritten = rewrite_text('Long transcript text...')
# print(rewritten)
