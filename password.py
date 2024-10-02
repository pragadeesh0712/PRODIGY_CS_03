#prodigy infotech cs task 03 
import re

def assess_password_strength(password):
   
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[\W_]', password) is not None  
    
   
    strength_score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

  
    if strength_score == 5:
        return "Strong", strength_score
    elif strength_score == 4:
        return "Moderate", strength_score
    elif strength_score == 3:
        return "Fair", strength_score
    else:
        return "Weak", strength_score


def provide_feedback(password):
    strength, score = assess_password_strength(password)

    print(f"Password Strength: {strength}")
    if score < 5:
        print("Suggestions to improve your password strength:")
        if len(password) < 8:
            print("- Make sure your password is at least 8 characters long.")
        if not re.search(r'[A-Z]', password):
            print("- Add some uppercase letters.")
        if not re.search(r'[a-z]', password):
            print("- Add some lowercase letters.")
        if not re.search(r'[0-9]', password):
            print("- Include at least one number.")
        if not re.search(r'[\W_]', password):
            print("- Add at least one special character (e.g., !@#$%^&*).")
    else:
        print("Your password is strong!")

password = input("Enter a password to assess: ")
provide_feedback(password)
