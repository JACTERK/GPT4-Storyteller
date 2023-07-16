# Class defining a list of users the discord bot will talk to

import ast
import aiLib
import pickle
import settings


# TODO: Add a function to make all users in a discord server each their own user object

class Userlist:
    def __init__(self):
        self.user_list = []

    # Getters and Setters
    def get_user_list(self):
        return self.user_list

    def get_user_list_as_string(self):
        return "[" + ", ".join(str(x) for x in self.user_list) + "]"

    # TODO: Remove before release
    def set_user_list(self, user_list):
        self.user_list = user_list

    # 'user' is a User object
    def add_user(self, user):
        # Check if user is already in the list
        if len(self.user_list) == 0:
            self.user_list.append(user)
            print("User added to list")
        else:
            for u in self.user_list:
                if u == user:
                    print("User already in list")
                else:
                    self.user_list.append(user)
                    print("User added to list")
        return

    def remove_user(self, user):
        try:
            self.user_list.remove(user)
            print("User removed from list")
        except ValueError:
            print("User not in list. No changes made.")

    def check_user(self, user):
        for u in self.user_list:
            if u == user:
                return True
        return False

    # Helper functions
    def load(self):
        try:
            with open('save/userlist.pickle', 'rb') as f:
                self.user_list = pickle.load(f)
        except FileNotFoundError:
            print("No userlist found, creating new userlist...")
            self.save()

    def save(self):
        with open('userlist.pickle', 'wb') as f:
            pickle.dump(self.user_list, f)
