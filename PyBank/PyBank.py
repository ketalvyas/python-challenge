import csv
import os

file_num = 1


file = os.path.join('budget_data_'+ str(file_num) +'.csv')


months = []
revenue = []


with open(file, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    
    next(csvread, None)

    for row in csvread:
        months.append(row[0])
        revenue.append(int(row[1]))


month_total = len(months)


greatest_increase_revenue = revenue[0]
greatest_decrease_revenue = revenue[0]
revenue_total = 0
total_revenue=0

for r in range(len(revenue)):
    if revenue[r] >= greatest_increase_revenue:
        greatest_increase_revenue = revenue[r]
        greatest_increase_month = months[r]
    elif revenue[r] <= greatest_decrease_revenue:
        greatest_decrease_revenue = revenue[r]
        greatest_decrease_month = months[r]
    total_revenue += revenue[r]


total_average = round(total_revenue/month_total,2)


output_destination = os.path.join('pybank_output_' + str(file_num) + '.txt')

data=[]

file_to_print=open(output_destination,"w")

data.append('Financial Analysis')
data.append('----------------------------')
data.append('Total Months: ' + str(month_total))
data.append('Total Revenue: $' + str(total_revenue))
data.append('Average Revenue Change: $' + str(total_average))
data.append('Greatest Increase in Revenue: ' + greatest_increase_month + ' of $' + str(greatest_increase_revenue))
data.append('Greatest Decrease in Revenue: ' + greatest_decrease_month + ' of $' + str(greatest_decrease_revenue))

for dat in data:
    print(dat)
    print(dat,file=file_to_print)

print()

file_to_print.close()



