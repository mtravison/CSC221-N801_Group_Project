# Import module example
import modules.stats as stats

# Uses the function stats.py inside the modules folder
deaths_by_year = stats.deaths_by_year()

print(deaths_by_year[2012])
print(deaths_by_year[2013])