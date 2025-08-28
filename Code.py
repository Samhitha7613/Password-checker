import requests
import hashlib
import re

def check_strength(password):
    strength = 0
    suggestions = []

    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    else:
        suggestions.append("Increase password length to at least 8 characters")

  
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        suggestions.append("Add at least one uppercase letter")

    if re.search(r'[a-z]', password):
        strength += 1
    else:
        suggestions.append("Add at least one lowercase letter")


    if re.search(r'\d', password):
        strength += 1
    else:
        suggestions.append("Add at least one number")
      
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        suggestions.append("Add at least one special character (!@#$...)")

    common_words = ["password", "123456", "qwerty", "letmein"]
    if any(word in password.lower() for word in common_words):
        suggestions.append("Avoid common passwords like 'password', '123456', etc.")

    return strength, suggestions

def check_pwned(password):
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error accessing HaveIBeenPwned API")
        return False

    hashes = (line.split(':') for line in response.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return int(count)
    return 0

def main():
    password = input("Enter your password: ")

    strength, suggestions = check_strength(password)
    pwned_count = check_pwned(password)

    print("\n--- Password Analysis ---")
    print(f"Strength score: {strength}/6")
    
    if suggestions:
        print("Suggestions to improve:")
        for s in suggestions:
            print(f"- {s}")
    else:
        print("Your password is strong!")

    if pwned_count:
        print(f"⚠️ This password has appeared in {pwned_count} data breaches! Consider changing it.")
    else:
        print("Good news! This password has not been found in known breaches.")

if __name__ == "__main__":
    main()
