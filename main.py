import os
import json
import subprocess
import base58
from solana.rpc.api import Client
from solders.keypair import Keypair

# إعداد الاتصال
HELIUS_API_KEY = os.getenv('HELIUS_API_KEY')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
client = Client(f"https://mainnet.helius-rpc.com/?api-key={HELIUS_API_KEY}")
keypair = Keypair.from_bytes(base58.b58decode(PRIVATE_KEY))

def get_quote():
    url = "https://quote-api.jup.ag/v6/quote?inputMint=So11111111111111111111111111111111111111112&outputMint=EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v&amount=1000000000"
    
    # -sk : تجاوز SSL (k) وتشغيل صامت (s)
    # -H : إضافة هويّة "متصفح" باش ما يحبسناش Jupiter
    cmd = ["curl", "-sk", "-H", "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36", url]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except Exception as e:
        print(f"خطأ في curl: {e}")
        return None

def main():
    print("--- محاولة جلب السعر ---")
    data = get_quote()
    
    if data and 'outAmount' in data:
        out_amount = int(data['outAmount'])
        print(f"السعر اللي وصل: {out_amount}")
        
        if out_amount > 135000000:
            print("فرصة مربحة! جاهز للتنفيذ.")
        else:
            print("السوق حالياً غير مربح.")
    else:
        print("لم يتم الحصول على بيانات صحيحة من السيرفر.")

if __name__ == "__main__":
    main()
