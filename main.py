import os
import json
import urllib.request
import ssl

def get_quote():
    # الرابط المباشر لـ Jupiter API
    url = "https://quote-api.jup.ag/v6/quote?inputMint=So11111111111111111111111111111111111111112&outputMint=EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v&amount=1000000000&slippageBps=50"
    
    # نستخدم سياق أمان لا يسبب تعارضاً مع خوادم GitHub
    context = ssl.create_default_context()
    
    # طلب البيانات بهوية متصفح لضمان عدم الحظر
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    with urllib.request.urlopen(req, context=context, timeout=15) as response:
        return json.loads(response.read().decode())

def main():
    print("--- بدأ فحص السوق ---")
    try:
        data = get_quote()
        out_amount = int(data.get('outAmount', 0))
        print(f"السعر الحالي (outAmount): {out_amount}")
        
        if out_amount > 135000000:
            print("فرصة مربحة! (هنا سنضع كود التنفيذ لاحقاً)")
        else:
            print("السوق هادئ حالياً.")
            
    except Exception as e:
        print(f"فشل الاتصال: {e}")

if __name__ == "__main__":
    main()
