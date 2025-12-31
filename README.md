# Lakjit - Chinese Vintage Calendar (日历)

A beautiful, mobile-responsive **Chinese Vintage Calendar** web application. Designed with a traditional "tear-off" aesthetic, featuring accurate Lunar dates, auspicious activities (Yi/Ji), and daily quotes.

Now fully migrated to a **Static Site** architecture for easy deployment on Netlify/GitHub Pages.

## Features

- **Vintage Design**: Green theme, "thick block" shadows, and classic typography.
- **Accurate Logic**: Powered by `lunar-javascript` (6tail) for precise Lunar Date and Solar Term calculations.
- **Typography**: Uses the rounded **Huninn** font (via Google Fonts).
- **Mobile Responsive**: Optimized layout for all screen sizes.
- **Static Architecture**: No backend server required. Runs entirely in the browser.

## Technologies

- **HTML5 / CSS3**: Flexbox & Grid layouts.
- **JavaScript**: Client-side logic replacing the original Flask backend.
- **Libraries**:
  - [lunar-javascript](https://github.com/6tail/lunar-javascript) (CDN)
  - [Huninn Font](https://fonts.google.com/specimen/Huninn)

## How to Run

### Static (Recommended)
Simply open `index.html` in your browser.

### Development (Legacy Python)
If you wish to use the original Flask backend (now superseded by the static version):
1. Install dependencies: `pip install flask lunar_python`
2. Run: `python app.py`
3. Visit: `http://localhost:5000`

## Deployment

This project is Netlify-ready.
1. Connect your GitHub repository to Netlify.
2. Netlify will detect `index.html` automatically.
3. Deploy!

## Credits
Built with 💚.
Fatt Choy HOH 2026.
