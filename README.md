# Lakjit (曆日) - Modern Traditional Chinese Calendar

A beautiful, modern web application that displays traditional Chinese calendar information with a minimalist aesthetic. Lakjit combines the wisdom of lunar calendars with contemporary design.

## 🌟 Features

### Core Calendar Features
- **Real-time Date Display**: Large, prominent date display with automatic updates
- **Lunar Calendar Integration**: Shows lunar month and day in Traditional Chinese
- **Weekday Display**: Current day of the week in Chinese
- **Chinese New Year Countdown**: Real-time countdown to CNY 2026 (Feb 17)
  - After CNY: Displays festive greeting "Lak-Jit恭祝大家 恭喜發財！萬事如意！馬年行大運"

### Daily Auspicious Activities (宜忌)
- **Yi (宜)**: 3 auspicious activities for the day
- **Ji (忌)**: 3 activities to avoid
- **Icon Display**: Red circle icon for Yi, gray circle icon for Ji
- **Inline Layout**: Activities displayed side-by-side with pipe separator

### Daily Quote System
- **100+ Traditional Quotes**: Curated collection of 4-character Chinese blessings
- **Deterministic Selection**: Same quote for everyone on the same date
- **Special February 2026**: 28 unique "Year of the Horse" themed quotes
  - Feb 1: 龍馬精神
  - Feb 17 (CNY): 馬年新禧
  - Feb 28: 順利馬年
- **Refresh-Proof**: Quote remains consistent across page refreshes

### Lucky Number Feature
- **Subtle Shimmer Effect**: Gold gradient sweep across daily quote (5s cycle, rounded corners)
- **Interactive Hint**: "點擊驚喜" caption below quote (fades after first click)
- **Slot Machine Animation**: Numbers scroll for 1 second before revealing
- **Random Generation**: Two 4-digit numbers (0000-9999) with proper padding
- **Auto-Close**: Modal disappears after 10 seconds
- **Touch & Click**: Works on both desktop and mobile devices
- **Refined Spacing**: Tight, clean layout with optimized padding

### Lunar Notification Banner
- **Smart Date Detection**: Triggers for 初一 and 初十五
  - T-minus 2 days: "提醒：2天後是初一/初十五"
  - T-minus 1 day: "提醒：明天是初一/初十五"
- **Incense Icons**: 
  - Day mode: Dark incense icon
  - Night mode: White incense icon
- **Dismissible**: Close button with localStorage memory
- **Fade-in Animation**: Smooth 0.5s entrance

### Visual Enhancements
- **Cherry Blossom Animation**: 18 falling sakura petals
  - Day mode: Soft pink (#FFD1DC)
  - Night mode: Deep rose (#E0115F with transparency)
  - CSS-only for optimal performance
  - Gentle sway and rotation effects
- **Background**: Vintage paper texture
- **Night Mode** (8 PM - 7 AM):
  - Dark charcoal background
  - Soft off-white text (#E0E0E0)
  - 60% brightness filter
  - Automatic icon switching
  - Smooth 1-second transitions

### Share as Image Feature
- **4:5 Aspect Ratio**: Perfect for social media (1080x1350px)
- **High Quality**: 2x scale PNG export
- **Smart Content**: Includes date, quote, and activities
- **Excludes UI**: No footer, progress bar, or share button in image
- **Theme Aware**: Captures current day/night mode styling
- **One-Click Download**: Auto-saves as `Lakjit-Calendar-[Date].png`

### Progressive Web App (PWA)
- **Installable**: Add to home screen on mobile and desktop
- **Offline Support**: Works without internet connection
- **Cache-First Strategy**: Instant loading after first visit
- **Service Worker**: Caches all static assets and resources
- **Manifest**: Standalone app experience with custom icons
- **Mobile Install Button**: Shows only on mobile devices (≤768px)
- **iOS Support**: Manual "Add to Home Screen" instructions
- **Auto-Update**: Updates automatically when online

### Progress & Indicators
- **Day Progress Bar**: Visual indicator of day completion (0-100%)
- **Breathing Animation**: Subtle pulsing effect (day mode only)
- **Night Mode Opacity**: 50% opacity for softer appearance

## 🎨 Design Philosophy

- **Minimalist Aesthetic**: Clean, uncluttered interface
- **100vh Layout**: No scrolling, everything fits on one screen
- **Traditional Chinese**: All text in Traditional Chinese characters
- **Noto Sans TC Font**: Professional, readable typography
- **Responsive Design**: Works on desktop and mobile devices
- **Accessibility**: Proper ARIA labels and semantic HTML

## 🛠️ Technology Stack

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with animations
- **JavaScript**: Client-side interactivity
- **lunar-javascript**: Lunar calendar calculations
- **html2canvas**: Image generation for sharing

### Backend
- **Python 3**: Server-side logic
- **Flask**: Lightweight web framework
- **lunar-python**: Lunar calendar library

### SEO & Performance
- **Meta Tags**: Comprehensive SEO optimization
- **Open Graph**: Rich social media previews
- **Sitemap.xml**: Daily update frequency
- **Robots.txt**: Search engine friendly
- **Favicon**: Custom Lak-Jit branding

## 📁 Project Structure

```
lakjit/
├── app.py                 # Flask application
├── index.html            # Static HTML version
├── templates/
│   └── index.html        # Flask template
├── static/
│   ├── style.css         # Main stylesheet
│   ├── background.jpg    # Day mode background
│   ├── background-night.jpg  # Night mode background
│   ├── yi-icon.png       # Gray Ji icon (忌)
│   ├── ji-icon.png       # Red Yi icon (宜)
│   ├── dark-incense.png  # Day mode notification icon
│   ├── white-incense.png # Night mode notification icon
│   └── lak-jit.jpg       # Favicon
├── sitemap.xml           # SEO sitemap
├── robots.txt            # Search engine directives
└── README.md             # This file
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/lakjit.git
cd lakjit
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install flask lunar-python
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to:
```
http://localhost:5001
```

### Static Version
The `index.html` file can be deployed directly to static hosting services like Netlify, Vercel, or GitHub Pages without requiring a Python backend.

## 🌙 Night Mode

Night mode automatically activates between 8 PM and 7 AM based on the user's local time. It features:
- Dark charcoal background
- Soft off-white text
- 60% brightness filter for reduced eye strain
- Automatic icon color switching
- Smooth transitions

## 📅 February 2026 Special Features

During February 2026 (Year of the Horse), the daily quote system displays special horse-themed quotes:
- 28 unique quotes, one for each day
- Direct day-of-month indexing (Feb 1 = Quote 1)
- Special CNY quote on Feb 17: 馬年新禧
- All quotes are 4-character Traditional Chinese

## 🔧 Customization

### Changing Quotes
Edit the `daily_quotes` array in `app.py` or the `quotes` array in `index.html` to customize the quote library.

### Adjusting Night Mode Hours
Modify the time check in the `checkNightMode()` function:
```javascript
const isNight = hour >= 20 || hour < 7;  // 8 PM to 7 AM
```

### Updating Activities Count
Change the slice value in both `app.py` and `index.html`:
```python
'good_for': lunar.getDayYi()[:3],  # Shows 3 activities
```

## 📱 Browser Compatibility

- Chrome/Edge (recommended)
- Firefox
- Safari
- Mobile browsers (iOS Safari, Chrome Mobile)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- lunar-python and lunar-javascript libraries for lunar calendar calculations
- Noto Sans TC font by Google Fonts
- html2canvas for image generation functionality

## � Contact

For questions or feedback, please open an issue on GitHub.

---

**Version**: 6.0  
**Last Updated**: February 16, 2026  
**Status**: Active Development
