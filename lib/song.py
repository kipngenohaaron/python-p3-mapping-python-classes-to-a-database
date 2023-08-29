from config import CONN, CURSOR

class Song:
    pass
    def __init__(self, name, album):
        self.id = None  # Initialize instance variable 'id' as None
        self.name = name  # Assign the provided 'name' parameter to the instance variable 'name'
        self.album = album  # Assign the provided 'album' parameter to the instance variable 'album'

    @classmethod
    def create_table(cls):
        """
        Create the 'songs' table if it doesn't exist.
        """
        sql = """
          CREATE TABLE IF NOT EXISTS songs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            album TEXT
          )   
        """
        CURSOR.execute(sql)  # Execute the SQL query to create the table
        CONN.commit()  # Commit the transaction

    def save(self):
        """
        Save the song instance to the database.
        """
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?,?)
        """
        CURSOR.execute(sql, (self.name, self.album))  # Execute the SQL query with provided values
        CONN.commit()  # Commit the transaction

        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM songs").fetchone()[0]
        # Update the instance variable 'id' with the ID of the last inserted row

    @classmethod
    def create(cls, name, album):
        """
        Create a new song instance and save it to the database.
        """
        song = Song(name, album)  # Create a new Song instance with the provided parameters
        song.save()  # Save the song instance to the database
        return song  # Return the created song instance