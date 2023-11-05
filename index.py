from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from google.cloud import vision

app = FastAPI()

@app.get("/upload-image/")
async def analyze_image(file: UploadFile = File(...)):
    
    # クライアントのインスタンスを生成
    client = vision.ImageAnnotatorClient()

    image_content = await file.read()

    # Vision AIが扱える画像データにする
    image = vision.Image(content=image_content)


    # テキスト検出を実行
    response = client.text_detection(image=image)

    # 検出されたテキストを出力
    texts = response.text_annotations
    rtn_texts = [{"description": text.description} for text in texts]

    return JSONResponse(content={"text": rtn_texts})