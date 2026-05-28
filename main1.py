import functions

def main_program():
    print("=== MALAYSIAN TAX INPUT PROGRAM ===")

    while True:
        print("\n--- MAIN MENU ---")
        print("1. Register / Login & Calculate Tax")
        print("2. Display Tax Records")
        print("3. Exit Program")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            print("\n--- User Authentication ---")
            user_id = input("Create / Enter User ID: ")
            ic = input("Enter IC Number (12 digits, e.g., 010203045566): ")
            password = input("Enter Password (Last 4 digits of your IC): ")

            if functions.verify_user(ic, password):
                print("\n[SUCCESS] Authentication successful!")

                try:

                    income = float(input("Enter Annual Income (RM): "))
                    relief = float(input("Enter Total Tax Relief Amount (RM): "))

                    tax_payable = functions.calculate_tax(income, relief)
                    print(f"\n>> Calculated Tax Payable: RM {tax_payable:.2f} <<")

                    user_data = {
                        "User ID": user_id,
                        "IC Number": ic,
                        "Annual Income": income,
                        "Tax Relief": relief,
                        "Tax Payable": tax_payable
                    }

                    functions.save_to_csv(user_data)
                    print("[INFO] Data successfully saved to CSV file.")

                except ValueError:
                    print("[ERROR] Invalid numeric input! Please enter numbers only for income and relief.")
            else:
                print("[FAILED] Authentication failed! Invalid IC length or incorrect password.")

        elif choice == '2':
            print("\n--- Displaying Tax Records From CSV ---")

            df_records = functions.read_from_csv()

            if df_records is not None and not df_records.empty:
                print(df_records.to_string(index=False))
            else:
                print("[INFO] No records found. CSV file is empty or does not exist.")

        elif choice == '3':
            print("\nThank you for using the program. Goodbye!")
            break
        else:
            print("[ALERT] Invalid choice! Please select 1, 2, or 3.")


if __name__ == "__main__":
    main_program()