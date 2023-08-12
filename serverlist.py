import pickle

# serverlist.py - Class for server lists - Stores server objects in a list to allow for persistence.


def new(listname):
    return ServerList(listname)


def load(listname):
    try:
        with open("save/serverlist/" + listname.lower() + ".serverlist", "rb") as f:
            return pickle.load(f)
    except Exception as e:
        print("Error loading serverlist object: " + str(e))
        exit(0)


# Class for server lists - Stores server objects in a list to allow for persistence.
class ServerList:
    def __init__(self, listname):
        self.listname = listname
        self.serverlist = []

    # Getters

    def get_listname(self):
        return self.listname

    def get_serverlist(self):
        return self.serverlist

    def get_server(self, index):
        return self.serverlist[index]

    # Setters

    def set_listname(self, listname):
        self.listname = listname

    def set_serverlist(self, serverlist):
        self.serverlist = serverlist

    def set_server(self, index, server):
        self.serverlist[index] = server

    # Modifiers

    def append_serverlist(self, server):
        try:
            self.serverlist.append(server)
        except Exception as e:
            print("Error appending serverlist: " + str(e))
            exit(0)

    def pop_serverlist(self, index):
        try:
            self.serverlist.pop(index)
        except Exception as e:
            print("Error popping serverlist: " + str(e))
            exit(0)

    # String representation of the object
    def __str__(self):
        return "ServerList object: " + self.get_listname() + " (" + str(len(self.get_serverlist())) + " servers)"

    # Saving object function
    def save(self):
        try:
            with open("save/serverlist/" + self.listname.lower() + ".serverlist", "wb") as f:
                pickle.dump(self, f)
        except Exception as e:
            print("Error saving serverlist object: " + str(e))
            exit(0)
