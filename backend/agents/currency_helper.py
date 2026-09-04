"""
Country and Currency Helper for Multi-Agent Strategy Platform.
Provides country-to-currency mapping, exchange rate estimation, and localization formatting.
"""

COUNTRY_CURRENCY_MAP = {
    "india": {"symbol": "₹", "code": "INR", "name": "Indian Rupee", "rate": 85.0},
    "bharat": {"symbol": "₹", "code": "INR", "name": "Indian Rupee", "rate": 85.0},
    "united states": {"symbol": "$", "code": "USD", "name": "US Dollar", "rate": 1.0},
    "usa": {"symbol": "$", "code": "USD", "name": "US Dollar", "rate": 1.0},
    "us": {"symbol": "$", "code": "USD", "name": "US Dollar", "rate": 1.0},
    "global": {"symbol": "$", "code": "USD", "name": "US Dollar", "rate": 1.0},
    "united kingdom": {"symbol": "£", "code": "GBP", "name": "British Pound", "rate": 0.78},
    "uk": {"symbol": "£", "code": "GBP", "name": "British Pound", "rate": 0.78},
    "great britain": {"symbol": "£", "code": "GBP", "name": "British Pound", "rate": 0.78},
    "england": {"symbol": "£", "code": "GBP", "name": "British Pound", "rate": 0.78},
    "germany": {"symbol": "€", "code": "EUR", "name": "Euro", "rate": 0.92},
    "france": {"symbol": "€", "code": "EUR", "name": "Euro", "rate": 0.92},
    "italy": {"symbol": "€", "code": "EUR", "name": "Euro", "rate": 0.92},
    "spain": {"symbol": "€", "code": "EUR", "name": "Euro", "rate": 0.92},
    "netherlands": {"symbol": "€", "code": "EUR", "name": "Euro", "rate": 0.92},
    "europe": {"symbol": "€", "code": "EUR", "name": "Euro", "rate": 0.92},
    "eu": {"symbol": "€", "code": "EUR", "name": "Euro", "rate": 0.92},
    "canada": {"symbol": "CA$", "code": "CAD", "name": "Canadian Dollar", "rate": 1.35},
    "australia": {"symbol": "AU$", "code": "AUD", "name": "Australian Dollar", "rate": 1.52},
    "japan": {"symbol": "¥", "code": "JPY", "name": "Japanese Yen", "rate": 155.0},
    "china": {"symbol": "¥", "code": "CNY", "name": "Chinese Yuan", "rate": 7.20},
    "united arab emirates": {"symbol": "AED ", "code": "AED", "name": "UAE Dirham", "rate": 3.67},
    "uae": {"symbol": "AED ", "code": "AED", "name": "UAE Dirham", "rate": 3.67},
    "dubai": {"symbol": "AED ", "code": "AED", "name": "UAE Dirham", "rate": 3.67},
    "singapore": {"symbol": "S$", "code": "SGD", "name": "Singapore Dollar", "rate": 1.34},
    "switzerland": {"symbol": "CHF ", "code": "CHF", "name": "Swiss Franc", "rate": 0.88},
    "saudi arabia": {"symbol": "SAR ", "code": "SAR", "name": "Saudi Riyal", "rate": 3.75},
    "brazil": {"symbol": "R$", "code": "BRL", "name": "Brazilian Real", "rate": 5.50},
    "mexico": {"symbol": "MX$", "code": "MXN", "name": "Mexican Peso", "rate": 19.50},
    "south africa": {"symbol": "R ", "code": "ZAR", "name": "South African Rand", "rate": 18.20},
    "nigeria": {"symbol": "₦", "code": "NGN", "name": "Nigerian Naira", "rate": 1500.0},
    "indonesia": {"symbol": "Rp ", "code": "IDR", "name": "Indonesian Rupiah", "rate": 15800.0},
    "malaysia": {"symbol": "RM ", "code": "MYR", "name": "Malaysian Ringgit", "rate": 4.40},
    "philippines": {"symbol": "₱", "code": "PHP", "name": "Philippine Peso", "rate": 58.0},
    "vietnam": {"symbol": "₫", "code": "VND", "name": "Vietnamese Dong", "rate": 25000.0},
    "south korea": {"symbol": "₩", "code": "KRW", "name": "South Korean Won", "rate": 1350.0},
    "korea": {"symbol": "₩", "code": "KRW", "name": "South Korean Won", "rate": 1350.0},
    "sweden": {"symbol": "kr ", "code": "SEK", "name": "Swedish Krona", "rate": 10.50},
    "norway": {"symbol": "kr ", "code": "NOK", "name": "Norwegian Krone", "rate": 10.80},
    "denmark": {"symbol": "kr ", "code": "DKK", "name": "Danish Krone", "rate": 6.85},
    "poland": {"symbol": "zł ", "code": "PLN", "name": "Polish Zloty", "rate": 3.95},
    "new zealand": {"symbol": "NZ$", "code": "NZD", "name": "New Zealand Dollar", "rate": 1.65},
    "pakistan": {"symbol": "₨ ", "code": "PKR", "name": "Pakistani Rupee", "rate": 278.0},
    "bangladesh": {"symbol": "৳", "code": "BDT", "name": "Bangladeshi Taka", "rate": 120.0},
    "egypt": {"symbol": "E£ ", "code": "EGP", "name": "Egyptian Pound", "rate": 48.0},
    "turkey": {"symbol": "₺", "code": "TRY", "name": "Turkish Lira", "rate": 34.0}
}

def get_country_currency_info(country: str) -> dict:
    if not country or not isinstance(country, str):
        return COUNTRY_CURRENCY_MAP["global"]
        
    c_lower = country.strip().lower()
    
    if c_lower in COUNTRY_CURRENCY_MAP:
        return COUNTRY_CURRENCY_MAP[c_lower]
        
    for k, v in COUNTRY_CURRENCY_MAP.items():
        if k in c_lower or c_lower in k:
            return v
            
    return {"symbol": "$", "code": "USD", "name": "US Dollar", "rate": 1.0}

def format_country_amount(amount: float, country: str) -> str:
    curr = get_country_currency_info(country)
    return f"{curr['symbol']}{int(amount):,}"
