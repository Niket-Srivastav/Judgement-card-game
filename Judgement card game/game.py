import random
#function for distribution of cards
def distribute_random(player,card_lst):
    for i in range(13):
        card=random.choice(card_lst)
        if card[0]=="H":
            player["H"].append(card)
        elif card[0]=="S":
            player["S"].append(card)
        elif card[0]=="D":
            player["D"].append(card)
        elif card[0]=="C":
            player["C"].append(card)
        card_lst.remove(card)

#function to distribute from custom file
def distribute_from_file(player,list):
    for i in list:
        if i[0]=="H":
            player["H"].append(i)
        elif i[0]=="S":
            player["S"].append(i)
        elif i[0]=="D":
            player["D"].append(i)
        elif i[0]=="C":
            player["C"].append(i)


#function for calling wins for each bot
def calling_win(player):
    count=0
    for j in player.values():
         for k in j:
                if(k.isalpha()):
                    count+=1
    return count

#function for player to throw the card
def player_card_throw_function(player):
    print("YOUR SET OF CARDS")
    lst=[]
    for i in player.values():
        for k in i:
            lst.append(k)
    print(player)
    card_thrown=input("which card do you want to throw : ")
    while card_thrown not in lst:
        print("You don't have the card in your set of cards")
        card_thrown=input("which card do you want to throw : ")
    if card_thrown[0]=="H":
        player["H"].remove(card_thrown)
    elif card_thrown[0]=="C":
        player["C"].remove(card_thrown)
    elif card_thrown[0]=="S":
        player["S"].remove(card_thrown)
    elif card_thrown[0]=="D":
        player["D"].remove(card_thrown)
    return card_thrown

#function to sort cards highest to lowest IN BOT DICTIONARY
def sort_card(bot):
    lst=[]
    for i in bot.values():
        for k in i:
            if k[1]=="A":
               lst.append((k,0))
            elif k[1]=="K":
               lst.append((k,1))
            elif k[1]=="Q":
               lst.append((k,2))
            elif k[1]=="J":
               lst.append((k,3))
            elif len(k)==3:
               lst.append((k,4)) 
            elif k[1]=="9":
               lst.append((k,5))
            elif k[1]=="8":
               lst.append((k,6))
            elif k[1]=="7":
               lst.append((k,7))
            elif k[1]=="6":
               lst.append((k,8))
            elif k[1]=="5":
               lst.append((k,9))
            elif k[1]=="4":
               lst.append((k,10))
            elif k[1]=="3":
               lst.append((k,11))
            elif k[1]=="2":
               lst.append((k,12))            
    lst.sort(key=lambda x:x[1])
    return lst

#function for first throw of card by bot
def bot_throw_card_first(bot):
    sorted_cards=sort_card(bot)
    if sorted_cards[0][0][0]=="H":
        bot["H"].remove(sorted_cards[0][0])
    elif sorted_cards[0][0][0]=="C":
        bot["C"].remove(sorted_cards[0][0])
    elif sorted_cards[0][0][0]=="S":
        bot["S"].remove(sorted_cards[0][0])
    elif sorted_cards[0][0][0]=="D":
        bot["D"].remove(sorted_cards[0][0])
    return sorted_cards[0][0]

def sort_card_in_list(lst):
    temp_list=[]
    for k in lst:
        if k[1]=="A":
            temp_list.append((k,0))
        elif k[1]=="K":
            temp_list.append((k,1))
        elif k[1]=="Q":
            temp_list.append((k,2))
        elif k[1]=="J":
            temp_list.append((k,3))
        elif len(k)==3:
            temp_list.append((k,4)) 
        elif k[1]=="9":
           temp_list.append((k,5))
        elif k[1]=="8":
           temp_list.append((k,6))
        elif k[1]=="7":
           temp_list.append((k,7))
        elif k[1]=="6":
           temp_list.append((k,8))
        elif k[1]=="5":
           temp_list.append((k,9))
        elif k[1]=="4":
            temp_list.append((k,10))
        elif k[1]=="3":
            temp_list.append((k,11))
        elif k[1]=="2":
            temp_list.append((k,12))            
    temp_list.sort(key=lambda x:x[1])
    return temp_list


#function to card throw by BOT during play
def bot_throw_card_in_game(lst,bot):
    temp_lst=[]
    for i in lst:
        if i[0]==lst[0][0]:
            temp_lst.append(i)
    if len(bot[lst[0][0]])==0:
        sorted_cards=sort_card(bot)
        bot[sorted_cards[-1][0][0]].remove(sorted_cards[-1][0])
        return sorted_cards[-1][0]
    elif len(bot[lst[0][0]])!=0:
        t_lst=sort_card_in_list(temp_lst)
        cur_list=[t_lst[0][0]]
        cur_list.extend(bot[lst[0][0]])
        cur_sort_list=sort_card_in_list(cur_list)
        if cur_sort_list[0][0]==t_lst[0][0]:
            bot[lst[0][0]].remove(cur_sort_list[-1][0])
            return cur_sort_list[-1][0]
        else:
            bot[lst[0][0]].remove(cur_sort_list[0][0])
            return cur_sort_list[0][0]

#selection of turn
def turn_selection(ran_num,dict,cyclic_order):
    if ran_num==0:
        return (dict[0],cyclic_order[0])
    elif ran_num==1:
        return (dict[1],cyclic_order[1])
    elif ran_num==2:
        return (dict[2],cyclic_order[2])
    elif ran_num==3:
        return (dict[3],cyclic_order[3])
#total cards

#function to decide winner
def winning(card_thrown):
    card_thrown_mod=[]
    for i in card_thrown:
        card_thrown_mod.append(i[0])
    temp_lst=[]
    for i in card_thrown_mod:
        if i[0]==card_thrown_mod[0][0]:
            temp_lst.append(i)
    sorted_cards=sort_card_in_list(temp_lst)
    i=card_thrown_mod.index(sorted_cards[0][0])
    return card_thrown[i][1]

#function to decide score
def calculate_score(call,wins):
    if(call>wins):
        return -10*call
    else:
        return 10*call+(wins-call)
#GAMEPLAY
bot_1_series=0
bot_2_series=0
bot_3_series=0
player_series=0
def gameplay():
    print("""
                      ____________
                     | A          |           J
                     |         ___|________   U
                     |    /\  | K          |  D 
                     |   /  \ |            |  G
                     |   \  / |     /\     |  E
                     |    \/  |    /  \    |  M
                     |        |    \  /    |  E
                     |________|     \/     |  N
                              |            |  T
                              |____________|
    """)
    print("~~~~~~~~~~~~~~~~~~WELCOME TO THE GAME:JUDGEMENT~~~~~~~~~~~~~~~~~~")
    #dictionary for each player 
    bot_1={"S":[],"H":[],"D":[],"C":[]}
    bot_2={"S":[],"H":[],"D":[],"C":[]}
    bot_3={"S":[],"H":[],"D":[],"C":[]}
    player={"S":[],"H":[],"D":[],"C":[]}

    card_lst=["HA","SK","DQ","CJ","H10","S9","D8","C7","H6","H5","H4","H3","H2","HK","SA","DJ","CQ","S10","D9","S8","S7","S6","S5","S4","S3","S2","HQ","SJ","DA","CK","C10","C9","C8","H7","C6","C5","C4","C3","C2","HJ","SQ","DK","CA","D10","H9","H8","D7","D6","D5","D4","D3","D2"]
    #distributing cards
    file=open("cards.txt","r")
    str1=file.readlines()
    str2=[]
    for i in str1:
        str2.append(i.rstrip("\n"))
    flag=0
    custom=input("do you want to perform for custom input (Y/N)")
    if custom.upper()=="Y":
        flag=1

    if flag==1:
        lst=str2[0].split(",")
        distribute_from_file(bot_1,lst)
        lst=str2[1].split(",")
        distribute_from_file(bot_2,lst)
        lst=str2[2].split(",")
        distribute_from_file(bot_3,lst)
        lst=str2[3].split(",")
        distribute_from_file(player,lst)
    elif flag==0:
        distribute_random(bot_1,card_lst)   
        distribute_random(bot_2,card_lst)
        distribute_random(bot_3,card_lst)
        distribute_random(player,card_lst)
    print("YOUR SET CARDS :")
    print(player)
    print("\n")

    #calculating call for each bot
    bot_1_call=calling_win(bot_1)
    bot_2_call=calling_win(bot_2)
    bot_3_call=calling_win(bot_3)

    #taking input player call
    player_call=int(input("ENTER THE NUMBER OF TIMES YOU CAN POTENTIALLY WIN : "))

    #printing calls of every player
    print(f"CALL OF PLAYERS : bot_1->{bot_1_call} | bot_2->{bot_2_call} | bot_3->{bot_3_call} | player->{player_call}")

    #cyclic order in which player will throw cards
    if flag==1:
        cyclic_order=[str2[4].split(",")[0],str2[4].split(",")[1],str2[4].split(",")[2],str2[4].split(",")[3]]
    else:
        cyclic_order=["bot_1","bot_2","player","bot_3"]
    print("cyclic_order  :")
    print(cyclic_order[0]+"->"+cyclic_order[1]+"->"+cyclic_order[2]+"->"+cyclic_order[3])

    bot1_wins=0
    bot2_wins=0
    bot3_wins=0
    player_wins=0
    a=random.randint(0,3)
    dict={0:0,1:0,2:0,3:0}
    for i in cyclic_order:
        if i=="bot_1":
            dict[cyclic_order.index(i)]=bot_1
        elif i=="bot_2":
            dict[cyclic_order.index(i)]=bot_2
        elif i=="bot_3":
            dict[cyclic_order.index(i)]=bot_3
        elif i=="player":
            dict[cyclic_order.index(i)]=player
    for i in range (13):
        print("***************ROUND"+str(i+1)+"*******************************")
        s=turn_selection(a,dict,cyclic_order)
        card_thrown=[]
        card_thrown_for_bot=[]
        if s[1][0]=="b":
            print(s[1]+" turn",end="->")
            card1=bot_throw_card_first(s[0])
        else:
            print("player turn",end="->")
            card1=player_card_throw_function(s[0])
        print(card1)
        card_thrown_for_bot.append(card1)
        card_thrown.append([card1,a])

        a=(a+1)%4
        s=turn_selection(a,dict,cyclic_order)
        if s[1][0]=="b":
            print(s[1]+" turn",end="->")
            card2=bot_throw_card_in_game(card_thrown_for_bot,s[0])
        else:
            print("player turn",end="->")
            card2=player_card_throw_function(s[0])
        print(card2)
        card_thrown_for_bot.append(card2)
        card_thrown.append([card2,a])

        a=(a+1)%4
        s=turn_selection(a,dict,cyclic_order)
        if s[1][0]=="b":
            print(s[1]+" turn",end="->")
            card3=bot_throw_card_in_game(card_thrown_for_bot,s[0])
        else:
            print("player turn",end="->")
            card3=player_card_throw_function(s[0])
        print(card3)
        card_thrown_for_bot.append(card3)
        card_thrown.append([card3,a])

        a=(a+1)%4
        s=turn_selection(a,dict,cyclic_order)
        if s[1][0]=="b":
            print(s[1]+" turn",end="->")
            card4=bot_throw_card_in_game(card_thrown_for_bot,s[0])
        else:
            print("player turn",end="->")
            card4=player_card_throw_function(s[0])
        print(card4)
        card_thrown_for_bot.append(card4)
        card_thrown.append([card4,a])

        a=winning(card_thrown)
        if a==0:
            print("~~~"+cyclic_order[0]+"wins~~~")
            if cyclic_order[0]=="bot_1":
                bot1_wins+=1
            elif cyclic_order[0]=="bot_2":
                bot2_wins+=1
            elif cyclic_order[0]=="player":
                player_wins+=1
            elif cyclic_order[0]=="bot_3":
                bot3_wins+=1
        elif a==1:
            print("~~~"+cyclic_order[1]+"wins~~~")
            if cyclic_order[1]=="bot_1":
                bot1_wins+=1
            elif cyclic_order[1]=="bot_2":
                bot2_wins+=1
            elif cyclic_order[1]=="player":
                player_wins+=1
            elif cyclic_order[1]=="bot_3":
                bot3_wins+=1
        elif a==2:
            print("~~~"+cyclic_order[2]+"wins~~~")
            if cyclic_order[2]=="bot_1":
                bot1_wins+=1
            elif cyclic_order[2]=="bot_2":
                bot2_wins+=1
            elif cyclic_order[2]=="player":
                player_wins+=1
            elif cyclic_order[2]=="bot_3":
                bot3_wins+=1
        elif a==3:
            print("~~~"+cyclic_order[3]+"wins~~~")
            if cyclic_order[3]=="bot_1":
                bot1_wins+=1
            elif cyclic_order[3]=="bot_2":
                bot2_wins+=1
            elif cyclic_order[3]=="player":
                player_wins+=1
            elif cyclic_order[3]=="bot_3":
                bot3_wins+=1
    global bot_1_series,bot_2_series,bot_3_series,player_series
    bot_1_score=calculate_score(bot_1_call,bot1_wins)
    bot_1_series+=bot_1_score
    bot_2_score=calculate_score(bot_2_call,bot2_wins)
    bot_2_series+=bot_2_score
    player_score=calculate_score(player_call,player_wins)
    player_series+=player_score
    bot_3_score=calculate_score(bot_3_call,bot3_wins)
    bot_3_series+=bot_3_score
    print("score of bot1 "+str(bot_1_score))
    print("score of bot2 "+str(bot_2_score))
    print("score of bot3 "+str(bot_3_score))
    print("score of player "+str(player_score))

    if max(bot_1_score,bot_2_score,bot_3_score,player_score)==bot_1_score:
        print("~~~~~bot 1 wins the game~~~~~")
    elif max(bot_1_score,bot_2_score,bot_3_score,player_score)==bot_2_score:
        print("~~~~~bot 2 wins the game~~~~~")
    elif max(bot_1_score,bot_2_score,bot_3_score,player_score)==bot_3_score:
        print("~~~~~bot 3 wins the game~~~~~")
    elif max(bot_1_score,bot_2_score,bot_3_score,player_score)==player_score:
        print("~~~~~player wins the game~~~~~")
    print("\n")
gameplay()

e=input("DO YOU WANT TO CONTINUE THE GAME(Y/N)")

while(e.upper()=="Y"):
    gameplay()
    e=input("DO YOU WANT TO CONTINUE THE GAME(Y/N)")

print("******************\n")


print("score of bot1 "+str(bot_1_series))
print("score of bot2 "+str(bot_2_series))
print("score of bot3 "+str(bot_3_series))
print("score of player "+str(player_series))


if max(bot_1_series,bot_2_series,bot_3_series,player_series)==bot_1_series:
        print("~~~~~bot 1 wins the series~~~~~")
elif max(bot_1_series,bot_2_series,bot_3_series,player_series)==bot_2_series:
        print("~~~~~bot 2 wins the series~~~~~")
elif max(bot_1_series,bot_2_series,bot_3_series,player_series)==bot_3_series:
        print("~~~~~bot 3 wins the series~~~~~")
elif max(bot_1_series,bot_2_series,bot_3_series,player_series)==player_series:
        print("~~~~~player wins the series~~~~~")



print("thanks!exiting")