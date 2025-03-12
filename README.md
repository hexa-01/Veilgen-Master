Veilgen is a powerful, open-source tool for generating fake data, designed for testing, development, and privacy protection.


---

Key Features

Generate various types of fake data:

Passwords

Email addresses

Usernames

Phone numbers

IP addresses

Credit card numbers

IMEI numbers

Complete fake identities (name, address, email, phone, etc.)

GPS coordinates

MAC addresses

Birthdates

National IDs (SSN)

Residential addresses

User agents


Encrypt generated data using Fernet encryption.

Decrypt and view encrypted data when needed.

Interactive interface using Rich for better user experience.

---

Technologies Used

Python 3.7+

Faker for generating accurate fake data

Cryptography for data encryption

Rich for an interactive command-line interface



---

Supported Environments

Works on Windows, Linux, and macOS

Lightweight and runs smoothly on any system with Python installed



---

Installation & Usage Guide

1. Install Dependencies

Manually install the required libraries:

pip install rich cryptography faker

2. Run the Tool

Once installed, run the tool using:

python veilgen.py

---

How It Works

When you run Veilgen, an interactive menu will appear, allowing you to choose the type of data to generate:

┌──────────────────────────────────────┐
│            Choose an Option          │
├───────┬──────────────────────────────┤
│  1    │ Generate Passwords            │
│  2    │ Generate Emails               │
│  3    │ Generate Usernames            │
│  4    │ Generate Aliases              │
│  5    │ Generate Phone Numbers        │
│  6    │ Generate IPs                  │
│  7    │ Generate Credit Cards         │
│  8    │ Generate IMEI Numbers         │
│  9    │ Generate Fake Identity        │
│ 10    │ Generate User Agents          │
│ 11    │ Generate GPS Coordinates      │
│ 12    │ Generate MAC Addresses        │
│ 13    │ Generate Birthdates           │
│ 14    │ Generate National ID (SSN)    │
│ 15    │ Generate Addresses            │
│ 99    │ Decrypt and Show Data         │
│  0    │ Exit                          │
└───────┴──────────────────────────────┘

Enter a number to choose an option.

Specify how many records you want to generate.

Data is automatically encrypted and saved as a .enc file.

Use option 99 to decrypt and view saved data.

---

Sample Output

Password Generation

[
    "X7y$!Tg9kLm#",
    "aB3@pQ#2fVw!",
    "Z9!yTr4&Uv@5"
]

Email Generation

[
    "user12345@gmail.com",
    "john_doe78@protonmail.com",
    "random_user99@outlook.com"
]

Fake Identity Generation

{
    "Full Name": "John Doe",
    "Address": "1234 Elm Street, Springfield, USA",
    "Email": "john.doe42@gmail.com",
    "Phone Number": "+1-555-987-6543",
    "Birthdate": "1987-04-23",
    "IP Address": "192.168.1.100",
    "Credit Card": "4539-1234-5678-9012",
    "IMEI": "356938035643809"
}

---

Decrypt and View Saved Data

If you previously saved encrypted data, you can decrypt it using option 99.
It will display a list of available encrypted files:

Available encrypted files:
1. data_2_10.enc
2. data_9_5.enc
3. data_7_3.enc

Select a file, and the decrypted data will be displayed in a structured format.


---

Contribute

Veilgen is open-source, and contributions are welcome. Feel free to submit issues, suggestions, or improvements.


---

Contact

Email: veilgen@proton.me

Telegram: https://t.me/VeilgenS


---

Veilgen – Powerful Fake Data Generation.

