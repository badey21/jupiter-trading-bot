import os
import time
import requests
from solana.rpc.api import Client
from solders.keypair import Keypair
import base58

# إعداد الاتصال بالسيرفر
HELIUS_API_KEY = os.getenv('HELIUS_API_KEY')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
client = Client(f"https://mainnet.helius-rpc.com/?api-key={HELIUS_API_KEY}")
keypair = Keypair.from_bytes(base58.b58decode(PRIVATE_KEY))

def get_quote(amount):
    """جلب أفضل عرض من Jupiter"""
    url = f"https://quote-api.jup.ag/v6/quote?inputMint=So11111111111111111111111111111111111111112&outputMint=EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v&amount={amount}&slippageBps=50"
    response = requests.get(url)
    return response.json()

def execute_swap(quote_data):
    """تنفيذ الصفقة"""
    url = "https://quote-api.jup.ag/v6/swap"
    payload = {
        "quoteResponse": quote_data,
        "userPublicKey": str(keypair.pubkey()),
        "wrapAndUnwrapSol": True
    }
    response = requests.post(url, json=payload)
    return response.json()

def main():
    print("البوت بدأ العمل... مراقبة مستمرة 24/7")
    while True: # هاد الحلقة هي اللي كتخليه يشري ويبيع بلا توقف
        try:
            # 1 SOL كمثال للتجربة
            quote = get_quote(1000000000) 
            
            # شرط الربح (بدل الرقم بـ الهدف ديالك)
            if int(quote.get('outAmount', 0)) > 135000000:
                print("تم اكتشاف فرصة ربح! جاري التنفيذ...")
                swap_result = execute_swap(quote)
                print(f"تمت الصفقة: {swap_result}")
            else:
                print(f"السوق غير مربح حالياً: {quote.get('outAmount', 0)}")
            
            time.sleep(2) # كيتسنى 2 ثواني باش ما يتبلوكاش الـ API
            
        except Exception as e:
            print(f"خطأ: {e}. جاري المحاولة مرة أخرى...")
            time.sleep(5)

if __name__ == "__main__":
    main()
