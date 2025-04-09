import os


def extract_frames(dst_base_dir, src_base_dir, video_name, fps=10):
    video_id = video_name.split('.')[0]
    os.makedirs("{}/{}".format(dst_base_dir, video_id), exist_ok=True )
    cmd = 'ffmpeg -i \"{}/{}\" -vf scale=-1:256 -pix_fmt yuvj422p -q:v 1 -r {} -y \"{}/{}/frame%06d.jpg\"'.format(
        src_base_dir, video_name, fps, dst_base_dir, video_id, fps)
    os.system(cmd)
    
if __name__ == "__main__":
    #output = "/home/longma/MA-LMM/data/msrvtt/frames/"
    #dir = "/home/data2/msrvttTrainValVideo/"
    
    #video_name = os.listdir(dir)
    #for name in video_name:
        #extract_frames(output, dir, name)
        
    #output = "/home/longma/MA-LMM/data/msrvtt/frames/"
    #dir = "/home/data2/msrvttTestVideo/"
    
    #video_name = os.listdir(dir)
    #for name in video_name: 
        #extract_frames(output, dir, name)
        
    output = "/home/data1/lvu_frames/"
    dir = "/home/data1/lvuvideos/"
    
    for set in os.listdir(dir):
        extract_frames(output, os.path.join(dir), set)
    print(len(os.listdir(dir)))