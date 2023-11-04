from google.cloud import vision
with open("test-shiba-inu.jpg", "rb") as image_file:
    content = image_file.read()

# Vision AIが扱える画像データにする
image = vision.Image(content=content)

# ImageAnnotatorClientのインスタンスを生成
annotator_client = vision.ImageAnnotatorClient()
response_data = annotator_client.label_detection(image=image)
labels = response_data.label_annotations