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

    # Daily quote - Special handling for February 2026 (Year of the Horse)
    today = datetime.now()
    
    if today.year == 2026 and today.month == 2:
        # February 2026: Year of the Horse quotes (28 quotes for 28 days)
        february_quotes = [
            '龍馬精神',  # Feb 1
            '馬到成功',  # Feb 2
            '一馬當先',  # Feb 3
            '萬馬奔騰',  # Feb 4
            '駿馬騰飛',  # Feb 5
            '躍馬揚鞭',  # Feb 6
            '天馬行空',  # Feb 7
            '龍騰馬躍',  # Feb 8
            '馬年大吉',  # Feb 9
            '馬年發財',  # Feb 10
            '金馬迎春',  # Feb 11
            '福馬迎新',  # Feb 12
            '策馬前進',  # Feb 13
            '奔馬報喜',  # Feb 14
            '神馬獻瑞',  # Feb 15
            '汗馬功勞',  # Feb 16
            '馬鳴得意',  # Feb 17 (CNY)
            '馬到功成',  # Feb 18
            '馬騰盛世',  # Feb 19
            '千里良馬',  # Feb 20
            '龍精虎馬',  # Feb 21
            '馬到福至',  # Feb 22
            '迎春接馬',  # Feb 23
            '瑞馬呈祥',  # Feb 24
            '馬步青雲',  # Feb 25
            '捷報馬傳',  # Feb 26
            '順利馬年',  # Feb 27
            '順利馬年'   # Feb 28
        ]
        # Use day of month (1-28) as direct index (subtract 1 for 0-based array)
        day_index = today.day - 1
        daily_quote = february_quotes[day_index] if day_index < len(february_quotes) else february_quotes[0]
    else:
        # All other months: Use deterministic hash-based selection
        daily_quotes = [
            '吉祥如意', '萬事大吉', '心想事成', '五福臨門', '招財進寶',
            '和氣生財', '金玉滿堂', '花開富貴', '國泰民安', '身體健康',
            '步步高升', '大吉大利', '財源廣進', '恭喜發財', '年年有餘',
            '龍馬精神', '鴻運當頭', '福星高照', '萬事如意', '事事順心',
            '平安喜樂', '闔家歡樂', '福壽雙全', '福如東海', '壽比南山',
            '笑口常開', '青春永駐', '前程似錦', '錦繡前程', '鵬程萬里',
            '一帆風順', '馬到成功', '功成名就', '名列前茅', '出類拔萃',
            '學業進步', '才高八斗', '學富五車', '滿腹經綸', '博學多才',
            '事業有成', '飛黃騰達', '平步青雲', '扶搖直上', '蒸蒸日上',
            '日進斗金', '財運亨通', '生意興隆', '貨如輪轉', '客似雲來',
            '家和萬事興', '闔家平安', '天倫之樂', '其樂融融', '幸福美滿',
            '百年好合', '白頭偕老', '永結同心', '琴瑟和鳴', '鸞鳳和鳴',
            '喜氣洋洋', '春風得意', '眉開眼笑', '喜上眉梢', '喜氣盈門',
            '萬象更新', '欣欣向榮', '蓬勃發展', '日新月異', '與時俱進',
            '龍騰虎躍', '虎虎生威', '生龍活虎', '龍飛鳳舞', '龍鳳呈祥',
            '紫氣東來', '瑞氣千條', '祥雲繚繞', '福氣滿堂', '喜氣沖天',
            '四季平安', '歲歲平安', '出入平安', '一路平安', '竹報平安',
            '吉星高照', '福星拱照', '吉慶有餘', '吉人天相', '天賜良緣',
            '心曠神怡', '神采奕奕', '精神煥發', '容光煥發', '煥然一新',
            '如意吉祥', '稱心如意', '萬事勝意', '諸事大吉', '百事可樂',
            '六六大順', '七星高照', '八方來財', '九九歸一', '十全十美',
            '百福駢臻', '千祥雲集', '萬事亨通', '億萬富翁', '財源滾滾'
        ]
        
        # Deterministic quote selection based on current date
        date_string = f"{today.year}-{today.month}-{today.day}"
        hash_value = sum(ord(c) * (i + 1) for i, c in enumerate(date_string))
        quote_index = hash_value % len(daily_quotes)
        daily_quote = daily_quotes[quote_index]

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

    # Calculate day progress (0-100% from midnight to 11:59 PM)
    current_time = datetime.now()
    seconds_since_midnight = (current_time.hour * 3600 + 
                             current_time.minute * 60 + 
                             current_time.second)
    total_seconds_in_day = 24 * 3600
    day_progress = (seconds_since_midnight / total_seconds_in_day) * 100

    # Calculate countdown to Chinese New Year (Feb 17, 2026)
    cny_date = datetime(2026, 2, 17, 0, 0, 0)
    time_remaining = cny_date - current_time
    days_remaining = time_remaining.days
    hours_remaining = time_remaining.seconds // 3600
    minutes_remaining = (time_remaining.seconds % 3600) // 60
    seconds_remaining = time_remaining.seconds % 60
    # Target timestamp in milliseconds for JavaScript
    cny_timestamp = int(cny_date.timestamp() * 1000)

    # Detect night mode (8 PM - 7 AM)
    current_hour = current_time.hour
    is_night_mode = current_hour >= 20 or current_hour < 7

    # Data for template
    context = {
        'year': current_date.year,
        'month': current_date.month,
        'day': f"{current_date.day:02d}",  # Zero-padded day
        'weekday_zh': weekday_zh,
        'daily_quote': daily_quote,
        'lunar_date': lunar_date,
        'lunar_date_short': lunar_date_short,
        'good_for': lunar.getDayYi()[:3],  # Limit to 3 items
        'bad_for': lunar.getDayJi()[:3],   # Limit to 3 items
        'day_progress': round(day_progress, 2),  # Percentage of day elapsed
        'countdown_days': days_remaining,
        'countdown_hours': hours_remaining,
        'countdown_minutes': minutes_remaining,
        'countdown_seconds': seconds_remaining,
        'cny_timestamp': cny_timestamp,
        'is_night_mode': is_night_mode,
    }

    return render_template('index.html', **context)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
