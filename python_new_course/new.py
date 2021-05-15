from urllib.parse import urljoin
base = "https://www.youtube.com"
vid_id = "adA_w4w9AWgXAc_A"[1:].replace("A", "").replace("_", "Q")
url = urljoin(base, f"watch?v={vid_id}")
print(url)