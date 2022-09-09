import csv
import calendar

infile = open('steps.csv', 'r')
outfile = open('avg_steps.csv','w', newline = '')
csvfile = csv.reader(infile, delimiter = ',')
next(csvfile)

writer = csv.writer(outfile, delimiter = ',')

header = ['Month', 'Steps']
writer.writerow(header)

tot_steps = 0
count = 0
cur_month = 1

for row in csvfile:
    if int(row[0]) == cur_month:
        count+=1
        tot_steps += int(row[1])

    else:
        avg = round((tot_steps / count), 2)
        month_name = calendar.month_name[int(row[0])]
        data = [month_name, avg]
        writer.writerow(data)
        cur_month = int(row[0])
        tot_steps = int(row[1])
        count = 1


outfile.close()
