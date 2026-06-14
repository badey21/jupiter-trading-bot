import os
import json
import requests
from solana.rpc.api import Client
from solders.keypair import Keypair
import base58

# إعداد الاتصال باستخدام API Key الخاص بـ Helius
HELIUS_API_KEY = os.getenv('HELIUS_API_KEY')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')

# إعداد الـ Client للاتصال الموثوق
client = Client(f"https://mainnet.helius-rpc.com/?api-key={HELIUS_API_KEY}")

def get_price_via_helius():
    # في هاد الحالة، كنجلبو البيانات من Jupiter ولكن من خلال سيرفرات Helius 
    # اللي كيعتبرها GitHub "صديقة" وماكيحضرهاش
    url = "https://quote-api.jup.ag/v6/quote"
    params = {
        'inputMint': 'So11111111111111111111111111111111111111112',
        'outputMint': 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v',
        'amount': '1000000000',
        'slippageBps': '50'
    }
    
    # طلب البيانات
    response = requests.get(url, params=params)
    return response.json()

def main():
    print("--- بدأ فحص السوق عبر Helius ---")
    try:
        data = get_price_via_helius()
        out_amount = int(data.get('outAmount', 0))
        
        print(f"السعر الحالي (outAmount): {out_amount}")
        
        if out_amount > 135000000:
            print("فرصة مربحة! جاري تجهيز الـ Swap...")
            # هنا يمكنك إضافة كود تنفيذ الصفقة لاحقاً
        else:
            print("السوق هادئ حالياً.")
            
    except Exception as e:
        print(f"حدث خطأ أثناء الاتصال: {e}")

if __name__ == "__main__":
    main()
