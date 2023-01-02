import click
import errno
import os
import pandas as pd
from sql_formatter.core import format_sql
import sqlparse

@click.command()
@click.option('--generate', '-g', help='Change TEXT to generate excel file into SQL insert')
@click.option('--outputdir', '-o', help='Change TEXT to create directory output file')
def main(generate, outputdir):
    try:
		# Validate generate file can not be None
        if generate is None:
            raise TypeError

		# Check if outputdir is not None
        if outputdir != None:
            try:
				# Create a directory
                os.makedirs(outputdir)
                outputdir = "{}/".format(outputdir)
            except OSError as exc:
				# If directory is exists use this directory
                if exc.errno == errno.EEXIST:
                        outputdir = "{}/".format(outputdir)
        file = pd.ExcelFile(generate)
        for sheet_name in file.sheet_names:
            data = file.parse(sheet_name)
            filename = "{}{}.sql".format(outputdir, sheet_name)
            click.echo("### {}:".format(filename))
            write_file = open(filename, "w")
            for i, _ in data.iterrows():
                field_names = ", ".join(list(data.columns))
                rows = list()
                #prdefined_cols = ['ID','FULLNAME','ADDRESS','IDENTITY_NUMBER','IDENTITY_TYPE','COUNTRY']
                prdefined_cols = ['ID','FULLNAME','ADDRESS','COUNTRY']
                #for column in data.columns:
                for column in prdefined_cols:
                    rows.append(str(data[column][i]))
                #names = ['Adam', 'Bob', 'Cyril']
                #text = f"Winners are:\n{'\n'.join(names)}"
                text = "'" + "', '".join(rows) + "'"
                text = text.replace(' ','\n')
                print(text)
                row_values = "'" + "', '".join(rows) + "'"
                #print(row_values)
                #click.echo("INSERT INTO {} ({}) VALUES ({});".format(sheet_name, field_names, row_values))
                #write_file.write("INSERT INTO {} ({}) VALUES ({});\n".format(sheet_name, field_names, row_values))
                query_temp = "INSERT INTO {} ({}) VALUES (\n{});".format(sheet_name, field_names, text) 
                #query_format = query_temp
                query_format = sqlparse.format(query_temp, keyword_case='upper', identifier_case='lower', reindent=True, wrap_after=1)
                click.echo("{}\n".format(query_format))
                write_file.write("{}\n".format(query_format))
            write_file.close()
    except TypeError as e:
        click.echo("Error: Unknown generate file! Type -h for help.")

if __name__ == "__main__":
    main()