import csv

def deaths_by_year():
    with open('data/Accidental_Drug_Related_Deaths_2012-2022.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        deaths_by_year = {
            2012: 0,
            2013: 0,
            2014: 0,
            2015: 0,
            2016: 0,
            2017: 0,
            2018: 0,
            2019: 0,
            2020: 0,
            2021: 0,
            2022: 0
        }
        for row in reader:
            year = int(row['Date'][6:])
            if year in deaths_by_year:
                deaths_by_year[year] += 1
    return deaths_by_year