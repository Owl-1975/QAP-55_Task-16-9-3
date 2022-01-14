class Clients:
    def __init__(self, surname, name, payment, cost):
        self.surname = surname
        self.name = name
        self.payment = sum(payment)
        self.cost = sum(cost)
    def get_balance(self):
        return self.payment - self.cost
    def __str__(self):
        return f'Клиент "{self.name} {self.surname}". Баланс: {self.get_balance()} руб.'

clients = [
            {'surname': 'White', 'name': 'John', 'payment': {500, 800, 1300}, 'cost': {275, 439, 839}},
            {'surname': 'Green', 'name': 'Philip', 'payment': {645, 927, 1145}, 'cost': {431, 179, 619}},
            {'surname': 'Black', 'name': 'Roger', 'payment': {617, 971, 873}, 'cost': {391, 127, 374}}
          ]
for client in clients:
    o_client = Clients(client['surname'], client['name'], client['payment'], client['cost'])
    print(o_client)
