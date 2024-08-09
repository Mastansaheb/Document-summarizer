



import google.generativeai as genai
GOOGLE_API_KEY = "AIzaSyCyq0jbEgSC9C-TykrFFVUK5_wQVhpjnS8"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')



from PIL import Image





def Summarize(img):
    summary = model.generate_content([img, "extract the data in the image and explain it in simple terms. explain complete document with side headings. dont give anything in bold font."])
    return summary
output = Summarize(img)