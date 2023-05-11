# Installation

```bash
pip3 install -r requirements.txt
```

# Start HTTP Server

```bash
flask --app src/app.py run --debug --port 8000
```

# Run Human Detection with Custom Images

1. Edit the file path inside the `app.py` file. e.g. `/Users/username/Desktop/people.png`

2. Run the following command:
     ```bash
     python3 src/app.py people.png
     ```
