import county_demographics
import build_data
import data
from data import CountyDemographics


# PART 1
# Returns the total 2014 Population from the given countries in the provided list
# INPUT: list of CountyDemographics objects
# OUTPUT: integer representing the population sum
def population_list(counties : list[data.CountyDemographics]) -> int:
    x = [county.population['2014 Population'] for county in counties]
    return sum(x)

# PART 2
# Returns a list of given county demographics objects within the specified state
# INPUT: list of County Demographics objects, two-letter state abbreviation str
# OUTPUT: list of County Demographic objects within the specified state
def filter_by_state(counties : list[data.CountyDemographics], text : str) -> list[data.CountyDemographics]:
    return [county for county in counties if county.state == text]

# PART 3
# Returns the total 2014 sub-population across the set of counties in the specified education key
# INPUT: list of County Demographic Objects, education key of interest
# OUTPUT: float repr total sub-population in the specified key of interest based on given counties
def population_by_education(counties : list[CountyDemographics], edu : str) -> float:
    x = [(county.education[edu]/100)*county.population['2014 Population'] for county in counties if edu in county.education]
    return sum(x)

# Returns the total 2014 sub-population across the set of counties in the specified ethnicity key
# INPUT: list of County Demographic Objects, ethnicity key of interest
# OUTPUT: float repr total sub-population in the specified key of interest based on given counties
def population_by_ethnicity(counties : list[CountyDemographics], eth : str) -> float:
    x = [(county.ethnicities[eth]/100)*county.population['2014 Population'] for county in counties if eth in county.ethnicities]
    return sum(x)

# Returns the total 2014 sub-population across the set of counties that are below poverty
# INPUT: list of County Demographic Objects
# OUTPUT: float repr total sub-population in the specified key of interest based on given counties
def population_below_poverty_level(counties : list[CountyDemographics]) -> float:
    x = [(county.income['Persons Below Poverty Level']/100)*county.population['2014 Population'] for county in counties]
    return sum(x)

# PART 4
# Returns the percentage of the total population across the set of counties that are in the specified education key
# INPUT: list of County Demographic Objects, education key of interest
# OUTPUT: float repr total sub-population in the specified key of interest based on given counties
def percent_by_education(counties : list[CountyDemographics], edu : str) -> float:
    return round((population_by_education(counties,edu)/population_list(counties))*100,2)

# Returns the percentage of the total population across the set of counties that are in the specified ethnicity key
# INPUT: list of County Demographic Objects, ethnicity key of interest
# OUTPUT: float repr total sub-population in the specified key of interest based on given counties
def percent_by_ethnicity(counties : list[CountyDemographics], eth : str) -> float:
    return round((population_by_ethnicity(counties,eth)/population_list(counties)) * 100,2)

# Returns the percentage of the total population across the set of counties that are below poverty level
# INPUT: list of County Demographic Objects
# OUTPUT: float repr total sub-population in the specified key of interest based on given counties
def percent_below_poverty_level(counties : list[CountyDemographics]) -> float:
    return round((population_below_poverty_level(counties)/population_list(counties)) * 100,2)

# PART 5
# Returns a list of counties whose specified education key value is greater than the given threshold
# INPUT: list of County Demographic objects, str of the education key of interest, float of the threshold value
# OUTPUT: list of County Demographic objects representing counties greater than the given threshold
def education_greater_than(counties : list[data.CountyDemographics], edu : str, threshold : float) -> list[data.CountyDemographics]:
    return [county for county in counties if edu in county.education and county.education[edu] > threshold]

# Returns a list of counties whose specified education key value is less than the given threshold
# INPUT: list of County Demographic objects, str of the education key of interest, float of the threshold value
# OUTPUT: list of County Demographic objects representing counties greater than the given threshold
def education_less_than(counties : list[data.CountyDemographics], edu : str, threshold : float) -> list[data.CountyDemographics]:
    return [county for county in counties if edu in county.education and county.education[edu] < threshold]

# Returns a list of counties whose specified ethnicity key value is greater than the given threshold
# INPUT: list of County Demographic objects, str of the ethnicity key of interest, float of the threshold value
# OUTPUT: list of County Demographic objects representing counties greater than the given threshold
def ethnicity_greater_than(counties : list[data.CountyDemographics], eth : str, threshold : float) -> list[data.CountyDemographics]:
    return [county for county in counties if eth in county.ethnicities and county.ethnicities[eth] > threshold]

# Returns a list of counties whose specified ethnicity key value is less than the given threshold
# INPUT: list of County Demographic objects, str of the ethnicity key of interest, float of the threshold value
# OUTPUT: list of County Demographic objects representing counties greater than the given threshold
def ethnicity_less_than(counties : list[data.CountyDemographics], eth : str, threshold : float) -> list[data.CountyDemographics]:
    return [county for county in counties if eth in county.ethnicities and county.ethnicities[eth] < threshold]

# Returns a list of counties whose population below poverty level is greater than the given threshold
# INPUT: list of County Demographic objects, float of the threshold value
# OUTPUT: list of County Demographic objects representing counties greater than the given threshold
def below_poverty_level_greater_than(counties : list[data.CountyDemographics], threshold : float) -> list[data.CountyDemographics]:
    return [county for county in counties if county.income['Persons Below Poverty Level'] > threshold]

# Returns a list of counties whose population below poverty level is less than the given threshold
# INPUT: list of County Demographic objects, float of the threshold value
# OUTPUT: list of County Demographic objects representing counties greater than the given threshold
def below_poverty_level_less_than(counties : list[data.CountyDemographics], threshold : float) -> list[data.CountyDemographics]:
    return [county for county in counties if county.income['Persons Below Poverty Level'] < threshold]