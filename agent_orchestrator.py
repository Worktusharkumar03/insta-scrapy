# Agent Orchestrator Module
# Coordinates flow using LangChain agents/tools (open-source)

# Placeholder for LangChain-based orchestration logic
# This will connect scraper, downloader, transcriber, filter, rewriter, and exporter

def run_pipeline(config):
    from scraper import scrape_instagram_by_hashtag
    from downloader import download_video
    from transcriber import transcribe_audio
    from filter import filter_transcript
    from rewriter import rewrite_text
    from doc_exporter import save_to_docx
    import os

    hashtags = config.get('hashtags', [])
    max_posts = config.get('max_posts', 5)
    keywords = config.get('keywords', [])
    language = config.get('language', None)
    rewrite_mode = config.get('rewrite_mode', 'summarize')
    llm_model = config.get('llm_model', 'mistralai/Mistral-7B-Instruct-v0.2')
    output_dir = 'outputs'
    os.makedirs(output_dir, exist_ok=True)

    instagram_username = config.get('instagram_username')
    instagram_password = config.get('instagram_password')
    instagram_sessionfile = config.get('instagram_sessionfile')

    for hashtag in hashtags:
        print(f"Scraping posts for #{hashtag}...")
        posts = scrape_instagram_by_hashtag(
            hashtag,
            max_posts=max_posts,
            username=instagram_username,
            password=instagram_password,
            sessionfile=instagram_sessionfile
        )
        for post in posts:
            if not post['is_video']:
                continue
            print(f"Downloading video: {post['url']}")
            video_path = download_video(post['url'])
            print(f"Transcribing video: {video_path}")
            transcript = transcribe_audio(video_path)
            if not filter_transcript(transcript, keywords=keywords, language=language):
                print("Transcript did not pass filter. Skipping.")
                continue
            print("Rewriting transcript...")
            rewritten = rewrite_text(transcript, model_name=llm_model)
            metadata = {
                'url': post['url'],
                'shortcode': post['shortcode'],
                'caption': post['caption'],
                'date_utc': str(post['date_utc'])
            }
            output_path = os.path.join(output_dir, f"{post['shortcode']}.docx")
            print(f"Saving results to {output_path}")
            save_to_docx(metadata, transcript, rewritten, output_path)
    print("Pipeline complete.")

# To be implemented with LangChain workflows
