from fastapi import FastAPI
from pydantic import BaseModel
import os, json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title='AI Saathi Kisan - Backend (Prototype)')

# Enable CORS for local demo
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
DATA_DIR = os.path.abspath(DATA_DIR)

class ChatReq(BaseModel):
    user_id: str
    message: str
    language: str = 'hi'  # 'hi'|'en'|'te' etc.

def read_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

# Simple mocks for weather and market queries
def get_mock_weather():
    return { "city": "DemoCity", "rain_prob": 0.35, "temp_c": 28 }

def get_market_price(city, crop):
    # read data/market.csv (simple CSV)
    import csv
    market_file = os.path.join(DATA_DIR, 'market.csv')
    try:
        with open(market_file, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['city'].lower() == city.lower() and row['crop'].lower() == crop.lower():
                    return row
    except FileNotFoundError:
        pass
    return {"city": city, "crop": crop, "price_per_quintal": "N/A"}

def build_prompt(message, weather, crop_rules=None):
    prompt = f"""You are AI Saathi Kisan, an expert agricultural assistant for smallholder farmers in India.
Keep answers short and actionable (3 sentences). Use weather context when relevant.

Weather: {weather}
Farmer asks: {message}

If the farmer mentions a crop, check crop rules and include a one-line recommendation."""
    if crop_rules:
        prompt += "\nCrop rules: " + str(crop_rules)
    return prompt

def call_openai_chat(prompt):
    # === STUBBED IMPLEMENTATION ===
    # Replace this function with real OpenAI API calls.
    # For demo/hackathon, we return deterministic helpful responses based on keywords.
    p = prompt.lower()
    if 'rain' in p or 'baarish' in p:
        return "Haan, kal halka baarish sambhav hai. Pani dekhkar irrigation adjust karein."
    if 'fertil' in p or 'khaad' in p:
        return "Mittii mein nitrogen kam hai — halka urea dene ka sujhav hai. 10-15 din baad phir check karein."
    if 'market' in p or 'daam' in p:
        return "Aaj mandi mein gehu ₹2350 per quintal dikha raha hai. Nearby mandi check karen."
    return "Yeh achha sawaal hai. Kripya crop aur location batayein taaki main specific salah de sakun."

@app.post('/api/chat')
async def chat(req: ChatReq):
    # Mock pipeline:
    # 1. Translate (mock) -> assume message is fine
    user_msg_en = req.message

    # 2. Fetch weather and crop rules
    weather = get_mock_weather()
    crop_rules = None
    # Attempt to find crop keyword from message (very simple)
    for crop in ['wheat','rice','maize','cotton','sugarcane','groundnut','soybean','millet','gehu']:
        if crop in user_msg_en.lower():
            # load crop rules if present
            try:
                crop_rules = read_json(os.path.join(DATA_DIR, 'crop_rules.json')).get(crop, None)
            except Exception:
                crop_rules = None
            break

    # 3. Build prompt and call AI (stub)
    prompt = build_prompt(user_msg_en, weather, crop_rules)
    reply = call_openai_chat(prompt)

    # 4. (Optional) Translate back to requested language - mocked as same
    return {"reply": reply, "weather": weather}

@app.get('/api/weather')
async def weather():
    return get_mock_weather()

@app.get('/api/market')
async def market(city: str = 'DemoCity', crop: str = 'wheat'):
    return get_market_price(city, crop)
