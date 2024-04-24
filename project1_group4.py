# Import module example
import modules.stats as stats

# Uses the function stats.py inside the modules folder
deaths_by_year = stats.deaths_by_year()
drug_distribution_by_year = stats.drug_distribution_by_year(2014)

print(deaths_by_year[2020])
print(drug_distribution_by_year)