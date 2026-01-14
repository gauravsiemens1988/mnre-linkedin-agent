import os
import shutil

PENDING = "drafts/pending/"
APPROVED = "drafts/approved/"
REJECTED = "drafts/rejected/"

def review(draft_id, action):
    src = f"{PENDING}{draft_id}.json"

    if action == "approve":
        shutil.move(src, f"{APPROVED}{draft_id}.json")
    elif action == "reject":
        shutil.move(src, f"{REJECTED}{draft_id}.json")
