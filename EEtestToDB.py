from requests_html import HTMLSession
import sqlite3
from sqlite3 import Error

def create_connection(db_path):
    conn = None
    try:
        conn =sqlite3.connect(db_path)
        return conn
    except Error as e:
        print(e)    
    return conn

def create_table(conn, table_sql):
    try:
        cur = conn.cursor()
        cur.execute(table_sql)
    except Error as e:
        print(e)


def add_flight(conn, flight_details):
    sql_insert_flight = """INSERT INTO tblFlights(flightno, origin, destination, estimated) VALUES (?,?,?,?)

                            """
    try:
        cur = conn.cursor()
        cur.execute(sql_insert_flight, flight_details)
        conn.commit()
    except Error as e:
        print(e)

db_path = r'C:\test\python\selenium\flights.db'

conn = create_connection(db_path)

sql_flight_table = """CREATE TABLE IF NOT EXISTS tblFlights(
                        id INTEGER PRIMARY KEY,
                        flightno text NOT NULL,
                        origin text NOT NULL,
                        destination text NOT NULL,
                        estimated text NOT NULL
                    )"""

if conn is not None:
    create_table(conn, sql_flight_table)    
    conn.close()

# create an HTML Session object
session = HTMLSession()

# Use the object above to connect to needed webpage
resp = session.get("https://www.adelaideairport.com.au/flight-information/flight-search/?flt_no=&carrier=All&city=&dte=Tomorrow&leg=")

# Run JavaScript code on webpage
resp.html.render()

# parse <span class="with-image"> elements containing airline names
airline_list = []
airline_spans = resp.html.find('.SearchResultFlightListRow')

airline_list = [span.text.split('\n') for span in airline_spans]

for flight in airline_list:
    if len(flight) == 7:
        flightno, origin, destination, scheduled, estimated, gate, status = flight 
    elif len(flight) == 6:
        flightno, origin, destination, scheduled, estimated, gate = flight 
        status = 'N/A'
    elif len(flight) == 5:
        flightno, origin, destination, scheduled, estimated = flight 
        gate = 'N/A'

    
    conn = create_connection(db_path)

    add_flight(conn, flight[:4])
    
    print (f'Flight no {flightno} from {origin} to {destination} is scheduled to depart at {scheduled} from gate {gate}')

if conn !=None:
    conn.close()