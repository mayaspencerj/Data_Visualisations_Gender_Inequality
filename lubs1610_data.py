import matplotlib.pyplot as plt
import numpy as np
##finals
year = [1870, 1875, 1880, 1885, 1890, 1895, 1900, 1905,1910, 1915, 1920, 1925, 1930, 1935, 1940, 1945, 1950, 1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010]

gdp_per_cap = [4149.064965, 4331.652597, 4345.705146, 4320.486679, 4627.015919, 4710.400054, 5101.102912, 5226.807135, 5296.030687, 6089.478978, 6089.478978, 5481.096857, 5746.45385, 6084.957325, 7501.049454, 7501.013727, 7736.751889,9252.545533,10436.79599, 11876.42568, 13269.594, 14626.81898, 16104.04128, 18073.09246, 21152.90774, 22600.47085, 25974.8933, 28933.50623, 28391.3067]

gender_ineq = [0.0, -0.1, -0.1, -0.2, -0.2, -0.4, -0.6, -0.3, -0.1, 0.2, 0.7, 1.1, 1.4, 0.7, 0.5,0.7, 2.2, 1.2, 0.9, -0.2, -0.6, -0.5,-0.9, -1.0, -0.2, -0.3, 0.0, -2.0, -3.5]

def plot_gdp_year(year,gdp_per_cap):
    plt.plot(year,gdp_per_cap)
    plt.title("A graph to show the changes in the Real GDP Per Capita between 1870 - 2010 in the UK")
    plt.yticks([0,5000,10000,15000,20000,25000,30000])
    plt.xticks(year, rotation=45)
    plt.xlabel('Year')
    plt.ylabel('GDP per Capita (Y)')
    plt.grid(True)
    plt.show()

def plot_gender_year(year,gender_ineq):
    plt.plot(year,gender_ineq, 'm')
    plt.title("A graph to show the changes in the Gender Inequalities in Secondary Education Attainment between 1870 - 2010 in the UK")
    plt.yticks([-3.5, -3,-2.5,-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5])
    plt.xticks(year, rotation=45)
    plt.xlabel('Year')
    plt.ylabel('Gender Inequality Differential in Secondary Education Attainment (Gi)')
    plt.grid(True)
    plt.show()

def plot_regression(gender_ineq,gdp_per_cap):
    x = np.linspace(-3.5,2.5,50)
    y = (-4057.7*x)+10512
    plt.plot(gender_ineq, gdp_per_cap, 'p',)
    plt.plot(x, y, '-m', label='Y=-4057.7Gi + 10512')
    plt.legend(loc='upper left')
    plt.title("Regression Analysis: Gender Inequality in Secondary Education Attainment and Real GDP per capita ")
    plt.yticks([0,5000,10000,15000,20000,25000,30000])
    plt.ylabel('GDP per Capita (Y)')
    plt.xticks([-3.5, -3,-2.5,-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5],rotation=45)
    plt.xlabel('Gender Inequality Differential in Secondary Education Attainment (Gi)')
    plt.grid(True)
    plt.show()


plot_regression(gender_ineq,gdp_per_cap)
plot_gdp_year(year,gdp_per_cap)
plot_gender_year(year,gender_ineq)
