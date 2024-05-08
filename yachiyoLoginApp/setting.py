import os
import pathlib

# pythonファイルのディレクトリを取得
BASE_DIR = pathlib.Path(__file__).parents[1]

CLOUD_GATE_URL = 'https://echizen.cloudgate.jp/user-hub/yachiyo-ind/'
GMAIL_URL = 'https://mail.google.com/a/yachiyo-ind.co.jp/'
CALENDAR_URL = 'https://calendar.google.com/calendar/u/0/r'
KOBETSU_GENKA_URL = 'https://echizen.cloudgate.jp/sso/yachiyo-ind/post.xhtml?providerUuid=284c5466-7256-49e3-99ab-04ff1a8178a8'
KINTAIKANRI_URL = 'https://yachiyo-ind.obic7.obicnet.ne.jp/Obic7FederationService'
GUEST_WIFI_URL = 'https://sites.google.com/yachiyo-ind.co.jp/yachiyo-portal/guest-wifi'
CAFE_BGM_CHANNEL_URL = 'https://www.youtube.com/channel/UCJhjE7wbdYAae1G25m0tHAA'
E_TYPING_URL = 'https://www.e-typing.ne.jp/member/'


YACHIYO_LOGIN_ID = 'makoto_yaguchi'
YACHIYO_EMAIL = 'makoto_yaguchi@yachiyo-ind.co.jp'
YACHIYO_LOGIN_PASSWORD = os.getenv('YACHIYO_LOGIN_PASSWORD')

E_TYPING_EMAIL = 'mkyaguchi@gmail.com'
# E_TYPING_LOGIN_PASSWORD = os.getenv('E_TYPING_LOGIN_PASSWORD')
E_TYPING_LOGIN_PASSWORD = 'mk31576821'
