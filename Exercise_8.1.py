import mysql.connector


db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="r00t",
    database="flight_game"
)


cursor = db_connection.cursor()


icao_code = input("Enter the ICAO code of the airport: ")

try:

    query = "SELECT name, municipality FROM airport WHERE ident = %s"
    cursor.execute(query, (icao_code,))


    airport_info = cursor.fetchone()

    if airport_info:
        airport_name, location = airport_info
        print(f"Airport Name: {airport_name}")
        print(f"Location: {location}")
    else:
        print(f"No airport found with ICAO code {icao_code}")

except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:

    cursor.close()
    db_connection.close()


