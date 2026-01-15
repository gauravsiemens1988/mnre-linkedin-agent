from flask import Flask, request
import json

app = Flask(__name__)

DRAFT_FILE = "drafts/index.json"

def update_status(draft_id, new_status):
    with open(DRAFT_FILE, "r") as f:
        drafts = json.load(f)

    for d in drafts:
        if d["draft_id"] == draft_id:
            d["status"] = new_status

    with open(DRAFT_FILE, "w") as f:
        json.dump(drafts, f, indent=2)

@app.route("/approve")
def approve():
    draft_id = request.args.get("draft_id")
    update_status(draft_id, "approved")
    return "✅ Draft approved. You can close this tab."

@app.route("/reject")
def reject():
    draft_id = request.args.get("draft_id")
    update_status(draft_id, "rejected")
    return "❌ Draft rejected. You can close this tab."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
