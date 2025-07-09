# Downloader Module
# Downloads videos from Instagram post URLs

import os
import requests

def download_video(url, output_dir='downloads'):
    os.makedirs(output_dir, exist_ok=True)
    local_filename = os.path.join(output_dir, url.split('/')[-1].split('?')[0])
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename

# Example usage:
# download_video('https://instagram.com/path/to/video.mp4')
