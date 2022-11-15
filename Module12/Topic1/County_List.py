class CountyList:

    def __init__(self, capita, hhincome, fincome, population, num_households):
        self.population = population
        self.num_households = num_households
        self.per_capita_income = capita
        self.median_household_income = hhincome
        self.median_family_income = fincome

    def population_data(self, county):
        return(f"{county} has a population of {self.population} and contains {self.num_households} households.")


