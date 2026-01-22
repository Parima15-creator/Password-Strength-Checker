Password Strength Checker
A robust Python script designed to help users create stronger, more secure passwords. This tool evaluates passwords based on several security criteria and provides actionable feedback to the user.

✨ Features
Complexity Analysis: Checks for uppercase, lowercase, numbers, and special characters.

Length Verification: Scores passwords based on minimum and ideal length requirements.

Common Password Detection: Compares input against a dictionary of frequently used (and therefore insecure) passwords.

Instant Feedback: Provides a clear strength rating (Weak, Medium, or Strong) and lists specific missing requirements.

🚀 How It Works
The script calculates a security score by checking for:

Length: Points for 8+ or 12+ characters.

Character Variety: Bonus points for mixing types.

Risk Assessment: Immediately fails any password found in the common_passwords.txt list.
