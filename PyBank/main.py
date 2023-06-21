######### David Duran Berkeley Bootcamp ###########
#########  12/21/22 Module 3 Challenge  ###########

import os
import csv


budget_data = os.path.join("Resources","budget_data.csv")
with open(budget_data, encoding = "utf-8-sig",) as csv_file:
    rdcsv = csv.reader(csv_file, delimiter=',')
  
### variable
    header = next(csv_file)
    frstrcrd = next(rdcsv)
    months = 1
    net_pl = int(frstrcrd[1])
    pl_previous = int(frstrcrd[1])
    dif_array = []
    months_array = []


    for row in rdcsv:
        months += 1
        net_pl += int(row[1])
        chnge = int(row[1])- pl_previous
        pl_previous = int(row[1])
        dif_array.append(chnge)
        months_array.append(row[0])
        
    max_val = max(dif_array)
    index_max = dif_array.index(max_val)
    month_max = months_array[index_max]
    
    min_val = min(dif_array)
    index_min = dif_array.index(min_val)
    month_min = months_array[index_min]
### Time To Concatenate
    title = """Financial Analysis
------------------------------"""

   
    line_2 = "Total Months: " + str(months)
    line_3 = "Total: $" + str(net_pl)
    line_4 = (f"Average Change: ${ sum(dif_array)/len(dif_array):.2f}\n"   
    f"Greatest Increase in Profits: {str(month_max)} $({str(int(max_val))})\n"
    f"Greatest Decrease in Profits: {str(month_min)} $({str(int(min_val))})\n")
  
title_1 = title

entire_string = ""
entire_string += title_1 + '\n'
entire_string += line_2 + "\n"
entire_string += line_3 + '\n'
entire_string += line_4 + '\n'


print(entire_string)
with open('Mod_3_DD_Challenge3_.txt','w') as f:
    f.write(entire_string)  
    


    




    




