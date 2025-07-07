import csv
data = [['Player', 'Team', 'Matches','Runs','Wickets'],
        ['Virat Kohli','India', 250, 1200,5], 
        ['Steave Smith', 'Australia', 200, 9500,10],
        ['Joe Root','England' ,220, 10200, 8], 
        ['Barbar Azam', 'Pakistan', 180, 8000,2],
        ['Kane Williamson', 'New Zealand', 210, 8900, 3]] 
filename = 'Sport_Data.csv'
with open(filename, 'w', newline='') as file:
    csvwriter = csv.writer(file)
    csvwriter.writerows(data)