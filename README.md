# Password Strength Checker (Entropy-Based)

## Overview
The **Password Strength Checker** is a Python-based security utility that evaluates the robustness of user passwords using **entropy analysis**, **pattern detection**, and **common password validation**.  
It’s designed for anyone learning **cybersecurity**, **ethical hacking**, or **secure coding practices**, offering detailed feedback on password strength and brute-force resistance.

This tool helps users understand how password complexity, length, and randomness affect their overall security posture.


## Features
✅ Detects use of **uppercase, lowercase, digits, and special characters**  
✅ Checks password against a **list of common passwords**  
✅ Ensures **minimum length (8 characters)**  
✅ Calculates **entropy** to measure brute-force resistance  
✅ Provides **detailed strength feedback** (Weak → Very Strong)  
✅ Explains missing components in invalid passwords  
✅ Lightweight and **fully written in Python (no dependencies except math & string)**  


## How It Works
The tool performs multiple validation checks:
1. **Character Diversity Check** – Ensures presence of uppercase, lowercase, digits, and special characters.  
2. **Common Password Detection** – Compares against a `common.txt` wordlist.  
3. **Entropy Calculation** – Uses Shannon entropy formula:  


