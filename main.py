import click
from flask.cli import AppGroup
from dbfread import DBF
from app import create_app, db, cli


dbf_cli = AppGroup('dbf')

app = create_app()

@dbf_cli.command('read')
@click.argument('table')
def read_table(table):
    print(table.upper())
    dbf = DBF('../penjualan/DATA92016B/' + table.lower())
    for r in dbf:
        print(r)


app.cli.add_command(dbf_cli)
