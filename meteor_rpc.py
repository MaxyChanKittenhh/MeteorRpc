from pypresence import Presence
from flask import Flask
import threading
import time

# ═══════════════════════════════════════
# YOUR CONFIG
# ═══════════════════════════════════════
CLIENT_ID = "1525834468756164749"
DISCORD_INVITE = "https://invites.gg/meteorofficial"

# Flask web server (keeps Render awake)
app = Flask('')

@app.route('/')
def home():
    return "✅ Meteor RPC is running!"

def run_web():
    app.run(host='0.0.0.0', port=10000)

# Start web server in background
threading.Thread(target=run_web, daemon=True).start()

# Connect to Discord
RPC = Presence(CLIENT_ID)
RPC.connect()

print("✅ Rich Presence active!")

RPC.update(
    state="Moderating",
    details="Assistant Of Meteor",
    start=time.time(),
    large_image="largebanner",
    large_text="Meteor",
    small_image="none",
    small_text="Rogue - Level 100",
    party_id="ae488379-351d-4a4f-ad32-2b9b01c9",
    party_size=[1, 1],
    buttons=[{"label": "Ask to Join", "url": DISCORD_INVITE}]
)

# Keep alive forever
while True:
    time.sleep(15)
