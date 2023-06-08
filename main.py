import requests, pwinput

def login(email, password):
    json = {
        "login": email,
        "password": password,
        "undelete": False,
        "captcha_key": None,
        "login_source": None,
        "gift_code_sku_id": None
    }

    headers = {
        "Content-Type": "application/json",
    }

    print("Logging in...")
    r = requests.post("https://discord.com/api/v9/auth/login", json=json, headers=headers)
    if r.status_code == 200:
        print(f"Your Discord token: {r.json()['token']}")
        return
    
    if "captcha" in r.text:
        print("Captcha detected")
        return
    
    print("Invalid login details/2FA enabled")

print("Get your Discord token simply via email & password!")

email = input("Email: ")
password = pwinput.pwinput("Password: ", "*")
login(email, password)
