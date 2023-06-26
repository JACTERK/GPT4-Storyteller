# Install dependencies only if they are not already installed.
if [ ! -d "venv" ]; then
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
fi

# Run the program
python3 start.py
