import csv
import datetime
import logging
import pyodbc
import sys

# Setup database connection
db_file = sys.argv[1] # read database file from command-line argument
conn_str = (
    r'DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};'
    r'DBQ={}'.format(db_file)
)
cnxn = pyodbc.connect(conn_str)
cursor = cnxn.cursor()


# Clear existing data from fields we want to update
tables = ['Dictionary', 'Separators', 'Standardisation0', 'Standardisation1', 'Standardisation2', 'TimeIntervals']
for table in tables:
    cursor.execute(f'DELETE FROM {table}')
cnxn.commit()


# Convert dates to dates for use in the database
def fix_date(date):
    if date != '':
        return datetime.datetime.strptime(date, '%d/%m/%Y').date().strftime('%d/%m/%Y')


# Convert years to integers for use in the database 
def fix_year(year):
    return int(year)


# Update Dictionary
def update_dictionary():
    query = '''
    INSERT INTO Dictionary (Icd1, Icd2, DiagnosisText, Comments, YearStart, YearEnd, DateIn, UserIn, DateOut, UserOut)
    VALUES (?,?,?,?,?,?,?,?,?,?);
    '''

    with open(r'D:\dev\dictionary-builder\data\dictionary.csv', 'r') as input: # should use os.path.join
        dict=csv.reader(input)
        fields = next(dict)

        for row in dict:
            row[4] = fix_year(row[4])
            row[5] = fix_year(row[5])
            row[6] = fix_date(row[6])
            row[8] = fix_date(row[8])
            cursor.execute(query, row)


# Update Separators


# Update Standardisation0
def update_standardisation0():
    query = '''
    INSERT INTO Standardisation0 (MainKey, YearStart, YearEnd, DateIn, UserIn, Rank, FilterIn, FilterOut, ActionVar, Likelihood, Prompt, DateOut, UserOut, Comments, NoApplyForDT, AddResultInDT)
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);
    '''

    with open(r'D:\dev\dictionary-builder\data\separators0.csv', 'r') as input: # should use os.path.join
        dict=csv.reader(input)
        fields = next(dict)

        for row in dict:
            row[1] = fix_year(row[1])
            row[2] = fix_year(row[2])
            row[3] = fix_date(row[3])
            row[11] = fix_date(row[11])
            cursor.execute(query, row)

# Update Standardisation1
# Update Standardisation2
# Update TimeIntervals


# Main function
def main():
    """Main function to run the script."""
    try:
        # Call update functions
        update_dictionary()
        update_standardisation0()
        # Add more update functions as needed

        # Commit changes and close connection
        cnxn.commit()
        cnxn.close()

        # Log success message
        logging.info('Database updated successfully.')
    except Exception as e:
        # Log error message and exit
        logging.error(f'An error occurred: {e}')
        sys.exit(1)

# Run main function
if __name__ == '__main__':
    main()