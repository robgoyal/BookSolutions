# Name: Question2.py
# Author: Robin Goyal
# Last-Modified: March 6, 2018
# Purpose: Expand from Question1 to include information
#          about capitals for each province


import sqlite3


def main():

    # Connect to census.db table
    con = sqlite3.connect("census.db")
    cur = con.cursor()

    # Create Capitals Table
    cur.execute("CREATE TABLE Capitals (Region TEXT, Capital TEXT, Population INTEGER)")

    # Populate Capitals table with data
    regions = [("Newfoundland and Labrador", "St. John's", 172918),
               ("Prince Edward Island", "Charlottetown", 58358),
               ("Nova Scotia", "Halifax", 359183),
               ("New Brunswick", "Fredericton", 81346),
               ("Quebec", "Quebec City", 682757),
               ("Ontario", "Toronto", 4682896),
               ("Manitoba", "Winnipeg", 192800),
               ("Saskatchewan", "Regina", 192800),
               ("Alberta", "Edmonton", 937845),
               ("British Columbia", "Victoria", 311902),
               ("Yukon Territory", "Whitehorse", 21405),
               ("Northwest Territories", "Yellowknife", 16541),
               ("Nunavut", "Iqaluit", 5236)]

    for region in regions:
        cur.execute("INSERT INTO Capitals VALUES (?, ?, ?)", region)

    # Commit changes to database
    con.commit()

    # Retrieve all contents of table
    cur.execute("SELECT * FROM Capitals")

    # Retrieve Populations of Provinces and Capitals
    cur.execute("""SELECT Density.Population, Capitals.Population FROM Density INNER JOIN Capitals WHERE Density.Region = Capitals.Region""")

    # Retrieve province land areas whose capitals have populations greater than 100000
    cur.execute("""SELECT Area FROM Density INNER JOIN Capitals WHERE Density.Region = Capitals.Region AND Capitals.Population > 100000""")

    # Retrieve provinces with land densities less than two people per sq km
    # and capital city populations more than 500000
    cur.execute("""SELECT C.Region FROM Capitals AS C INNER JOIN Density AS D ON C.Region = D.Region WHERE (C.Population > 500000 AND (D.Population / D.Area) < 2)""")

    # Retrieve total land area of Canada
    cur.execute("""SELECT SUM(Population) FROM Density""")

    # Retrieve average capital city population
    cur.execute("""SELECT AVG(Population) FROM Capitals""")

    # Retreve lowest cpaital city population
    cur.execute("""SELECT MIN(Population) FROM Capitals""")

    # Retrieve highest province/territory population
    cur.execute("""SELECT MAX(Population) FROM Density""")

    # Retrieve provinces with land densities within 0.5 persons per sq km
    cur.execute("""SELECT A.Region, B.Region FROM Density AS A INNER JOIN Density AS B WHERE ABS((A.Population / A.Area) - (B.Population / B.Area)) <= 0.5 AND (A.Region < B.Region)""")


if __name__ == "__main__":
    main()
