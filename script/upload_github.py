"""Upload May 30 HTML files to GitHub repo wushanchi/news via REST API."""
import json
import base64
import urllib.request
import urllib.error
import sys
import io
import os

# Fix Windows console encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

TOKEN = os.environ.get("GITHUB_TOKEN", "")
OWNER = "wushanchi"
REPO = "news"
WORKDIR = r"C:\Users\Wu Shanchi\WorkBuddy\2026-05-22-AI news"

FILES = [
    "ai-morning-2026-06-06.html",
    "world-news-2026-06-06.html",
    "tech-news-2026-06-06.html",
    "sports-health-2026-06-06.html",
    "wechat-article-2026-06-06.html",
]

def api_request(method, path, data=None):
    """Make a GitHub API request."""
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{path}"
    headers = {
        "Authorization": f"token {TOKEN}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "WorkBuddy-uploader"
    }
    if data is not None:
        body = json.dumps(data).encode("utf-8")
        headers["Content-Type"] = "application/json"
    else:
        body = None
    
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode()), resp.status
    except urllib.error.HTTPError as e:
        err_body = e.read().decode()
        print(f"  HTTP {e.code}: {err_body}")
        return None, e.code

def upload_file(filename):
    """Upload a single file, handling create vs update."""
    filepath = os.path.join(WORKDIR, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    encoded = base64.b64encode(content.encode("utf-8")).decode("utf-8")
    size_kb = len(content.encode("utf-8")) / 1024
    
    # Check if file already exists
    print(f"\n[FILE] {filename} ({size_kb:.1f} KB)")
    existing, status = api_request("GET", filename)
    
    payload = {
        "message": f"Add {filename} - daily report Jun 6",
        "content": encoded,
        "branch": "master"
    }
    
    if status == 200 and existing:
        # File exists, need sha for update
        payload["sha"] = existing["sha"]
        print(f"  -> Updating existing file (sha: {existing['sha'][:8]}...)")
    else:
        print(f"  -> Creating new file")
    
    result, code = api_request("PUT", filename, payload)
    if result and code in (200, 201):
        print(f"  [OK] Success! {result['commit']['html_url']}")
        return True
    else:
        print(f"  [FAIL] Failed (status {code})")
        return False

def main():
    print("=" * 60)
    print(f"Uploading {len(FILES)} files to {OWNER}/{REPO}")
    print("=" * 60)
    
    success = 0
    for f in FILES:
        if upload_file(f):
            success += 1
    
    print(f"\n{'=' * 60}")
    print(f"Done: {success}/{len(FILES)} files uploaded successfully")
    return 0 if success == len(FILES) else 1

if __name__ == "__main__":
    sys.exit(main())
