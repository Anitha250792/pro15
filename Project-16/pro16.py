from werkzeug.security import generate_password_hash, check_password_hash

def main():
    # Input password from user
    password = input("Enter your password: ")

    # Generate hash
    hashed_password = generate_password_hash(password)
    print("Generated Hash:", hashed_password)

    # Verification
    password_to_check = input("Re-enter password to verify: ")

    if check_password_hash(hashed_password, password_to_check):
        print("✅ Password verified successfully!")
    else:
        print("❌ Password does not match!")

if __name__ == "__main__":
    main()
