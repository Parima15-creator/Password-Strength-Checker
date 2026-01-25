import re
import os
import math

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
COMMON_PASSWORDS_PATH = os.path.join(BASE_DIR, "data", "common_password.txt")

#Password length based score
def length_score(password):
    if len(password) >= 16:
        return 4
    elif len(password) >= 12:
        return 3
    elif len(password) >= 8:
        return 1
    return 0

#Checks for Upper Case
def has_uppercase(password):
    return bool(re.search(r"[A-Z]", password))

#Checks for Lower Case
def has_lowercase(password):
    return bool(re.search(r"[a-z]", password))

#Checks for Digits
def has_digit(password):
    return bool(re.search(r"[0-9]", password))

#Checks for special characters
def has_special_char(password):
    return bool(re.search(r"[!@#$%^&*()?_\-+=]", password))

#Loads the commmon paswords file
def load_common_passwords(filename):
    try:
        with open(filename, "r") as file:
            return [line.strip().lower() for line in file]
    except FileNotFoundError:
        return []

#Checks if password is there in common password list
def is_common_password(password, common_passwords):
    pwd = password.lower()
    return any(common in pwd for common in common_passwords)

#Checks for sequential numbers
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

#Checks for repeated patterns
def has_repeated_patterns(password, min_pattern_length=2):
    n = len(password)

    # Detect simple repeats like aaa, 111
    if re.search(r"(.)\1{2,}", password):
        return True

    # Detect repeated substrings like abab, 1212
    for size in range(min_pattern_length, n // 2 + 1):
        for i in range(n - 2 * size + 1):
            if password[i:i + size] == password[i + size:i + 2 * size]:
                return True

    return False

#Calculates randomness of a password
def calculate_entropy(password):
    pool = 0

    if has_lowercase(password):
        pool += 26
    if has_uppercase(password):
        pool += 26
    if has_digit(password):
        pool += 10
    if has_special_char(password):
        pool += 32

    if pool == 0:
        return 0

    return len(password) * math.log2(pool)

#Calculates Score
def calculate_strength(password, common_passwords):
    score = 0
    feedback = []

    if is_common_password(password, common_passwords):
        feedback.append("Password found in common password list (high risk)")
    
    length_points = length_score(password)
    score += length_points

    if length_points < 3:
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

    if has_sequential_numbers(password):
        score -= 2
        feedback.append("Contains sequential numbers (e.g. 1234, 9876)")

    if has_repeated_patterns(password):
        score -= 2
        feedback.append("Contains repeated patterns (e.g. aaa, abab, 1212)")

    entropy = calculate_entropy(password)

    if entropy < 35:
        feedback.append("Password is highly predictable (low entropy)")
    elif entropy < 60:
        score += 1
    else:
        score += 3
        feedback.append("Password is highly unpredictable (good randomness)")

    score = max(score, 0)
    return score, feedback

#Classify strength based on score
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