import os
import json
import httpx
from solana.rpc.api import Client
import base58

# إعدادات
HELIUS_API_KEY = os.getenv('HELIUS_API_KEY')
# ملاحظة: سنعتمد على httpx لأنه يدعم اتصالات أكثر استقراراً
def get_quote():
    url = "https://quote-api.jup.ag/v6/quote"
    params = {
        'inputMint': 'So11111111111111111111111111111111111111112',
        'outputMint': 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v',
        'amount': '1000000000',
        'slippageBps': '50'
    }
    headers = {"User-Agent": "Mozilla/5.0"}
    
    # استخدام httpx مع تعطيل التحقق من الشهادات
    with httpx.Client(verify=False) as client:
        response = client.get(url, params=params, headers=headers, timeout=10.0)
        return response.json()

def main():
    print("--- محاولة فحص السوق ---")
    try:
        data = get_quote()
        out_amount = int(data.get('outAmount', 0))
        print(f"السعر الحالي: {out_amount}")
    except Exception as e:
        print(f"حدث خطأ: {e}")

if __name__ == "__main__":
    main()
