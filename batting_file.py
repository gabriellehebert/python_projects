#GABRIELLE HEBERT
#
#CS 1411
#05/07/2017
#
#BATTING FILE STATISTIC ORGANIZER
#
#MAJOR PROGRAM SEQUENCE:
#OPENS A FILE OF BASEBALL BATTING STATISTICS
#ASKS USER WHAT INFORMATION THEY ARE LOOKING FOR
#CALLS A FUNCTION
#FUNCTION ORGANIZES THAT INFORMATION INTO A DICTIONARY WITH THE PLAYER+YR AS A KEY
#ASKS USER FOR PLAYER ID AND YEAR (KEY)
#DISPLAYS INFO
#REDISPLAYS MENU
#USER MUST CHOOSE TO EXIT PROGRAM
#
#INPUT: MENU SELECTION, BATTING FILE, PLAYER ID AND YEAR
#OUTPUT: MENU SELECTION AND CORRESPONDING STATISTIC
#
#INCLUDES EXCEPTION HANDLING
#
#TEST CASES INCLUDED:
#ALL 1-12 OF MENU SELECTIONS
#CORRECT AND INCORRECT PLAYER IDS AND YEARS
#A NUMBER SELECTION NOT INCLUDED ON MENU
#THE CHOICE TO EXIT THE PROGRAM
#ATTEMPTING TO RUN THE PROGRAM WITHOUT THE FILE DOWNLAODED
#
#USER MUST FIRST DOWNLOAD BATTING_TXT.TXT FILE
#
#INCLUDES PDF INSTRUCTIONS FOR RUNNING PROGRAM, AND PDF REFERENCE FOR PLAYER ID
#
#FILE USED FROM SEAN LAHMAN

import string

#FUNCTIONS FOR CREATING DICTIONARIES OF DIFFERENT COLUMNS OF DATA
def games (batting_file):
    g_dictionary={}
    player={}
    for line in (batting_file): #GOES THROUGH EACH LINE/PLAYER
        a=line.split(',') #SPLIT EACH PLAYER'S STATS INTO A LIST
        player[a[0]+a[1]]=a[5] #KEY IS PLAYERID+YEAR
        g_dictionary.update(player) #ADDS THAT PLAYER'S DICTIONARY TO DICTIONARY OF ALL PLAYERS
    return g_dictionary #RETURNS DICTIONARY OF ALL PLAYERS

#DICT FOR AB
def at_bats (batting_file):
    ab_dict={}
    player_b={}
    for line in (batting_file):
        b=line.split(',')
        player_b[b[0]+b[1]]=b[6]
        ab_dict.update(player_b)
    return ab_dict

#DICT FOR R
def runs (batting_file):
    r_dict={}
    player_c={}
    for line in (batting_file):
        c=line.split(',')
        player_c[c[0]+c[1]]=c[7]
        r_dict.update(player_c)
    return r_dict

#DICT FOR H
def hits (batting_file):
    h_dict={}
    player_d={}
    for line in (batting_file):
        d=line.split(',')
        player_d[d[0]+d[1]]=d[8]
        h_dict.update(player_d)
    return h_dict

#DICT FOR 2B
def doubles (batting_file):
    dbl_dict={}
    player_e={}
    for line in (batting_file):
        e=line.split(',')
        player_e[e[0]+e[1]]=e[9]
        dbl_dict.update(player_e)
    return dbl_dict

#DICT FOR 3B
def triples (batting_file):
    trpl_dict={}
    player_f={}
    for line in (batting_file):
        f=line.split(',')
        player_f[f[0]+f[1]]=f[10]
        trpl_dict.update(player_f)
    return trpl_dict

#DICT FOR HR
def homeruns (batting_file):
    hr_dict={}
    player_g={}
    for line in (batting_file):
        g=line.split(',')
        player_g[g[0]+g[1]]=g[11]
        hr_dict.update(player_g)
    return hr_dict

#DICT FOR RBI
def rbi (batting_file):
    rbi_dict={}
    player_h={}
    for line in (batting_file):
        h=line.split(',')
        player_h[h[0]+h[1]]=h[12]
        rbi_dict.update(player_h)
    return rbi_dict

#DICT FOR SB
def stolen_bases (batting_file):
    sb_dict={}
    player_i={}
    for line in (batting_file):
        i=line.split(',')
        player_i[i[0]+i[1]]=i[13]
        sb_dict.update(player_i)
    return sb_dict

#DICT FOR CS
def caught_steal (batting_file):
    cs_dict={}
    player_j={}
    for line in (batting_file):
        j=line.split(',')
        player_j[j[0]+j[1]]=j[14]
        cs_dict.update(player_j)
    return cs_dict

#DICT FOR BB
def base_balls (batting_file):
    bb_dict={}
    player_k={}
    for line in (batting_file):
        k=line.split(',')
        player_k[k[0]+k[1]]=k[15]
        bb_dict.update(player_k)
    return bb_dict

#DICT FOR SO
def strikeouts (batting_file):
    so_dict={}
    player_l={}
    for line in (batting_file):
        l=line.split(',')
        player_l[l[0]+l[1]]=l[16]
        so_dict.update(player_l)
    return so_dict


try:
    
#USER MENU
    menu_selection=input("""
Please select an option from the following menu using number or characters in parentheses:
0. Close Program (EXIT)
1. Games (G)
2. At Bats (AB)
3. Runs (R)
4. Hits (H)
5. Doubles (2B)
6. Triples (3B)
7. Homeruns (HR)
8. Runs Batted In (RBI)
9. Stolen Bases  (SB)
10. Caught Stealing (CS)
11. Base on Balls (BB)
12. Strikeouts    (SO)
""")
    
#OPENS FILE, ONLY TO READ
    batting_file=open('Batting_txt.txt', "r")

#WHILE STATEMENT TO CONTROL MENU LOOP
    while menu_selection!='0' and menu_selection!='EXIT':

#IF AND ELIF STATEMENTS CALL ON FUNCTIONS, BASED ON MENU SELECTION
        if menu_selection=='G' or menu_selection=='1':
            main_dict=games(batting_file)
    
        elif menu_selection=='AB' or menu_selection=='2':
            main_dict=at_bats(batting_file)
    
        elif menu_selection=='R' or menu_selection=='3':
            main_dict=runs(batting_file)

        elif menu_selection=='H' or menu_selection=='4':
            main_dict=hits(batting_file)

        elif menu_selection=='2B' or menu_selection=='5':
            main_dict=doubles(batting_file)
        
        elif menu_selection=='3B' or menu_selection=='6':
            main_dict=triples(batting_file)
        
        elif menu_selection=='HR' or menu_selection=='7':
            main_dict=homeruns(batting_file)

        elif menu_selection=='RBI' or menu_selection=='8':
            main_dict=rbi(batting_file)

        elif menu_selection=="SB" or menu_selection=='9':
            main_dict=stolen_bases(batting_file)

        elif menu_selection=='CS' or menu_selection=='10':
            main_dict=caught_steal(batting_file)

        elif menu_selection=='BB' or menu_selection=='11':
            main_dict=base_balls(batting_file)

        elif menu_selection=='SO' or menu_selection=='12':
            main_dict=strikeouts(batting_file)

#IF USER INSERTED SOMETHING OTHER THAN A MENU OPTION, "TRY AGAIN", REDISPLAYS MENU, THEN BREAKS
        else:
            print("Try Again")
            menu_selection=input("""
Please select an option from the following menu using number or characters in parentheses:
0. Close Program (EXIT)
1. Games (G)
2. At Bats (AB)
3. Runs (R)
4. Hits (H)
5. Doubles (2B)
6. Triples (3B)
7. Homeruns (HR)
8. Runs Batted In (RBI)
9. Stolen Bases  (SB)
10. Caught Stealing (CS)
11. Base on Balls (BB)
12. Strikeouts    (SO)
""")
            break
    
#INPUT PLAYER AND YEAR FROM USER AND COMBINES AS KEY IN DICTIONARY
        player=input("Insert playerID:")

        year=input("Insert year:")

        player_year=player+year

#SHOWS VALUE TO USER
        print("Your menu selection was:", menu_selection, ':', main_dict[player_year])

#DISPLAYS MENU FOR USER AGAIN
        menu_selection=input("""
Please select an option from the following menu using number or characters in parentheses:
0. Close Program (EXIT)
1. Games (G)
2. At Bats (AB)
3. Runs (R)
4. Hits (H)
5. Doubles (2B)
6. Triples (3B)
7. Homeruns (HR)
8. Runs Batted In (RBI)
9. Stolen Bases  (SB)
10. Caught Stealing (CS)
11. Base on Balls (BB)
12. Strikeouts    (SO)
""")

#EXCEPTIONS
except IOError:
    print("The file can't be found")
except ValueError:
    print("Player can't be found")
except KeyError:
    print("Player and/or year can't be found")
    
#CLOSE FILE   
batting_file.close()



