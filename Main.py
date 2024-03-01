import os
import cv2

# This function extracts frames from video
# Input parameters: video path : Path of the video to be converted into frames
#                   output_directory : The directory into which the frames will be stored upon execution
def split_video_into_frames(video_path, output_directory):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Get the video's frames per second (fps)
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    frame_count = 0
    #start_frame = 150
    while True:
        # Read a frame from the video
        ret, frame = cap.read()

        # If there are no more frames, break from the loop
        if not ret:
            break
        
        # Save the frame as an image in the output directory
        frame_count += 1
        # If the frames are not in grayscale, convert them to grayscale frames
        if len(frame.shape) != 2:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_filename = os.path.join(output_directory, f"frame_{frame_count:04d}.png")
        cv2.imwrite(frame_filename, frame)

    # Release the video capture object
    cap.release()

# This function merges all the frames in a particular Folder into a video
# Input parameters: input_frames_directory : path to the directory containing the frames to be combined
#                   output_video_path : the path where the output video should be saved
#                   fps : the number of frames that have to be combined per second
def frames_to_video(input_frames_directory, output_video_path, fps):
    # Get the list of frame files in the input directory
    frame_files = sorted([f for f in os.listdir(input_frames_directory) if f.startswith("frame_")])

    # Read the first frame to get its size
    first_frame = cv2.imread(os.path.join(input_frames_directory, frame_files[0]))
    height, width = first_frame.shape[:2] 

    # Create a VideoWriter object to save the output video
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height), isColor=True)

    for frame_file in frame_files:
        # Read each frame and write it to the output video
        # print("In for loop")
        frame_path = os.path.join(input_frames_directory, frame_file)
        frame = cv2.imread(frame_path)
        out.write(frame)

    # Release the VideoWriter object
    out.release()

if __name__ == "__main__":
    # Specify the paths to the video file and the directory where you would like the frames to dumped at
    video_name = "corrupted_video.mp4"
    file_path = os.path.join(os.getcwd(), video_name)
    assert os.path.isfile(file_path), "wrong dir"
    base_path = './'
    video_pth = base_path + video_name
    output_dir = base_path + "Test_directory"
    
    split_video_into_frames(video_pth, output_dir)
    print("==================================== Video has been splitted into its corresponding frames ====================================")

    # Specify the path to the directory containing the frames, path to the output video file and the required fps of the video

    # input_frames_directory = r'C:\Users\Anirudh Koti\IPCV_TA\Mini_project_1\ManikaBatraTT1_corrupted_frames'
    # output_video_path = 'corrupt_video2.mp4'
    # fps = 25  # Adjust the frames per second as needed

    # frames_to_video(input_frames_directory, output_video_path, fps)
    # print("==================================== Video has been formed from its corresponding frames ====================================")