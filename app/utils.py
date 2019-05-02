import json

# Accepted values for coins,
# 50 is 50 pence, 100 is one pound, 200 is two pounds
coins = ("1", "2", "5", "10", "20", "50", "100", "200")
# coins = ("200", "100", "50", "20", "10", "5", "2", "1")
coins = (200, 100, 50, 20, 10, 5, 2, 1)

# from flask import current_app as app


def is_valid_input(value):
    '''
    Check if the input is in the expected form of a dictionary of coins.
    Coins are: "1", "2", "5", "10", "20", "50", "100", "200"
    :param value: the dictionary of coins to check
    :return: True is the data is a dictionary of coins and amount of coins
    '''
    try:
        value = json.loads(value)
    except json.decoder.JSONDecodeError as e:
        return "Bad input data format. Not Able to decode the input. " + str(e)
    if type(value) is not dict:
        return "Input data is not a dictionary as expected."
    for ele in value:
        if int(ele) not in coins:
            return "{} is not one of the expected coins: {}".format(ele, coins)
    return True

#
# print(is_valid_input("1 2 3"))
# print(is_valid_input( {"1":10, "5":10, "10":10, "20":10} ))
# print(is_valid_input({"1":10, "5":10, "110":10, "20":10}))
# print(is_valid_input({"1":10, "5":10, "10":10, "20":10}))
#
#
# print(is_valid_input( {"1":10, "5":10, "10":10, "20":10} ))

def compute_change(change, avail_coins):
    '''
    Find a collection of coins that sum to the change to be given
    :param change: change to be given
    :param avail_coins: dictionary of coins available
    :return: change to be given in the form of a dictionary,
                if it is not possible to find the collection of coins then it returns False
    '''
    change_dic = {}
    change_left = change
    avail_coins_copy = avail_coins.copy()
    i = 0
    while (change_left != 0):
        i +=1
        if (i > len(coins) -1) :
            return False
        while (change_left - coins[i] >= 0) and (avail_coins_copy.get(str(coins[i]),0) >0 ):
            change_left = change_left - coins[i]
            change_dic[str(coins[i])] = change_dic.get(str(coins[i]),0) + 1
            avail_coins_copy[str(coins[i])] = avail_coins_copy[str(coins[i])] - 1
    return change_dic


def add_to_bank(coins, bank):
    '''
    Add coins to the bank
    :param coins: dictionary of coins to be added to the bank
    :param bank: dictionary of coins that represents the money in the vending machine
    :return: updated value of the bank
    '''
    for i in coins:
        bank[i] = bank.get(i,0) + coins[i]
    return bank

def remove_from_bank(coins, bank):
    for i in coins:
        bank[i] = bank.get(i,0) - coins[i]
    return bank
#
# c= {"1":2,"5":2, "100":1, "10":1}
# d={"1":2,"5":2, "100":1}
# # p=5
# # print(compute_change(p,d))
#
# print(add_to_bank({}, d))

class Account():
    account = {}

    def __init__(self, value):
        self.account = value

    # Flask-Login integration
    def add_value(self):
        return True

    def update(self, value):
        self.account = value

    def get_value(self):
        return self.account
