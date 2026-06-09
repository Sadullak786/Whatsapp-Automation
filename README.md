# WhatsApp Web Screenshot Automation

A Python automation script that captures screenshots of webpages and automatically sends them to WhatsApp contacts with custom captions.

## Features

* Read multiple contacts from a JSON file
* Open websites automatically using Selenium
* Capture webpage screenshots
* Send screenshots via WhatsApp Web
* Custom message caption for each recipient
* Automatic ChromeDriver installation
* Error handling for failed URLs or WhatsApp deliveries

---

## Repository Structure

```text
.
├── main.py
├── contacts.json
├── PyWhatKit_DB.txt
├── screenshot_Ali Reza.png
└── screenshot_Sadulla.png
```

### File Description

| File                      | Purpose                                      |
| ------------------------- | -------------------------------------------- |
| `main.py`                 | Main automation script                       |
| `contacts.json`           | Stores contact details, URLs, and captions   |
| `PyWhatKit_DB.txt`        | Auto-generated log file created by PyWhatKit |
| `screenshot_Ali Reza.png` | Example generated screenshot                 |
| `screenshot_Sadulla.png`  | Example generated screenshot                 |

---

## How It Works

### 1. Load Contacts

The script reads contact information from `contacts.json`.

Example:

```json
[
  {
    "name": "Ali Reza",
    "phone": "+911234567890",
    "url": "https://example.com",
    "caption": "Hello Ali Reza"
  }
]
```

---

### 2. Capture Website Screenshots

For each contact:

* Open the provided URL
* Wait for page loading
* Capture screenshot
* Save screenshot locally

Generated format:

```text
screenshot_<name>.png
```

Example:

```text
screenshot_Ali Reza.png
```

---

### 3. Send Screenshot via WhatsApp

Using PyWhatKit:

* Opens WhatsApp Web
* Attaches screenshot
* Sends custom caption
* Closes tab automatically

---

## Requirements

### Python Version

```text
Python 3.9+
```

### Install Dependencies

```bash
pip install selenium webdriver-manager pywhatkit
```

---

## Usage

### Step 1

Clone the repository:

```bash
git clone <repository-url>
cd <repository-folder>
```

### Step 2

Update `contacts.json` with your recipients.

### Step 3

Run the script:

```bash
python main.py
```

---

## Sample Output

```text
Loaded 2 contacts

Opening https://example.com for Ali Reza...
Screenshot saved: screenshot_Ali Reza.png

Sending to Ali Reza...
Sent successfully!

Done! All messages sent.
```

---

## Notes

* WhatsApp Web must be logged in before running.
* Phone numbers must include country code.
* Stable internet connection is required.
* Screenshots are stored locally before sending.
* Large webpages may require increasing page load wait time.

---

## Generated Files

After execution, screenshots are automatically generated:

```text
screenshot_<contact_name>.png
```

PyWhatKit may also create:

```text
PyWhatKit_DB.txt
```

which stores internal logs used by the library.

---

## Future Improvements

* CSV/Excel contact import
* Headless browser support
* Scheduled sending
* Automatic screenshot cleanup
* Logging system
* Multi-threaded screenshot generation

---

## Disclaimer

This project is intended for educational and automation purposes. Users are responsible for complying with WhatsApp policies and applicable regulations when sending messages.
