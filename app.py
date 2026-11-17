import streamlit as st
import pandas as pd
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo
from pathlib import Path

# Resolve logo files relative to this app.py file. This also tolerates users
# uploading the PNGs into the repository root or retaining their original names.
APP_DIR = Path(__file__).resolve().parent
ASSET_DIR = APP_DIR / "assets"

def find_logo(candidates):
    for candidate in candidates:
        path = APP_DIR / candidate
        if path.is_file():
            return str(path)
    return None

ICON_PATH = find_logo([
    "assets/ausome_icon.png",
    "ausome_icon.png",
    "Tiger with steak, boater hat and cutlery plus.png",
    "assets/Tiger with steak, boater hat and cutlery plus.png",
])
PRIMARY_LOGO_PATH = find_logo([
    "assets/ausome_primary_logo.png",
    "ausome_primary_logo.png",
    "Primary logo.png",
    "assets/Primary logo.png",
])

st.set_page_config(
    page_title="AUsome | Tiger Dining Plus",
    page_icon=ICON_PATH if ICON_PATH else None,
    layout="wide",
)

TODAY = datetime.now(ZoneInfo("America/Chicago")).date()
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
DAY_NUM = {name: i for i, name in enumerate(DAYS)}

# Auburn University 2026-27 no-class dates, sourced from official calendars.
# No-class dates are excluded from expected campus-day counts. Some dates
# overlap with official university closures; this model treats all listed
# academic breaks as days students are not expected on campus.
AUBURN_NO_CLASS_DATES = {
    date(2026, 9, 7): "Labor Day",
    date(2026, 10, 8): "Fall Break",
    date(2026, 10, 9): "Fall Break",
    date(2026, 11, 23): "Thanksgiving Break",
    date(2026, 11, 24): "Thanksgiving Break",
    date(2026, 11, 25): "Thanksgiving Break",
    date(2026, 11, 26): "Thanksgiving Break",
    date(2026, 11, 27): "Thanksgiving Break",
    date(2026, 12, 5): "Reading Days",
    date(2026, 12, 6): "Reading Days",
    date(2027, 1, 18): "Martin Luther King Jr. Day",
    date(2027, 3, 8): "Spring Break",
    date(2027, 3, 9): "Spring Break",
    date(2027, 3, 10): "Spring Break",
    date(2027, 3, 11): "Spring Break",
    date(2027, 3, 12): "Spring Break",
}

# ---------------- SESSION DATA ----------------
def sample_transactions():
    # Illustrative sample purchases. Panda - Auburn examples are informed by
    # its publicly listed menu; other prices are estimates for demo purposes.
    # These are not verified Tiger Dining Dollar-eligible transactions.
    examples = [
        (13, "Panda - Auburn Chicken & Broccoli Lunch Special", "Lunch", 8.00),
        (12, "Campus Coffee and Bagel", "Breakfast", 5.25),
        (11, "Chick-fil-A Chicken Sandwich (estimate)", "Lunch", 6.50),
        (9, "Panda - Auburn Teriyaki Chicken Combo", "Dinner", 10.30),
        (8, "Breakfast Sandwich and Coffee", "Breakfast", 7.25),
        (7, "Pizza Slice and Drink (estimate)", "Lunch", 9.50),
        (6, "Chicken Burrito Bowl (estimate)", "Dinner", 10.75),
        (4, "Panda - Auburn Chicken Fried Rice", "Lunch", 8.63),
        (3, "Yogurt and Granola Snack (estimate)", "Snack", 4.00),
        (2, "Panda - Auburn Sesame Chicken Combo", "Dinner", 10.30),
    ]
    return pd.DataFrame([
        {"Date": TODAY - timedelta(days=d), "Description": desc, "Category": cat, "Amount": amount}
        for d, desc, cat, amount in examples
    ])

if "active_page" not in st.session_state:
    st.session_state.active_page = "Home"
if "purchases" not in st.session_state:
    st.session_state.purchases = sample_transactions()
if "demo_mode" not in st.session_state:
    st.session_state.demo_mode = True

# ---------------- FIXED LIGHT THEME ----------------
# Current presentation build uses light mode only. A complete dark theme is
# reserved for a future release after native Streamlit widgets are tested.
T = dict(
    bg="#F4F6F9", surface="#FFFFFF", surface2="#F0F3F7",
    text="#17233D", muted="#5E6B80", border="#DCE2EA",
    nav="#FFFFFF", input="#FFFFFF", input_text="#17233D",
    success_bg="#E5F3EB", success_text="#185C3B",
    warning_bg="#FFF2DE", warning_text="#784500",
    selected="#FFF0E2"
)

# ---------------- EXPLICIT CSS ----------------
st.markdown(f"""
<style>
:root {{
 --app-bg:{T['bg']}; --surface:{T['surface']}; --surface2:{T['surface2']};
 --app-text:{T['text']}; --muted:{T['muted']}; --border:{T['border']};
 --nav-bg:{T['nav']}; --input-bg:{T['input']}; --input-text:{T['input_text']};
 --orange:#E87500; --navy:#14213D;
 --shadow:0 3px 12px rgba(20,33,61,.055);
}}
html, body, .stApp, [data-testid="stAppViewContainer"] {{
 background:var(--app-bg) !important; color:var(--app-text) !important;
}}
[data-testid="stHeader"] {{ background:var(--app-bg) !important; }}
.block-container {{ max-width:1280px; padding-top:1.25rem; padding-bottom:6.5rem; }}
[data-testid="stSidebar"] {{ background:var(--surface) !important; border-right:1px solid var(--border); }}
[data-testid="stSidebar"] * {{ color:var(--app-text); }}
h1,h2,h3,h4,h5,p,li {{ color:var(--app-text); }}
.st-key-au_header {{
  background:#FFFFFF !important;
  border:1px solid #DCE2EA;
  border-left:6px solid #E87500;
  padding:45px 26px 25px 26px !important;
  margin-bottom:24px;
  border-radius:8px;
  box-shadow:0 5px 18px rgba(20,33,61,.07);
}}
 .st-key-au_header .eyebrow {{ color:#657187 !important; font-size:.73rem; font-weight:800; letter-spacing:.12em; }}
 .st-key-au_header p {{ color:#17233D !important; -webkit-text-fill-color:#17233D !important; margin:0; }}
.section-heading {{ color:var(--app-text) !important; font-size:1.22rem; font-weight:800; margin:1.35rem 0 .75rem; letter-spacing:-.015em; }}
.stCaption, [data-testid="stCaptionContainer"] {{ color:var(--muted) !important; }}
[data-testid="stDataFrame"], [data-testid="stTable"] {{ border-radius:8px; overflow:hidden; }}
div[data-testid="stMetric"] {{ box-shadow:var(--shadow); }}
div[data-testid="stAlert"] {{ border-radius:8px; }}
div[data-testid="stForm"] {{ border:1px solid var(--border); border-radius:9px; padding:16px; }}

.panel {{ background:var(--surface); border:1px solid var(--border); padding:18px 20px; border-radius:9px; box-shadow:0 2px 8px rgba(20,33,61,.035); }}
.metric-panel {{ background:var(--surface); border:1px solid var(--border); padding:16px 18px; border-radius:9px; min-height:112px; box-shadow:0 2px 8px rgba(20,33,61,.035); }}
.metric-label {{ color:var(--muted) !important; font-size:.82rem; font-weight:650; }}
.metric-value {{ color:var(--app-text) !important; font-size:2rem; line-height:1.25; font-weight:800; }}
.metric-note {{ color:var(--muted) !important; font-size:.8rem; }}
.demo-label {{ color:#D96B00 !important; font-size:.75rem; font-weight:800; letter-spacing:.07em; }}
.status-box {{ padding:13px 16px; border-radius:7px; margin:10px 0 18px; font-weight:600; }}
.status-success {{ background:{T['success_bg']} !important; color:{T['success_text']} !important; }}
.status-warning {{ background:{T['warning_bg']} !important; color:{T['warning_text']} !important; }}
.status-box span {{ color:inherit !important; }}


/* Force Streamlit's native widgets and popovers into the light palette. */
[data-baseweb="calendar"], [data-baseweb="calendar"] *,
[data-baseweb="popover"], [data-baseweb="popover"] *,
[data-baseweb="menu"], [data-baseweb="menu"] *,
[role="listbox"], [role="option"] {{
    background-color:#FFFFFF !important;
    color:#17233D !important;
}}
[data-testid="stDateInput"] input,
[data-testid="stNumberInput"] input,
[data-testid="stTextInput"] input,
[data-testid="stTextArea"] textarea {{
    background:#FFFFFF !important;
    color:#17233D !important;
    -webkit-text-fill-color:#17233D !important;
    border-color:#DCE2EA !important;
}}
[data-testid="stDateInput"] button,
[data-testid="stNumberInput"] button {{
    background:#FFFFFF !important;
    color:#17233D !important;
}}
[data-testid="stMultiSelect"] [data-baseweb="tag"] {{
    background:#E87500 !important;
}}
[data-testid="stMultiSelect"] [data-baseweb="tag"] * {{
    color:#FFFFFF !important;
}}

/* Streamlit metrics */
div[data-testid="stMetric"] {{
 background:var(--surface) !important; border:1px solid var(--border) !important;
 border-radius:5px !important; padding:13px 15px !important;
}}
div[data-testid="stMetric"] label,
div[data-testid="stMetric"] label *,
div[data-testid="stMetric"] [data-testid="stMetricValue"],
div[data-testid="stMetric"] [data-testid="stMetricValue"] * {{
 color:var(--app-text) !important; -webkit-text-fill-color:var(--app-text) !important; opacity:1 !important;
}}
div[data-testid="stMetric"] label {{ color:var(--muted) !important; }}

/* Inputs: target Streamlit/BaseWeb controls and their nested text */
[data-testid="stTextInput"] input,
[data-testid="stNumberInput"] input,
[data-testid="stDateInput"] input,
[data-testid="stTextArea"] textarea {{
 background:var(--input-bg) !important; color:var(--input-text) !important;
 -webkit-text-fill-color:var(--input-text) !important;
 border:1px solid var(--border) !important; caret-color:var(--input-text) !important;
}}
[data-testid="stSelectbox"] [data-baseweb="select"] > div,
[data-testid="stMultiSelect"] [data-baseweb="select"] > div {{
 background:var(--input-bg) !important; color:var(--input-text) !important;
 border-color:var(--border) !important;
}}
[data-testid="stSelectbox"] [data-baseweb="select"] *,
[data-testid="stMultiSelect"] [data-baseweb="select"] *,
[data-testid="stDateInput"] *,
[data-testid="stNumberInput"] button {{
 color:var(--input-text) !important;
}}
[data-baseweb="popover"], [data-baseweb="menu"], [role="listbox"] {{
 background:var(--surface) !important; color:var(--app-text) !important;
}}
[data-baseweb="menu"] *, [role="option"] {{ color:var(--app-text) !important; }}
[data-testid="stRadio"] label, [data-testid="stCheckbox"] label {{ color:var(--app-text) !important; }}
.stButton > button, .stDownloadButton > button {{
 border:1px solid var(--border); border-radius:4px; font-weight:700;
 background:var(--surface); color:var(--app-text);
}}
.stButton > button[kind="primary"] {{ background:#E87500 !important; color:#FFFFFF !important; border-color:#E87500 !important; }}
div[data-testid="stDataFrame"] {{ border:1px solid var(--border); }}
hr {{ border-color:var(--border) !important; }}

/* Bottom navigation is a dedicated button row, not a radio group */
.bottom-nav-wrap {{
 position:fixed; z-index:99999; bottom:0; left:0; right:0;
 background:{T['nav']} !important; border-top:1px solid {T['border']};
 padding:9px 12px 11px; box-shadow:0 -3px 12px rgba(0,0,0,.08);
}}
.bottom-nav-inner {{ max-width:520px; margin:0 auto; }}
.bottom-nav-inner [data-testid="stButton"] button {{
 width:100%; min-height:42px; border:1px solid transparent !important;
 background:transparent !important; color:{T['muted']} !important;
 border-radius:7px !important; font-weight:700 !important;
}}
.bottom-nav-inner [data-testid="stButton"] button:hover {{
 border-color:{T['border']} !important; background:{T['surface2']} !important;
}}
.bottom-nav-inner [data-testid="stButton"] button[kind="primary"] {{
 background:{T['selected']} !important; border-color:{T['border']} !important;
 color:{T['text']} !important;
}}
footer {{ visibility:hidden; }}
@media(max-width:700px) {{
 .block-container {{ padding-left:1rem; padding-right:1rem; }}
 .metric-value {{ font-size:1.55rem; }}
 .bottom-nav-inner [data-testid="stButton"] button {{ font-size:.82rem; padding:4px; }}
}}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
if ICON_PATH:
    st.sidebar.image(ICON_PATH, use_container_width=True)
else:
    st.sidebar.markdown("<div style='text-align:center;font-size:2rem;font-weight:900;color:#E87500;'>AU+</div>", unsafe_allow_html=True)
    st.sidebar.caption("Logo not found — add the PNG files to the assets folder.")
st.sidebar.markdown("<div style='text-align:center;font-weight:800;color:#14213D;letter-spacing:.08em;margin-top:-8px;'>AUSOME</div><div style='text-align:center;color:#657187;font-size:.78rem;margin-bottom:8px;'>TIGER DINING PLUS</div>", unsafe_allow_html=True)
st.sidebar.divider()
st.sidebar.markdown("### Your information")
balance = st.sidebar.number_input("Dining Dollars remaining ($)", min_value=0.0, value=250.0, step=5.0)
semester_end = st.sidebar.date_input("Last day of semester", value=max(TODAY, date(TODAY.year, 12, 10)), min_value=TODAY)
campus_days = st.sidebar.multiselect("Expected campus days", DAYS, default=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
use_auburn_calendar = st.sidebar.checkbox("Apply Auburn academic calendar", value=True)
st.sidebar.caption("Selected 2026–27 no-class dates are built in; add personal days off below.")
days_off_raw = st.sidebar.text_area("Your additional days off (YYYY-MM-DD, one per line)", placeholder="2026-12-01\\n2026-12-02")
days_off = set(AUBURN_NO_CLASS_DATES.keys()) if use_auburn_calendar else set()
bad_dates = []
for line in days_off_raw.splitlines():
    if line.strip():
        try:
            days_off.add(date.fromisoformat(line.strip()))
        except ValueError:
            bad_dates.append(line.strip())
if bad_dates:
    st.sidebar.error("Invalid date(s): " + ", ".join(bad_dates))

st.sidebar.divider()
st.sidebar.markdown("### Prediction settings")
forecast_method = st.sidebar.radio("Forecast method", ["Recent spending average", "Planned daily spending"])
planned_daily = st.sidebar.number_input("Planned spend per campus day ($)", min_value=0.0, value=12.0, step=0.5)
st.sidebar.divider()
st.sidebar.markdown("### Demo data")
st.sidebar.caption("Fictional demo purchases; some prices are menu-informed and others are estimates.")
if st.sidebar.button("Reset sample transactions", use_container_width=True):
    st.session_state.purchases = sample_transactions()
    st.session_state.demo_mode = True
    st.rerun()
if st.sidebar.button("Clear transactions", use_container_width=True):
    st.session_state.purchases = pd.DataFrame(columns=["Date", "Description", "Category", "Amount"])
    st.session_state.demo_mode = False
    st.rerun()

# ---------------- FORECAST ----------------
weekday_numbers = {DAY_NUM[d] for d in campus_days}
def campus_dates(start, end):
    out = []
    d = start
    while d <= end:
        if d.weekday() in weekday_numbers and d not in days_off:
            out.append(d)
        d += timedelta(days=1)
    return out

future_dates = campus_dates(TODAY, semester_end) if semester_end >= TODAY else []
recent_dates = campus_dates(TODAY - timedelta(days=13), TODAY)
purchases = st.session_state.purchases.copy()
if not purchases.empty:
    purchases["Date"] = pd.to_datetime(purchases["Date"]).dt.date
    purchases["Amount"] = pd.to_numeric(purchases["Amount"], errors="coerce").fillna(0)
    recent_total = float(purchases.loc[purchases["Date"].between(TODAY - timedelta(days=13), TODAY), "Amount"].sum())
else:
    recent_total = 0.0
recent_avg = recent_total / len(recent_dates) if recent_dates else 0.0
daily_spend = recent_avg if forecast_method == "Recent spending average" else planned_daily
future_count = len(future_dates)
daily_target = balance / future_count if future_count else 0.0
weekly_target = daily_target * min(5, len(weekday_numbers))
forecast_end = balance - daily_spend * future_count

# Find the next upcoming Auburn no-class period for the Home page.
upcoming_calendar_items = []
if use_auburn_calendar:
    for calendar_day, event_name in sorted(AUBURN_NO_CLASS_DATES.items()):
        if calendar_day >= TODAY:
            upcoming_calendar_items.append((calendar_day, event_name))
next_campus_break = upcoming_calendar_items[0] if upcoming_calendar_items else None

# ---------------- HEADER ----------------
# A native Streamlit container keeps the header styling around all its content.
# Opening an HTML div in one Streamlit call and closing it in another can
# produce detached wrappers and the stray orange strip seen in the previous UI.
with st.container(key="au_header"):
    logo_col, message_col = st.columns([1.15, 1], vertical_alignment="center")
    with logo_col:
        if PRIMARY_LOGO_PATH:
            st.image(PRIMARY_LOGO_PATH, width=330)
        else:
            st.markdown("<div style='font-size:3rem;font-weight:900;color:#14213D;'>AU<span style='color:#E87500;'>some</span></div><div style='font-weight:700;letter-spacing:.18em;color:#657187;'>TIGER DINING PLUS</div>", unsafe_allow_html=True)
    with message_col:
        st.markdown("""
        <div style="padding:12px 8px 12px 12px;">
          <div class="eyebrow">AUBURN UNIVERSITY · STUDENT BUDGETING</div>
          <p style="font-size:1.05rem;font-weight:650;margin-top:12px;">
            A clearer picture of your Dining Dollars, one campus day at a time.
          </p>
        </div>
        """, unsafe_allow_html=True)

# ---------------- BOTTOM NAV ----------------
st.markdown("<div class='bottom-nav-wrap'><div class='bottom-nav-inner'>", unsafe_allow_html=True)
nav_cols = st.columns(3)
for col, name in zip(nav_cols, ["Home", "Statistics", "Profile"]):
    with col:
        kind = "primary" if st.session_state.active_page == name else "secondary"
        if st.button(name, key=f"nav_{name}", type=kind, use_container_width=True):
            st.session_state.active_page = name
            st.rerun()
st.markdown("</div></div>", unsafe_allow_html=True)

# Read the selected page after navigation has updated session state.
page = st.session_state.active_page

# ---------------- HOME ----------------
if page == "Home":
    st.markdown("<div class='section-heading'>Your spending game plan</div>", unsafe_allow_html=True)
    c1, c2 = st.columns([1.25, 1])
    with c1:
        st.markdown(f"""
        <div class="panel">
         <div class="metric-label">YOUR DAILY TARGET</div>
         <div class="metric-value" style="font-size:2.6rem;">${daily_target:,.2f}</div>
         <p style="color:{T['muted']} !important;">Based on ${balance:,.2f} across {future_count} expected campus days.</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="panel">
         <h3 style="margin-top:0;">Semester outlook</h3>
         <p style="color:{T['muted']} !important;">{future_count} campus days remaining<br>
         ${weekly_target:,.2f} suggested weekly target<br>
         Semester ends {semester_end.strftime('%b %d, %Y')}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div class='section-heading'>The numbers behind your plan</div>", unsafe_allow_html=True)
    a, b, c = st.columns(3)
    a.metric("Logged in last 14 days", f"${recent_total:,.2f}")
    b.metric("Average per campus day", f"${recent_avg:,.2f}")
    c.metric("Projected end balance", f"${forecast_end:,.2f}")

    if not purchases.empty:
        category_totals = purchases.groupby("Category")["Amount"].sum().sort_values(ascending=False)
        top_category = str(category_totals.index[0])
        top_amount = float(category_totals.iloc[0])
        st.caption(f"Quick insight: **{top_category}** is your highest-spend category in the recorded transactions (${top_amount:,.2f}).")
    else:
        st.caption("Quick insight: add a few purchases to start seeing patterns in your spending.")

    st.markdown("<div class='section-heading'>Recent transactions</div>", unsafe_allow_html=True)
    if purchases.empty:
        st.info("No transactions yet. Add a transaction in Statistics.")
    else:
        recent = purchases.sort_values("Date", ascending=False).head(5).copy()
        recent["Date"] = pd.to_datetime(recent["Date"]).dt.strftime("%b %d")
        st.dataframe(recent, width="stretch", hide_index=True)

# ---------------- STATISTICS ----------------
elif page == "Statistics":
    st.markdown("<div class='section-heading'>Spending analysis</div>", unsafe_allow_html=True)
    if purchases.empty:
        st.info("Add transactions below or reset sample transactions to populate the charts.")
    else:
        chart_data = purchases.copy()
        chart_data["Date"] = pd.to_datetime(chart_data["Date"])
        by_day = chart_data.groupby("Date")["Amount"].sum()
        # Fill dates with $0 so the daily chart has a consistent, honest timeline
        # instead of showing isolated bars only on purchase dates.
        chart_start = pd.Timestamp(TODAY - timedelta(days=13))
        chart_end = pd.Timestamp(TODAY)
        daily_index = pd.date_range(chart_start, chart_end, freq="D")
        daily_series = by_day.reindex(daily_index, fill_value=0.0)
        daily_chart = pd.DataFrame({
            "Date": daily_series.index.strftime("%a, %b %d"),
            "Spent": daily_series.values
        }).set_index("Date")
        by_category = chart_data.groupby("Category")["Amount"].sum().sort_values(ascending=False)
        left, right = st.columns([1.5, 1])
        with left:
            st.markdown("#### Daily spending · last 14 days")
            st.caption("Every day is shown, including days with no recorded purchases.")
            st.bar_chart(daily_chart, y="Spent", color="#E87500", height=270)
        with right:
            st.markdown("#### Spending by category")
            st.caption("Total recorded spending by meal type.")
            st.bar_chart(by_category, color="#263F70", height=270)

        week_start = pd.Timestamp(TODAY - timedelta(days=TODAY.weekday()))
        weekly_data = chart_data.copy()
        weekly_data["Week"] = weekly_data["Date"].dt.to_period("W-SUN").dt.start_time
        weekly_totals = weekly_data.groupby("Week")["Amount"].sum().sort_index()
        st.markdown("#### Weekly spending trend")
        st.caption("A wider view makes it easier to spot changes in spending habits.")
        if len(weekly_totals):
            weekly_display = weekly_totals.copy()
            weekly_display.index = weekly_display.index.strftime("%b %d")
            st.bar_chart(weekly_display, color="#263F70", height=220)

    st.markdown("<div class='section-heading'>Semester-end forecast</div>", unsafe_allow_html=True)
    f1, f2, f3 = st.columns(3)
    f1.metric("Daily spend assumed", f"${daily_spend:,.2f}")
    f2.metric("Projected future spend", f"${daily_spend * future_count:,.2f}")
    f3.metric("Estimated ending balance", f"${forecast_end:,.2f}")
    st.caption("Forecast is an estimate based on the selected recent or planned spending rate.")

    if future_dates:
        projected = []
        running = balance
        for d in future_dates:
            running -= daily_spend
            projected.append({"Date": pd.Timestamp(d), "Projected balance": running})
        st.markdown("#### Projected balance over time")
        st.line_chart(pd.DataFrame(projected).set_index("Date"), y="Projected balance", color="#E87500")

    if not purchases.empty:
        st.markdown("<div class='section-heading'>Transaction history</div>", unsafe_allow_html=True)
        history = purchases.copy()
        history["Date"] = pd.to_datetime(history["Date"]).dt.strftime("%b %d, %Y")
        st.dataframe(history.sort_values("Date", ascending=False), width="stretch", hide_index=True)
        st.download_button("Download transactions (CSV)", st.session_state.purchases.to_csv(index=False).encode("utf-8"), "ausome_transactions.csv", "text/csv")

    st.markdown("<div class='section-heading'>Add a transaction</div>", unsafe_allow_html=True)
    with st.form("add_transaction", clear_on_submit=True):
        x, y = st.columns(2)
        trans_date = x.date_input("Date", value=TODAY, max_value=TODAY)
        desc = y.text_input("Description", placeholder="Example: lunch")
        q, r = st.columns(2)
        category = q.selectbox("Category", ["Breakfast", "Lunch", "Dinner", "Snack", "Coffee", "Other"])
        amount = r.number_input("Amount ($)", min_value=0.01, value=8.50, step=0.25)
        if st.form_submit_button("Add transaction", type="primary"):
            row = pd.DataFrame([{"Date": trans_date, "Description": desc.strip() or category, "Category": category, "Amount": float(amount)}])
            st.session_state.purchases = pd.concat([st.session_state.purchases, row], ignore_index=True)
            st.session_state.demo_mode = False
            st.rerun()

    if not st.session_state.purchases.empty:
        st.markdown("#### Manage transactions")
        st.caption("Remove an entry if you added it by mistake.")
        transaction_options = {
            f"{pd.to_datetime(row['Date']).strftime('%b %d')} · {row['Description']} · ${float(row['Amount']):.2f}": idx
            for idx, row in st.session_state.purchases.iterrows()
        }
        selected_transaction = st.selectbox("Choose a transaction to remove", list(transaction_options.keys()))
        if st.button("Remove selected transaction"):
            remove_index = transaction_options[selected_transaction]
            st.session_state.purchases = st.session_state.purchases.drop(index=remove_index).reset_index(drop=True)
            st.session_state.demo_mode = False
            st.rerun()

# ---------------- PROFILE ----------------
elif page == "Profile":
    st.markdown("<div class='section-heading'>Student profile and preferences</div>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="panel">
      <h3 style="margin-top:0;">Your settings</h3>
      <p style="color:{T['muted']} !important;">Use the controls in the left panel to update your balance, semester dates, campus schedule, days away, and forecast preferences.</p>
    </div>
    """, unsafe_allow_html=True)
    profile = pd.DataFrame([
        {"Preference": "Dining Dollars balance", "Current setting": f"${balance:,.2f}"},
        {"Preference": "Semester end", "Current setting": semester_end.strftime("%B %d, %Y")},
        {"Preference": "Campus days", "Current setting": ", ".join(campus_days) if campus_days else "None selected"},
        {"Preference": "Days off entered", "Current setting": str(len(days_off))},
        {"Preference": "Forecast method", "Current setting": forecast_method},
    ])
    st.dataframe(profile, width="stretch", hide_index=True)
    st.markdown("<div class='section-heading'>How the prediction works</div>", unsafe_allow_html=True)
    st.markdown("""
    1. The app totals manually entered purchases from the previous 14 calendar days.
    2. It divides that total by expected campus days in the same period.
    3. It estimates future spending using that daily average or your planned daily amount.
    4. It subtracts estimated future spending from your current balance.

    This is a baseline estimate, not a guarantee. Its accuracy depends on complete and representative transaction entries.
    """)
    st.markdown("<div class='section-heading'>What comes next</div>", unsafe_allow_html=True)
    st.markdown("""
    This final prototype focuses on the core budgeting experience: balance planning, campus-day
    forecasting, transaction tracking, and clear spending trends.

    The larger product vision includes meal-swipe tracking, dining-location and favorite-food
    insights, nutrition or calories-per-dollar comparisons where reliable data is available,
    schedule-aware meal suggestions, and (with Auburn approval) a future GET Mobile connection.
    These are roadmap ideas—not active features in this demo.
    """)
    st.markdown("<div class='section-heading'>Auburn academic calendar</div>", unsafe_allow_html=True)
    st.write(f"Auburn calendar integration is {'on' if use_auburn_calendar else 'off'}.")
    st.caption("The built-in calendar currently includes selected 2026–27 no-class dates. Always verify dates against Auburn's official calendar; dates may change.")
    st.markdown("[Auburn Office of the Registrar — Academic Calendars](https://www.auburn.edu/administration/registrar/secure/academic-calendar/rolling-year-academic-calendar.php)")
    st.markdown("[Auburn Fall 2026 Dates to Know](https://studentaffairs.auburn.edu/articles/2026/08/fall-2026-dates-to-know.php)")
    st.markdown("<div class='section-heading'>Sample transaction notes</div>", unsafe_allow_html=True)
    st.caption("Sample transactions are fictional. Some item names and prices are informed by publicly listed Auburn-area menus; others are estimates. Restaurant examples do not imply acceptance of Tiger Dining Dollars.")
    st.markdown("[Panda - Auburn online menu](https://order.pandaauburn.com/menu)")

st.divider()
st.caption("AUsome · Final prototype v7 · Sample transactions are illustrative · Not connected to Auburn or GET Mobile · Demo data is temporary for this session.")
