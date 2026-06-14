import os
import requests
import json

def get_quote():
    url = "https://quote-api.jup.ag/v6/quote"
    params = {
        'inputMint': 'So11111111111111111111111111111111111111112',
        'outputMint': 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v',
        'amount': '1000000000',
        'slippageBps': '50'
    }
    
    # هنا نستخدم وكيل وسيط (Proxy) لتجاوز حظر GitHub للـ DNS
    # إذا لم يعمل هذا الـ Proxy، يجب عليك شراء Proxy خاص بك من مواقع مثل BrightData أو Webshare
    proxies = {
        "http": "http://8.210.83.33:80",
        "https": "http://8.210.83.33:80",
    }
    
    response = requests.get(url, params=params, proxies=proxies, timeout=10)
    return response.json()

def main():
    print("--- محاولة الاتصال عبر Proxy ---")
    try:
        data = get_quote()
        print(f"تم بنجاح! الناتج هو: {data.get('outAmount')}")
    except Exception as e:
        print(f"فشل الاتصال عبر Proxy: {e}")

if __name__ == "__main__":
    main()
