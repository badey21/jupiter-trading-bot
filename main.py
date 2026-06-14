import os
import requests
from solana.rpc.api import Client
from solders.keypair import Keypair
import base58

# 1. إعداد الاتصال باستخدام Secrets
client = Client(f"https://mainnet.helius-rpc.com/?api-key={os.getenv('HELIUS_API_KEY')}")
keypair = Keypair.from_bytes(base58.b58decode(os.getenv("PRIVATE_KEY")))

def get_quote():
    # جلب سعر الشراء (SOL -> USDC)
    url = "https://quote-api.jup.ag/v6/quote?inputMint=So11111111111111111111111111111111111111112&outputMint=EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v&amount=1000000000&slippageBps=50"
    return requests.get(url).json()

def execute_swap(quote_data):
    # تنفيذ عملية الـ Swap
    url = "https://quote-api.jup.ag/v6/swap"
    payload = {
        "quoteResponse": quote_data,
        "userPublicKey": str(keypair.pubkey()),
        "wrapAndUnwrapSol": True
    }
    return requests.post(url, json=payload).json()

def main():
    quote = get_quote()
    out_amount = int(quote['outAmount'])
    
    # حساب الربح: (الناتج - المبلغ الأصلي - رسوم تقديرية)
    # ملاحظة: 1000000000 هو 1 SOL، يجب تعديل الشرط حسب رأس مالك
    if out_amount > 135000000: 
        print(f"فرصة مربحة تم العثور عليها! الناتج: {out_amount}")
        swap = execute_swap(quote)
        print(f"تم تنفيذ الصفقة: {swap}")
    else:
        print(f"الربح غير كافٍ حالياً. الناتج: {out_amount}")

if __name__ == "__main__":
    main()
