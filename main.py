import os
import requests
import json

def get_quote():
    # استخدام الـ IP المباشر لسيرفرات Jupiter لتجاوز الـ DNS المعطل
    url = "https://104.18.25.132/v6/quote"
    params = {
        'inputMint': 'So11111111111111111111111111111111111111112',
        'outputMint': 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v',
        'amount': '1000000000'
    }
    headers = {
        "Host": "quote-api.jup.ag",
        "User-Agent": "Mozilla/5.0"
    }
    
    # تعطيل التحقق من الشهادة (verify=False) للعمل عبر الـ IP
    response = requests.get(url, params=params, headers=headers, verify=False, timeout=10)
    return response.json()

def main():
    print("--- محاولة الاتصال عبر IP مباشر ---")
    try:
        data = get_quote()
        out_amount = int(data.get('outAmount', 0))
        print(f"تم بنجاح! السعر هو: {out_amount}")
    except Exception as e:
        print(f"فشل الاتصال: {e}")

if __name__ == "__main__":
    main()
