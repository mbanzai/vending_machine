def is_winner(l):
    '''
    finds the winner if there is any
    
    :param l: the representation of the tic-tac-toc
    :return: 
    '''
    for i in range(3):
        sum_o = 0
        sum_v = 0
        for j in range(3):

            sum_o += l[i][j]
            sum_v += l[j][i]

        if sum_o == 3 or sum_v == 3:
            print("the winner is X")
        if sum_o == 0 or sum_v == 0:
            print("the winner is O")

    sum_ltr = l[0][0] + l[1][1] + l[2][2]
    sum_rtl = l[0][2] + l[1][1] + l[2][0]
    if sum_ltr == 3 or sum_rtl == 3:
        print("the winner is X")
    if  sum_ltr == 0 or sum_rtl == 0:
        print("the winner is O")


tic = [[0,1,4],
       [1,4,4],
       [0,1,0]
       ]

tac = [[1,4,1],
       [0,0,4],
       [0,0,4]
       ]

toc = [[1,0,1],
       [4,0,1],
       [4,1,0]
       ]

is_winner(tic)
is_winner(tac)
is_winner(toc)

def change (V, coins=[1,5,6,8,11] ):
    '''
    Finds the change using dinamic programming.

    :param V: value for which we need to find the change
    :param coins: list of accepted coins
    :return: the dinamic table
    '''

    table = [ [V+1]*(V+1) for _ in coins ]

    for i, coin in enumerate(coins):
        table[i][0] = 0

    for i, coin in enumerate(coins):
        for j in range(0,V+1):
            if j >= coin:
                a = table[i-1][j]
                b = 1+ table[i][j - coin]
                table[i][j] = min(table[i-1][j], 1+ table[i][j - coin] )
            else:
                c = table[i-1][j]
                table[i][j] = table[i-1][j]

    print(table[(len(coins))-1][V])
    return table


# a=change(9,coins=[1,3,4])
# print(a)
