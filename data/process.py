import cv2
import os


def extract_frames(video_path, output_dir, fps=10):
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Capture video from file
    cap = cv2.VideoCapture(video_path)
    video_fps = cap.get(cv2.CAP_PROP_FPS)  # Get the original video's FPS

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Total frames: {frame_count}, Video FPS: {video_fps}")

    # If video fps is lower than the target fps, extract every frame
    if video_fps <= fps:
        frame_interval = 1
    else:
        frame_interval = int(video_fps / fps)

    count = 0
    frame_id = 0

    while True:
        success, frame = cap.read()
        if not success:
            break

        # Check if this frame needs to be saved
        if count % frame_interval == 0:
            frame_filename = f"frame{frame_id:06d}.jpg"
            frame_path = os.path.join(output_dir, frame_filename)
            cv2.imwrite(frame_path, frame)
            frame_id += 1
            print(f"Saved {frame_path}")

        count += 1

    cap.release()
    print("Done extracting frames.")

if __name__ == "__main__":
    output = "/home/longma/MA-LMM/data/breakfast/frames/"
    dir = "/home/data2/BreakfastII_15fps_qvga_sync/"
    P = os.listdir(dir)
    for p in P:
        new_dir = "/home/data2/BreakfastII_15fps_qvga_sync/" + p + "/"
        cams = os.listdir(new_dir)
        for cam in cams:
            new_new_dir = new_dir + cam + "/"
            names = os.listdir(new_new_dir)
            for name in names:
                new_name = p + "-" + cam + "-" + name
                extract_frames(f'{new_new_dir}/{name}', f'{output}/{new_name.split(".")[0]}')
