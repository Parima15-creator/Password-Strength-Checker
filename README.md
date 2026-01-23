# Password Strength Analyzer
A Python-based password strength analyzer designed to evaluate passwords using real-world security principles. This project demonstrates my interest in cybersecurity, password security best practices, and secure coding principles.

It goes beyond simple rule-checking by combining character variety, common password detection, pattern recognition, and entropy-based scoring to provide actionable feedback to users.

## ✨ Features
- Length-based scoring: Encourages longer passwords (8–16+ characters) for stronger security.

- Character diversity checks: Ensures inclusion of uppercase letters, lowercase letters, digits, and special characters.

- Common password detection: Identifies passwords found in known weak password lists.

- Sequential number detection: Flags numeric sequences like 1234 or 9876.

- Repeated pattern detection: Detects patterns like aaa, abab, or 1212.

- Entropy-based scoring: Measures unpredictability of passwords to reward truly strong, random passwords.

- Positive feedback: Highlights passwords with high entropy to reinforce good security practices.

- User-friendly feedback: Provides actionable suggestions to improve password security.

## 🛡️ How It Works
The analyzer scores a password on multiple aspects:

1. Length and character variety
Longer passwords with a mix of letters, numbers, and special characters are scored higher.

2. Structural weaknesses
Sequential numbers, repeated characters, and repeated substrings reduce the score.

3. Known compromises
Passwords found in common password lists are immediately flagged as high risk.

3. Entropy calculation
Password entropy is calculated in bits to quantify randomness. Higher entropy = stronger password.

After evaluation, the password is classified as:  
-Weak
-Medium
-Strong

Users also receive feedback messages highlighting strengths and weaknesses.

Example Usage
```
Enter your password: Abc123!@

Password Strength: Medium
Password Score: 6 / 12

Feedback:
• Consider using at least 12 characters for stronger security
• Password is highly predictable (low entropy)
```
```
Enter your password: tQ7#Lx!9R2a$

Password Strength: Strong
Password Score: 12 / 12

Feedback:
• Password is highly unpredictable (good randomness)
```
## Why This Project Matters
This project demonstrates:
- Practical understanding of password security principles 
- Ability to implement security rules in Python
- Knowledge of entropy-based analysis and pattern recognition
- Attention to user-friendly security feedback
It serves as a portfolio piece showing my interest and capability in cybersecurity fundamentals.

## Technical Stack
Language: Python 3
Libraries: re (regular expressions), math
Data: Custom common password list for high-risk detection

## Next Steps / Future Enhancements
- Detect alphabetic sequences (e.g., abcd, zyxw)
- Detect keyboard patterns (e.g., qwerty, asdf)
- Add CLI color output or optional web interface
- Provide estimated crack time for user awareness

## 🚀 Installation & Usage
1. Prerequisites
Ensure you have Python 3.x installed on your system.

2. Clone the Repository
```
git clone https://github.com/Parima15-creator/Password-Strength-Checker.git
cd Password-Strength-Checker
```

4. Run the Script
Execute the program from the root directory using the following command:
```
python src/password_checker.py
```

## 📂 Project Structure
A specific folder structure is required for the script to locate the common password database:
Password-Strength-Checker/
```
├── data/
│   └── common_password.txt  # Dictionary of insecure passwords
├── src/
│   └── pasword_checker.py   # Main logic and complexity analysis
├── .gitignore               # Git configuration
├── LICENSE                  # MIT License
└── README.md                # Project documentation
```

## 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.
