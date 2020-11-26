def create_image_annotation(file_name, width, height, image_id):
    file_name = file_name.split('/')[-1] # ~~~.jpg가 file_name이 되도록 문자열 split
    images = {
        'file_name': file_name,
        'height': height,
        'width': width,
        'id': image_id
    }
    return images

def create_annotation_yolo_format(min_x, min_y, width, height, image_id, category_id, annotation_id):
    bbox = (min_x, min_y, width, height)
    area = width * height

    annotation = {
        'id': annotation_id,
        'image_id': image_id,
        'bbox': bbox,
        'area': area,
        'iscrowd': 0,
        'category_id': category_id,
        'segmentation': []
    }

    return annotation

# Create the annotations of the ECP dataset (Coco format)
coco_format = {
    "images": [
        {
        }
    ],
    "categories": [

    ],
    "annotations": [
        {
        }
    ]
}
