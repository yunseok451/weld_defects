import os
import json
from tqdm import tqdm

def convert_to_yolo_seg_format(data, class_mapping):
    if 'image_data' not in data or 'annotations' not in data:
        return []

    image_width = data['image_data']['width']
    image_height = data['image_data']['height']

    yolo_annotations = []

    for annotation in data['annotations']:
        if 'coordinate' not in annotation:
            continue
        
        polygon = annotation['coordinate']
        # Use 'class' as the primary key, if not present use 'case'
        # If 'class' is 'defect', use 'case', otherwise use 'class'
        class_name = annotation['case'] if annotation['class'] == 'defect' else annotation['class']

        if class_name not in class_mapping:
            continue

        class_id = class_mapping[class_name]

        # Compute bounding box
        x_min, y_min, x_max, y_max = min(polygon['x']), min(polygon['y']), max(polygon['x']), max(polygon['y'])
        width = x_max - x_min
        height = y_max - y_min
        x_center = (x_min + x_max) / 2
        y_center = (y_min + y_max) / 2

        # Normalize the bounding box coordinates
        x_center /= image_width
        y_center /= image_height
        width /= image_width
        height /= image_height

        # Normalize the polygon x, y values
        normalized_polygon_coords = []
        for x, y in zip(polygon['x'], polygon['y']):
            normalized_x = x / image_width
            normalized_y = y / image_height
            normalized_polygon_coords.extend([normalized_x, normalized_y])

        # 폴리곤의 첫 좌표만 다시 추가합니다.
        normalized_polygon_coords.extend(normalized_polygon_coords[:2])

        yolo_annotation = [class_id] + normalized_polygon_coords


        #yolo_annotation = [class_id] + normalized_polygon_coords
        yolo_annotations.append(yolo_annotation)

    return yolo_annotations

def process_json_files(input_directory, output_directory, class_mapping):
    os.makedirs(output_directory, exist_ok=True)

    for file_name in tqdm(os.listdir(input_directory), desc='Processing Files'):
        if not file_name.endswith('.json'):
            continue

        json_path = os.path.join(input_directory, file_name)

        with open(json_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

            yolo_annotations = convert_to_yolo_seg_format(data, class_mapping)

            if not yolo_annotations:
                continue

            output_filename = os.path.splitext(file_name)[0] + ".txt"
            output_path = os.path.join(output_directory, output_filename)

            with open(output_path, 'w') as output_file:
                for annotation in yolo_annotations:
                    output_file.write(" ".join(map(str, annotation)) + "\n")

input_directory = 'weld_rt/data_rt/json' # '경로'/json
output_directory = 'weld_rt/data_rt/labels' # '경로'/labels
#input_directory = 'C:/yolov5-master/utils/docker/json'
#output_directory = 'C:/yolov5-master/utils/docker/labels'

# @@
#VT인 경우
#class_mapping = {'normal': 0, 'porosity': 1, 'incomplete_penetration': 2, 'lack_of_fusion': 3, 'undercut': 4}
#RT인 경우
#class_mapping = {'normal': 0, 'porosity':1, 'lack of fusion': 2, 'crack': 3, 'slag inclusion': 4}
class_mapping = {'normal': 0, 'crack':1, 'porosity': 2, 'lack of fusion': 3, 'slag inclusion': 4}
process_json_files(input_directory, output_directory, class_mapping)