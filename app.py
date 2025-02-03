from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()

# apiエンドポイント定義

# ありがとうございます
@app.get("/thanks")
def get_voice():
    audio_path = "voice/thanks.m4a"
    if os.path.exists(audio_path):
        return FileResponse(audio_path, media_type="audio/mpeg", filename="thanks.m4a")
    return {"error": "Audio file not found"}

# はい
@app.get("/hi")
def get_voice():
    audio_path = "voice/hi.m4a"
    if os.path.exists(audio_path):
        return FileResponse(audio_path, media_type="audio/mpeg", filename="hi.m4a")
    return {"error": "Audio file not found"}

# 置き配でお願いします
@app.get("/doorDelivery")
def get_voice():
    audio_path = "voice/doorDelivery.m4a"
    if os.path.exists(audio_path):
        return FileResponse(audio_path, media_type="audio/mpeg", filename="doorDelivery.m4a")
    return {"error": "Audio file not found"}

# 警察呼びますよ
@app.get("/police")
def get_voice():
    audio_path = "voice/police.m4a"
    if os.path.exists(audio_path):
        return FileResponse(audio_path, media_type="audio/mpeg", filename="police.m4a")
    return {"error": "Audio file not found"}

# 迷惑なんで
@app.get("/nuisance")
def get_voice():
    audio_path = "voice/nuisance.m4a"
    if os.path.exists(audio_path):
        return FileResponse(audio_path, media_type="audio/mpeg", filename="nuisance.m4a")
    return {"error": "Audio file not found"}

# 結構です
@app.get("/noThanks")
def get_voice():
    audio_path = "voice/noThanks.m4a"
    if os.path.exists(audio_path):
        return FileResponse(audio_path, media_type="audio/mpeg", filename="noThanks.m4a")
    return {"error": "Audio file not found"}