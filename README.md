Password Strength Checker
A robust Python script designed to help users create stronger, more secure passwords. This tool evaluates passwords based on several security criteria and provides actionable feedback to the user.

✨ Features
Complexity Analysis: Checks for uppercase, lowercase, numbers, and special characters.

Length Verification: Scores passwords based on minimum and ideal length requirements.

Common Password Detection: Compares input against a dictionary of frequently used (and therefore insecure) passwords.

Instant Feedback: Provides a clear strength rating (Weak, Medium, or Strong) and lists specific missing requirements.

🚀 Installation & Usage
1. Prerequisites
Ensure you have Python 3.x installed on your system.

2. Clone the Repository
git clone https://github.com/Parima15-creator/Password-Strength-Checker.git
cd Password-Strength-Checker

3. Run the Script
Execute the program from the root directory using the following command:
python src/password_checker.py

📂 Project Structure
A specific folder structure is required for the script to locate the common password database:
Password-Strength-Checker/
├── data/
│   └── common_password.txt  # Dictionary of insecure passwords
├── src/
│   └── pasword_checker.py   # Main logic and complexity analysis
├── LICENSE                  # MIT License
└── README.md                # Project documentation


🛡️ How It Works
The script calculates a security score by checking for:

Length: Points are awarded for 8+ or 12+ characters.

Character Variety: Bonus points are awarded for mixing character types using Regular Expressions.

Risk Assessment: The script immediately flags any password found in the common_password.txt list to prevent dictionary attacks.

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.
