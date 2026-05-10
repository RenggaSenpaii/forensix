# FORENSIX

```text
███████╗ ██████╗ ██████╗ ███████╗███╗   ██╗███████╗██╗██╗  ██╗
██╔════╝██╔═══██╗██╔══██╗██╔════╝████╗  ██║██╔════╝██║╚██╗██╔╝
█████╗  ██║   ██║██████╔╝█████╗  ██╔██╗ ██║███████╗██║ ╚███╔╝
██╔══╝  ██║   ██║██╔══██╗██╔══╝  ██║╚██╗██║╚════██║██║ ██╔██╗
██║     ╚██████╔╝██║  ██║███████╗██║ ╚████║███████║██║██╔╝ ██╗
╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝╚═╝  ╚═╝
```

Forensix is a DFIR-focused browser forensic toolkit built with Python.

The framework is designed to parse browser artifacts such as:

- Chrome History
- Downloads
- Login Data
- Browser Activity Timeline

Forensix provides clean terminal output and HTML forensic reports for investigation workflows.

---

# Features

- Chrome History Parser
- Downloads Artifact Parser
- Login Data Parser
- Browser Activity Timeline
- HTML Timeline Report
- Rich Terminal UI
- SQLite Artifact Parsing
- Modular DFIR Structure

---

# Project Structure

```bash
forensix/
│
├── cli.py
├── setup.py
├── requirements.txt
│
├── forensix/
│   ├── core/
│   └── parsers/
│
└── reports/
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/RenggaSenpaii/forensix.git
```

```bash
cd forensix
```

---

## Create Virtual Environment

```bash
python3 -m venv venv
```

---

## Activate Virtual Environment

### Linux

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Browser Artifact Acquisition

## Chrome / Chromium History

```bash
cp ~/.config/chromium/Default/History .
```

---

## Chrome / Chromium Login Data

```bash
cp ~/.config/chromium/Default/"Login Data" .
```

---

# Usage

## Parse Browser History

```bash
PYTHONPATH=. python cli.py chrome History
```

---

## Parse Downloads

```bash
PYTHONPATH=. python cli.py downloads History
```

---

## Parse Login Data

```bash
PYTHONPATH=. python cli.py logins "Login Data"
```

---

## Generate Browser Timeline

```bash
PYTHONPATH=. python cli.py timeline History "Login Data"
```

---

## Generate HTML Timeline Report

```bash
PYTHONPATH=. python cli.py timeline History "Login Data" -o timeline.html
```

---

# Example Output

## Timeline View

```text
[HISTORY] https://github.com

[DOWNLOAD] payload.zip

[LOGIN] https://github.com -> admin@gmail.com
```

---

# HTML Report

Generate forensic investigation reports in HTML format.

```bash
firefox timeline.html
```

---

# Requirements

- Python 3
- Rich
- Typer
- SQLite3

---

# Legal Disclaimer

This tool is intended for:

- Digital Forensics
- DFIR Learning
- Security Research
- Authorized Investigations

The author is not responsible for misuse.

---

# Author

Built for DFIR & Security Research.