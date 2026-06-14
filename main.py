import ssl
import os
import json
import urllib.request
import base58
from solana.rpc.api import Client
from solders.keypair import Keypair

# هذا السطر هو الحل الجذري لإلغاء قيود SSL التي تسبب الخطأ
ssl._create_default_https_context = ssl._create_unverified_context

# إعداد المحفظة والاتصال بـ Helius
HELIUS_API_KEY = os.getenv('HELIUS_API_KEY')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
client = Client(f"https://mainnet.helius-rpc.com/?api-key={HELIUS_API_KEY}")

def get_quote():
    # الرابط لجلب السعر (1 SOL إلى USDC)
    url = "https://quote-api.jup.ag/v6/quote?inputMint=So11111111111111111111111111111111111111112&outputMint=EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v&amount=1000000000"
    
    # استخدام urllib للاتصال بدون تعقيدات SSL
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode())

def main():
    print("--- بدأ فحص السوق ---")
    try:
        quote = get_quote()
        out_amount = int(quote.get('outAmount', 0))
        
        print(f"السعر الحالي (الناتج): {out_amount}")
        
        # شرط التنفيذ (عدل الرقم حسب هدفك)
        if out_amount > 135000000:
            print("فرصة مربحة تم اكتشافها! البدء في تنفيذ الصفقة...")
            # هنا سيتم إضافة كود الـ Swap لاحقاً بعد التأكد من أن الاتصال يعمل
        else:
            print("السوق حالياً غير مربح، سأحاول لاحقاً.")
            
    except Exception as e:
        print(f"حدث خطأ أثناء الاتصال: {e}")

if __name__ == "__main__":
    main()
