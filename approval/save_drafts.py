import json
import uuid
from datetime import datetime

def save_drafts(drafts):
    for d in drafts:
        filename = f"drafts/pending/{datetime.now().date()}_{uuid.uuid4().hex}.json"
        with open(filename, "w") as f:
            json.dump(d, f, indent=2)
