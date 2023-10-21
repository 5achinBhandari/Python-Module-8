'''Write a program that asks the user to enter the ICAO codes of two airports.
The program prints out the distance between the two airports in kilometers. import mysql.connector'''

from geopy.distance import geodesic
import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="r00t",
    database="flight_game"
)
cursor = db.cursor()
airport1_icao = input("Enter the ICAO code of the first airport: ")
airport2_icao = input("Enter the ICAO code of the second airport: ")

cursor.execute(f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{airport1_icao}'")
airport1_coords = cursor.fetchone()

cursor.execute(f"select latitude_deg, longitude_deg from airport where ident = '{airport2_icao}'")
airport2_coords = cursor.fetchone()

if airport1_coords is None or airport2_coords is None:
    print("One or both airports not found in the database.")
else:
    # Extract latitude and longitude values
    lat1, lon1 = airport1_coords
    lat2, lon2 = airport2_coords

    # Calculate the distance between the two airports using Geopy
    airport1 = (lat1, lon1)
    airport2 = (lat2, lon2)
    distance_km = geodesic(airport1, airport2).kilometers

    print(f"The distance between two airports is approximately {distance_km:.2f} kilometers.")


db.close()
