import psycopg2


# Connect to Chinook database #
connection = psycopg2.connect(database="chinook")

# Build cursor object of the database #
cursor = connection.cursor()

# Query 1 - select all records from the "Artist" table #
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select only the name column from the artist table #
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only the name Queen from the artist table #
# cursor.execute('SELECT * FROM "Artist" WHERE "Name"= %s', ["Queen"])

# Query 4 - select only ArtistId 51 from the artist table #
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId"= %s', [51])

# Query 5 - select only albums with ArtistId 51 from the album table #
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId"= %s', [51])

# Query 6 - select all tracks where composer is "Queen" from the track table #
# cursor.execute('SELECT * FROM "Track" WHERE "Composer"= %s', ["Queen"])

# Challenge #
# Query 7 - select only albums with ArtistId 51 from the album table #
# cursor.execute('SELECT * FROM "Album" WHERE "Name"= %s', ["Pink Floyd"])

# # Query 7 - select all tracks where composer is "Queen" from the track table #
# cursor.execute('SELECT * FROM "Track" WHERE "Composer"= %s', ["Pink Floyd"])

# Fetch the results (multiple) #
results = cursor.fetchall()

# Fetch the results (single) #
# results = cursor.fetchone()

# Close the connection #
connection.close()

# Print results #
for result in results:
    print(result)

