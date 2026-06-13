import requests
import urllib3
import ssl
from requests.adapters import HTTPAdapter

# 1. إعداد الـ Adapter باش يفرض استخدام TLS الحديث
class TLSAdapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        ctx.set_ciphers('DEFAULT@SECLEVEL=1') # خفض مستوى الأمان مؤقتاً لتجاوز البلوكاج
        kwargs['ssl_context'] = ctx
        return super(TLSAdapter, self).init_poolmanager(*args, **kwargs)

# 2. إعداد الـ Session
session = requests.Session()
session.mount('https://', TLSAdapter())
session.headers.update({
    'Host': 'quote-api.jup.ag',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
})

# 3. دالة تجربة الاتصال (بدون تعقيدات)
def test_connection():
    try:
        # استعملنا الـ IP المباشر اللي ديجا جربناه
        url = "https://104.21.75.158/v6/quote"
        params = {'inputMint': 'So11111111111111111111111111111111111111112', 'outputMint': 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v', 'amount': '100000000', 'slippageBps': 50}
        response = session.get(url, params=params, timeout=10, verify=False)
        print("اتصال ناجح! البيانات:", response.json())
    except Exception as e:
        print("خطأ لا يزال قائماً:", e)

test_connection()