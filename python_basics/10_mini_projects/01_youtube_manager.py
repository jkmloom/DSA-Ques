import json

yt_data = 'YouTube_DB.txt'

def load_data():
    try:
        with open(yt_data, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open(yt_data, 'w') as file:
        json.dump(videos, file) #(what_to_dump, where_to_dump)

def list_all_videos(videos):
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {videos}")

def add_video(videos):
    video_name = input("Enter video name: ")
    video_duration = input("Enter video duration: ")
    videos.append({'name': video_name, 'duration': video_duration})
    save_data_helper(videos)

def update_video(videos):
    pass

def delete_video(videos):
    pass

def main():
    videos = load_data()
    while True:
        print("---*---*---\n YouTube Manager\n---*---*---")
        print("Choose an option:\n")
        print("1. List all YouTube Videos")
        print("2. Add a YouTube Video")
        print("3. Update a YouTube Video Detail")
        print("4. Delete a YouTube Video")
        print("5. Exit the App")

        user_choice = input("Enter your choice: ")

        match user_choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid choice..!!")

if __name__ == "__main__":
    main()