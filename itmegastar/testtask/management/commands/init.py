from django.core.management.base import BaseCommand, CommandError
from psycopg2 import connect
from django.conf import settings
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Initializes PostgreSQL database'

    def recreate_db(self):
        dbname = settings.POSTGRESQL_DB['NAME']
        user = settings.POSTGRESQL_DB['USER']
        password = settings.POSTGRESQL_DB['PASSWORD']
        host = settings.POSTGRESQL_DB['HOST']
        port = settings.POSTGRESQL_DB['PORT']

        con = connect(dbname=dbname, user=user, password=password, host=host, port=port)
        # Позволяет удалять БД
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        cursor = con.cursor()

        cursor.execute(f'DROP DATABASE IF EXISTS {dbname}')
        cursor.execute(f'CREATE DATABASE {dbname}')
        cursor.execute(f'GRANT ALL PRIVILEGES ON DATABASE {dbname} TO {user}')

        con.close()

        call_command('makemigrations')
        call_command('migrate')

    def handle(self, *args, **options):
        call_command('makemigrations')
        call_command('migrate')
        call_command('loaddata', settings.TEST_TASK_FIXTURE)
