import re

#-------------------------
#password checker function
#-------------------------

def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r"[A-Z]", password))
    number_criteria = bool(re.search(r"\d", password))
    special_char_criteria = bool(re.search(r"[!@#$%^&*()\-=+{}\[\]|;:'\",.<>?/`~]", password))

    strength_score = sum([length_criteria, uppercase_criteria, number_criteria, special_char_criteria])

    #-------------------------
    # Suggestions for improvement
    #-------------------------
    
    suggestions = []
    if not length_criteria:
        suggestions.append("🔹 Increase the password length to at least 8 characters.")
    if not uppercase_criteria:
        suggestions.append("🔹 Add at least one uppercase letter (A-Z).")
    if not number_criteria:
        suggestions.append("🔹 Include at least one number (0-9).")
    if not special_char_criteria:
        suggestions.append("🔹 Use at least one special character (!@#$%^&* etc.).")

    if strength_score == 4:
        return "Strong", "green", 100, ["✅ Great job! Your password is strong."]
    elif strength_score == 3:
        return "Medium", "orange", 70, suggestions
    else:
        return "Weak", "red", 30, suggestions
