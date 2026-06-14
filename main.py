import os
import requests
from solana.rpc.api import Client
from solders.keypair import Keypair
from solders.transaction import VersionedTransaction
import base58

# إعداد الاتصال
client = Client(f"https://mainnet.helius-rpc.com/?api-key={os.getenv('HELIUS_API_KEY')}")
keypair = Keypair.from_bytes(base58.b58decode(os.getenv("PRIVATE_KEY")))

def get_quote(amount):
    """جلب أفضل عرض من Jupiter"""
    url = f"https://quote-api.jup.ag/v6/quote?inputMint=So11111111111111111111111111111111111111112&outputMint=EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v&amount={amount}&slippageBps=50"
    return requests.get(url).json()

def execute_swap(quote_data):
    """تنفيذ عملية البيع والشراء"""
    url = "https://quote-api.jup.ag/v6/swap"
    payload = {
        "quoteResponse": quote_data,
        "userPublicKey": str(keypair.pubkey()),
        "wrapAndUnwrapSol": True
    }
    response = requests.post(url, json=payload).json()
    return response # هنا كيرجع بيانات الصفقة اللي غنتسنيوها

def main():
    # 1. تحليل السوق
    print("جاري تحليل الفرص...")
    quote = get_quote(1000000000) # 1 SOL
    
    # 2. حساب الربح (مثلاً إذا كان السعر أكبر من X)
    out_amount = int(quote['outAmount'])
    if out_amount > 135000000: # شرط الربح (مثلاً)
        print(f"فرصة مربحة! جاري تنفيذ الصفقة بـ {out_amount}...")
        # swap = execute_swap(quote)
        # print("تمت الصفقة بنجاح!")
    else:
        print(f"لا توجد فرصة مربحة حالياً (الناتج: {out_amount/10**6}).")

if __name__ == "__main__":
    main()
