import psycopg2

HOST = "localhost"
DB_NAME = "naochallenge23"
USER = "postgres"
PASSWORD = "postgres"


class DB:
    def __init__(self):
        self.connection = psycopg2.connect(host=HOST, database=DB_NAME,
                                           user=USER, password=PASSWORD)
        with self.connection:
            with self.connection.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS Reports(
                        id SERIAL PRIMARY KEY,
                        date DATE NOT NULL UNIQUE,
                        temperature NUMERIC(5, 2) NOT NULL,
                        co2 NUMERIC(6),
                        humidity NUMERIC(3));""")

                print("Esito inizializzazione db:", cur.statusmessage)

    def save_report(self, report):
        with self.connection:
            with self.connection.cursor() as cur:
                print(report)
                cur.execute("""
                    INSERT INTO Reports(date, temperature, co2, humidity)
                    VALUES (%s, %s, %s, %s)""",
                            (report['date'], report['temperature'], report['co2'], report['humidity']))

                return cur.statusmessage

    def get_report(self, id):
        with self.connection:
            with self.connection.cursor() as cur:
                cur.execute("""
                    SELECT * FROM Reports
                    WHERE id = %s;""",
                            (id,))

                if (cur.rowcount == 0):
                    return {}
                for tupla in cur:
                    return {'id': tupla[0], 'date': tupla[1], 'temperature': tupla[2], 'co2': tupla[3], 'humidity': tupla[4]}

    def get_reports(self):
        with self.connection:
            with self.connection.cursor() as cur:
                data = []
                cur.execute("""SELECT * FROM Reports""")

                for tupla in cur:
                    data.append(
                        {'id': tupla[0], 'date': tupla[1], 'temperature': tupla[2], 'co2': tupla[3], 'humidity': tupla[4]})

                return data
