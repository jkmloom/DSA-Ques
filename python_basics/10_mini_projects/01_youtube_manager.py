# Managing YouTube Videos in a List (Dedicated File) through this Python Program

import json

youtube_data = "YouTube_DB.txt"

def load_data():
    try:
        with open(youtube_data, 'r') as file:
            test = json.load(file)
            # print(type(test))
            return test
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open(youtube_data, 'w') as file:
        json.dump(videos, file) # json.dump(what, where)

def list_all_videos(videos):
    videos_list = enumerate(videos, start=1)
    print('*'*90)
    for index, video in videos_list:
        print(f"{index}. {video['name']}, Duration: {video['duration']}")
    print('*'*90)

def add_video(videos):
    video_name = input("Enter video's name: ")
    video_duration = input("Enter Video's duration: ")
    videos.append({"name": video_name, "duration": video_duration})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    video_index = int(input("Enter the index value to update the video: "))
    if 1 <= video_index <= len(videos):
        video_name = input("Enter the new video name: ")
        video_duration = input("Enter the new video duration: ")
        videos[video_index - 1] = {'name': video_name, 'duration':video_duration}
        save_data_helper(videos)
    else:
        print("Invalid index selected..!")

def delete_videos(videos):
    list_all_videos(videos)
    video_index = int(input("Enter the index value to delete a video: "))
    if 1 <= video_index <= len(videos):
            del videos[video_index - 1]
            save_data_helper(videos)
    else:
            print("Invalid video selected..!")

def main():
    videos = load_data()

    while True:
        print("-----------------\n YOUTUBE MANAGER \n-----------------")
        print("Choose an option:\n----------------")
        print("1. List all YouTube videos")
        print("2. Add a Youtube video")
        print("3. Update a YouTube details")
        print("4. Delete a YouTube video")
        print("5. Exit the app")

        user_choice = input("Enter your choice: ")
        # print(videos)

        print("\n")
        match user_choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_videos(videos)
            case '5':
                exit()
            case _:
                print("Invalid choice..!")

if __name__ == "__main__":
    main()