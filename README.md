# AUsome — Tiger Dining Plus

An Auburn-inspired Streamlit prototype designed to help students plan and track Tiger Dining Dollars throughout the semester.

## Features

- **Home, Statistics, and Profile** sections with a consistent Auburn navy-and-orange design.
- Automatic Auburn-timezone date handling for the current date and new transaction defaults.
- Balance planning with daily and weekly spending targets based on selected campus weekdays and days off.
- Selected Auburn academic-calendar exclusions for configured 2026–27 dates, including Thanksgiving Break. Users can also add their own days off.
- Recent spending averages and semester-end balance estimates using either recent spending or a planned daily spending amount.
- Daily spending chart showing every day in the last 14 days, including zero-spend days, along with category and weekly summaries.
- Transaction entry, removal, history, and CSV export.
- Sample meal descriptions with illustrative prices for demonstrating the experience.

## Important Limitations

- This is a class-project prototype, not a production financial application.
- Sample purchases are fictional. Some names and prices are illustrative and do not confirm that a restaurant accepts Tiger Dining Dollars.
- The app does not connect to Auburn systems, GET Mobile, student accounts, dining menus, or live account balances.
- Transaction data is held in Streamlit session state and is temporary. There is no permanent database, account login, or cross-device synchronization.
- Forecasts are estimates based on the transactions and campus schedule entered by the user.
- Built-in 2026–27 academic dates are manually configured, not connected to a live Auburn calendar feed. Dates should be verified against Auburn's official academic calendar.
- Meal swipes, nutrition or calories-per-dollar tracking, location intelligence, schedule-aware meal recommendations, and GET Mobile integration are possible future features, not currently implemented.
- Do not enter passwords, student ID numbers, payment details, or other sensitive information.

## Project Files

- `app.py` — Streamlit application.
- `requirements.txt` — Python package dependencies.
- `ausome_primary_logo.png` — Full horizontal AUsome logo used in the main header.
- `ausome_icon.png` — Tiger icon used for the browser page icon and sidebar.
- `.streamlit/config.toml` — Streamlit theme configuration.

## Technology

- **Python** — Application logic and calculations.
- **Streamlit** — Interactive web interface.
- **Pandas** — Transaction data handling and summaries.

## Version

Final class-project prototype, version 7.
