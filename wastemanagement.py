import datetime

class EDevice:
    def __init__(self, name, category, purchase_date, lifespan_years):
        self.name = name
        self.category = category
        self.purchase_date = purchase_date
        self.lifespan_years = lifespan_years
        self.history = []

    def calculate_age(self, current_date):
        return (current_date - self.purchase_date).days // 365

    def is_due_for_replacement(self, current_date):
        age = self.calculate_age(current_date)
        return age >= self.lifespan_years

    def add_event(self, event):
        self.history.append(event)

    def display_history(self):
        if not self.history:
            print("No history for this device.")
        for event in self.history:
            print(event)

class User:
    def __init__(self, username):
        self.username = username
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)
        print(f"{device.name} has been added for user {self.username}.")

    def list_devices(self):
        if not self.devices:
            print("No devices found.")
        for device in self.devices:
            print(f"{device.name} ({device.category}) - Purchased: {device.purchase_date} - Lifespan: {device.lifespan_years} years")

    def check_replacements(self, current_date):
        print(f"\nDevices due for replacement for user {self.username}:")
        for device in self.devices:
            if device.is_due_for_replacement(current_date):
                print(f"{device.name} ({device.category}) - Purchased on {device.purchase_date} - Consider recycling.")

    def generate_report(self, current_date):
        print(f"\n--- E-waste Report for {self.username} ---")
        total_devices = len(self.devices)
        due_for_replacement = sum(device.is_due_for_replacement(current_date) for device in self.devices)
        sustainability_score = ((total_devices - due_for_replacement) / total_devices) * 100 if total_devices else 0
        print(f"Total devices: {total_devices}")
        print(f"Devices due for replacement: {due_for_replacement}")
        print(f"Sustainability score: {sustainability_score:.2f}%")
        print("----------------------------------")

def main():
    users = {}

    while True:
        print("\n--- Advanced E-waste Monitoring System ---")
        print("1. Create a new user")
        print("2. Login as a user")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            username = input("Enter new username: ")
            if username in users:
                print("Username already exists.")
            else:
                users[username] = User(username)
                print(f"User {username} has been created.")

        elif choice == '2':
            username = input("Enter username: ")
            if username not in users:
                print("User not found.")
            else:
                current_user = users[username]
                while True:
                    print(f"\n--- Welcome {current_user.username} ---")
                    print("1. Add a new electronic device")
                    print("2. List all devices")
                    print("3. Check devices for replacement")
                    print("4. View device history")
                    print("5. Generate e-waste report")
                    print("6. Logout")

                    user_choice = input("Enter your choice (1/2/3/4/5/6): ")

                    if user_choice == '1':
                        name = input("Enter device name: ")
                        category = input("Enter device category: ")
                        purchase_date = datetime.datetime.strptime(input("Enter purchase date (YYYY-MM-DD): "), "%Y-%m-%d")
                        lifespan_years = int(input("Enter expected lifespan (years): "))
                        device = EDevice(name, category, purchase_date, lifespan_years)
                        current_user.add_device(device)

                    elif user_choice == '2':
                        current_user.list_devices()

                    elif user_choice == '3':
                        current_date = datetime.datetime.now()
                        current_user.check_replacements(current_date)

                    elif user_choice == '4':
                        device_name = input("Enter device name to view history: ")
                        found_device = next((d for d in current_user.devices if d.name == device_name), None)
                        if found_device:
                            found_device.display_history()
                        else:
                            print("Device not found.")

                    elif user_choice == '5':
                        current_date = datetime.datetime.now()
                        current_user.generate_report(current_date)

                    elif user_choice == '6':
                        print(f"Logging out {current_user.username}.")
                        break

                    else:
                        print("Invalid choice. Please select 1, 2, 3, 4, 5, or 6.")

        elif choice == '3':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
