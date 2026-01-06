from flask import Flask, render_template, request
from lunar_python import Lunar, Solar
from datetime import datetime
import random

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

    # Weekday mapping to Traditional Chinese
    weekday_map = {
        0: '一', 1: '二', 2: '三', 3: '四', 
        4: '五', 5: '六', 6: '日'
    }
    weekday_zh = f"星期{weekday_map[current_date.weekday()]}"

    # Daily 4-character quotes
    daily_quotes = [
        "宜積極進取", "努力積極", "心想事成", "萬事如意",
        "步步高升", "財源廣進", "吉祥如意", "福壽安康",
        "大吉大利", "五福臨門", "招財進寶", "和氣生財",
        "金玉滿堂", "花開富貴", "國泰民安", "身體健康"
    ]
    daily_quote = random.choice(daily_quotes)

    # Lunar date formatting - use numeric month
    lunar_month_num = lunar.getMonth()
    lunar_day_chinese = lunar.getDayInChinese()
    
    # Convert month number to Chinese numerals
    month_chinese_map = {
        1: '一', 2: '二', 3: '三', 4: '四', 5: '五', 6: '六',
        7: '七', 8: '八', 9: '九', 10: '十', 11: '十一', 12: '十二'
    }
    lunar_month_chinese = month_chinese_map.get(lunar_month_num, str(lunar_month_num))
    lunar_date = f"農曆：{lunar_month_chinese}月{lunar_day_chinese}"
    lunar_date_short = f"{lunar_month_chinese}月{lunar_day_chinese}"  # Without prefix

    # Data for template
    context = {
        'year': current_date.year,
        'month': current_date.month,
        'day': f"{current_date.day:02d}",  # Zero-padded day
        'weekday_zh': weekday_zh,
        'daily_quote': daily_quote,
        'lunar_date': lunar_date,
        'lunar_date_short': lunar_date_short,
        'good_for': lunar.getDayYi()[:4],  # Limit to 4 items
        'bad_for': lunar.getDayJi()[:4],   # Limit to 4 items
    }

    return render_template('index.html', **context)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
