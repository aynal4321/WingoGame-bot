import requests
import time

# আপনার ডাটা
URL = "https://draw.ar-lottery01.com/WinGo/WinGo_30S/GetHistoryIssuePage.json"
COOKIE = "_cf_bm=YON.Yc2XHaaBjZYh4zS2.B1dUG1BrJX4UqsABy6Kxyw-1778414908.1170332-1.0.1.1-fg6l_dLmkBC0dW6cPNtiTzPpX_bi6e6vpCIOQykovAJthh.GRWebcrlPTXYN6q9aLPQ4jINIuMimKWU.i2EvwFsgShPhYRHEA46BsFJrYPWBYCARA3YJUoYzV1hylp2T"

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Cookie": COOKIE
}

def fetch_data():
    try:
        response = requests.get(f"{URL}?ts={int(time.time()*1000)}", headers=HEADERS)
        if response.status_code == 200:
            data = response.json()
            latest = data['data']['list'][0]
            
            content = f"Period: {latest['issueNumber']} | Num: {latest['number']} | Color: {latest['color']}\n"
            
            with open("history.txt", "a") as f:
                f.write(content)
            print("Saved successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fetch_data()
