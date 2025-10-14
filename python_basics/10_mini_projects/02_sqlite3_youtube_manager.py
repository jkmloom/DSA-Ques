import sqlite3

conn = sqlite3.connect("youtube_videos.db") # connect to the database
cursor = conn.cursor() # communicate directly to the database
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                duration TEXT NOT NULL
                )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name, duration):
    cursor.execute("INSERT INTO videos (name, duration) VALUES (?,?)", (name, duration))
    conn.commit()

def update_video(video_id, nwe_name, new_duration):
    cursor.execute("UPDATE videos SET name = ?, duraiton = ? WHERE id = ?", (new_duration, new_duration, video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()

def main():
    while True:
        print("---------\nYouTube Manager App with Database SQLITE3\n---------")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Video")
        print("5. Exit App")

        user_choice = input("Enter your choice: ")

        # should have used match-case but wanted to have variety in the mini projects hence, used if-else
        if user_choice == '1':
            list_videos()
        
        elif user_choice == '2':
            name = input("Ente the video name: ")
            duration = input("Enter video duration: ")
            add_video(name, duration)
        
        elif user_choice == '3':
            video_id = input("Enter video ID to update: ")
            name = input("Enter the video name: ")
            duration = input("Enter video duration: ")
            update_video(video_id, name, duration)

        elif user_choice == '4':
            video_id = input("Enter the video ID to delete: ")
            delete_video(video_id)
        
        elif user_choice == '5':
            break

        else:
            print("Invalid choice..!")
    
    conn.close() # for better memoy management

if __name__ == "__main__":
    main()