import json

db_file = "YouTube.txt"

def load_data():
    try:
        with open(db_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open(db_file, 'w') as file:
        json.dump(videos, file) # syntax: json.dump(to_write, where_to)

def list_all_videos(videos):
    for index, video_name in enumerate(videos, start=1):
        print(f"{index}. {video_name}")

def add_video(videos):
    video_name = input("Enter video name: ")
    video_duration = input("Enter video duration: ")
    videos.append({'name':video_name}, {'duration':video_duration})
    save_data_helper(videos)

def update_video(videos):
    pass

def delete_video(videos):
    pass


def main():
    videos = load_data()
    while True:
        print("\n YouTube Manager \nChoose an option:")
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video detail")
        print("4. Delete a YouTube video")
        print("5. Exit the app")

        user_choice = int(input("Enter your choice: "))
        print(videos)

        match user_choice:
            case 1:
                list_all_videos(videos)
            case 2:
                add_video(videos)
            case 3:
                update_video(videos)
            case 4:
                delete_video(videos)
            case 5:
                break
            case _:
                print("Invalid Choice..!")

if __name__ == "__main__":
    main()