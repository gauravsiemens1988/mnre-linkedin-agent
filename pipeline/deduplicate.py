import hashlib

def article_hash(title, link):
    return hashlib.md5(f"{title}{link}".encode()).hexdigest()
