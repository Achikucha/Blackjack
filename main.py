import random
import math

suits = ['♠', '♥', '♦', '♣']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

class Blackjack:
    def __init__(self,suits,ranks,bal,bet,client,dealer):
        self.suits = suits
        self.ranks = ranks
        self.bal = bal
        self.bet = bet
        self.client = client
        self.dealer = dealer
    def shuffle():
        suits = ['♠', '♥', '♦', '♣']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        client = []
        dealer = []
        dealer.append(random.choice(suits))
        dealer.append(random.choice(ranks))
        for i in range(2):
            client.append(random.choice(suits))
            client.append(random.choice(ranks))
        return client, dealer