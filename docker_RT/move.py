import glob
import os
import shutil

# 이미지 폴더 경로
image_folder = "C:/Users/bigdata01/Desktop/docker_RT/test/images/05"
# JSON 폴더 경로
json_folder = "C:/Users/bigdata01/Desktop/docker_RT/test//json/"
# 이동할 폴더 경로
destination_folder = "C:/Users/bigdata01/Desktop/docker_RT/test/validation"

# JSON 폴더 내 파일 목록 가져오기
json_files = glob.glob(os.path.join(json_folder, "*.json"))

# JSON 파일을 찾아서 이동
for json_file in json_files:
    # JSON 파일의 이름
    json_name = os.path.splitext(os.path.basename(json_file))[0]
    # 해당 JSON 파일에 대응하는 이미지 파일 경로
    image_file = os.path.join(image_folder, json_name + ".jpg")
    
    # 이미지 파일이 존재하면 이동
    if os.path.exists(image_file):
        # 이동할 파일의 경로
        destination_file = os.path.join(destination_folder, os.path.basename(json_file))
        # 폴더가 없다면 생성
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        # 파일 이동
        shutil.move(json_file, destination_file)
        #print(f"Moved {json_file} to {destination_file}")
