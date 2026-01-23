import re
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
COMMON_PASSWORDS_PATH = os.path.join(BASE_DIR, "data", "common_passwords.txt")

def length_score(password):
    if len(password) >= 16:
        return 4
    elif len(password) >= 12:
        return 3
    elif len(password) >= 8:
        return 1
    return 0


def has_uppercase(password):
    return bool(re.search(r"[A-Z]", password))


def has_lowercase(password):
    return bool(re.search(r"[a-z]", password))


def has_digit(password):
    return bool(re.search(r"[0-9]", password))


def has_special_char(password):
    return bool(re.search(r"[!@#$%^&*()?_\-+=]", password))


def load_common_passwords(filename):
    try:
        with open(filename, "r") as file:
            return [line.strip().lower() for line in file]
    except FileNotFoundError:
        return []


def is_common_password(password, common_passwords):
    return password.lower() in common_passwords


def has_sequential_numbers(password):
    digits = [int(ch) for ch in password if ch.isdigit()]

    if len(digits) < 4:
        return False

    for i in range(len(digits) - 3):
        seq = digits[i:i+4]

        if all(seq[j] + 1 == seq[j + 1] for j in range(3)):
            return True

        if all(seq[j] - 1 == seq[j + 1] for j in range(3)):
            return True

    return False


def calculate_strength(password, common_passwords):
    score = 0
    feedback = []

    score += length_score(password)
    if length_score(password) < 3:
        feedback.append("Consider using at least 12 characters for stronger security")


    if len(password) < 8:
        feedback.append("Password is too short (minimum 8 characters)")

    if has_uppercase(password):
        score += 1
    else:
        feedback.append("Missing uppercase letter")

    if has_lowercase(password):
        score += 1
    else:
        feedback.append("Missing lowercase letter")

    if has_digit(password):
        score += 1
    else:
        feedback.append("Missing number")

    if has_special_char(password):
        score += 2
    else:
        feedback.append("Missing special character (! @ # $ % ^ & * ? _ - + =)")

    if is_common_password(password, common_passwords):
        score = 0
        feedback.append("Password found in common password list (high risk)")

    if has_sequential_numbers(password):
        score -= 2
        feedback.append("Contains sequential numbers (e.g. 1234, 9876)")

    score = max(score, 0)
    return score, feedback


def classify_strength(score):
    if score <= 3:
        return "Weak"
    elif score <= 7:
        return "Medium"
    else:
        return "Strong"


def main():
    common_passwords = load_common_passwords(COMMON_PASSWORDS_PATH)

    password = input("Enter your password: ")

    score, feedback = calculate_strength(password, common_passwords)
    strength = classify_strength(score)

    print("\nPassword Strength:", strength)
    print("Password Score:", score, "/ 12")

    if feedback:
        print("\nFeedback:")
        for issue in feedback:
            print("•", issue)


if __name__ == "__main__":
    main()

