# Third-party imports
from flask import current_app as app
from flask import abort, jsonify, request, session
import json


# Local imports
from . import setup
from .. import utils

bank = utils.Account({})
# bank = utils.Account({"1":10, "2":10, "5":10, "10":10})

@setup.route('/')
def index():
    return "Hello, World! This is a Vending Machine :-)"


@setup.route('/status/')
def status():
    '''
    Print the status of the current cash in the machine.
    {"1":10, "5":10, "10":10, "20":10, "100":10} means that there are:
    10 One penny
    10 Two pence
    10 Five pence
    10 Ten pence
    10 Twenty pence
    10 One pound
    ....


    :return: dictionary of coin:amount

    Example to invoke from commad line:
    > curl -H "Content-Type: application/json" -X GET  http://localhost:8001/status/
    '''

    if bank.get_value():
        return jsonify(bank.get_value()), 200
    else:
        return jsonify("Empty bank"), 400


@setup.route('/initialise/', methods=['GET', 'POST'])
def initialise():
    '''
    Update the current amount of coins (aka bank) available in the vending machine

    :return: dictionary of coin:amount

    Example to invoke from commad line:
    curl -H "Content-Type: application/json"  -X POST -i 'http://localhost:8001/initialise/' --data '{"1":20,"2":30}'
    '''

    if not request.data:
        return jsonify({"error": "Missing data in the request"}), 400
    if not request.is_json:
        return jsonify({"error": "Invalid data in the request, Content Type is not json"}), 400

    check_in_coins = utils.is_valid_input(request.data)

    if check_in_coins == True:
        bank.update(json.loads(request.data))

        return ("Operation Completed Succesfully"), 200

    return jsonify({"error": check_in_coins + " The data provided was: " + str(request.data)}), 400


@setup.route('/payment/', methods=['GET', 'POST'])
def payment():
    '''
    Initialise the initial float of the machine (the coins placed in the machine for customer change)

    :return: dictionary of coin:amount

    Example to invoke from commad line:
    curl -H "Content-Type: application/json"  -X POST -i 'http://localhost:8001/payment/' --data '{"1":20,"2":30}'
    '''

    if not request.data:
        return jsonify({"error": "Missing data in the request"}), 400
    if not request.is_json:
        return jsonify({"error": "Invalid data in the request, Content Type is not json"}), 400

    if not bank.get_value():
        return jsonify({"error": "The vending machine has not been initialised." }), 500

    check_in_coins = utils.is_valid_input(request.data)

    if check_in_coins == True:
        bank.update(utils.add_to_bank(json.loads(request.data), bank.get_value()))
        return "Operation Completed Succesfully", 200

    return jsonify({"error": check_in_coins + " The data provided was: " + str(request.data)}), 400


@setup.route('/change/<int:value>', methods=['GET', 'POST'])
def change(value):
    '''
    Compute the change for the user
    :return: dictionary of coin:amount

    Example to invoke from commad line:
    curl -H "Content-Type: application/json" -X GET  http://localhost:8001/change/6
    '''

    if not bank:
        return jsonify({"error": "The vending machine has not been initialised." }), 500

    if int(value) > 0:
        value_account = utils.Account(bank.get_value())

        change_to_give = utils.compute_change(value, value_account.get_value())

        if change_to_give != False:
            bank.update(utils.remove_from_bank(change_to_give,bank.get_value()))
        return jsonify(change_to_give), 200

    else:
        return jsonify("Bad data"), 400
