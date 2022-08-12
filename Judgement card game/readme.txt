FIRST FOUR LINE CONTAINS THE CARDS TO BE GIVEN TO A PARTICULAR PLAYER
WHERE LINE 1 CORRESPONDS TO bot_1
LINE 2 CORRESPONDS TO bot_2
LINE 3 CORRESPONDS TO BOT_3
LINE 4 CORRESPONDS TO player
LINE 5 CORRESPONDS TO CYCLIC ORDER

*****cards must be enter in each separated by commas(,) with no spaces like if want to ditribute these sets of cards :****

bot1: HA,SK,DQ,CJ,H10,S9,D8,C7,H6,H5,H4,H3,H2
bot2: HK,SA,DJ,CQ,S10,D9,S8,S7,S6,S5,S4,S3,S2
bot3: HQ,SJ,DA,CK,C10,C9,C8,H7,C6,C5,C4,C3,C2
player:HJ,SQ,DK,CA,D10,H9,H8,D7,D6,D5,D4,D3,D2

******first four lines of file should look like this :*****

HA,SK,DQ,CJ,H10,S9,D8,C7,H6,H5,H4,H3,H2
HK,SA,DJ,CQ,S10,D9,S8,S7,S6,S5,S4,S3,S2
HQ,SJ,DA,CK,C10,C9,C8,H7,C6,C5,C4,C3,C2
HJ,SQ,DK,CA,D10,H9,H8,D7,D6,D5,D4,D3,D2

*****conventions for cyclic order*****
each bot and player must be written in desired cyclic order separated by commas(,) without any spaces
*****bot 1 must be written as bot_1*****
*****bot 2 must be written as bot_2*****
*****bot 3 must be written as bot_3*****
*****player must be written as player*****
So if we want to enter the cyclic order :
bot 1->bot 2->bot 3->player

LINE 5 of input file must be written as following:
bot_1,bot_2,bot_3,player


*************************SAMPLE INPUT OF FILE ACCORDING TO FOLLOWING CONVENTIONS*************************
HA,SK,DQ,CJ,H10,S9,D8,C7,H6,H5,H4,H3,H2
HK,SA,DJ,CQ,S10,D9,S8,S7,S6,S5,S4,S3,S2
HQ,SJ,DA,CK,C10,C9,C8,H7,C6,C5,C4,C3,C2
HJ,SQ,DK,CA,D10,H9,H8,D7,D6,D5,D4,D3,D2
bot_1,bot_2,player,bot_3


