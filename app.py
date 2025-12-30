from flask import Flask, render_template, request
from lunar_python import Lunar, Solar
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    # Get date from query param or use today
    date_str = request.args.get('date')
    if date_str:
        try:
            current_date = datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            current_date = datetime.now()
    else:
        current_date = datetime.now()

    # Solar to Lunar
    solar = Solar.fromYmd(current_date.year, current_date.month, current_date.day)
    lunar = solar.getLunar()

    # Calculate Month Size (Big/Small)
    try:
        # Try to create the 30th day of this lunar month
        Lunar.fromYmd(lunar.getYear(), lunar.getMonth(), 30)
        month_size = "大" # Big (30 days)
    except Exception:
        month_size = "小" # Small (29 days)

    # Random Auspicious Quote
    quotes = [
        "财源广进", "生意兴隆", "五福临门", "大吉大利",
        "心想事成", "身体健康", "万事如意", "吉祥如意",
        "福寿安康", "步步高升", "招财进宝", "和气生财",
        "金玉满堂", "吉星高照", "花开富贵", "国泰民安"
    ]
    import random
    # Select 2 unique quotes
    random_quotes = random.sample(quotes, 2)

    # Data for template
    context = {
        'gregorian_date': current_date.strftime('%Y-%m-%d'),
        'year': current_date.year,
        'month': current_date.month, # Number (8)
        'month_name': current_date.strftime('%B'), # Full name (August)
        'day': current_date.day,
        'weekday': current_date.strftime('%A'),
        
        # Lunar Data
        'lunar_year_chinese': lunar.getYearInGanZhi() + ' (' + lunar.getYearShengXiao() + ')', # e.g. Bing-Yin (Tiger)
        'lunar_month_chinese': lunar.getMonthInChinese(),
        'lunar_month_size': month_size,
        'lunar_day_chinese': lunar.getDayInChinese(),
        'lunar_date_full': f"{lunar.getMonthInChinese()}月{lunar.getDayInChinese()}", # Requested format: Month + Day
        
        # Lucky/Unlucky
        'good_for': lunar.getDayYi(), # List
        'bad_for': lunar.getDayJi(),  # List
        
        # Solar Terms
        'solar_term': lunar.getJieQi(), 
        
        # Aesthetics helpers
        'season': get_season(current_date.month),
        
        # New Feature: List of quotes
        'random_quotes': random_quotes
    }

    return render_template('index.html', **context)

def get_season(month):
    if 3 <= month <= 5: return 'Spring'
    if 6 <= month <= 8: return 'Summer'
    if 9 <= month <= 11: return 'Autumn'
    return 'Winter'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
