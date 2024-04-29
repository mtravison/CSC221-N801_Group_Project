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

# gonna clean this up later
def drug_distribution_by_year(year):
    with open('data/Accidental_Drug_Related_Deaths_2012-2022.csv') as csvfile:
        drugs = {
            # Drug: [Deaths, Percentage]
            'Alcohol': [0, 0],
            'Heroin': [0, 0],
            'Cocaine': [0, 0],
            'Fentanyl': [0, 0],
            'Oxycodone': [0, 0],
            'Oxymorphone': [0, 0],
            'Ethanol': [0, 0],
            'Hydrocodone': [0, 0],
            'Benzodiazepine': [0, 0],
            'Methadone': [0, 0],
            'Amphet': [0, 0],
            'Tramad': [0, 0],
            'Morphine': [0, 0],
            'Xylazine': [0, 0],
            'Gabapentin': [0, 0],
            'Other': [0, 0],
            'Total': 0
        }
        reader = csv.DictReader(csvfile)
        for row in reader:
            if int(row['Date'][6:]) == year:
                drug = row['Cause of Death']
                keys = drugs.keys()
                done = False
                for key in keys:
                    if key in drug:
                        done = True
                        drugs[key][0] += 1
                        drugs['Total'] += 1
                        drugs[key][1] = round(((drugs[key][0] / drugs['Total']) * 100),2)
                    elif not done and key == 'Other':
                        drugs['Other'][0] += 1
                        drugs['Total'] += 1
                        drugs['Other'][1] = round(((drugs['Other'][0] / drugs['Total']) * 100),2)
    return drugs

def death_age_range(lowest, highest):
    with open('data/Accidental_Drug_Related_Deaths_2012-2022.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        ages = {}
        for i in range(1,101):
            ages[i] = 0
        for row in reader:
            if int(row['Age']) >= lowest and int(row['Age']) <= highest:
                ages["Age"] += 1
    return ages
        
def death_by_race(year):
    with open('data/Accidental_Drug_Related_Deaths_2012-2022.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        races = {
            White: 0
            Black: 0
            Asian: 0
        }
        for row in reader:
            if row['Date'][6:] == year:
                races[row['Race']] += 1
    return races
