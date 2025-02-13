import os
import ctypes
import subprocess

class NanoTracker:
    def __init__(self):
        self.user_accounts = self._get_user_accounts()

    def _get_user_accounts(self):
        try:
            output = subprocess.check_output('net user', shell=True, text=True)
            users = output.splitlines()[4:-2]
            return [user.strip() for user in users]
        except subprocess.CalledProcessError as e:
            print(f"Error fetching user accounts: {e}")
            return []

    def switch_user(self, username):
        if username in self.user_accounts:
            try:
                ctypes.windll.user32.LockWorkStation()
                os.system(f"runas /user:{username} cmd.exe")
                print(f"Switched to user: {username}")
            except Exception as e:
                print(f"Error switching user: {e}")
        else:
            print(f"User {username} not found.")

    def display_users(self):
        if self.user_accounts:
            print("Available user accounts:")
            for user in self.user_accounts:
                print(f"- {user}")
        else:
            print("No user accounts found.")

if __name__ == "__main__":
    nano_tracker = NanoTracker()
    nano_tracker.display_users()

    username = input("Enter the username to switch to: ")
    nano_tracker.switch_user(username)