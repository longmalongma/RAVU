import os


def extract_frames(dst_base_dir, src_base_dir, video_name, new_name, fps=10):
    video_id = new_name.split('.')[0]
    os.makedirs("{}/{}".format(dst_base_dir, video_id), exist_ok=True)
    cmd = 'ffmpeg -i \"{}/{}\" -vf scale=-1:256 -pix_fmt yuvj422p -q:v 1 -r {} -y \"{}/{}/frame%06d.jpg\"'.format(
        src_base_dir, video_name, fps, dst_base_dir, video_id, fps)
    os.system(cmd)
    
if __name__ == "__main__":
    output = "/home/longma/MA-LMM/data/breakfast/frames/"
    dir = "/home/data2/BreakfastII_15fps_qvga_sync/"
    
    P = os.listdir(dir)
    for p in P:
        new_dir = "/home/data2/BreakfastII_15fps_qvga_sync/" + p + "/"
        cams = os.listdir(new_dir)
        for cam in cams:
            new_new_dir = new_dir + cam
            names = os.listdir(new_new_dir)
            for name in names:
                if len(name.split('.')) != 2:
                    continue
                new_name = p + "-" + cam + "-" + name
                extract_frames(output, new_new_dir, name, new_name)