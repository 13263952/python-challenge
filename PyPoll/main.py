######### David Duran Berkeley Bootcamp ###########
#########  12/21/22 Module 3 Challenge  ###########
import os
import csv


elect_data = os.path.join("Resources","election_data.csv")
with open(elect_data, encoding = "utf-8-sig",) as csv_file:
    elect_dt = csv.reader(csv_file, delimiter=',')
    header = next(csv_file)

 
    #dont forget headers

    #total votes
    votes_csted = 0
    diff_can = 0
    elect_rnnrs = {}
    winner_array = ["",0]


    for row in elect_dt:
        votes_csted += 1
        if row[2] in elect_rnnrs:  
            elect_rnnrs [row[2]] += 1  
        else:
            elect_rnnrs [row[2]] = 1  

    for key,value in elect_rnnrs.items():
        if winner_array[1]< value:
            winner_array[0]= key
            winner_array[1]= value
        cnd = {"votes":value,"percentage":f'{(value/votes_csted)*100:.3f}'}
        elect_rnnrs[key] = cnd

  
    effit = (f'h {elect_rnnrs["Charles Casper Stockham"]["votes"]}\n'
    f'h {elect_rnnrs["Diana DeGette"]["votes"]}') 
    effit2 = [f'{k}: {v["percentage"]}% ({v["votes"]})' for k,v in elect_rnnrs.items()]
    effit2 = "\n".join(effit2)
###concatenate
    
    title_1 = """Election Results
-------------------------"""
    title_2 = """-------------------------"""
entire_string = "" 
title_1 = title_1 + '\n'
entire_string += title_1
line_2 = ("Total Votes: " + str(votes_csted)) + '\n'
entire_string += line_2 
title_2 += '\n' 
entire_string += title_2
effit2 += '\n'
entire_string += effit2
entire_string += title_2
entire_string += "Winner: " + winner_array[0] + '\n'
entire_string += title_2
print(entire_string)    

###export data
with open('Mod_3_DD_Challenge3.txt','w') as f:
    f.write(entire_string)