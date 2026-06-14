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
    # كنستعملو curl باش نتجاوزو كل مشاكل الـ SSL ديال بايثون
    url = "https://quote-api.jup.ag/v6/quote?inputMint=So11111111111111111111111111111111111111112&outputMint=EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v&amount=1000000000"
    
    # -k كيعني تجاهل الـ SSL
    # -s كيعني صامت (بدون إحصائيات)
    cmd = ["curl", "-sk", url]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return json.loads(result.stdout)

def main():
    try:
        print("جاري جلب السعر عبر curl...")
        quote = get_quote()
        out_amount = int(quote.get('outAmount', 0))
        print(f"السعر اللي وصل: {out_amount}")
        
        if out_amount > 135000000:
            print("فرصة ربح! غنكملو كود التنفيذ دابا...")
        else:
            print("السوق هادئ...")
            
    except Exception as e:
        print(f"خطأ: {e}")

if __name__ == "__main__":
    main()
