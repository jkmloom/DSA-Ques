import json

def load_data():
    try:
        with open("YouTube.txt", 'r') as file:
            test = json.load(file)
            print(type(test))
            return test
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open("YouTube.txt", 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    for index, video in enumerate(videos, start = 1):
        print(f"{index}. {video['name']}, Durarion: {'time'}")

def add_videos(videos):
    video_name = input("Enter video name: ")
    video_duraiton = input("Enter video duration: ")
    videos.append({'name': video_name, 'duration': video_duraiton})
    save_data_helper(videos)

def update_videos(videos):
    pass

def delete_videos(videos):
    pass


def main():
    videos = load_data()

    while True:
        print("\n YouTube Manager by @jkmloom\n Choose an option:\n")
        print("1. List all YouTube videos")
        print("2. Add YouTube video")
        print("3. Update a YouTube video detail/s.")
        print("4. Delete a YouTube video from list")
        print("5. Exit the app")

        user_choice = input("Enter your choice:\t")

        print(videos)

        match user_choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_videos(videos)
            case '3':
                update_videos(videos)
            case '4':
                update_videos(videos)
            case '5':
                break
            case _: # _ is used as the default case from other languages
                print("Invalid option..!")

if __name__ == "__main__":
    main()