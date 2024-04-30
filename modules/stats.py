import csv

# Returns # of deaths per year
def deaths_by_year():
    with open('data/Accidental_Drug_Related_Deaths_2012-2022.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        # Dict containing deaths per year
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
        # Iterates through csv file
        for row in reader:
            year = int(row['Date'][6:])
            # Adds a death to respective year in the dict
            if year in deaths_by_year:
                deaths_by_year[year] += 1
    return deaths_by_year

# Returns # and % of drugs used in a given year
def drug_distribution_by_year(year):
    with open('data/Accidental_Drug_Related_Deaths_2012-2022.csv') as csvfile:
        # Dict containing drugs and their totals and percentages
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
            # Checks if year in file matches given year
            if int(row['Date'][6:]) == year:
                # Gets cause of death and drugs involved in it
                drug = row['Cause of Death'].lower()
                # Get drugs in the dict
                keys = drugs.keys()
                # Checks if listed drugs were found in the cause of death column
                done = False
                # Iterates through drugs in the dict
                for key in keys:
                    # Checks if the drug is found in the cause of death
                    if key.lower() in drug:
                        done = True
                        # Updates totals and percentages
                        drugs[key][0] += 1
                        drugs['Total'] += 1
                        drugs[key][1] = round(((drugs[key][0] / drugs['Total']) * 100),2)
                    # If known drug not found, add to other
                    elif not done and key == 'Other':
                        drugs['Other'][0] += 1
                        drugs['Total'] += 1
                        drugs['Other'][1] = round(((drugs['Other'][0] / drugs['Total']) * 100),2)
    return drugs

# Returns total deaths of each age in a given range
def death_age_range(lowest, highest):
  with open('data/Accidental_Drug_Related_Deaths_2012-2022.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    ages = {}
    # Fills out the age dict
    for i in range(lowest, highest+1):
      ages[str(i)] = 0
    for row in reader:
      # Checks if age is known
      if row['Age'].isdigit():
        # Checks if age in row is in the range
        if int(row['Age']) >= lowest and int(row['Age']) <= highest:
          ages[row["Age"]] += 1
  return ages

# Returns death by race in a given year
def death_by_race(year):
  with open('data/Accidental_Drug_Related_Deaths_2012-2022.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    races = {"White": 0, "Black": 0, "Asian": 0, "Black or African American": 0, "Asian/Indian": 0, "Other": 0}
    for row in reader:
      if int(row['Date'][6:]) == year:
        # If the race in the row is found in the dict, adds 1
        try:
          races[row['Race']] += 1
        # If race not found adds to other
        except:
          races["Other"] += 1
  return races

# Returns drug usage between male and female of a given drug
def male_female_drug_usage(drug):
    with open('data/Accidental_Drug_Related_Deaths_2012-2022.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        # Known drugs
        drugs = ['Alcohol', 'Heroin','Cocaine','Fentanyl','Oxycodone','Oxymorphone','Ethanol','Hydrocodone','Benzodiazepine','Methadone','Amphet','Tramad','Morphine','Xylazine','Gabapentin']
        # Dict with totals
        male_female = {
            "Drug": drug,
            "Male": 0,
            "Female": 0
        }
        for row in reader:
            # Checks if row matches given drug
            if drug.lower() in row['Cause of Death'].lower():
                # Checks row for male/female and adds to total accordingly
                if row['Sex'] == 'Male':
                    male_female["Male"] += 1
                else:
                    male_female["Female"] += 1
    return male_female