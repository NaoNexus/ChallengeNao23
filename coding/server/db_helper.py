import psycopg2
import config_helper
from datetime import datetime


class DB:
    def __init__(self, config: config_helper.Config):
        self.connection = psycopg2.connect(host=config.db_host, database=config.db_name,
                                           user=config.db_user, password=config.db_password)

        with self.connection:
            with self.connection.cursor() as cur:
                cur.execute('''
                    CREATE TABLE IF NOT EXISTS Reports(
                        id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
                        date TEXT NOT NULL UNIQUE,
                        temperature NUMERIC(5, 2) NOT NULL,
                        co2 NUMERIC(6),
                        humidity NUMERIC(3),
                        nPeople NUMERIC(4),
                        interiorLight NUMERIC(4),
                        exteriorLight NUMERIC(4));''')

                print('DB initialized:', cur.statusmessage)

    def save_report(self, report):
        with self.connection:
            with self.connection.cursor() as cur:
                if (report.get('date', '') == ''):
                    report['date'] = datetime.now().isoformat()

                if (report.get('id', '') == ''):
                    cur.execute('''
                        INSERT INTO Reports(date, temperature, co2, humidity, nPeople, interiorLight, exteriorLight)
                        VALUES (%s, %s, %s, %s, %s, %s, %s);''',
                                (report['date'], report['temperature'], report['co2'], report['humidity'], report.get('nPeople', 0), report.get('interiorLight', 0), report.get('exteriorLight', 0),))
                else:
                    cur.execute('''
                        UPDATE Reports
                        SET date = %s, temperature = %s, co2 = %s, humidity = %s, nPeople = %s, interiorLight = %s, exteriorLight = %s
                        WHERE id = %s
                        ORDER BY date;''',
                                (report['date'], report['temperature'], report['co2'], report['humidity'], report['nPeople'], report['interiorLight'], report['exteriorLight'], report['id']))

                return cur.statusmessage

    def get_report(self, id):
        with self.connection:
            with self.connection.cursor() as cur:
                cur.execute('''
                    SELECT * FROM Reports
                    WHERE id::text = %s
                    ORDER BY date;''',
                            (str(id),))

                if (cur.rowcount == 0):
                    return {}
                for tupla in cur:
                    return {'id': tupla[0], 'date': tupla[1], 'temperature': tupla[2], 'co2': tupla[3], 'humidity': tupla[4]}

    def get_reports(self):
        with self.connection:
            with self.connection.cursor() as cur:
                data = []
                cur.execute('''
                    SELECT * FROM Reports
                    ORDER BY date;''')

                for tupla in cur:
                    data.append(
                        {'id': tupla[0], 'date': tupla[1], 'temperature': tupla[2], 'co2': tupla[3], 'humidity': tupla[4]})

                return data
