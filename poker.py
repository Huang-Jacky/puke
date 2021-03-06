# _*_coding:utf-8_*_
# /usr/bin/python

import random
import uniout


flower = ['黑桃', '红心', '方块', '草花']
num = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
boss = ['JOKER', 'joker']


def my_random():
    card_list = []
    while len(card_list) < 52:
        f_choice = random.choice(flower)
        n_choice = random.choice(num)
        card = f_choice + '_' + n_choice
        if card in card_list:
            pass
        else:
            card_list.append(card)
    card_list.insert(random.randint(0, 52), boss[0])
    card_list.insert(random.randint(0, 53), boss[1])
    return card_list


def send_card(card_list, player_num):
    players = []
    game = {}
    if isinstance(player_num, int) and player_num > 0:
        for i in range(player_num):
            players.append('Player_' + str(i))
    else:
        print '请输入参与人数且参与人数需要大于等于1人！'
        exit()
    for player in players:
        game[player] = card_list[players.index(player):len(card_list) + 1:player_num]
    return game


if __name__ == "__main__":
    game = send_card(my_random(), 4)
    for k, v in game.iteritems():
        print "[%s] =" % k, v
