import sys

input = sys.stdin.read().split('\n')

data = []

for i in range(len(input)):
    data.append(input[i].split(' ')

print (data)


'''
n = int(data[0][0])
K = int(data[0][1])

coins =[]
collection = []

for i in range(1,len(data)):
    coins.append(int(data[i][0]))
    if int(data[i][1]) > 0:
        collection.append(True)
    else:
        collection.append(False)


K=25
coins = [1,2,3,5,10,13,20]
collection = [False, False, True, False, False,False,False]

def calc_change (value, K, coins):
    ans = []
    change = K - value
    for i in range (len(coins)-1, -1, -1):
        if coins[i] <= change:
            ans.append(coins[i])
            change = change%coins[i]
    return ans

def find_num_new_coins (change_array, collection):
    num_new =0
    for i in range (len(coins)):      
        if (coins[i] in change_array):
            if (not collection[i]):
                num_new = num_new +1
    return num_new

max_new_coins = 0
max_value = 0

for i in range (K-1, 0, -1):
    change = calc_change(i, K, coins)
    new_coins = find_num_new_coins(change, collection)

    if new_coins > max_new_coins:
        max_new_coins = new_coins
        max_value = i

print (max_new_coins, "\n", max_value)
'''

