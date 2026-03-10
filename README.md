# timecapsule-chain
send encrypted messages into the future 
# TimeCapsule Chain

![Python](https://img.shields.io/badge/python-3.10-blue)
![Encryption](https://img.shields.io/badge/encryption-AES256-green)
![License](https://img.shields.io/badge/license-MIT-yellow)

TimeCapsule Chain is a secure system that allows users to send encrypted messages or files into the future.

Messages stay encrypted until the specified unlock date.

## Features

- AES-256 encryption
- future unlock timestamps
- encrypted message vault
- automatic unlock daemon
- CLI interface

## Example Use Cases

• digital time capsules  
• delayed messages  
• secure archives  
• future reminders  

## Installation

```bash
git clone https://github.com/Ivanalqadri/timecapsule-chain
cd timecapsule-chain
pip install -r requirements.txt
```

# Create Capsule 
```
python examples/create_capsule.py
```

# Run Unlock Daemon
```
phyton main.py
```

# Security
All messages are encrypted using AES-256 before storage.

No plaintext is stored.

# License
MIT
