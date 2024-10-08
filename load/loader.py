import csv, os, sys
import mysql.connector


def insert_species():
    """Read the species lookup file and insert the species"""
    try:
        conn = mysql.connector.connect(
            user=os.environ["DB_USER"],
            password = os.environ["DB_PASS"],
            database="bto_data"
        )
        insert_bird = (
            "INSERT INTO species_lookup (SPEC_CODE, ENGLISH_NAME, SCIENTIFIC_NAME, TAXONOMIC_RANK)"
            "VALUES (%s, %s, %s, %s)"
        )
        with open("./data/species_lookup.csv", encoding="cp1252") as species_file:
            cur = conn.cursor(buffered=True)
            species_read = csv.reader(
                species_file,
                delimiter=",",
                quotechar='"'
            )
            past_header = False
            for rownum, bird in enumerate(species_read):
                if past_header:
                    # print(f"{bird[0]}, {bird[1]}, {bird[2]}, {bird[3]}")
                    cur.execute(insert_bird, (bird[0], bird[1], bird[2], bird[3]))
                else:
                    past_header = True
            print(f"Loaded {rownum+1} species of bird")

            conn.commit()
            conn.close()
    except mysql.connector.Error as e:
        print(e)
    else:
        conn.close()

def insert_distributions():
    """Read the distributions file and insert the spots"""
    try:
        conn = mysql.connector.connect(
            user=os.environ["DB_USER"],
            password = os.environ["DB_PASS"],
            database="bto_data"
        )
        insert_distribution = (
            "INSERT INTO distributions (DATE_PERIOD, SEASON, SPEC_CODE, GRID_REF, ISLAND, RESOLUTION, N_TENKMS, STATUS)"
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        )
        with open("./data/distributions.csv", encoding="cp1252") as distributions_file:
            cur = conn.cursor(buffered=True)
            distributions_read = csv.reader(
                distributions_file,
                delimiter=",",
                quotechar='"'
            )
            for rownum, row in enumerate(distributions_read):
                commit_flag = rownum%1000
                if rownum > 0:
                    # print(row)
                    cur.execute(insert_distribution, (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
                elif commit_flag:
                    conn.commit()
            conn.commit()
            conn.close()
            print(f"Loaded {rownum+1} rows of distribution data")
    except mysql.connector.Error as e:
        print(e)
    else:
        conn.close()


insert_species()
insert_distributions()