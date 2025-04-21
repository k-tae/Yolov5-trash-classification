import os
import json

def convert_to_yolo_format(data):
    yolo_labels = []
    
    class_mapping = {"비닐류": "0", "유리병류": "1", "종이류": "2", "캔류": "3", "페트병류": "4"}
    
    for box in data["Bounding"]:
        if box["Drawing"] == "POLYGON":
            # POLYGON Drawing인 경우는 처리하지 않음
            continue
        elif box["Drawing"] == "BOX":
            # BOX Drawing인 경우 YOLO 레이블 생성
            x1, y1 = int(box["x1"]), int(box["y1"])
            x2, y2 = int(box["x2"]), int(box["y2"])
            
            # 이미지의 너비와 높이
            img_width = int(data["RESOLUTION"].split("*")[0])
            img_height = int(data["RESOLUTION"].split("*")[1])
            
            # YOLO 레이블 포맷: class x_center y_center width height
            x_center = (x1 + x2) / (2 * img_width)
            y_center = (y1 + y2) / (2 * img_height)
            box_width = (x2 - x1) / img_width
            box_height = (y2 - y1) / img_height

            yolo_label = f"{class_mapping.get(box['CLASS'], box['CLASS'])} {x_center:.6f} {y_center:.6f} {box_width:.6f} {box_height:.6f}"
            yolo_labels.append(yolo_label)
    
    return yolo_labels

def process_json_files(folder_path, output_folder):
    # 폴더 내의 모든 JSON 파일에 대해 처리
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            json_path = os.path.join(folder_path, filename)
            with open(json_path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
            
            # YOLO 포맷으로 변환
            yolo_labels = convert_to_yolo_format(data)
            
            # 출력 파일 경로 생성
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".txt")
            
            # 변환된 YOLO 레이블을 텍스트 파일로 저장
            with open(output_path, 'w', encoding='utf-8') as output_file:
                for label in yolo_labels:
                    output_file.write(label + '\n')
            
            print(f"YOLO labels saved to {output_path}.")

# JSON 파일이 있는 폴더 경로
json_folder_path = 'C:\\Users\\rnjsx\\Downloads\\yolov5-master\\yolov5-master\\data\\trash\\train\\labels'

# 출력 폴더 경로
output_folder_path = 'C:\\Users\\rnjsx\\Downloads\\yolov5-master\\yolov5-master\\data\\trash\\train\\labels'

# JSON 파일 처리 및 YOLO 레이블 생성
process_json_files(json_folder_path, output_folder_path)
