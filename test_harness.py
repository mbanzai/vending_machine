'''
Docstring
'''
import requests


def main():
    '''
    Test Harness script, it can be executed from command line with:
    python test_harness.py
    :return:
    '''

    headers = {'content-type': 'application/json'}

    def print_out(status_code, text):
        print("****************************")
        print("Command executed: status")
        print("Status code: ", status_code)
        print("Response: ", text)
        print("****************************")


    while True:
        print('''
        Commands available:
        0. Greetings: A simple message 
        1. Status: Print the cash available in the machine
        2. Initialise: Setting the initial float. You need to provide the initial float as a dictionary.
            Example:
                {"1":10, "5":10, "10":10, "20":10, "100":10} means that there are:
                10 pieces of One penny coin
                10 pieces of Two pence coin
                10 pieces of Five pence coin
                10 pieces of Ten pence coin
                10 pieces of Twenty pence coin
                10 pieces of One pound coin 
        3. Change: Compute the change for the user. The response will be a dictionary, eg:
                Response:  {"5": 1}, which means one piece of Five pence coin
                Response:  {"1": 2, "10": 1}: two pieces of One penny coin and one piece of Ten pence coin
        4. Payment: Add the payment to the amount of coins in the machine. The Payment is a dictionary.
                Eg: {"1":20,"2":30} 20 pieces of One penny coin and 30 pieces of Two pence coin
        ''')

        com = input('Type the number corresponding to the command, eg 1:  ')

        if com == '0':
            url = 'http://localhost:8001/'
            res = requests.get(url, headers=headers)
            print_out(res.status_code, res.text)

        if com == '1':
            url = 'http://localhost:8001/status/'
            res = requests.get(url, headers=headers)
            print_out(res.status_code, res.text)

        if com == '2':
            coins = input('Dictionary of coins, eg: {"1":10, "5":10, "10":10, "20":10, "100":10}:  ')
            url = 'http://localhost:8001/initialise/'
            payload = coins
            res = requests.post(url, data=payload, headers=headers)
            print_out(res.status_code, res.text)

        if com == '3':
            coins = input('The change is an integer to represent the pence, eg: 5 is 5 pence:  ')
            url = 'http://localhost:8001/change/'+ str(coins)
            payload = coins
            res = requests.post(url, data=payload, headers=headers)
            print_out(res.status_code, res.text)

        if com == '4':
            coins = input('The payment dictionary of coins, eg:{"1":20,"2":30}  ')
            url = 'http://localhost:8001/payment/'
            payload = coins
            res = requests.post(url, data=payload, headers=headers)
            print_out(res.status_code, res.text)

if __name__ == "__main__":
    main()
