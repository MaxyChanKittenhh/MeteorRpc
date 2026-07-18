from pypresence import Presence
import time

CLIENT_ID = "1525834468756164749"
DISCORD_INVITE = "https://invites.gg/meteorofficial"

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

while True:
    time.sleep(15)
