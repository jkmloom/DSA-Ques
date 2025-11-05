# Using sqlite3 - a friendly database generally builtin Python

# official docs: https://docs.python.org/3/library/sqlite3.html#module-sqlite3
import sqlite3

db = "youtube_videos.db"

conn = sqlite3.connect(db) # connect sqlite3 to database 
cursor = conn.cursor() # create cursor - for direct interaction with the server

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL)
''')

def list_videos():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    if not tables:
        print("\nThe database is empty.\n")
    else:
        table_name = tables[0][0]
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        count = cursor.fetchone()[0]
        if count == 0:
            print(f"\nDatabase > Table > {table_name}: is empty.\n")
        else:
            cursor.execute("SELECT * FROM videos")
            for row in cursor.fetchall():
                print(row)

def add_videos(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()
    print("Video Added! :)")

def update_videos(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    conn.commit()
    print("Video Updated! :)")

def delete_videos(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()

def main():
    decor = "-"
    while True:
        print(f"{decor*29}\nYouTube Manager App | SQLite3\n{decor*29}")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Video")
        print("4. Delete Videos")
        print("5. Exit App")

        user_choice = input("Enter your choice: ")

        if user_choice == '1':
            list_videos()
        elif user_choice == '2':
            name = input("Enter YouTube video name: ")
            time = input("Enter video duration: ")
            add_videos(name, time)
        elif user_choice == '3':
            video_id = input("Enter video ID to update: ")
            name = input("Enter YouTube video name: ")
            time = input("Enter video duration: ")
            update_videos(video_id, name, time)
        elif user_choice == '4':
            video_id = input("Enter video ID to delete: ")
            delete_videos(video_id)
        elif user_choice == '5':
            exit()
        else:
            print("\nInvalid choice!\n")

    conn.close()

if __name__ == "__main__":
    main()