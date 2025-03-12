import os
import random
import string
import json
from rich.console import Console
from rich.progress import track
from rich.table import Table
from cryptography.fernet import Fernet
from faker import Faker

console = Console()
fake = Faker()

# جعل المسارات مرنة لدعم التشغيل من أي مكان
base_dir = os.getcwd()
key_file_path = os.path.join(base_dir, "secret.key")

# توليد مفتاح التشفير أو قراءته إذا كان موجودًا
if not os.path.exists(key_file_path):
    key = Fernet.generate_key()
    with open(key_file_path, "wb") as key_file:
        key_file.write(key)
else:
    with open(key_file_path, "rb") as key_file:
        key = key_file.read()

cipher = Fernet(key)

# توليد بيانات عشوائية
def random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_passwords(count):
    return ["".join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=12)) for _ in range(count)]

def generate_emails(count):
    domains = ["gmail.com", "protonmail.com", "outlook.com", "yahoo.com", "icloud.com"]
    return [f"{fake.user_name()}{random.randint(10, 99)}@{random.choice(domains)}" for _ in range(count)]

def generate_usernames(count):
    return [fake.user_name() for _ in range(count)]

def generate_aliases(count):
    return [fake.name() for _ in range(count)]

def generate_phone_numbers(count):
    return [fake.phone_number() for _ in range(count)]

def generate_ips(count):
    return [fake.ipv4() for _ in range(count)]

def generate_credit_cards(count):
    return [fake.credit_card_number() for _ in range(count)]

def generate_imei(count):
    return [str(fake.random_number(digits=15, fix_len=True)) for _ in range(count)]

def generate_fake_identity(count):
    return [
        {
            "Full Name": fake.name(),
            "Address": fake.address(),
            "Email": f"{fake.user_name()}{random.randint(10, 99)}@{random.choice(['gmail.com', 'protonmail.com', 'outlook.com'])}",
            "Phone Number": fake.phone_number(),
            "Birthdate": fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d'),
            "IP Address": fake.ipv4(),
            "Credit Card": fake.credit_card_number(),
            "IMEI": str(fake.random_number(digits=15, fix_len=True))
        }
        for _ in track(range(count), description="Generating Fake Identities...")
    ]

def generate_user_agents(count):
    return [fake.user_agent() for _ in range(count)]

def generate_gps_coordinates(count):
    return [f"{fake.latitude()}, {fake.longitude()}" for _ in range(count)]

def generate_mac_addresses(count):
    return [fake.mac_address() for _ in range(count)]

def generate_birthdates(count):
    return [fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d') for _ in range(count)]

def generate_national_ids(count):
    return [fake.ssn() for _ in range(count)]

def generate_addresses(count):
    return [fake.address() for _ in range(count)]

def encrypt_and_save(filename, data):
    encrypted_data = cipher.encrypt(json.dumps(data).encode())
    file_path = os.path.join(base_dir, filename)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)
    console.print(f"[green]Data encrypted and saved to {file_path}[/green]")

def decrypt_and_show():
    enc_files = [f for f in os.listdir(base_dir) if f.endswith(".enc")]

    if not enc_files:
        console.print("[red]No encrypted files found![/red]")
        return

    console.print("\n[bold yellow]Available encrypted files:[/bold yellow]")
    for idx, file in enumerate(enc_files, start=1):
        console.print(f"{idx}. {file}")

    choice = console.input("[bold cyan]Enter file number to decrypt: [/bold cyan]").strip()
    if not choice.isdigit() or int(choice) not in range(1, len(enc_files) + 1):
        console.print("[red]Invalid choice![/red]")
        return

    filename = enc_files[int(choice) - 1]
    file_path = os.path.join(base_dir, filename)

    with open(file_path, "rb") as file:
        encrypted_data = file.read()

    try:
        decrypted_data = cipher.decrypt(encrypted_data).decode()
        console.print(json.dumps(json.loads(decrypted_data), indent=4), style="bold green")
    except Exception as e:
        console.print(f"[red]Failed to decrypt '{filename}': {e}[/red]")

def process_and_save(choice, count):
    data_generators = {
        "1": generate_passwords,
        "2": generate_emails,
        "3": generate_usernames,
        "4": generate_aliases,
        "5": generate_phone_numbers,
        "6": generate_ips,
        "7": generate_credit_cards,
        "8": generate_imei,
        "9": generate_fake_identity,
        "10": generate_user_agents,
        "11": generate_gps_coordinates,
        "12": generate_mac_addresses,
        "13": generate_birthdates,
        "14": generate_national_ids,
        "15": generate_addresses
    }

    if choice == "99":
        decrypt_and_show()
        return

    if choice not in data_generators:
        console.print("[red]Invalid choice![/red]")
        return

    try:
        data = data_generators[choice](count)
    except Exception as e:
        console.print(f"[red]Error generating data: {e}[/red]")
        return

    console.print(json.dumps(data, indent=4))

    filename = f"data_{choice}_{count}.enc"
    encrypt_and_save(filename, data)
    console.print(f"[green]Data saved as {filename}[/green]")

def main():
    os.system("cls" if os.name == "nt" else "clear")  # تنظيف الشاشة عند كل تشغيل

    table = Table(title="Choose an Option")
    options = [
        ("1", "Generate Passwords"),
        ("2", "Generate Emails"),
        ("3", "Generate Usernames"),
        ("4", "Generate Aliases"),
        ("5", "Generate Phone Numbers"),
        ("6", "Generate IPs"),
        ("7", "Generate Credit Cards"),
        ("8", "Generate IMEI Numbers"),
        ("9", "Generate Fake Identity"),
        ("10", "Generate User Agents"),
        ("11", "Generate GPS Coordinates"),
        ("12", "Generate MAC Addresses"),
        ("13", "Generate Birthdates"),
        ("14", "Generate National ID (SSN)"),
        ("15", "Generate Addresses"),
        ("99", "[bold yellow]Decrypt and Show Data[/bold yellow]"),
        ("0", "[bold red]Exit[/bold red]")
    ]
    
    for opt, desc in options:
        table.add_row(opt, desc)

    console.print(table)
    
    choice = console.input("[bold blue]Enter your choice: [/bold blue]").strip()
    if choice == "0":
        console.print("\n[bold green]Thank you for using our tool! Goodbye! 👋[/bold green]")
        return
    
    try:
        count = int(console.input("[bold yellow]Enter count (default=10): [/bold yellow]") or 10)
    except ValueError:
        console.print("[red]Invalid number! Using default value (10).[/red]")
        count = 10

    process_and_save(choice, count)

if __name__ == "__main__":
    main()