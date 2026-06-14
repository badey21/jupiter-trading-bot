import os
import json
import http.client
import base58
from solana.rpc.api import Client
from solders.keypair import Keypair

# إعدادات
HELIUS_API_KEY = os.getenv('HELIUS_API_KEY')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
client = Client(f"https://mainnet.helius-rpc.com/?api-key={HELIUS_API_KEY}")
keypair = Keypair.from_bytes(base58.b58decode(PRIVATE_KEY))

def get_quote():
    conn = http.client.HTTPSConnection("quote-api.jup.ag")
    conn.request("GET", "/v6/quote?inputMint=So11111111111111111111111111111111111111112&outputMint=EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v&amount=1000000000")
    response = conn.getresponse()
    return json.loads(response.read().decode())

def main():
    print("جاري التحليل...")
    try:
        quote = get_quote()
        out_amount = int(quote.get('outAmount', 0))
        print(f"السعر الحالي: {out_amount}")
        
        if out_amount > 135000000:
            print("فرصة! جاري التنفيذ...")
            # هنا غنكملو كود التنفيذ لاحقاً
        else:
            print("لا توجد فرصة مربحة حالياً.")
    except Exception as e:
        print(f"حدث خطأ: {e}")

if __name__ == "__main__":
    main()
