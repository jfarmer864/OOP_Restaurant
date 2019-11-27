
class Restaurant():

    def __init__(self, name):
        self.seats = 40
        self.restaurant_name = name
        self.plate = []

    def welcome(self):
        self.seats -= 1
        print('Welcome to {}'.format(self.restaurant_name))
        waiter = Waiter()
        waiter.makeorder()
        self.plate.append(waiter.serveorder())

    def eat(self):
        for food in self.plate:
            print('This tasted of {}'.format(food.meat))
            print('I guess I have to pay {}'.format(food.price))

class Worker():

    def __init__(self, name):
        self.worker_name = name

class Chef(Worker):

    def __init__(self, name = 'John'):
        super().__init__(name)

    def makesushi(self):
        prepared = Sushi()
        return prepared

    def makewagyu(self):
        prepared = Wagyu()
        return prepared


class Waiter(Worker):

    def __init__(self, name = 'Tim'):
        super().__init__(name)
        self.holding = ''

    def makeorder(self):
        choice = int(input('Good Evening, would you like Sushi or Wagyu? (1 or 2) '))
        if choice == 1:
            sushimeal = Chef().makesushi()
            self.holding = sushimeal
        elif choice == 2:
            wagyumeal = Chef().makewagyu()
            self.holding = wagyumeal

    def serveorder(self):
        print('here is your meal. Enjoy!')
        return self.holding

class JapaneseFood():

    def __init__(self):
        self.origin = 'Japan'

class Sushi(JapaneseFood):

    def __init__(self):
        super().__init__()
        self.price = '£10'
        self.meat = 'Tuna'

class Wagyu(JapaneseFood):

    def __init__(self):
        super().__init__()
        self.price = '£100'
        self.meat = 'Beef'


Shoneys = Restaurant('Shoneys')
Shoneys.welcome()
Shoneys.eat()