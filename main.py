import json
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pywhatkit as kit

# ── Step 1: Load contacts ──────────────────────────────
with open("contacts.json", "r") as f:
    contacts = json.load(f)

print(f"Loaded {len(contacts)} contacts")

# ── Step 2: Setup Chrome ───────────────────────────────
options = Options()
options.add_argument("--start-maximized")
# Remove below line if you want to SEE the browser open
# options.add_argument("--headless")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

screenshots = []

# ── Step 3: Open each URL and take screenshot ──────────
for contact in contacts:
    print(f"\nOpening {contact['url']} for {contact['name']}...")
    
    try:
        driver.get(contact['url'])
        time.sleep(3)  # wait for page to fully load
        
        filename = f"screenshot_{contact['name']}.png"
        driver.save_screenshot(filename)
        print(f"Screenshot saved: {filename}")
        
        screenshots.append({
            "name":    contact['name'],
            "phone":   contact['phone'],
            "caption": contact['caption'],
            "image":   os.path.abspath(filename)  # full path needed
        })
        
    except Exception as e:
        print(f"Failed for {contact['name']}: {e}")

driver.quit()
print("\nAll screenshots taken. Starting WhatsApp sending...")

# ── Step 4: Send via WhatsApp ──────────────────────────
for item in screenshots:
    print(f"\nSending to {item['name']} ({item['phone']})...")
    
    now = time.localtime()
    hour   = now.tm_hour
    minute = now.tm_min + 2  # 2 minutes from now
    
    if minute >= 60:
        minute -= 60
        hour   += 1
    
    try:
        kit.sendwhats_image(
            receiver=item['phone'],
            img_path=item['image'],
            caption=item['caption'],
            wait_time=15,       # seconds to wait before sending
            tab_close=True      # close tab after sending
        )
        print(f"Sent to {item['name']} successfully!")
        time.sleep(20)          # gap between each message
        
    except Exception as e:
        print(f"Failed to send to {item['name']}: {e}")

print("\nDone! All messages sent.")