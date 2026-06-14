import os
import json
import urllib.request
import ssl

def get_quote():
    # هذا الرابط هو نفسه ولكن مكتوب بطريقة مباشرة
    url = "https://quote-api.jup.ag/v6/quote?inputMint=So11111111111111111111111111111111111111112&outputMint=EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v&amount=1000000000"
    
    # ننشئ سياق SSL يتجاهل كل شيء (أكثر تساهلاً من قبل)
    context = ssl._create_unverified_context()
    
    # نجهز الطلب بهوية المتصفح
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    with urllib.request.urlopen(req, context=context, timeout=10) as response:
        return json.loads(response.read().decode())

def main():
    print("--- محاولة جلب السعر عبر urllib ---")
    try:
        data = get_quote()
        out_amount = int(data.get('outAmount', 0))
        print(f"تم بنجاح! الناتج هو: {out_amount}")
    except Exception as e:
        print(f"فشل الاتصال: {e}")

if __name__ == "__main__":
    main()
