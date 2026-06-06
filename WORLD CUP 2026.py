import sys, math, random
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

# ═══════════════════════════════════════════════════════════════
#  THEMES
# ═══════════════════════════════════════════════════════════════
THEMES = {
    "dark": {
        "bg": "#0a0e1a", "bg2": "#0d1220", "bg3": "#111827",
        "card": "#1a2035", "card2": "#1e2640",
        "acc": "#00d4ff", "acc2": "#0099cc", "acc3": "#006699",
        "text": "#e8f4f8", "text2": "#8899aa",
        "border": "#2a3a4a", "grass": "#1a4a1a",
        "pitch": "#2d7a2d", "pitch2": "#267026",
        "net": "#cccccc", "post": "#f0f0f0",
        "hud": "rgba(10,14,26,200)",
    },
    "light": {
        "bg": "#e8f0f8", "bg2": "#d0dce8", "bg3": "#c8d8e8",
        "card": "#ffffff", "card2": "#f0f4f8",
        "acc": "#0066cc", "acc2": "#0055aa", "acc3": "#004488",
        "text": "#1a2030", "text2": "#4a5a6a",
        "border": "#b0c0d0", "grass": "#4a9a4a",
        "pitch": "#5ab85a", "pitch2": "#52aa52",
        "net": "#888888", "post": "#cccccc",
        "hud": "rgba(232,240,248,200)",
    }
}

# ═══════════════════════════════════════════════════════════════
#  TRANSLATIONS
# ═══════════════════════════════════════════════════════════════
TR = {
    "en": {
        "title": "WORLD CUP 2026", "subtitle": "Penalty Shootout",
        "play": "PLAY", "settings": "SETTINGS", "quit": "QUIT",
        "back": "BACK", "theme": "Theme", "language": "Language",
        "dark": "Dark", "light": "Light",
        "select_team": "Select Your Team", "select_opponent": "Select Opponent",
        "select_stadium": "Select Stadium", "select_goalkeeper": "Select Goalkeeper",
        "select_shooters": "Select Penalty Takers",
        "start_match": "START MATCH",
        "penalty_shootout": "PENALTY SHOOTOUT",
        "shoot": "SHOOT", "save": "SAVE", "goal": "GOAL!", "miss": "MISS!",
        "round": "Round", "of": "of",
        "your_turn": "Your Turn", "cpu_turn": "CPU Turn",
        "score": "Score", "wins": "WINS!", "draw": "DRAW!",
        "sudden_death": "SUDDEN DEATH",
        "choose_direction": "Choose Direction",
        "left": "Left", "center": "Center", "right": "Right",
        "top": "Top", "bottom": "Bottom",
        "match_result": "Match Result",
        "penalties_taken": "Penalties Taken",
        "next": "NEXT", "retry": "RETRY", "menu": "MENU",
        "stadium": "Stadium", "capacity": "Capacity",
        "confirm": "CONFIRM", "cancel": "CANCEL",
        "player": "Player", "number": "Number",
        "gk": "Goalkeeper", "shooters": "Shooters",
        "add_player": "Add Player", "remove": "Remove",
        "name": "Name", "position": "Position",
        "instructions": "Click to aim, then SHOOT!",
        "cpu_thinking": "CPU is thinking...",
        "phase_normal": "Normal Penalties (5 rounds)",
        "phase_sudden": "Sudden Death",
    },
    "fa": {
        "title": "جام جهانی ۲۰۲۶", "subtitle": "ضربات پنالتی",
        "play": "بازی", "settings": "تنظیمات", "quit": "خروج",
        "back": "بازگشت", "theme": "تم", "language": "زبان",
        "dark": "تاریک", "light": "روشن",
        "select_team": "انتخاب تیم", "select_opponent": "انتخاب حریف",
        "select_stadium": "انتخاب ورزشگاه", "select_goalkeeper": "انتخاب دروازه‌بان",
        "select_shooters": "انتخاب ضربه‌زنندگان",
        "start_match": "شروع بازی",
        "penalty_shootout": "ضربات پنالتی",
        "shoot": "شوت", "save": "دفع شد", "goal": "گل!", "miss": "خطا!",
        "round": "دور", "of": "از",
        "your_turn": "نوبت شما", "cpu_turn": "نوبت حریف",
        "score": "امتیاز", "wins": "برنده شد!", "draw": "مساوی!",
        "sudden_death": "مرگ ناگهانی",
        "choose_direction": "جهت را انتخاب کنید",
        "left": "چپ", "center": "وسط", "right": "راست",
        "top": "بالا", "bottom": "پایین",
        "match_result": "نتیجه بازی",
        "penalties_taken": "پنالتی‌های زده شده",
        "next": "بعدی", "retry": "دوباره", "menu": "منو",
        "stadium": "ورزشگاه", "capacity": "ظرفیت",
        "confirm": "تأیید", "cancel": "لغو",
        "player": "بازیکن", "number": "شماره",
        "gk": "دروازه‌بان", "shooters": "ضربه‌زنندگان",
        "add_player": "افزودن بازیکن", "remove": "حذف",
        "name": "نام", "position": "پست",
        "instructions": "کلیک کنید تا هدف بگیرید، سپس شوت!",
        "cpu_thinking": "حریف در حال فکر کردن...",
        "phase_normal": "پنالتی‌های عادی (۵ دور)",
        "phase_sudden": "مرگ ناگهانی",
    },
    "zh": {
        "title": "2026世界杯", "subtitle": "点球大战",
        "play": "开始游戏", "settings": "设置", "quit": "退出",
        "back": "返回", "theme": "主题", "language": "语言",
        "dark": "深色", "light": "浅色",
        "select_team": "选择球队", "select_opponent": "选择对手",
        "select_stadium": "选择球场", "select_goalkeeper": "选择守门员",
        "select_shooters": "选择点球手",
        "start_match": "开始比赛",
        "penalty_shootout": "点球大战",
        "shoot": "射门", "save": "扑救", "goal": "进球!", "miss": "未中!",
        "round": "轮", "of": "/",
        "your_turn": "你的回合", "cpu_turn": "对手回合",
        "score": "比分", "wins": "获胜!", "draw": "平局!",
        "sudden_death": "突然死亡",
        "choose_direction": "选择方向",
        "left": "左", "center": "中", "right": "右",
        "top": "上", "bottom": "下",
        "match_result": "比赛结果",
        "penalties_taken": "已踢点球",
        "next": "下一步", "retry": "重试", "menu": "菜单",
        "stadium": "球场", "capacity": "容量",
        "confirm": "确认", "cancel": "取消",
        "player": "球员", "number": "号码",
        "gk": "守门员", "shooters": "点球手",
        "add_player": "添加球员", "remove": "删除",
        "name": "姓名", "position": "位置",
        "instructions": "点击瞄准，然后射门！",
        "cpu_thinking": "对手思考中...",
        "phase_normal": "常规点球（5轮）",
        "phase_sudden": "突然死亡",
    }
}

# ═══════════════════════════════════════════════════════════════
#  WORLD CUP 2026 TEAMS
# ═══════════════════════════════════════════════════════════════
TEAMS = {
    # Group A
    "USA":         {"name": "United States",  "color": "#B22234", "color2": "#FFFFFF", "flag": "🇺🇸", "group": "A"},
    "MEX":         {"name": "Mexico",          "color": "#006847", "color2": "#FFFFFF", "flag": "🇲🇽", "group": "A"},
    "CAN":         {"name": "Canada",          "color": "#FF0000", "color2": "#FFFFFF", "flag": "🇨🇦", "group": "A"},
    "URU":         {"name": "Uruguay",         "color": "#5AAAFA", "color2": "#FFFFFF", "flag": "🇺🇾", "group": "A"},
    # Group B
    "ARG":         {"name": "Argentina",       "color": "#74ACDF", "color2": "#FFFFFF", "flag": "🇦🇷", "group": "B"},
    "CHI":         {"name": "Chile",           "color": "#D52B1E", "color2": "#FFFFFF", "flag": "🇨🇱", "group": "B"},
    "PER":         {"name": "Peru",            "color": "#D91023", "color2": "#FFFFFF", "flag": "🇵🇪", "group": "B"},
    "AUS":         {"name": "Australia",       "color": "#FFCD00", "color2": "#00843D", "flag": "🇦🇺", "group": "B"},
    # Group C
    "BRA":         {"name": "Brazil",          "color": "#009C3B", "color2": "#FFDF00", "flag": "🇧🇷", "group": "C"},
    "COL":         {"name": "Colombia",        "color": "#FCD116", "color2": "#003087", "flag": "🇨🇴", "group": "C"},
    "ECU":         {"name": "Ecuador",         "color": "#FFD100", "color2": "#003087", "flag": "🇪🇨", "group": "C"},
    "VEN":         {"name": "Venezuela",       "color": "#CF142B", "color2": "#003087", "flag": "🇻🇪", "group": "C"},
    # Group D
    "FRA":         {"name": "France",          "color": "#002395", "color2": "#FFFFFF", "flag": "🇫🇷", "group": "D"},
    "BEL":         {"name": "Belgium",         "color": "#EF3340", "color2": "#000000", "flag": "🇧🇪", "group": "D"},
    "WAL":         {"name": "Wales",           "color": "#C8102E", "color2": "#FFFFFF", "flag": "🏴󠁧󠁢󠁷󠁬󠁳󠁿", "group": "D"},
    "TUN":         {"name": "Tunisia",         "color": "#E70013", "color2": "#FFFFFF", "flag": "🇹🇳", "group": "D"},
    # Group E
    "GER":         {"name": "Germany",         "color": "#FFFFFF", "color2": "#000000", "flag": "🇩🇪", "group": "E"},
    "ESP":         {"name": "Spain",           "color": "#AA151B", "color2": "#F1BF00", "flag": "🇪🇸", "group": "E"},
    "JPN":         {"name": "Japan",           "color": "#003087", "color2": "#FFFFFF", "flag": "🇯🇵", "group": "E"},
    "CRC":         {"name": "Costa Rica",      "color": "#002B7F", "color2": "#FFFFFF", "flag": "🇨🇷", "group": "E"},
    # Group F
    "ENG":         {"name": "England",         "color": "#FFFFFF", "color2": "#CF081F", "flag": "🏴󠁧󠁢󠁥󠁮󠁧󠁿", "group": "F"},
    "NED":         {"name": "Netherlands",     "color": "#FF6600", "color2": "#FFFFFF", "flag": "🇳🇱", "group": "F"},
    "SEN":         {"name": "Senegal",         "color": "#00853F", "color2": "#FDEF42", "flag": "🇸🇳", "group": "F"},
    "IRN":         {"name": "Iran",            "color": "#239F40", "color2": "#FFFFFF", "flag": "🇮🇷", "group": "F"},
    # Group G
    "POR":         {"name": "Portugal",        "color": "#006600", "color2": "#FF0000", "flag": "🇵🇹", "group": "G"},
    "GHA":         {"name": "Ghana",           "color": "#006B3F", "color2": "#FCD116", "flag": "🇬🇭", "group": "G"},
    "URG":         {"name": "Uruguay B",       "color": "#5AAAFA", "color2": "#FFFFFF", "flag": "🇺🇾", "group": "G"},
    "KOR":         {"name": "South Korea",     "color": "#CD2E3A", "color2": "#FFFFFF", "flag": "🇰🇷", "group": "G"},
    # Group H
    "MAR":         {"name": "Morocco",         "color": "#C1272D", "color2": "#006233", "flag": "🇲🇦", "group": "H"},
    "CRO":         {"name": "Croatia",         "color": "#FF0000", "color2": "#FFFFFF", "flag": "🇭🇷", "group": "H"},
    "BIH":         {"name": "Bosnia",          "color": "#002395", "color2": "#FFCD00", "flag": "🇧🇦", "group": "H"},
    "CMR":         {"name": "Cameroon",        "color": "#007A5E", "color2": "#CE1126", "flag": "🇨🇲", "group": "H"},
    # Group I
    "ITA":         {"name": "Italy",           "color": "#003087", "color2": "#FFFFFF", "flag": "🇮🇹", "group": "I"},
    "SUI":         {"name": "Switzerland",     "color": "#FF0000", "color2": "#FFFFFF", "flag": "🇨🇭", "group": "I"},
    "ALB":         {"name": "Albania",         "color": "#E41E20", "color2": "#000000", "flag": "🇦🇱", "group": "I"},
    "NGA":         {"name": "Nigeria",         "color": "#008751", "color2": "#FFFFFF", "flag": "🇳🇬", "group": "I"},
    # Group J
    "DEN":         {"name": "Denmark",         "color": "#C60C30", "color2": "#FFFFFF", "flag": "🇩🇰", "group": "J"},
    "AUT":         {"name": "Austria",         "color": "#ED2939", "color2": "#FFFFFF", "flag": "🇦🇹", "group": "J"},
    "SVK":         {"name": "Slovakia",        "color": "#FFFFFF", "color2": "#003DA5", "flag": "🇸🇰", "group": "J"},
    "EGY":         {"name": "Egypt",           "color": "#CE1126", "color2": "#FFFFFF", "flag": "🇪🇬", "group": "J"},
    # Group K
    "MEX2":        {"name": "Mexico B",        "color": "#006847", "color2": "#FFFFFF", "flag": "🇲🇽", "group": "K"},
    "POL":         {"name": "Poland",          "color": "#FFFFFF", "color2": "#DC143C", "flag": "🇵🇱", "group": "K"},
    "SAU":         {"name": "Saudi Arabia",    "color": "#006C35", "color2": "#FFFFFF", "flag": "🇸🇦", "group": "K"},
    "QAT":         {"name": "Qatar",           "color": "#8D1B3D", "color2": "#FFFFFF", "flag": "🇶🇦", "group": "K"},
    # Group L
    "POR2":        {"name": "Portugal B",      "color": "#006600", "color2": "#FF0000", "flag": "🇵🇹", "group": "L"},
    "TUR":         {"name": "Turkey",          "color": "#E30A17", "color2": "#FFFFFF", "flag": "🇹🇷", "group": "L"},
    "CZE":         {"name": "Czech Republic",  "color": "#D7141A", "color2": "#FFFFFF", "flag": "🇨🇿", "group": "L"},
    "NZL":         {"name": "New Zealand",     "color": "#000000", "color2": "#FFFFFF", "flag": "🇳🇿", "group": "L"},
}

# ═══════════════════════════════════════════════════════════════
#  STADIUMS (FIFA WC 2026 venues)
# ═══════════════════════════════════════════════════════════════
STADIUMS = {
    "metlife":    {"name": "MetLife Stadium",          "city": "New York/New Jersey", "capacity": 82500,  "country": "USA", "icon": "🏟️"},
    "sofi":       {"name": "SoFi Stadium",             "city": "Los Angeles",         "capacity": 70240,  "country": "USA", "icon": "🏟️"},
    "att":        {"name": "AT&T Stadium",             "city": "Dallas",              "capacity": 80000,  "country": "USA", "icon": "🏟️"},
    "nrg":        {"name": "NRG Stadium",              "city": "Houston",             "capacity": 72220,  "country": "USA", "icon": "🏟️"},
    "lincoln":    {"name": "Lincoln Financial Field",  "city": "Philadelphia",        "capacity": 69796,  "country": "USA", "icon": "🏟️"},
    "levis":      {"name": "Levi's Stadium",           "city": "San Francisco",       "capacity": 68500,  "country": "USA", "icon": "🏟️"},
    "seattle":    {"name": "Lumen Field",              "city": "Seattle",             "capacity": 68740,  "country": "USA", "icon": "🏟️"},
    "boston":     {"name": "Gillette Stadium",         "city": "Boston",              "capacity": 65878,  "country": "USA", "icon": "🏟️"},
    "miami":      {"name": "Hard Rock Stadium",        "city": "Miami",               "capacity": 65326,  "country": "USA", "icon": "🏟️"},
    "kansas":     {"name": "Arrowhead Stadium",        "city": "Kansas City",         "capacity": 76416,  "country": "USA", "icon": "🏟️"},
    "azteca":     {"name": "Estadio Azteca",           "city": "Mexico City",         "capacity": 87523,  "country": "MEX", "icon": "🏟️"},
    "guadalajara":{"name": "Estadio Akron",            "city": "Guadalajara",         "capacity": 49850,  "country": "MEX", "icon": "🏟️"},
    "monterrey":  {"name": "Estadio BBVA",             "city": "Monterrey",           "capacity": 53500,  "country": "MEX", "icon": "🏟️"},
    "toronto":    {"name": "BMO Field",                "city": "Toronto",             "capacity": 45736,  "country": "CAN", "icon": "🏟️"},
    "vancouver":  {"name": "BC Place",                 "city": "Vancouver",           "capacity": 54500,  "country": "CAN", "icon": "🏟️"},
}

# ═══════════════════════════════════════════════════════════════
#  DEFAULT SQUAD TEMPLATES
# ═══════════════════════════════════════════════════════════════
DEFAULT_SQUAD = {
    "ARG": [
        {"name": "E. Martínez", "number": 23, "pos": "GK"},
        {"name": "L. Messi",    "number": 10, "pos": "FW"},
        {"name": "J. Álvarez",  "number": 9,  "pos": "FW"},
        {"name": "A. Mac Allister","number":20,"pos":"MF"},
        {"name": "R. De Paul",  "number": 7,  "pos": "MF"},
        {"name": "L. Martínez", "number": 22, "pos": "FW"},
    ],
    "BRA": [
        {"name": "Alisson",     "number": 1,  "pos": "GK"},
        {"name": "Vinicius Jr", "number": 7,  "pos": "FW"},
        {"name": "Rodrygo",     "number": 11, "pos": "FW"},
        {"name": "Neymar Jr",   "number": 10, "pos": "FW"},
        {"name": "Casemiro",    "number": 5,  "pos": "MF"},
        {"name": "Raphinha",    "number": 19, "pos": "FW"},
    ],
    "FRA": [
        {"name": "M. Maignan",  "number": 16, "pos": "GK"},
        {"name": "K. Mbappé",   "number": 10, "pos": "FW"},
        {"name": "A. Griezmann","number": 7,  "pos": "FW"},
        {"name": "O. Giroud",   "number": 9,  "pos": "FW"},
        {"name": "A. Tchouaméni","number":8,  "pos": "MF"},
        {"name": "M. Camavinga","number":29,  "pos": "MF"},
    ],
    "ENG": [
        {"name": "J. Pickford", "number": 1,  "pos": "GK"},
        {"name": "H. Kane",     "number": 9,  "pos": "FW"},
        {"name": "B. Saka",     "number": 7,  "pos": "FW"},
        {"name": "J. Bellingham","number":22, "pos": "MF"},
        {"name": "P. Foden",    "number": 10, "pos": "MF"},
        {"name": "M. Rashford", "number": 11, "pos": "FW"},
    ],
    "GER": [
        {"name": "M. Neuer",    "number": 1,  "pos": "GK"},
        {"name": "K. Havertz",  "number": 7,  "pos": "FW"},
        {"name": "J. Musiala",  "number": 10, "pos": "MF"},
        {"name": "L. Goretzka", "number": 8,  "pos": "MF"},
        {"name": "T. Müller",   "number": 13, "pos": "FW"},
        {"name": "S. Gnabry",   "number": 10, "pos": "FW"},
    ],
    "ESP": [
        {"name": "U. Simón",    "number": 23, "pos": "GK"},
        {"name": "A. Morata",   "number": 7,  "pos": "FW"},
        {"name": "P. Pedri",    "number": 26, "pos": "MF"},
        {"name": "G. Rodríguez","number": 14, "pos": "MF"},
        {"name": "F. Torres",   "number": 19, "pos": "FW"},
        {"name": "D. Olmo",     "number": 10, "pos": "MF"},
    ],
    "POR": [
        {"name": "R. Patrício", "number": 1,  "pos": "GK"},
        {"name": "C. Ronaldo",  "number": 7,  "pos": "FW"},
        {"name": "B. Fernandes","number": 8,  "pos": "MF"},
        {"name": "J. Félix",    "number": 11, "pos": "FW"},
        {"name": "R. Leão",     "number": 17, "pos": "FW"},
        {"name": "Bernardo S.", "number": 10, "pos": "MF"},
    ],
    "ITA": [
        {"name": "G. Donnarumma","number":1,  "pos": "GK"},
        {"name": "C. Immobile", "number": 17, "pos": "FW"},
        {"name": "L. Insigne",  "number": 10, "pos": "FW"},
        {"name": "M. Verratti","number": 6,  "pos": "MF"},
        {"name": "N. Barella",  "number": 18, "pos": "MF"},
        {"name": "F. Chiesa",   "number": 14, "pos": "FW"},
    ],
    "NED": [
        {"name": "A. Flekken",  "number": 1,  "pos": "GK"},
        {"name": "V. van Dijk", "number": 4,  "pos": "DF"},
        {"name": "M. Depay",    "number": 10, "pos": "FW"},
        {"name": "D. Dumfries", "number": 22, "pos": "MF"},
        {"name": "F. de Jong",  "number": 21, "pos": "MF"},
        {"name": "C. Gakpo",    "number": 11, "pos": "FW"},
    ],
    "USA": [
        {"name": "M. Turner",   "number": 1,  "pos": "GK"},
        {"name": "C. Pulisic",  "number": 10, "pos": "FW"},
        {"name": "G. Reyna",    "number": 7,  "pos": "MF"},
        {"name": "W. McKennie", "number": 8,  "pos": "MF"},
        {"name": "J. Sargent",  "number": 9,  "pos": "FW"},
        {"name": "Y. Musah",    "number": 6,  "pos": "MF"},
    ],
    "MEX": [
        {"name": "G. Ochoa",    "number": 13, "pos": "GK"},
        {"name": "H. Lozano",   "number": 22, "pos": "FW"},
        {"name": "R. Jiménez",  "number": 9,  "pos": "FW"},
        {"name": "A. Guardado", "number": 18, "pos": "MF"},
        {"name": "C. Vela",     "number": 11, "pos": "FW"},
        {"name": "H. Herrera",  "number": 16, "pos": "MF"},
    ],
}

def get_default_squad(team_id):
    if team_id in DEFAULT_SQUAD:
        return [p.copy() for p in DEFAULT_SQUAD[team_id]]
    team = TEAMS.get(team_id, {})
    return [
        {"name": f"Player {i+1}", "number": i+1, "pos": "GK" if i == 0 else "FW"}
        for i in range(6)
    ]

# ═══════════════════════════════════════════════════════════════
#  PITCH WIDGET  (animated football pitch + goal)
# ═══════════════════════════════════════════════════════════════
class PitchWidget(QWidget):
    shot_taken = pyqtSignal(int, int)  # col(0-2), row(0-1)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.theme = "dark"
        self._anim_t = 0.0
        self._ball_x = 0.5
        self._ball_y = 0.85
        self._ball_target_x = 0.5
        self._ball_target_y = 0.85
        self._ball_animating = False
        self._ball_anim_progress = 0.0
        self._ball_start_x = 0.5
        self._ball_start_y = 0.85
        self._result = None  # "goal" / "save" / "miss"
        self._result_alpha = 0
        self._gk_x = 0.5
        self._gk_target_x = 0.5
        self._gk_animating = False
        self._gk_anim_progress = 0.0
        self._hover_col = -1
        self._hover_row = -1
        self._aim_col = -1
        self._aim_row = -1
        self._interactive = False
        self._crowd_dots = [(random.uniform(0,1), random.uniform(0,1), random.uniform(2,5)) for _ in range(200)]
        self._timer = QTimer(self)
        self._timer.timeout.connect(self._tick)
        self._timer.start(16)
        self.setMouseTracking(True)
        self.setCursor(Qt.CursorShape.CrossCursor)

    def set_theme(self, t): self.theme = t

    def set_interactive(self, v):
        self._interactive = v
        self._aim_col = -1
        self._aim_row = -1

    def _tick(self):
        self._anim_t += 0.02
        if self._ball_animating:
            self._ball_anim_progress = min(1.0, self._ball_anim_progress + 0.04)
            t = self._ball_anim_progress
            ease = t * t * (3 - 2 * t)
            self._ball_x = self._ball_start_x + (self._ball_target_x - self._ball_start_x) * ease
            self._ball_y = self._ball_start_y + (self._ball_target_y - self._ball_start_y) * ease
            if self._ball_anim_progress >= 1.0:
                self._ball_animating = False
        if self._gk_animating:
            self._gk_anim_progress = min(1.0, self._gk_anim_progress + 0.05)
            t = self._gk_anim_progress
            ease = t * t * (3 - 2 * t)
            self._gk_x = 0.5 + (self._gk_target_x - 0.5) * ease
            if self._gk_anim_progress >= 1.0:
                self._gk_animating = False
        if self._result is not None:
            self._result_alpha = min(255, self._result_alpha + 8)
        self.update()

    def animate_shot(self, col, row, result, gk_col):
        # col: 0=left,1=center,2=right  row: 0=top,1=bottom
        tx = [0.2, 0.5, 0.8][col]
        ty = [0.22, 0.38][row]
        self._ball_start_x = self._ball_x
        self._ball_start_y = self._ball_y
        self._ball_target_x = tx
        self._ball_target_y = ty
        self._ball_animating = True
        self._ball_anim_progress = 0.0
        self._gk_target_x = [0.25, 0.5, 0.75][gk_col]
        self._gk_animating = True
        self._gk_anim_progress = 0.0
        self._result = result
        self._result_alpha = 0

    def reset_ball(self):
        self._ball_x = 0.5
        self._ball_y = 0.85
        self._ball_animating = False
        self._gk_x = 0.5
        self._gk_animating = False
        self._result = None
        self._result_alpha = 0
        self._aim_col = -1
        self._aim_row = -1

    def mouseMoveEvent(self, e):
        if not self._interactive:
            return
        w, h = self.width(), self.height()
        gw = w * 0.7
        gx = (w - gw) / 2
        goal_top = h * 0.15
        goal_bot = h * 0.45
        goal_h = goal_bot - goal_top
        mx, my = e.position().x(), e.position().y()
        if gx <= mx <= gx + gw and goal_top <= my <= goal_bot:
            col = int((mx - gx) / (gw / 3))
            row = int((my - goal_top) / (goal_h / 2))
            self._hover_col = max(0, min(2, col))
            self._hover_row = max(0, min(1, row))
        else:
            self._hover_col = -1
            self._hover_row = -1

    def mousePressEvent(self, e):
        if not self._interactive:
            return
        if self._hover_col >= 0 and self._hover_row >= 0:
            self._aim_col = self._hover_col
            self._aim_row = self._hover_row
            self.shot_taken.emit(self._aim_col, self._aim_row)

    def paintEvent(self, e):
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        th = THEMES[self.theme]
        w, h = self.width(), self.height()
        self._draw_background(p, w, h, th)
        self._draw_pitch(p, w, h, th)
        self._draw_goal(p, w, h, th)
        self._draw_aim_zones(p, w, h, th)
        self._draw_goalkeeper(p, w, h, th)
        self._draw_ball(p, w, h, th)
        self._draw_result_overlay(p, w, h)
        p.end()

    def _draw_background(self, p, w, h, th):
        grad = QLinearGradient(0, 0, 0, h)
        grad.setColorAt(0, QColor("#1a0a2e") if self.theme == "dark" else QColor("#87CEEB"))
        grad.setColorAt(0.5, QColor("#0d1220") if self.theme == "dark" else QColor("#98D8C8"))
        grad.setColorAt(1, QColor(th["pitch"]))
        p.fillRect(0, 0, w, h, grad)
        # crowd
        for cx, cy, sz in self._crowd_dots:
            px = int(cx * w)
            py = int(cy * h * 0.35)
            alpha = int(80 + 40 * math.sin(self._anim_t + cx * 10))
            c = QColor(255, 220, 180, alpha)
            p.setBrush(c)
            p.setPen(Qt.PenStyle.NoPen)
            p.drawEllipse(px - int(sz/2), py - int(sz/2), int(sz), int(sz))

    def _draw_pitch(self, p, w, h, th):
        # grass stripes
        stripe_w = w / 8
        for i in range(8):
            c = QColor(th["pitch"]) if i % 2 == 0 else QColor(th["pitch2"])
            p.fillRect(int(i * stripe_w), int(h * 0.4), int(stripe_w) + 1, int(h * 0.6), c)
        # penalty spot
        p.setBrush(QColor(255, 255, 255, 180))
        p.setPen(Qt.PenStyle.NoPen)
        p.drawEllipse(int(w * 0.5) - 4, int(h * 0.82) - 4, 8, 8)
        # penalty arc
        pen = QPen(QColor(255, 255, 255, 80), 2)
        p.setPen(pen)
        p.setBrush(Qt.BrushStyle.NoBrush)
        p.drawArc(int(w * 0.3), int(h * 0.55), int(w * 0.4), int(h * 0.3), 0, 180 * 16)

    def _draw_goal(self, p, w, h, th):
        gw = w * 0.7
        gx = (w - gw) / 2
        goal_top = h * 0.15
        goal_bot = h * 0.45
        goal_h = goal_bot - goal_top
        post_color = QColor(th["post"])
        net_color = QColor(th["net"])
        # net background
        net_grad = QLinearGradient(gx, goal_top, gx, goal_bot)
        net_grad.setColorAt(0, QColor(0, 0, 0, 120))
        net_grad.setColorAt(1, QColor(0, 0, 0, 40))
        p.fillRect(int(gx), int(goal_top), int(gw), int(goal_h), net_grad)
        # net lines horizontal
        p.setPen(QPen(QColor(th["net"] + "60"), 1))
        rows = 8
        for i in range(rows + 1):
            y = goal_top + i * goal_h / rows
            p.drawLine(int(gx), int(y), int(gx + gw), int(y))
        # net lines vertical
        cols = 12
        for i in range(cols + 1):
            x = gx + i * gw / cols
            p.drawLine(int(x), int(goal_top), int(x), int(goal_bot))
        # posts
        post_w = 6
        p.setBrush(post_color)
        p.setPen(QPen(QColor(200, 200, 200), 1))
        # left post
        p.drawRect(int(gx) - post_w, int(goal_top), post_w, int(goal_h))
        # right post
        p.drawRect(int(gx + gw), int(goal_top), post_w, int(goal_h))
        # crossbar
        p.drawRect(int(gx) - post_w, int(goal_top) - post_w, int(gw) + post_w * 2, post_w)
        # goal line
        p.setPen(QPen(QColor(255, 255, 255, 200), 3))
        p.drawLine(int(gx), int(goal_bot), int(gx + gw), int(goal_bot))
        # zone dividers (aim zones)
        if self._interactive or self._aim_col >= 0:
            p.setPen(QPen(QColor(255, 255, 255, 40), 1, Qt.PenStyle.DashLine))
            p.drawLine(int(gx + gw / 3), int(goal_top), int(gx + gw / 3), int(goal_bot))
            p.drawLine(int(gx + 2 * gw / 3), int(goal_top), int(gx + 2 * gw / 3), int(goal_bot))
            p.drawLine(int(gx), int(goal_top + goal_h / 2), int(gx + gw), int(goal_top + goal_h / 2))

    def _draw_aim_zones(self, p, w, h, th):
        gw = w * 0.7
        gx = (w - gw) / 2
        goal_top = h * 0.15
        goal_bot = h * 0.45
        goal_h = goal_bot - goal_top
        zone_w = gw / 3
        zone_h = goal_h / 2
        for row in range(2):
            for col in range(3):
                zx = gx + col * zone_w
                zy = goal_top + row * zone_h
                if self._aim_col == col and self._aim_row == row:
                    p.fillRect(int(zx), int(zy), int(zone_w), int(zone_h),
                               QColor(255, 50, 50, 80))
                    p.setPen(QPen(QColor(255, 100, 100, 200), 2))
                    p.drawRect(int(zx), int(zy), int(zone_w), int(zone_h))
                elif self._hover_col == col and self._hover_row == row and self._interactive:
                    p.fillRect(int(zx), int(zy), int(zone_w), int(zone_h),
                               QColor(255, 255, 100, 50))
                    p.setPen(QPen(QColor(255, 255, 100, 150), 2))
                    p.drawRect(int(zx), int(zy), int(zone_w), int(zone_h))

    def _draw_goalkeeper(self, p, w, h, th):
        gw = w * 0.7
        gx = (w - gw) / 2
        goal_bot = h * 0.45
        gk_cx = gx + self._gk_x * gw
        gk_y = goal_bot - h * 0.12
        gk_h = h * 0.1
        gk_w = w * 0.05
        # body
        body_color = QColor("#FF6600")
        p.setBrush(body_color)
        p.setPen(QPen(QColor(0, 0, 0, 150), 1))
        p.drawRoundedRect(int(gk_cx - gk_w / 2), int(gk_y), int(gk_w), int(gk_h), 4, 4)
        # head
        head_r = gk_w * 0.6
        p.setBrush(QColor("#FDBCB4"))
        p.drawEllipse(int(gk_cx - head_r / 2), int(gk_y - head_r), int(head_r), int(head_r))
        # arms
        p.setPen(QPen(body_color, max(2, int(gk_w * 0.3))))
        p.drawLine(int(gk_cx - gk_w), int(gk_y + gk_h * 0.3),
                   int(gk_cx + gk_w), int(gk_y + gk_h * 0.3))

    def _draw_ball(self, p, w, h, th):
        bx = int(self._ball_x * w)
        by = int(self._ball_y * h)
        # scale ball based on y position (perspective)
        scale = 0.5 + 0.5 * (self._ball_y - 0.15) / 0.7
        r = max(4, int(w * 0.025 * scale))
        # shadow
        p.setBrush(QColor(0, 0, 0, 80))
        p.setPen(Qt.PenStyle.NoPen)
        p.drawEllipse(bx - r, by + r // 2, r * 2, r)
        # ball
        ball_grad = QRadialGradient(bx - r // 3, by - r // 3, r * 2)
        ball_grad.setColorAt(0, QColor(255, 255, 255))
        ball_grad.setColorAt(0.4, QColor(220, 220, 220))
        ball_grad.setColorAt(1, QColor(50, 50, 50))
        p.setBrush(ball_grad)
        p.setPen(QPen(QColor(30, 30, 30), 1))
        p.drawEllipse(bx - r, by - r, r * 2, r * 2)
        # pentagon pattern
        p.setPen(QPen(QColor(30, 30, 30, 180), 1))
        p.setBrush(QColor(30, 30, 30, 120))
        pts = []
        for i in range(5):
            angle = math.radians(i * 72 - 90)
            pts.append(QPointF(bx + r * 0.45 * math.cos(angle + self._anim_t * 0.5),
                               by + r * 0.45 * math.sin(angle + self._anim_t * 0.5)))
        poly = QPolygonF(pts)
        p.drawPolygon(poly)

    def _draw_result_overlay(self, p, w, h):
        if self._result is None or self._result_alpha == 0:
            return
        alpha = self._result_alpha
        if self._result == "goal":
            color = QColor(50, 255, 50, alpha)
            text = "GOAL!"
        elif self._result == "save":
            color = QColor(255, 100, 50, alpha)
            text = "SAVED!"
        else:
            color = QColor(255, 50, 50, alpha)
            text = "MISS!"
        p.fillRect(0, int(h * 0.35), w, int(h * 0.25), QColor(0, 0, 0, alpha // 2))
        font = QFont("Arial Black", max(20, w // 12), QFont.Weight.Black)
        p.setFont(font)
        p.setPen(QPen(color, 2))
        p.drawText(QRect(0, int(h * 0.35), w, int(h * 0.25)),
                   Qt.AlignmentFlag.AlignCenter, text)


# ═══════════════════════════════════════════════════════════════
#  STYLED BUTTON
# ═══════════════════════════════════════════════════════════════
class GlowButton(QPushButton):
    def __init__(self, text, parent=None, accent=None, size="normal"):
        super().__init__(text, parent)
        self._accent = accent or "#00d4ff"
        self._size = size
        self._hovered = False
        self._pressed = False
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        if size == "large":
            self.setMinimumHeight(56)
            self.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        elif size == "small":
            self.setMinimumHeight(32)
            self.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        else:
            self.setMinimumHeight(44)
            self.setFont(QFont("Arial", 12, QFont.Weight.Bold))

    def enterEvent(self, e):
        self._hovered = True
        self.update()

    def leaveEvent(self, e):
        self._hovered = False
        self.update()

    def mousePressEvent(self, e):
        self._pressed = True
        self.update()
        super().mousePressEvent(e)

    def mouseReleaseEvent(self, e):
        self._pressed = False
        self.update()
        super().mouseReleaseEvent(e)

    def paintEvent(self, e):
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        r = self.rect()
        acc = QColor(self._accent)
        if self._pressed:
            alpha = 220
            scale = 0.97
        elif self._hovered:
            alpha = 180
            scale = 1.0
        else:
            alpha = 120
            scale = 1.0
        # glow
        if self._hovered:
            glow = QColor(acc.red(), acc.green(), acc.blue(), 40)
            p.setBrush(glow)
            p.setPen(Qt.PenStyle.NoPen)
            p.drawRoundedRect(r.adjusted(-3, -3, 3, 3), 12, 12)
        # background
        bg = QColor(acc.red(), acc.green(), acc.blue(), alpha)
        grad = QLinearGradient(0, 0, 0, r.height())
        grad.setColorAt(0, QColor(acc.red(), acc.green(), acc.blue(), min(255, alpha + 40)))
        grad.setColorAt(1, QColor(acc.red() // 2, acc.green() // 2, acc.blue() // 2, alpha))
        p.setBrush(grad)
        p.setPen(QPen(acc, 2))
        p.drawRoundedRect(r.adjusted(1, 1, -1, -1), 8, 8)
        # text
        p.setPen(QColor(255, 255, 255))
        p.setFont(self.font())
        p.drawText(r, Qt.AlignmentFlag.AlignCenter, self.text())
        p.end()


# ═══════════════════════════════════════════════════════════════
#  TEAM CARD WIDGET
# ═══════════════════════════════════════════════════════════════
class TeamCard(QWidget):
    clicked = pyqtSignal(str)

    def __init__(self, team_id, theme="dark", parent=None):
        super().__init__(parent)
        self.team_id = team_id
        self.theme = theme
        self._selected = False
        self._hovered = False
        self.setFixedSize(110, 90)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setMouseTracking(True)

    def set_selected(self, v):
        self._selected = v
        self.update()

    def enterEvent(self, e):
        self._hovered = True
        self.update()

    def leaveEvent(self, e):
        self._hovered = False
        self.update()

    def mousePressEvent(self, e):
        self.clicked.emit(self.team_id)

    def paintEvent(self, e):
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        th = THEMES[self.theme]
        team = TEAMS[self.team_id]
        r = self.rect().adjusted(2, 2, -2, -2)
        # background
        if self._selected:
            bg = QColor(team["color"])
            bg.setAlpha(200)
        elif self._hovered:
            bg = QColor(th["card2"])
        else:
            bg = QColor(th["card"])
        p.setBrush(bg)
        border_color = QColor(team["color"]) if self._selected else QColor(th["border"])
        p.setPen(QPen(border_color, 2 if self._selected else 1))
        p.drawRoundedRect(r, 8, 8)
        # jersey color strip
        jersey = QColor(team["color"])
        p.fillRect(r.x(), r.y(), r.width(), 8, jersey)
        # flag emoji
        p.setFont(QFont("Segoe UI Emoji", 22))
        p.setPen(Qt.PenStyle.NoPen)
        p.drawText(QRect(r.x(), r.y() + 8, r.width(), 40),
                   Qt.AlignmentFlag.AlignCenter, team["flag"])
        # name
        p.setPen(QColor(th["text"]))
        p.setFont(QFont("Arial", 7, QFont.Weight.Bold))
        p.drawText(QRect(r.x(), r.y() + 52, r.width(), 20),
                   Qt.AlignmentFlag.AlignCenter, team["name"])
        # group badge
        p.setFont(QFont("Arial", 7))
        p.setPen(QColor(th["text2"]))
        p.drawText(QRect(r.x(), r.y() + 68, r.width(), 14),
                   Qt.AlignmentFlag.AlignCenter, f"Group {team['group']}")
        p.end()


# ═══════════════════════════════════════════════════════════════
#  STADIUM CARD
# ═══════════════════════════════════════════════════════════════
class StadiumCard(QWidget):
    clicked = pyqtSignal(str)

    def __init__(self, stadium_id, theme="dark", parent=None):
        super().__init__(parent)
        self.stadium_id = stadium_id
        self.theme = theme
        self._selected = False
        self._hovered = False
        self.setFixedSize(200, 80)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

    def set_selected(self, v):
        self._selected = v
        self.update()

    def enterEvent(self, e):
        self._hovered = True
        self.update()

    def leaveEvent(self, e):
        self._hovered = False
        self.update()

    def mousePressEvent(self, e):
        self.clicked.emit(self.stadium_id)

    def paintEvent(self, e):
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        th = THEMES[self.theme]
        st = STADIUMS[self.stadium_id]
        r = self.rect().adjusted(2, 2, -2, -2)
        bg = QColor(th["card2"]) if self._selected else (QColor(th["card2"]) if self._hovered else QColor(th["card"]))
        p.setBrush(bg)
        border = QColor(th["acc"]) if self._selected else QColor(th["border"])
        p.setPen(QPen(border, 2 if self._selected else 1))
        p.drawRoundedRect(r, 8, 8)
        p.setFont(QFont("Segoe UI Emoji", 18))
        p.drawText(QRect(r.x() + 4, r.y(), 36, r.height()), Qt.AlignmentFlag.AlignCenter, "🏟️")
        p.setPen(QColor(th["text"]))
        p.setFont(QFont("Arial", 8, QFont.Weight.Bold))
        p.drawText(QRect(r.x() + 44, r.y() + 8, r.width() - 48, 20),
                   Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter, st["name"])
        p.setPen(QColor(th["text2"]))
        p.setFont(QFont("Arial", 7))
        p.drawText(QRect(r.x() + 44, r.y() + 28, r.width() - 48, 16),
                   Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter, st["city"])
        p.drawText(QRect(r.x() + 44, r.y() + 44, r.width() - 48, 16),
                   Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter,
                   f"Cap: {st['capacity']:,}")
        p.end()


# ═══════════════════════════════════════════════════════════════
#  SCORE DISPLAY WIDGET
# ═══════════════════════════════════════════════════════════════
class ScoreWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.theme = "dark"
        self.team1_id = "ARG"
        self.team2_id = "BRA"
        self.score1 = 0
        self.score2 = 0
        self.round_num = 1
        self.max_rounds = 5
        self.shots1 = []  # list of True/False/None
        self.shots2 = []
        self.phase = "normal"
        self.setMinimumHeight(100)

    def update_state(self, t1, t2, s1, s2, rnd, maxr, sh1, sh2, phase="normal"):
        self.team1_id = t1
        self.team2_id = t2
        self.score1 = s1
        self.score2 = s2
        self.round_num = rnd
        self.max_rounds = maxr
        self.shots1 = sh1
        self.shots2 = sh2
        self.phase = phase
        self.update()

    def paintEvent(self, e):
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        th = THEMES[self.theme]
        w, h = self.width(), self.height()
        # background
        p.fillRect(0, 0, w, h, QColor(th["card"]))
        t1 = TEAMS.get(self.team1_id, {})
        t2 = TEAMS.get(self.team2_id, {})
        # team 1 flag
        p.setFont(QFont("Segoe UI Emoji", 20))
        p.drawText(QRect(10, 5, 50, 50), Qt.AlignmentFlag.AlignCenter, t1.get("flag", "🏳️"))
        # team 2 flag
        p.drawText(QRect(w - 60, 5, 50, 50), Qt.AlignmentFlag.AlignCenter, t2.get("flag", "🏳️"))
        # score
        p.setFont(QFont("Arial Black", 28, QFont.Weight.Black))
        p.setPen(QColor(th["text"]))
        p.drawText(QRect(w // 2 - 60, 5, 50, 50), Qt.AlignmentFlag.AlignCenter, str(self.score1))
        p.setFont(QFont("Arial", 20))
        p.setPen(QColor(th["text2"]))
        p.drawText(QRect(w // 2 - 10, 5, 20, 50), Qt.AlignmentFlag.AlignCenter, "-")
        p.setFont(QFont("Arial Black", 28, QFont.Weight.Black))
        p.setPen(QColor(th["text"]))
        p.drawText(QRect(w // 2 + 10, 5, 50, 50), Qt.AlignmentFlag.AlignCenter, str(self.score2))
        # shot indicators
        dot_r = 8
        dot_spacing = 20
        total = self.max_rounds
        start_x1 = w // 2 - (total * dot_spacing) // 2 - dot_spacing
        start_x2 = w // 2 + dot_spacing // 2
        for i in range(total):
            # team 1
            dx = start_x1 + i * dot_spacing
            dy = h - 22
            if i < len(self.shots1):
                color = QColor("#00ff88") if self.shots1[i] else QColor("#ff4444")
            else:
                color = QColor(th["border"])
            p.setBrush(color)
            p.setPen(QPen(QColor(th["text2"]), 1))
            p.drawEllipse(dx, dy, dot_r, dot_r)
            # team 2
            dx2 = start_x2 + i * dot_spacing
            if i < len(self.shots2):
                color2 = QColor("#00ff88") if self.shots2[i] else QColor("#ff4444")
            else:
                color2 = QColor(th["border"])
            p.setBrush(color2)
            p.drawEllipse(dx2, dy, dot_r, dot_r)
        # phase label
        if self.phase == "sudden":
            p.setFont(QFont("Arial", 9, QFont.Weight.Bold))
            p.setPen(QColor("#ff6600"))
            p.drawText(QRect(0, h - 38, w, 16), Qt.AlignmentFlag.AlignCenter, "⚡ SUDDEN DEATH")
        p.end()


# ═══════════════════════════════════════════════════════════════
#  GAME STATE / LOGIC
# ═══════════════════════════════════════════════════════════════
class PenaltyGame:
    def __init__(self, team1_id, team2_id, squad1, squad2, stadium_id):
        self.team1_id = team1_id
        self.team2_id = team2_id
        self.squad1 = squad1
        self.squad2 = squad2
        self.stadium_id = stadium_id
        self.score1 = 0
        self.score2 = 0
        self.round_num = 0
        self.max_rounds = 5
        self.shots1 = []
        self.shots2 = []
        self.phase = "normal"  # "normal" or "sudden"
        self.current_team = 1  # 1 or 2
        self.finished = False
        self.winner = None
        self.shooter_idx1 = 0
        self.shooter_idx2 = 0

    def get_current_shooter(self):
        if self.current_team == 1:
            shooters = [p for p in self.squad1 if p["pos"] != "GK"]
            if not shooters:
                shooters = self.squad1
            idx = self.shooter_idx1 % len(shooters)
            return shooters[idx]
        else:
            shooters = [p for p in self.squad2 if p["pos"] != "GK"]
            if not shooters:
                shooters = self.squad2
            idx = self.shooter_idx2 % len(shooters)
            return shooters[idx]

    def get_goalkeeper(self, team):
        squad = self.squad1 if team == 1 else self.squad2
        for p in squad:
            if p["pos"] == "GK":
                return p
        return squad[0] if squad else {"name": "GK", "number": 1}

    def cpu_choose_shot(self):
        col = random.randint(0, 2)
        row = random.randint(0, 1)
        return col, row

    def cpu_choose_dive(self):
        return random.randint(0, 2)

    def resolve_shot(self, shot_col, shot_row, gk_col):
        # gk_col: 0=left, 1=center, 2=right
        # If GK dives to same column as shot → save (with some probability)
        if gk_col == shot_col:
            save_prob = 0.75 if shot_row == 1 else 0.55
            if random.random() < save_prob:
                return "save"
        # Miss probability
        miss_prob = 0.08
        if random.random() < miss_prob:
            return "miss"
        return "goal"

    def record_shot(self, result):
        scored = result == "goal"
        if self.current_team == 1:
            self.shots1.append(scored)
            if scored:
                self.score1 += 1
            self.shooter_idx1 += 1
        else:
            self.shots2.append(scored)
            if scored:
                self.score2 += 1
            self.shooter_idx2 += 1

    def advance_turn(self):
        if self.current_team == 1:
            self.current_team = 2
        else:
            self.current_team = 1
            self.round_num += 1
            self._check_phase()

    def _check_phase(self):
        if self.phase == "normal":
            if self.round_num >= self.max_rounds:
                if self.score1 != self.score2:
                    self.finished = True
                    self.winner = 1 if self.score1 > self.score2 else 2
                else:
                    self.phase = "sudden"
                    self.max_rounds = self.round_num + 1
            else:
                # Early finish check
                remaining = self.max_rounds - self.round_num
                if self.score1 > self.score2 + remaining:
                    self.finished = True
                    self.winner = 1
                elif self.score2 > self.score1 + remaining:
                    self.finished = True
                    self.winner = 2
        else:
            # sudden death
            if len(self.shots1) == len(self.shots2):
                if self.score1 != self.score2:
                    self.finished = True
                    self.winner = 1 if self.score1 > self.score2 else 2
                else:
                    self.max_rounds += 1

    def is_round_complete(self):
        return len(self.shots1) == len(self.shots2)


# ═══════════════════════════════════════════════════════════════
#  SCREENS
# ═══════════════════════════════════════════════════════════════
class BaseScreen(QWidget):
    def __init__(self, app_ref, parent=None):
        super().__init__(parent)
        self.app = app_ref

    def tr(self, key):
        return TR.get(self.app.lang, TR["en"]).get(key, key)

    def paintEvent(self, e):
        p = QPainter(self)
        th = THEMES[self.app.theme]
        p.fillRect(self.rect(), QColor(th["bg"]))
        p.end()


# ───────────────────────────────────────────────
#  MAIN MENU
# ───────────────────────────────────────────────
class MenuScreen(BaseScreen):
    def __init__(self, app_ref, parent=None):
        super().__init__(app_ref, parent)
        self._build_ui()
        self._anim_t = 0.0
        self._timer = QTimer(self)
        self._timer.timeout.connect(self._tick)
        self._timer.start(16)

    def _tick(self):
        self._anim_t += 0.01
        self.update()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(16)
        layout.setContentsMargins(40, 40, 40, 40)

        # Spacer top
        layout.addStretch(2)

        # Title
        self.lbl_title = QLabel(self.tr("title"))
        self.lbl_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_title.setFont(QFont("Arial Black", 36, QFont.Weight.Black))
        layout.addWidget(self.lbl_title)

        self.lbl_sub = QLabel(self.tr("subtitle"))
        self.lbl_sub.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_sub.setFont(QFont("Arial", 16))
        layout.addWidget(self.lbl_sub)

        layout.addStretch(1)

        self.btn_play = GlowButton(self.tr("play"), size="large", accent="#00ff88")
        self.btn_play.setMinimumWidth(220)
        self.btn_play.clicked.connect(self.app.go_team_select)
        layout.addWidget(self.btn_play, alignment=Qt.AlignmentFlag.AlignCenter)

        self.btn_settings = GlowButton(self.tr("settings"), size="normal", accent="#00d4ff")
        self.btn_settings.setMinimumWidth(220)
        self.btn_settings.clicked.connect(self.app.go_settings)
        layout.addWidget(self.btn_settings, alignment=Qt.AlignmentFlag.AlignCenter)

        self.btn_quit = GlowButton(self.tr("quit"), size="normal", accent="#ff4444")
        self.btn_quit.setMinimumWidth(220)
        self.btn_quit.clicked.connect(self.app.quit_app)
        layout.addWidget(self.btn_quit, alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addStretch(2)

    def paintEvent(self, e):
        p = QPainter(self)
        th = THEMES[self.app.theme]
        w, h = self.width(), self.height()
        # animated gradient background
        grad = QLinearGradient(0, 0, w, h)
        grad.setColorAt(0, QColor(th["bg"]))
        grad.setColorAt(0.5, QColor(th["bg2"]))
        grad.setColorAt(1, QColor(th["bg3"]))
        p.fillRect(0, 0, w, h, grad)
        # floating circles
        for i in range(8):
            angle = self._anim_t + i * math.pi / 4
            cx = int(w * 0.5 + math.cos(angle) * w * 0.35)
            cy = int(h * 0.5 + math.sin(angle * 0.7) * h * 0.3)
            r = 30 + i * 15
            c = QColor(0, 212, 255, 15)
            p.setBrush(c)
            p.setPen(Qt.PenStyle.NoPen)
            p.drawEllipse(cx - r, cy - r, r * 2, r * 2)
        p.end()
        super().paintEvent(e)

    def refresh(self):
        self.lbl_title.setText(self.tr("title"))
        self.lbl_sub.setText(self.tr("subtitle"))
        self.btn_play.setText(self.tr("play"))
        self.btn_settings.setText(self.tr("settings"))
        self.btn_quit.setText(self.tr("quit"))
        th = THEMES[self.app.theme]
        self.lbl_title.setStyleSheet(f"color: {th['acc']}; background: transparent;")
        self.lbl_sub.setStyleSheet(f"color: {th['text2']}; background: transparent;")


# ───────────────────────────────────────────────
#  SETTINGS SCREEN
# ───────────────────────────────────────────────
class SettingsScreen(BaseScreen):
    def __init__(self, app_ref, parent=None):
        super().__init__(app_ref, parent)
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(60, 40, 60, 40)
        layout.setSpacing(20)

        self.lbl_title = QLabel(self.tr("settings"))
        self.lbl_title.setFont(QFont("Arial Black", 24, QFont.Weight.Black))
        self.lbl_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.lbl_title)

        layout.addStretch(1)

        # Theme
        row_theme = QHBoxLayout()
        self.lbl_theme = QLabel(self.tr("theme") + ":")
        self.lbl_theme.setFont(QFont("Arial", 13))
        row_theme.addWidget(self.lbl_theme)
        row_theme.addStretch()
        self.btn_dark = GlowButton(self.tr("dark"), accent="#334466", size="small")
        self.btn_dark.setMinimumWidth(90)
        self.btn_dark.clicked.connect(lambda: self.app.set_theme("dark"))
        row_theme.addWidget(self.btn_dark)
        self.btn_light = GlowButton(self.tr("light"), accent="#aabbcc", size="small")
        self.btn_light.setMinimumWidth(90)
        self.btn_light.clicked.connect(lambda: self.app.set_theme("light"))
        row_theme.addWidget(self.btn_light)
        layout.addLayout(row_theme)

        # Language
        row_lang = QHBoxLayout()
        self.lbl_lang = QLabel(self.tr("language") + ":")
        self.lbl_lang.setFont(QFont("Arial", 13))
        row_lang.addWidget(self.lbl_lang)
        row_lang.addStretch()
        for code, label in [("en", "English"), ("fa", "فارسی"), ("zh", "中文")]:
            btn = GlowButton(label, accent="#00d4ff", size="small")
            btn.setMinimumWidth(80)
            btn.clicked.connect(lambda _, c=code: self.app.set_lang(c))
            row_lang.addWidget(btn)
        layout.addLayout(row_lang)

        layout.addStretch(2)

        self.btn_back = GlowButton(self.tr("back"), accent="#ff6600", size="normal")
        self.btn_back.setMinimumWidth(160)
        self.btn_back.clicked.connect(self.app.go_menu)
        layout.addWidget(self.btn_back, alignment=Qt.AlignmentFlag.AlignCenter)

    def refresh(self):
        th = THEMES[self.app.theme]
        self.lbl_title.setStyleSheet(f"color: {th['acc']}; background: transparent;")
        self.lbl_theme.setStyleSheet(f"color: {th['text']}; background: transparent;")
        self.lbl_lang.setStyleSheet(f"color: {th['text']}; background: transparent;")
        self.lbl_title.setText(self.tr("settings"))
        self.btn_back.setText(self.tr("back"))


# ───────────────────────────────────────────────
#  TEAM SELECT SCREEN
# ───────────────────────────────────────────────
class TeamSelectScreen(BaseScreen):
    def __init__(self, app_ref, parent=None):
        super().__init__(app_ref, parent)
        self.selected_team = None
        self.selected_opponent = None
        self.selected_stadium = None
        self.step = 0  # 0=team, 1=opponent, 2=stadium
        self._team_cards = {}
        self._opp_cards = {}
        self._stadium_cards = {}
        self._build_ui()

    def _build_ui(self):
        self._main_layout = QVBoxLayout(self)
        self._main_layout.setContentsMargins(20, 20, 20, 20)
        self._main_layout.setSpacing(10)

        self.lbl_title = QLabel()
        self.lbl_title.setFont(QFont("Arial Black", 18, QFont.Weight.Black))
        self.lbl_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._main_layout.addWidget(self.lbl_title)

        # Stacked pages
        self._stack = QStackedWidget()
        self._main_layout.addWidget(self._stack, 1)

        self._build_team_page()
        self._build_opponent_page()
        self._build_stadium_page()

        # Bottom buttons
        row = QHBoxLayout()
        self.btn_back = GlowButton(self.tr("back"), accent="#ff6600", size="small")
        self.btn_back.clicked.connect(self._go_back)
        row.addWidget(self.btn_back)
        row.addStretch()
        self.btn_next = GlowButton(self.tr("next"), accent="#00ff88", size="normal")
        self.btn_next.setMinimumWidth(160)
        self.btn_next.clicked.connect(self._go_next)
        self.btn_next.setEnabled(False)
        row.addWidget(self.btn_next)
        self._main_layout.addLayout(row)

        self._update_title()

    def _build_team_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        container = QWidget()
        grid = QGridLayout(container)
        grid.setSpacing(6)
        teams = list(TEAMS.keys())
        for i, tid in enumerate(teams):
            card = TeamCard(tid, self.app.theme)
            card.clicked.connect(lambda t=tid: self._select_team(t))
            self._team_cards[tid] = card
            grid.addWidget(card, i // 6, i % 6)
        scroll.setWidget(container)
        layout.addWidget(scroll)
        self._stack.addWidget(page)

    def _build_opponent_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        container = QWidget()
        grid = QGridLayout(container)
        grid.setSpacing(6)
        teams = list(TEAMS.keys())
        for i, tid in enumerate(teams):
            card = TeamCard(tid, self.app.theme)
            card.clicked.connect(lambda t=tid: self._select_opponent(t))
            self._opp_cards[tid] = card
            grid.addWidget(card, i // 6, i % 6)
        scroll.setWidget(container)
        layout.addWidget(scroll)
        self._stack.addWidget(page)

    def _build_stadium_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        container = QWidget()
        grid = QGridLayout(container)
        grid.setSpacing(8)
        stadiums = list(STADIUMS.keys())
        for i, sid in enumerate(stadiums):
            card = StadiumCard(sid, self.app.theme)
            card.clicked.connect(lambda s=sid: self._select_stadium(s))
            self._stadium_cards[sid] = card
            grid.addWidget(card, i // 3, i % 3)
        scroll.setWidget(container)
        layout.addWidget(scroll)
        self._stack.addWidget(page)

    def _select_team(self, tid):
        self.selected_team = tid
        for k, c in self._team_cards.items():
            c.set_selected(k == tid)
        self.btn_next.setEnabled(True)

    def _select_opponent(self, tid):
        self.selected_opponent = tid
        for k, c in self._opp_cards.items():
            c.set_selected(k == tid)
        self.btn_next.setEnabled(True)

    def _select_stadium(self, sid):
        self.selected_stadium = sid
        for k, c in self._stadium_cards.items():
            c.set_selected(k == sid)
        self.btn_next.setEnabled(True)

    def _update_title(self):
        titles = [self.tr("select_team"), self.tr("select_opponent"), self.tr("select_stadium")]
        self.lbl_title.setText(titles[self.step])

    def _go_next(self):
        if self.step == 0 and self.selected_team:
            self.step = 1
            self._stack.setCurrentIndex(1)
            self.btn_next.setEnabled(self.selected_opponent is not None)
        elif self.step == 1 and self.selected_opponent:
            self.step = 2
            self._stack.setCurrentIndex(2)
            self.btn_next.setEnabled(self.selected_stadium is not None)
        elif self.step == 2 and self.selected_stadium:
            self.app.start_game(
                self.selected_team,
                self.selected_opponent,
                self.selected_stadium
            )
        self._update_title()

    def _go_back(self):
        if self.step == 0:
            self.app.go_menu()
        else:
            self.step -= 1
            self._stack.setCurrentIndex(self.step)
            self._update_title()
            self.btn_next.setEnabled(True)

    def refresh(self):
        th = THEMES[self.app.theme]
        self.lbl_title.setStyleSheet(f"color: {th['acc']}; background: transparent;")
        for c in self._team_cards.values():
            c.theme = self.app.theme
            c.update()
        for c in self._opp_cards.values():
            c.theme = self.app.theme
            c.update()
        for c in self._stadium_cards.values():
            c.theme = self.app.theme
            c.update()

    def reset(self):
        self.step = 0
        self.selected_team = None
        self.selected_opponent = None
        self.selected_stadium = None
        self._stack.setCurrentIndex(0)
        for c in self._team_cards.values():
            c.set_selected(False)
        for c in self._opp_cards.values():
            c.set_selected(False)
        for c in self._stadium_cards.values():
            c.set_selected(False)
        self.btn_next.setEnabled(False)
        self._update_title()


# ───────────────────────────────────────────────
#  GAME SCREEN
# ───────────────────────────────────────────────
class GameScreen(BaseScreen):
    def __init__(self, app_ref, parent=None):
        super().__init__(app_ref, parent)
        self.game = None
        self._waiting = False
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(6)

        # Score widget
        self.score_widget = ScoreWidget()
        self.score_widget.setFixedHeight(100)
        layout.addWidget(self.score_widget)

        # Status label
        self.lbl_status = QLabel()
        self.lbl_status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_status.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        layout.addWidget(self.lbl_status)

        # Pitch
        self.pitch = PitchWidget()
        self.pitch.setMinimumHeight(300)
        self.pitch.shot_taken.connect(self._on_player_shot)
        layout.addWidget(self.pitch, 1)

        # Shooter info
        self.lbl_shooter = QLabel()
        self.lbl_shooter.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_shooter.setFont(QFont("Arial", 11))
        layout.addWidget(self.lbl_shooter)

        # Shoot button
        self.btn_shoot = GlowButton(self.tr("shoot"), accent="#ff4444", size="large")
        self.btn_shoot.setMinimumWidth(200)
        self.btn_shoot.clicked.connect(self._on_shoot_btn)
        self.btn_shoot.setVisible(False)
        layout.addWidget(self.btn_shoot, alignment=Qt.AlignmentFlag.AlignCenter)

        # Menu button
        self.btn_menu = GlowButton(self.tr("menu"), accent="#666666", size="small")
        self.btn_menu.clicked.connect(self.app.go_menu)
        layout.addWidget(self.btn_menu, alignment=Qt.AlignmentFlag.AlignRight)

    def setup_game(self, game: PenaltyGame):
        self.game = game
        self.pitch.set_theme(self.app.theme)
        self.score_widget.theme = self.app.theme
        self._waiting = False
        self._update_ui()
        self._next_turn()

    def _update_score(self):
        g = self.game
        self.score_widget.update_state(
            g.team1_id, g.team2_id,
            g.score1, g.score2,
            g.round_num + 1, g.max_rounds,
            g.shots1, g.shots2,
            g.phase
        )

    def _update_ui(self):
        self._update_score()
        th = THEMES[self.app.theme]
        self.lbl_status.setStyleSheet(f"color: {th['acc']}; background: transparent;")
        self.lbl_shooter.setStyleSheet(f"color: {th['text2']}; background: transparent;")

    def _next_turn(self):
        if self.game.finished:
            QTimer.singleShot(1200, self.app.go_result)
            return

        self.pitch.reset_ball()
        self._update_score()

        g = self.game
        shooter = g.get_current_shooter()
        team_name = TEAMS[g.team1_id if g.current_team == 1 else g.team2_id]["name"]
        self.lbl_shooter.setText(f"#{shooter['number']} {shooter['name']}  —  {team_name}")

        is_player_turn = (g.current_team == 1)

        if is_player_turn:
            self.lbl_status.setText(self.tr("your_turn"))
            self.pitch.set_interactive(True)
            self.btn_shoot.setVisible(False)
        else:
            self.lbl_status.setText(self.tr("cpu_thinking"))
            self.pitch.set_interactive(False)
            self.btn_shoot.setVisible(False)
            QTimer.singleShot(1000, self._cpu_take_shot)

    def _on_player_shot(self, col, row):
        if self._waiting:
            return
        self._waiting = True
        self.pitch.set_interactive(False)
        g = self.game
        gk_col = g.cpu_choose_dive()
        result = g.resolve_shot(col, row, gk_col)
        self.pitch.animate_shot(col, row, result, gk_col)
        g.record_shot(result)
        self._update_score()
        QTimer.singleShot(2000, self._after_shot)

    def _on_shoot_btn(self):
        # fallback if user clicks shoot without aiming
        if self.pitch._aim_col >= 0:
            self._on_player_shot(self.pitch._aim_col, self.pitch._aim_row)

    def _cpu_take_shot(self):
        if self._waiting:
            return
        self._waiting = True
        g = self.game
        col, row = g.cpu_choose_shot()
        gk_col = random.randint(0, 2)  # player's GK dives randomly
        result = g.resolve_shot(col, row, gk_col)
        self.pitch.animate_shot(col, row, result, gk_col)
        g.record_shot(result)
        self._update_score()
        QTimer.singleShot(2000, self._after_shot)

    def _after_shot(self):
        self._waiting = False
        self.game.advance_turn()
        self._next_turn()

    def refresh(self):
        self.pitch.set_theme(self.app.theme)
        self.score_widget.theme = self.app.theme
        self.score_widget.update()
        th = THEMES[self.app.theme]
        self.lbl_status.setStyleSheet(f"color: {th['acc']}; background: transparent;")
        self.lbl_shooter.setStyleSheet(f"color: {th['text2']}; background: transparent;")


# ───────────────────────────────────────────────
#  RESULT SCREEN
# ───────────────────────────────────────────────
class ResultScreen(BaseScreen):
    def __init__(self, app_ref, parent=None):
        super().__init__(app_ref, parent)
        self._build_ui()
        self._anim_t = 0.0
        self._timer = QTimer(self)
        self._timer.timeout.connect(self._tick)
        self._timer.start(16)

    def _tick(self):
        self._anim_t += 0.02
        self.update()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(20)
        layout.setContentsMargins(40, 40, 40, 40)

        layout.addStretch(1)

        self.lbl_result = QLabel()
        self.lbl_result.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_result.setFont(QFont("Arial Black", 32, QFont.Weight.Black))
        layout.addWidget(self.lbl_result)

        self.lbl_score = QLabel()
        self.lbl_score.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_score.setFont(QFont("Arial", 22))
        layout.addWidget(self.lbl_score)

        self.lbl_teams = QLabel()
        self.lbl_teams.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_teams.setFont(QFont("Segoe UI Emoji", 28))
        layout.addWidget(self.lbl_teams)

        self.lbl_stadium = QLabel()
        self.lbl_stadium.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_stadium.setFont(QFont("Arial", 11))
        layout.addWidget(self.lbl_stadium)

        layout.addStretch(1)

        row = QHBoxLayout()
        self.btn_retry = GlowButton(self.tr("retry"), accent="#00ff88", size="normal")
        self.btn_retry.setMinimumWidth(140)
        self.btn_retry.clicked.connect(self.app.retry_game)
        row.addWidget(self.btn_retry)

        self.btn_menu = GlowButton(self.tr("menu"), accent="#00d4ff", size="normal")
        self.btn_menu.setMinimumWidth(140)
        self.btn_menu.clicked.connect(self.app.go_menu)
        row.addWidget(self.btn_menu)

        layout.addLayout(row)
        layout.addStretch(1)

    def show_result(self, game: PenaltyGame):
        th = THEMES[self.app.theme]
        t1 = TEAMS[game.team1_id]
        t2 = TEAMS[game.team2_id]
        st = STADIUMS.get(game.stadium_id, {})

        if game.winner == 1:
            self.lbl_result.setText(f"{t1['name']} {self.tr('wins')}")
            self.lbl_result.setStyleSheet(f"color: #00ff88; background: transparent;")
        elif game.winner == 2:
            self.lbl_result.setText(f"{t2['name']} {self.tr('wins')}")
            self.lbl_result.setStyleSheet(f"color: #ff4444; background: transparent;")
        else:
            self.lbl_result.setText(self.tr("draw"))
            self.lbl_result.setStyleSheet(f"color: #ffcc00; background: transparent;")

        self.lbl_score.setText(f"{game.score1}  —  {game.score2}")
        self.lbl_score.setStyleSheet(f"color: {th['text']}; background: transparent;")
        self.btn_quit = GlowButton(self.tr("quit"), size="normal", accent="#ff4466")
        self.btn_quit.setMinimumWidth(220)
        self.btn_quit.clicked.connect(QApplication.quit)
        layout.addWidget(self.btn_quit, alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addStretch(2)

    def paintEvent(self, e):
        p = QPainter(self)
        th = THEMES[self.app.theme]
        grad = QLinearGradient(0, 0, 0, self.height())
        grad.setColorAt(0, QColor(th["bg"]))
        grad.setColorAt(1, QColor(th["bg"]).darker(130))
        p.fillRect(self.rect(), grad)

        # Animated stars
        p.setPen(QColor(255, 255, 255, 60))
        random.seed(42)
        for _ in range(60):
            x = random.randint(0, self.width())
            y = random.randint(0, self.height())
            r = random.uniform(0, math.pi * 2)
            alpha = int(128 + 127 * math.sin(self._anim_t * 2 + r))
            p.setPen(QColor(255, 255, 255, alpha))
            p.drawPoint(x, y)
        p.end()

    def showEvent(self, e):
        self.lbl_title.setText(self.tr("title"))
        self.lbl_sub.setText(self.tr("subtitle"))
        self.btn_play.setText(self.tr("play"))
        self.btn_settings.setText(self.tr("settings"))
        self.btn_quit.setText(self.tr("quit"))


# ───────────────────────────────────────────────
#  SETTINGS SCREEN
# ───────────────────────────────────────────────
class SettingsScreen(BaseScreen):
    def __init__(self, app_ref, parent=None):
        super().__init__(app_ref, parent)
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(20)
        layout.setContentsMargins(60, 40, 60, 40)

        self.lbl_title = QLabel(self.tr("settings"))
        self.lbl_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_title.setFont(QFont("Arial Black", 28, QFont.Weight.Black))
        layout.addWidget(self.lbl_title)

        layout.addSpacing(20)

        # Language
        row_lang = QHBoxLayout()
        lbl_lang = QLabel(self.tr("language") + ":")
        lbl_lang.setFont(QFont("Arial", 14))
        row_lang.addWidget(lbl_lang)
        row_lang.addStretch()
        self.combo_lang = QComboBox()
        self.combo_lang.addItems(["English", "فارسی", "Español", "Français", "Deutsch"])
        self.combo_lang.setFont(QFont("Arial", 13))
        self.combo_lang.setMinimumWidth(160)
        self.combo_lang.currentIndexChanged.connect(self._on_lang_change)
        row_lang.addWidget(self.combo_lang)
        layout.addLayout(row_lang)

        # Theme
        row_theme = QHBoxLayout()
        lbl_theme = QLabel(self.tr("theme") + ":")
        lbl_theme.setFont(QFont("Arial", 14))
        row_theme.addWidget(lbl_theme)
        row_theme.addStretch()
        self.combo_theme = QComboBox()
        self.combo_theme.addItems(["dark", "light", "neon"])
        self.combo_theme.setFont(QFont("Arial", 13))
        self.combo_theme.setMinimumWidth(160)
        self.combo_theme.currentIndexChanged.connect(self._on_theme_change)
        row_theme.addWidget(self.combo_theme)
        layout.addLayout(row_theme)

        # Rounds
        row_rounds = QHBoxLayout()
        lbl_rounds = QLabel(self.tr("rounds") + ":")
        lbl_rounds.setFont(QFont("Arial", 14))
        row_rounds.addWidget(lbl_rounds)
        row_rounds.addStretch()
        self.spin_rounds = QSpinBox()
        self.spin_rounds.setRange(3, 10)
        self.spin_rounds.setValue(5)
        self.spin_rounds.setFont(QFont("Arial", 13))
        self.spin_rounds.setMinimumWidth(80)
        self.spin_rounds.valueChanged.connect(self._on_rounds_change)
        row_rounds.addWidget(self.spin_rounds)
        layout.addLayout(row_rounds)

        # Sound
        row_sound = QHBoxLayout()
        lbl_sound = QLabel(self.tr("sound") + ":")
        lbl_sound.setFont(QFont("Arial", 14))
        row_sound.addWidget(lbl_sound)
        row_sound.addStretch()
        self.chk_sound = QCheckBox()
        self.chk_sound.setChecked(True)
        self.chk_sound.stateChanged.connect(self._on_sound_change)
        row_sound.addWidget(self.chk_sound)
        layout.addLayout(row_sound)

        layout.addStretch()

        self.btn_back = GlowButton(self.tr("back"), accent="#aaaaaa")
        self.btn_back.setMinimumWidth(180)
        self.btn_back.clicked.connect(self.app.go_menu)
        layout.addWidget(self.btn_back, alignment=Qt.AlignmentFlag.AlignCenter)

    def showEvent(self, e):
        lang_map = {"en": 0, "fa": 1, "es": 2, "fr": 3, "de": 4}
        self.combo_lang.setCurrentIndex(lang_map.get(self.app.lang, 0))
        theme_map = {"dark": 0, "light": 1, "neon": 2}
        self.combo_theme.setCurrentIndex(theme_map.get(self.app.theme, 0))
        self.spin_rounds.setValue(self.app.max_rounds)
        self._refresh_labels()

    def _refresh_labels(self):
        self.lbl_title.setText(self.tr("settings"))
        self.btn_back.setText(self.tr("back"))

    def _on_lang_change(self, idx):
        langs = ["en", "fa", "es", "fr", "de"]
        self.app.lang = langs[idx]
        self._refresh_labels()
        self.app.refresh_all()

    def _on_theme_change(self, idx):
        themes = ["dark", "light", "neon"]
        self.app.theme = themes[idx]
        self.app.apply_theme()
        self.update()

    def _on_rounds_change(self, val):
        self.app.max_rounds = val

    def _on_sound_change(self, state):
        self.app.sound_on = bool(state)


# ───────────────────────────────────────────────
#  TEAM SELECT SCREEN
# ───────────────────────────────────────────────
class TeamSelectScreen(BaseScreen):
    def __init__(self, app_ref, parent=None):
        super().__init__(app_ref, parent)
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(16)
        layout.setContentsMargins(30, 30, 30, 30)

        self.lbl_title = QLabel(self.tr("select_teams"))
        self.lbl_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_title.setFont(QFont("Arial Black", 24, QFont.Weight.Black))
        layout.addWidget(self.lbl_title)

        # Team cards row
        cards_row = QHBoxLayout()
        cards_row.setSpacing(20)

        # Team 1
        col1 = QVBoxLayout()
        lbl1 = QLabel(self.tr("team1"))
        lbl1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lbl1.setFont(QFont("Arial", 13))
        col1.addWidget(lbl1)
        self.scroll1 = QScrollArea()
        self.scroll1.setWidgetResizable(True)
        self.scroll1.setFixedHeight(340)
        inner1 = QWidget()
        self.grid1 = QGridLayout(inner1)
        self.grid1.setSpacing(8)
        self.scroll1.setWidget(inner1)
        col1.addWidget(self.scroll1)
        cards_row.addLayout(col1)

        # VS label
        lbl_vs = QLabel("VS")
        lbl_vs.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lbl_vs.setFont(QFont("Arial Black", 22, QFont.Weight.Black))
        cards_row.addWidget(lbl_vs)

        # Team 2
        col2 = QVBoxLayout()
        lbl2 = QLabel(self.tr("team2"))
        lbl2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lbl2.setFont(QFont("Arial", 13))
        col2.addWidget(lbl2)
        self.scroll2 = QScrollArea()
        self.scroll2.setWidgetResizable(True)
        self.scroll2.setFixedHeight(340)
        inner2 = QWidget()
        self.grid2 = QGridLayout(inner2)
        self.grid2.setSpacing(8)
        self.scroll2.setWidget(inner2)
        col2.addWidget(self.scroll2)
        cards_row.addLayout(col2)

        layout.addLayout(cards_row)

        # Stadium select
        stad_row = QHBoxLayout()
        lbl_stad = QLabel(self.tr("stadium") + ":")
        lbl_stad.setFont(QFont("Arial", 13))
        stad_row.addWidget(lbl_stad)
        self.combo_stad = QComboBox()
        for sid, sd in STADIUMS.items():
            self.combo_stad.addItem(sd["name"], sid)
        self.combo_stad.setFont(QFont("Arial", 12))
        stad_row.addWidget(self.combo_stad)
        layout.addLayout(stad_row)

        # Buttons
        btn_row = QHBoxLayout()
        self.btn_back = GlowButton(self.tr("back"), accent="#aaaaaa")
        self.btn_back.clicked.connect(self.app.go_menu)
        btn_row.addWidget(self.btn_back)
        btn_row.addStretch()
        self.btn_start = GlowButton(self.tr("start_game"), accent="#00ff88", size="large")
        self.btn_start.clicked.connect(self._start)
        btn_row.addWidget(self.btn_start)
        layout.addLayout(btn_row)

        self.selected_team1 = list(TEAMS.keys())[0]
        self.selected_team2 = list(TEAMS.keys())[1]
        self._populate_teams()

    def _populate_teams(self):
        teams_list = list(TEAMS.items())
        for i, (tid, td) in enumerate(teams_list):
            card1 = TeamCard(tid, td, self.selected_team1 == tid)
            card1.clicked.connect(lambda checked, t=tid: self._select_team1(t))
            self.grid1.addWidget(card1, i // 2, i % 2)

            card2 = TeamCard(tid, td, self.selected_team2 == tid)
            card2.clicked.connect(lambda checked, t=tid: self._select_team2(t))
            self.grid2.addWidget(card2, i // 2, i % 2)

    def _select_team1(self, tid):
        self.selected_team1 = tid
        self._refresh_cards()

    def _select_team2(self, tid):
        self.selected_team2 = tid
        self._refresh_cards()

    def _refresh_cards(self):
        teams_list = list(TEAMS.items())
        for i, (tid, _) in enumerate(teams_list):
            w1 = self.grid1.itemAtPosition(i // 2, i % 2)
            if w1:
                w1.widget().set_selected(self.selected_team1 == tid)
            w2 = self.grid2.itemAtPosition(i // 2, i % 2)
            if w2:
                w2.widget().set_selected(self.selected_team2 == tid)

    def _start(self):
        if self.selected_team1 == self.selected_team2:
            QMessageBox.warning(self, self.tr("warning"), self.tr("same_team_warning"))
            return
        stad_id = self.combo_stad.currentData()
        self.app.start_game(self.selected_team1, self.selected_team2, stad_id)

    def showEvent(self, e):
        self.lbl_title.setText(self.tr("select_teams"))
        self.btn_back.setText(self.tr("back"))
        self.btn_start.setText(self.tr("start_game"))


# ───────────────────────────────────────────────
#  GAME SCREEN
# ───────────────────────────────────────────────
class GameScreen(BaseScreen):
    def __init__(self, app_ref, parent=None):
        super().__init__(app_ref, parent)
        self.game: PenaltyGame = None
        self.state = "idle"
        self.shot_col = 1
        self.shot_row = 0
        self.gk_col = 1
        self.last_result = ""
        self._anim_t = 0.0
        self._anim_timer = QTimer(self)
        self._anim_timer.timeout.connect(self._tick)
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(8)
        layout.setContentsMargins(20, 16, 20, 16)

        # Score bar
        self.score_widget = ScoreWidget()
        layout.addWidget(self.score_widget)

        # Pitch
        self.pitch = PitchWidget()
        self.pitch.setMinimumHeight(260)
        layout.addWidget(self.pitch, stretch=3)

        # Result label
        self.lbl_result = QLabel("")
        self.lbl_result.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_result.setFont(QFont("Arial Black", 22, QFont.Weight.Black))
        layout.addWidget(self.lbl_result)

        # Shooter info
        self.lbl_shooter = QLabel("")
        self.lbl_shooter.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_shooter.setFont(QFont("Arial", 13))
        layout.addWidget(self.lbl_shooter)

        # Shot direction selector
        self.shot_selector = ShotSelectorWidget()
        self.shot_selector.shot_chosen.connect(self._on_shot_chosen)
        layout.addWidget(self.shot_selector)

        # Action button
        self.btn_action = GlowButton(self.tr("shoot"), size="large", accent="#00ff88")
        self.btn_action.clicked.connect(self._on_action)
        layout.addWidget(self.btn_action, alignment=Qt.AlignmentFlag.AlignCenter)

        self.btn_menu = GlowButton(self.tr("menu"), accent="#aaaaaa")
        self.btn_menu.clicked.connect(self.app.go_menu)
        layout.addWidget(self.btn_menu, alignment=Qt.AlignmentFlag.AlignCenter)

    def setup_game(self, game: PenaltyGame):
        self.game = game
        self.state = "choosing"
        self.last_result = ""
        self.lbl_result.setText("")
        self._update_ui()
        self._anim_timer.start(16)

    def _tick(self):
        self._anim_t += 0.02
        self.pitch.set_anim(self._anim_t)
        self.update()

    def _update_ui(self):
        if not self.game:
            return
        g = self.game
        t1 = TEAMS[g.team1_id]
        t2 = TEAMS[g.team2_id]
        self.score_widget.update_score(
            t1["name"], t2["name"],
            g.score1, g.score2,
            g.shots1, g.shots2,
            g.round_num, g.max_rounds,
            g.phase
        )
        shooter = g.get_current_shooter()
        team_name = t1["name"] if g.current_team == 1 else t2["name"]
        self.lbl_shooter.setText(
            f"{self.tr('shooter')}: {shooter['name']} #{shooter['number']} ({team_name})"
        )
        is_player_turn = (g.current_team == 1)
        self.shot_selector.setVisible(is_player_turn and self.state == "choosing")
        self.btn_action.setVisible(self.state in ("choosing", "result"))
        if self.state == "choosing":
            self.btn_action.setText(self.tr("shoot") if is_player_turn else self.tr("cpu_shoot"))
        elif self.state == "result":
            self.btn_action.setText(self.tr("next"))

    def _on_shot_chosen(self, col, row):
        self.shot_col = col
        self.shot_row = row

    def _on_action(self):
        if self.state == "choosing":
            self._do_shot()
        elif self.state == "result":
            self._advance()

    def _do_shot(self):
        g = self.game
        is_player = (g.current_team == 1)
        if is_player:
            col, row = self.shot_col, self.shot_row
        else:
            col, row = g.cpu_choose_shot()
        gk_col = g.cpu_choose_dive()
        self.gk_col = gk_col
        result = g.resolve_shot(col, row, gk_col)
        g.record_shot(result)
        self.last_result = result
        self.state = "result"

        # Update pitch animation
        self.pitch.set_shot(col, row, gk_col, result)

        # Result label
        if result == "goal":
            self.lbl_result.setText("⚽ " + self.tr("goal") + "!")
            self.lbl_result.setStyleSheet("color: #00ff88;")
        elif result == "save":
            self.lbl_result.setText("🧤 " + self.tr("saved") + "!")
            self.lbl_result.setStyleSheet("color: #ff4466;")
        else:
            self.lbl_result.setText("❌ " + self.tr("missed") + "!")
            self.lbl_result.setStyleSheet("color: #ffaa00;")

        self._update_ui()

    def _advance(self):
        g = self.game
        g.advance_turn()
        if g.finished:
            self._anim_timer.stop()
            self.app.go_result(g)
            return
        self.state = "choosing"
        self.last_result = ""
        self.lbl_result.setText("")
        self.pitch.reset_shot()
        self._update_ui()


# ───────────────────────────────────────────────
#  RESULT SCREEN
# ───────────────────────────────────────────────
class ResultScreen(BaseScreen):
    def __init__(self, app_ref, parent=None):
        super().__init__(app_ref, parent)
        self._build_ui()
        self._anim_t = 0.0
        self._timer = QTimer(self)
        self._timer.timeout.connect(self._tick)

    def _tick(self):
        self._anim_t += 0.02
        self.update()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(18)
        layout.setContentsMargins(40, 40, 40, 40)

        layout.addStretch()

        self.lbl_trophy = QLabel("🏆")
        self.lbl_trophy.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_trophy.setFont(QFont("Segoe UI Emoji", 64))
        layout.addWidget(self.lbl_trophy)

        self.lbl_result = QLabel("")
        self.lbl_result.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_result.setFont(QFont("Arial Black", 30, QFont.Weight.Black))
        layout.addWidget(self.lbl_result)

        self.lbl_score = QLabel("")
        self.lbl_score.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_score.setFont(QFont("Arial", 20))
        layout.addWidget(self.lbl_score)

        self.lbl_detail = QLabel("")
        self.lbl_detail.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_detail.setFont(QFont("Arial", 13))
        layout.addWidget(self.lbl_detail)

        layout.addStretch()

        self.btn_rematch = GlowButton(self.tr("rematch"), size="large", accent="#00ff88")
        self.btn_rematch.setMinimumWidth(200)
        self.btn_rematch.clicked.connect(self.app.go_team_select)
        layout.addWidget(self.btn_rematch, alignment=Qt.AlignmentFlag.AlignCenter)

        self.btn_menu = GlowButton(self.tr("menu"), accent="#aaaaaa")
        self.btn_menu.setMinimumWidth(200)
        self.btn_menu.clicked.connect(self.app.go_menu)
        layout.addWidget(self.btn_menu, alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addStretch()

    def show_result(self, game: PenaltyGame):
        t1 = TEAMS[game.team1_id]
        t2 = TEAMS[game.team2_id]
        if game.winner == 1:
            self.lbl_result.setText(f"{t1['name']} {self.tr('wins')}!")
            self.lbl_result.setStyleSheet("color: #00ff88;")
            self.lbl_trophy.setText("🏆")
        elif game.winner == 2:
            self.lbl_result.setText(f"{t2['name']} {self.tr('wins')}!")
            self.lbl_result.setStyleSheet("color: #00ff88;")
            self.lbl_trophy.setText("🏆")
        else:
            self.lbl_result.setText(self.tr("draw"))
            self.lbl_result.setStyleSheet("color: #ffaa00;")
            self.lbl_trophy.setText("🤝")

        self.lbl_score.setText(f"{game.score1}  –  {game.score2}")
        shots1_str = " ".join("✅" if s else "❌" for s in game.shots1)
        shots2_str = " ".join("✅" if s else "❌" for s in game.shots2)
        self.lbl_detail.setText(
            f"{t1['name']}: {shots1_str}\n{t2['name']}: {shots2_str}"
        )
        self._timer.start(16)

    def paintEvent(self, e):
        super().paintEvent(e)
        p = QPainter(self)
        # Confetti
        random.seed(int(self._anim_t * 10) % 100)
        for _ in range(40):
            x = random.randint(0, self.width())
            y = int((random.randint(0, self.height()) + self._anim_t * 80) % self.height())
            color = random.choice(["#00ff88", "#00d4ff", "#ff4466", "#ffaa00", "#ffffff"])
            p.setPen(Qt.PenStyle.NoPen)
            p.setBrush(QColor(color))
            p.drawEllipse(x, y, 6, 6)
        p.end()

    def showEvent(self, e):
        self.btn_rematch.setText(self.tr("rematch"))
        self.btn_menu.setText(self.tr("menu"))


# ═══════════════════════════════════════════════════════════════
#  HELPER WIDGETS
# ═══════════════════════════════════════════════════════════════
class GlowButton(QPushButton):
    def __init__(self, text="", size="normal", accent="#00ff88", parent=None):
        super().__init__(text, parent)
        self.accent = accent
        self._hovered = False
        sz = {"large": (14, 14, 48), "normal": (12, 12, 38), "small": (10, 10, 30)}
        fs, pad, h = sz.get(size, sz["normal"])
        self.setMinimumHeight(h)
        self.setFont(QFont("Arial", fs, QFont.Weight.Bold))
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self._apply_style(False)
        self.installEventFilter(self)

    def _apply_style(self, hovered):
        a = self.accent
        bg = a if hovered else "transparent"
        tc = "#000000" if hovered else a
        self.setStyleSheet(f"""
            QPushButton {{
                background: {bg};
                color: {tc};
                border: 2px solid {a};
                border-radius: 8px;
                padding: 6px 24px;
            }}
        """)

    def eventFilter(self, obj, event):
        if obj is self:
            if event.type() == event.Type.Enter:
                self._apply_style(True)
            elif event.type() == event.Type.Leave:
                self._apply_style(False)
        return super().eventFilter(obj, event)


class TeamCard(QPushButton):
    def __init__(self, team_id, team_data, selected=False, parent=None):
        super().__init__(parent)
        self.team_id = team_id
        self.team_data = team_data
        self._selected = selected
        self.setFixedSize(110, 80)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self._refresh()

    def set_selected(self, val):
        self._selected = val
        self._refresh()

    def _refresh(self):
        color = self.team_data.get("color", "#ffffff")
        border = "3px solid #00ff88" if self._selected else f"2px solid {color}"
        bg = "#1a2a1a" if self._selected else "#1a1a2e"
        self.setStyleSheet(f"""
            QPushButton {{
                background: {bg};
                border: {border};
                border-radius: 8px;
                color: {color};
                font-size: 11px;
                font-weight: bold;
            }}
        """)
        flag = self.team_data.get("flag", "")
        name = self.team_data.get("name", "")
        self.setText(f"{flag}\n{name}")


class StadiumCard(QPushButton):
    def __init__(self, stad_id, stad_data, selected=False, parent=None):
        super().__init__(parent)
        self.stad_id = stad_id
        self._selected = selected
        self.setFixedSize(130, 60)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        color = stad_data.get("color", "#ffffff")
        border = "3px solid #00ff88" if selected else f"2px solid {color}"
        self.setStyleSheet(f"""
            QPushButton {{
                background: #1a1a2e;
                border: {border};
                border-radius: 8px;
                color: {color};
                font-size: 11px;
            }}
        """)
        self.setText(stad_data.get("name", ""))


class ScoreWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(90)
        self._data = {}

    def update_score(self, t1, t2, s1, s2, shots1, shots2, rnd, max_rnd, phase):
        self._data = dict(t1=t1, t2=t2, s1=s1, s2=s2,
                          shots1=shots1, shots2=shots2,
                          rnd=rnd, max_rnd=max_rnd, phase=phase)
        self.update()

    def paintEvent(self, e):
        if not self._data:
            return
        d = self._data
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        w, h = self.width(), self.height()

        # Background
        p.fillRect(self.rect(), QColor(20, 20, 40, 200))

        # Team names & score
        p.setFont(QFont("Arial Black", 18, QFont.Weight.Black))
        p.setPen(QColor("#ffffff"))
        p.drawText(QRect(0, 4, w // 3, 36), Qt.AlignmentFlag.AlignCenter, d["t1"])
        p.drawText(QRect(w * 2 // 3, 4, w // 3, 36), Qt.AlignmentFlag.AlignCenter, d["t2"])

        p.setFont(QFont("Arial Black", 26, QFont.Weight.Black))
        p.setPen(QColor("#00ff88"))
        p.drawText(QRect(w // 3, 0, w // 3, 44), Qt.AlignmentFlag.AlignCenter,
                   f"{d['s1']}  –  {d['s2']}")

        # Round info
        phase_str = "SD" if d["phase"] == "sudden" else f"R{d['rnd']+1}/{d['max_rnd']}"
        p.setFont(QFont("Arial", 11))
        p.setPen(QColor("#aaaaaa"))
        p.drawText(QRect(w // 3, 44, w // 3, 20), Qt.AlignmentFlag.AlignCenter, phase_str)

        # Shot indicators team 1
        dot_size = 14
        spacing = 18
        start_x1 = 10
        y_dots = 62
        for i, scored in enumerate(d["shots1"]):
            color = QColor("#00ff88") if scored else QColor("#ff4466")
            p.setBrush(color)
            p.setPen(Qt.PenStyle.NoPen)
            p.drawEllipse(start_x1 + i * spacing, y_dots, dot_size, dot_size)

        # Shot indicators team 2
        start_x2 = w - 10 - (len(d["shots2"]) * spacing)
        for i, scored in enumerate(d["shots2"]):
            color = QColor("#00ff88") if scored else QColor("#ff4466")
            p.setBrush(color)
            p.setPen(Qt.PenStyle.NoPen)
            p.drawEllipse(start_x2 + i * spacing, y_dots, dot_size, dot_size)

        p.end()


class PitchWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._anim_t = 0.0
        self._shot_col = -1
        self._shot_row = -1
        self._gk_col = -1
        self._result = ""

    def set_anim(self, t):
        self._anim_t = t
        self.update()

    def set_shot(self, col, row, gk_col, result):
        self._shot_col = col
        self._shot_row = row
        self._gk_col = gk_col
        self._result = result
        self.update()

    def reset_shot(self):
        self._shot_col = -1
        self._shot_row = -1
        self._gk_col = -1
        self._result = ""
        self.update()

    def paintEvent(self, e):
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        w, h = self.width(), self.height()

        # Grass background
        p.fillRect(self.rect(), QColor(30, 100, 30))

        # Grass stripes
        stripe_w = w // 10
        for i in range(10):
            if i % 2 == 0:
                p.fillRect(i * stripe_w, 0, stripe_w, h, QColor(35, 110, 35))

        # Penalty area
        area_w = int(w * 0.55)
        area_h = int(h * 0.55)
        area_x = (w - area_w) // 2
        area_y = 10
        p.setPen(QPen(QColor(255, 255, 255, 180), 2))
        p.setBrush(Qt.BrushStyle.NoBrush)
        p.drawRect(area_x, area_y, area_w, area_h)

        # Goal
        goal_w = int(w * 0.36)
        goal_h = int(h * 0.22)
        goal_x = (w - goal_w) // 2
        goal_y = 10
        p.setPen(QPen(QColor(255, 255, 255), 3))
        p.setBrush(QColor(0, 0, 0, 120))
        p.drawRect(goal_x, goal_y, goal_w, goal_h)

        # Goal grid lines
        p.setPen(QPen(QColor(255, 255, 255, 60), 1))
        # Vertical thirds
        third_w = goal_w // 3
        p.drawLine(goal_x + third_w, goal_y, goal_x + third_w, goal_y + goal_h)
        p.drawLine(goal_x + 2 * third_w, goal_y, goal_x + 2 * third_w, goal_y + goal_h)
        # Horizontal half
        p.drawLine(goal_x, goal_y + goal_h // 2, goal_x + goal_w, goal_y + goal_h // 2)

        # Penalty spot
        spot_x = w // 2
        spot_y = int(h * 0.72)
        p.setPen(Qt.PenStyle.NoPen)
        p.setBrush(QColor(255, 255, 255, 200))
        p.drawEllipse(spot_x - 4, spot_y - 4, 8, 8)

        # Penalty arc
        p.setPen(QPen(QColor(255, 255, 255, 180), 2))
        p.setBrush(Qt.BrushStyle.NoBrush)
        arc_rect = QRect(spot_x - 60, spot_y - 60, 120, 120)
        p.drawArc(arc_rect, 30 * 16, 120 * 16)

        # Draw GK
        if self._gk_col >= 0:
            gk_positions = [
                goal_x + third_w // 2,
                goal_x + goal_w // 2,
                goal_x + 2 * third_w + third_w // 2
            ]
            gk_x = gk_positions[self._gk_col]
            gk_y = goal_y + goal_h // 2

            # GK dive animation
            dive_offset = int(math.sin(self._anim_t * 8) * 4) if self._result == "" else 0
            p.setBrush(QColor("#ffaa00"))
            p.setPen(QPen(QColor("#ffffff"), 2))
            p.drawEllipse(gk_x - 14, gk_y - 28 + dive_offset, 28, 28)  # head
            p.drawRect(gk_x - 12, gk_y + dive_offset, 24, 20)           # body

        # Draw ball / shot result
        if self._shot_col >= 0:
            third_w_g = goal_w // 3
            ball_positions_x = [
                goal_x + third_w_g // 2,
                goal_x + goal_w // 2,
                goal_x + 2 * third_w_g + third_w_g // 2
            ]
            ball_y_positions = [
                goal_y + goal_h // 4,      # top (row 0)
                goal_y + 3 * goal_h // 4   # bottom (row 1)
            ]
            bx = ball_positions_x[self._shot_col]
            by = ball_y_positions[self._shot_row]

            if self._result == "goal":
                p.setBrush(QColor("#ffffff"))
                p.setPen(QPen(QColor("#000000"), 2))
                p.drawEllipse(bx - 10, by - 10, 20, 20)
                # Net ripple
                p.setPen(QPen(QColor(255, 255, 255, 100), 1))
                for ring in range(1, 4):
                    p.drawEllipse(bx - ring * 8, by - ring * 8,
                                  ring * 16, ring * 16)
            elif self._result == "save":
                # Ball near GK hands
                p.setBrush(QColor("#ffaa00"))
                p.setPen(QPen(QColor("#ffffff"), 2))
                p.drawEllipse(bx - 10, by - 10, 20, 20)
                p.setPen(QPen(QColor("#ff4466"), 3))
                p.drawLine(bx - 14, by - 14, bx + 14, by + 14)
                p.drawLine(bx + 14, by - 14, bx - 14, by + 14)
            else:  # miss
                miss_x = bx + random.choice([-1, 1]) * (goal_w // 2 + 20)
                p.setBrush(QColor("#888888"))
                p.setPen(QPen(QColor("#ffffff"), 2))
                p.drawEllipse(miss_x - 10, by - 10, 20, 20)

        # Shooter (player) at bottom
        shooter_x = w // 2
        shooter_y = int(h * 0.82)
        bob = int(math.sin(self._anim_t * 3) * 3)
        p.setBrush(QColor("#00d4ff"))
        p.setPen(QPen(QColor("#ffffff"), 2))
        p.drawEllipse(shooter_x - 12, shooter_y - 26 + bob, 24, 24)  # head
        p.drawRect(shooter_x - 10, shooter_y - 2 + bob, 20, 18)       # body

        p.end()


class ShotSelectorWidget(QWidget):
    shot_chosen = pyqtSignal(int, int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.selected_col = 1
        self.selected_row = 0
        self.setFixedHeight(90)
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(4)
        layout.setContentsMargins(0, 0, 0, 0)

        lbl = QLabel("🎯 Choose direction:")
        lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lbl.setFont(QFont("Arial", 11))
        layout.addWidget(lbl)

        grid = QGridLayout()
        grid.setSpacing(6)
        self.btns = {}
        labels = [["↖ Top L", "⬆ Top C", "↗ Top R"],
                  ["← Bot L", "⬇ Bot C", "→ Bot R"]]
        for row in range(2):
            for col in range(3):
                btn = QPushButton(labels[row][col])
                btn.setFixedSize(90, 28)
                btn.setFont(QFont("Arial", 9))
                btn.setCursor(Qt.CursorShape.PointingHandCursor)
                btn.clicked.connect(lambda _, c=col, r=row: self._select(c, r))
                self.btns[(col, row)] = btn
                grid.addWidget(btn, row, col)
        layout.addLayout(grid)
        self._refresh_styles()

    def _select(self, col, row):
        self.selected_col = col
        self.selected_row = row
        self._refresh_styles()
        self.shot_chosen.emit(col, row)

    def _refresh_styles(self):
        for (c, r), btn in self.btns.items():
            if c == self.selected_col and r == self.selected_row:
                btn.setStyleSheet("""
                    QPushButton {
                        background: #00ff88;
                        color: #000000;
                        border: 2px solid #00ff88;
                        border-radius: 6px;
                        font-weight: bold;
                    }
                """)
            else:
                btn.setStyleSheet("""
                    QPushButton {
                        background: transparent;
                        color: #aaaaaa;
                        border: 1px solid #444444;
                        border-radius: 6px;
                    }
                    QPushButton:hover {
                        border: 1px solid #00ff88;
                        color: #ffffff;
                    }
                """)


# ═══════════════════════════════════════════════════════════════
#  MAIN APPLICATION
# ═══════════════════════════════════════════════════════════════
class PenaltyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.lang = "en"
        self.theme = "dark"
        self.max_rounds = 5
        self.sound_on = True
        self.setWindowTitle("Penalty Shootout")
        self.setMinimumSize(600, 700)
        self._build_ui()
        self.apply_theme()
        self.go_menu()

    def _build_ui(self):
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.screen_menu = MenuScreen(self)
        self.screen_settings = SettingsScreen(self)
        self.screen_team_select = TeamSelectScreen(self)
        self.screen_game = GameScreen(self)
        self.screen_result = ResultScreen(self)

        for s in [self.screen_menu, self.screen_settings,
                  self.screen_team_select, self.screen_game, self.screen_result]:
            self.stack.addWidget(s)

    def apply_theme(self):
        th = THEMES[self.theme]
        self.setStyleSheet(f"""
            QWidget {{
                background-color: {th['bg']};
                color: {th['text']};
            }}
            QComboBox, QSpinBox {{
                background: {th['card']};
                color: {th['text']};
                border: 1px solid {th['border']};
                border-radius: 6px;
                padding: 4px 8px;
            }}
            QScrollArea {{
                border: none;
                background: transparent;
            }}
            QCheckBox {{
                color: {th['text']};
            }}
        """)


    def refresh_all(self):
        for s in [self.screen_menu, self.screen_settings,
                  self.screen_team_select, self.screen_game, self.screen_result]:
            if hasattr(s, "showEvent"):
                s.showEvent(None)

    def go_menu(self):
        self.stack.setCurrentWidget(self.screen_menu)

    def go_settings(self):
        self.stack.setCurrentWidget(self.screen_settings)

    def go_team_select(self):
        self.stack.setCurrentWidget(self.screen_team_select)

    def start_game(self, team1_id, team2_id, stadium_id):
        squad1 = get_default_squad(team1_id)
        squad2 = get_default_squad(team2_id)
        game = PenaltyGame(
            team1_id, team2_id,
            squad1, squad2,
            stadium_id
        )
        game.max_rounds = self.max_rounds
        self.screen_game.setup_game(game)
        self.stack.setCurrentWidget(self.screen_game)

    def go_result(self, game: PenaltyGame):
        self.screen_result.show_result(game)
        self.stack.setCurrentWidget(self.screen_result)

    def quit_app(self):
        QApplication.quit()

# ═══════════════════════════════════════════════════════════════
#  ENTRY POINT
# ═══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = PenaltyApp()
    window.show()
    sys.exit(app.exec())
