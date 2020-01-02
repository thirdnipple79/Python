from random import randint
from random import sample


class Player:
    def __init__(self, name):
        self.name = name
        self.cash = 2000
        self.debt = 2000
        self.health = 100
        self.days_remaining = 30
        self.location = Location()
        self.inventory = []

    def travel(self):
        self.choice = input("""
        Where to?
        1) Downtown     4) North York
        2) Etobicoke    5) Mississauga
        3) Scarborough  6) Brampton
        : """)
        location.loc = location.cities[int(self.choice) - 1]
        self.drugs.populate_drug_list()

    def __str__(self):
        player_status = '''
            Player: {}
        Cash = {}       Health = {}         Current Location = {}
        Debt = {}       Days Remaining = {}'''.format(self.name, self.cash, self.health, self.location.loc, self.debt,
                                                      self.days_remaining)
        return player_status


class Location:
    def __init__(self):
        self.cities = ("Downtown", "Etobicoke", "Scarborough", "North York", "Mississauga", "Brampton")
        self.loc = self.cities[0]
        self.drugs = Drugs()
        self.drugs_here = self.drugs.drugs_available

    # def travel(self):
    #     self.choice = input("""
    #     Where to?
    #     1) Downtown     4) North York
    #     2) Etobicoke    5) Mississauga
    #     3) Scarborough  6) Brampton
    #     : """)
    #     self.loc = self.cities[int(self.choice) - 1]
    #     self.drugs.populate_drug_list()


class Drugs:
    def __init__(self):
        # Drug list values [Drug, min value, max value,
        self.all_drugs = ({'drug':"Acid", 'minval': 500,'maxval': 1200, 'MrktFlood': True, 'bust': False},
                          {'drug':'Cocaine','minval': 500,'maxval': 1200, 'MrktFlood': True, 'bust': False},
                          {'drug':"Heroin", 'minval': 500,'maxval': 1200, 'MrktFlood': True, 'bust': False},
                          {'drug':"Hash", 'minval': 500,'maxval': 1200, 'MrktFlood': True, 'bust': False},
                          {'drug':"Weed", 'minval': 500,'maxval': 1200, 'MrktFlood': True, 'bust': False},
                          {'drug':"Speed", 'minval': 500,'maxval': 1200, 'MrktFlood': True, 'bust': False},
                          {'drug':"Ecstasy", 'minval': 500,'maxval': 1200, 'MrktFlood': True, 'bust': False},
                          {'drug':"Peyote", 'minval': 500,'maxval': 1200, 'MrktFlood': True, 'bust': False},
                          {'drug':"Meth", 'minval': 500,'maxval': 1200, 'MrktFlood': True, 'bust': False},
                          {'drug':"Shrooms",'minval': 500,'maxval': 1200, 'MrktFlood': True, 'bust': False},
                          {'drug':"Opium", 'minval': 500,'maxval': 1200, 'MrktFlood': True, 'bust': False},
                          {'drug':"Ludes", 'minval': 500,'maxval': 1200, 'MrktFlood': True, 'bust': False})
        self.drugs_available = ()
        self.populate_drug_list()
        self.price_list = {}

    def populate_drug_list(self):
        num_of_drugs = randint(6, 10)
        self.drugs_available = sample(self.all_drugs, num_of_drugs)

    def drug_prices(self):
        pass

    def __str__(self):
        return self.drugs_available


class GameLoop:

    print("\nWelcome to Dopewars!\nMake some cash and watch out for Officer Hardass.\n\n")
    name = input("Please enter your name: ")
    player1 = Player(name)
    while ((player1.health > 0) and (player1.days_remaining >= 0)):
        print(player1)
        choice = input( "\n(B)uy (S)ell or (J)et: ")
        if ((choice.upper() == "B") or (choice.upper() == "BUY")):
            print(player1.location.drugs_here)
        elif ((choice.upper() == "S") or (choice.upper() == "SELL")):
            print(player1.location.drugs_here)
        elif ((choice.upper() == "J") or (choice.upper() == "JET")):
            print(player1.location.drugs_here)
        else:
            continue
