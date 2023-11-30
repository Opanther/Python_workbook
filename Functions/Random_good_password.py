from random_password import generate_pass
from check_a_password import password_checker

def main():
    attempts = 0
    max_attempts = 100  # You can adjust this value based on your needs

    while attempts < max_attempts:
        password = generate_pass()
        attempts += 1

        if password_checker(password):
            print(f"Good password generated in {attempts} attempts: {password}")
            break

    if attempts == max_attempts:
        print(f"Unable to generate a good password after {attempts} attempts.")

if __name__ == "__main__":
    main()

