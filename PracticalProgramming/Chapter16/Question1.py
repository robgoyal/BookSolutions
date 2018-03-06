# Name: Question1.py
# Author: Robin Goyal
# Last-Modified: March 6, 2018
# Purpose: Solve challenges regarding population and land
#           area of Candian provinces and territories


import sqlite3


def main():

    # Create a new database called census.db
    con = sqlite3.connect("census.db")
    cur = con.cursor()

    # Create DENSITY table
    cur.execute("CREATE TABLE Density(Region TEXT, Population INTEGER, Area REAL)")

    # Populate table with data
    regions = [("Newfoundland and Labrador", 512930, 370501.69),
               ("Prince Edward Island", 135294, 5684.39),
               ("Nova Scotia", 908007, 52917.43),
               ("New Brunswick", 729498, 71355.67),
               ("Quebec", 7237479, 1357743.08),
               ("Ontario", 11410046, 907655.59),
               ("Manitoba", 1119583, 551937.87),
               ("Saskatchewan", 978933, 551937.87),
               ("Alberta", 2974807, 639987.12),
               ("British Columbia", 3907739, 926492.48),
               ("Yukon Territory", 28674, 474706.97),
               ("Northwest Territories", 37360, 1141108.37),
               ("Nunavut", 26745, 1925460.18)]

    for region in regions:
        cur.execute("INSERT INTO Density VALUES (?, ?, ?)", region)

    # Commit changes to database
    con.commit()

    # Retrieve all content from the table
    cur.execute("SELECT * FROM Density")

    # Retrieve the population column from the table
    cur.execute("SELECT Population FROM Density")

    # Retrieve provinces with populations less than 1 million
    cur.execute("SELECT Region FROM Density WHERE (Population < 1000000)")

    # Retrieve the provinces with populations less than 1 million or greater than 5 million
    cur.execute("SELECT Region FROM Density WHERE (Population < 1000000 OR Population > 5000000)")

    # Retrieve provinces with population between 1 and 5 million
    cur.execute("SELECT Region FROM Density WHERE Population BETWEEN 1000000 AND 5000000")

    # Retrieve populations of provinces with land area greater than 200000 square km
    cur.execute("SELECT Population FROM Density WHERE (Area > 200000)")

    # Retrieve provinces and population densities
    cur.execute("SELECT Region, Population / Area FROM Density")


if __name__ == "__main__":
    main()
