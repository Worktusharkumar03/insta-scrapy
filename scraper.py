# Instagram Scraper Module
# Scrapes Instagram by hashtag or location using Instaloader (open-source)

def scrape_instagram_by_hashtag(hashtag, max_posts=10, username=None, password=None, sessionfile=None):
    """Scrape public Instagram posts by hashtag using Instaloader with login support."""
    import instaloader
    L = instaloader.Instaloader()
    # Login if credentials provided
    if sessionfile:
        L.load_session_from_file(username, sessionfile)
    elif username and password:
        L.login(username, password)
    posts = instaloader.Hashtag.from_name(L.context, hashtag).get_posts()
    results = []
    for idx, post in enumerate(posts):
        if idx >= max_posts:
            break
        results.append({
            'url': post.url,
            'shortcode': post.shortcode,
            'caption': post.caption,
            'date_utc': post.date_utc,
            'is_video': post.is_video
        })
    return results

# Example usage:
# posts = scrape_instagram_by_hashtag('nature', max_posts=5)
# print(posts)
