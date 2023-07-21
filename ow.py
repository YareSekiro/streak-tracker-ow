import json

class Streak:
    def __init__(self) -> None:
        self.stats = {
            "dps": {"win": 0, "loose": 0},
            "heal": {"win": 0, "loose": 0},
            "tank": {"win": 0, "loose": 0}
        }

    
    def update(self, role,  type):
        self.stats[role][type] += 1
        if self.stats[role][type] == 7 and type == 'win':
            self.reset(role)
            print("Role reset")

    def reset(self, role):
        self.stats[role] = {"win": 0, "loose": 0}
    
    def save(self):
        with open("data.json", "w") as data:
            json.dump(self.stats, data)
    
    def load(self):
        with open("data.json", "r") as data:
            self.stats = json.load(data)
    
    def show(self):
        print("")
        print("============= [CURRENT] ===============")
        for key, value in self.stats.items():
            print("%s -> WIN | %s - LOOSE | %s" % (key.upper(), value["win"], value["loose"]))
        print("=======================================")
        print("")
    
    def ask(self):
        response = input("Saisissez le role ainsi que le type a augmenté (ex: dps win / dps loose) : ")
        filter = response.split(" ")
        if filter[0] in self.stats.keys():
            if filter[1] in self.stats[filter[0]].keys():
                self.stats[filter[0]][filter[1]] += 1
            else:
                if filter[1] == "reset":
                    self.reset(filter[0])
        else:
            if filter[0] == "save":
                self.save()
        
        self.show()
        self.save()
        self.ask()

S = Streak()

if __name__ == "__main__":
    S.load()
    S.show()
    S.ask()
