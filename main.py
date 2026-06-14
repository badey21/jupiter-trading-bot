import urllib3
import os
import requests
from solana.rpc.api import Client
from solders.keypair import Keypair
import base58

# تعطيل تحذيرات الـ SSL باش ما يتبلوكا البوت
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# إعداد الاتصال باستخدام Secrets
HELIUS_API_KEY = os.getenv('HELIUS_API_KEY')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')

client = Client(f"https://mainnet.helius-rpc.com/?api-key={HELIUS_API_KEY}")
keypair = Keypair.from_bytes(base58.b58decode(PRIVATE_KEY))

def get_quote():
    # جلب السعر مع إضافة verify=False لتجاوز مشكل الـ SSL
    url = "https://quote-api.jup.ag/v6/quote?inputMint=So11111111111111111111111111111111111111112&outputMint=EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v&amount=1000000000&slippageBps=50"
    response = requests.get(url, verify=False)
    return response.json()

def execute_swap(quote_data):
    # تنفيذ الـ Swap مع verify=False
    url = "https://quote-api.jup.ag/v6/swap"
    payload = {
        "quoteResponse": quote_data,
        "userPublicKey": str(keypair.pubkey()),
        "wrapAndUnwrapSol": True
    }
    response = requests.post(url, json=payload, verify=False)
    return response.json()

def main():
    try:
        print("جاري جلب البيانات من Jupiter...")
        quote = get_quote()
        out_amount = int(quote.get('outAmount', 0))
        
        # شرط الربح (بدل الرقم حسب الهدف ديالك)
        if out_amount > 135000000: 
            print(f"فرصة مربحة! الناتج هو: {out_amount}")
            swap = execute_swap(quote)
            print(f"تم تنفيذ الصفقة: {swap}")
        else:
            print(f"السوق هادئ، الربح غير كافٍ حالياً. الناتج: {out_amount}")
            
    except Exception as e:
        print(f"وقع خطأ أثناء التشغيل: {e}")

if __name__ == "__main__":
    main()
