
from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from PIL import Image
from fastapi.staticfiles import StaticFiles
from io import BytesIO


import google.generativeai as genai
GOOGLE_API_KEY = "AIzaSyCyq0jbEgSC9C-TykrFFVUK5_wQVhpjnS8"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

app = FastAPI()



templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/summarize")
async def summarize(request: Request, file: UploadFile = File(...)):
    image_data = await file.read()
    img = Image.open(BytesIO(image_data))
    summary = model.generate_content([img, "extract the data in the image and explain it in simple terms. explain complete document with side headings.don't give anything in bold"])
    return templates.TemplateResponse("result.html", {"request": request, "summary": summary.text})

