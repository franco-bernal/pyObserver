
import requests

# Lista de bots a verificar con sus User-Agent correspondientes
bots = {
    'GoogleBot': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'AdsBot-Google': 'Mozilla/5.0 (compatible; AdsBot-Google; +http://www.google.com/adsbot.html)',
    'BingBot': 'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)',
    'DuckDuckBot': 'DuckDuckBot/1.0; (+http://duckduckgo.com/duckduckbot.html)',
    'Yahoo! Slurp': 'Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)',
    'BaiduSpider': 'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)',
    'YandexBot': 'Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)',
    'SogouSpider': 'Mozilla/5.0 (compatible; Sogou web spider/4.0; +http://www.sogou.com/docs/help/webmasters.htm#07)',
    'FacebookExternalHit': 'facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)',
    'TwitterBot': 'Twitterbot/1.0',
    'LinkedInBot': 'LinkedInBot/1.0 (+https://www.linkedin.com)',
    'PinterestBot': 'Mozilla/5.0 (compatible; Pinterestbot/1.0; +http://www.pinterest.com/bot.html)',
    'FaceBot': 'facebookexternalhit/1.1',
    'AhrefsBot': 'Mozilla/5.0 (compatible; AhrefsBot/6.1; +http://ahrefs.com/robot/)',
    'MJ12bot': 'Mozilla/5.0 (compatible; MJ12bot/v1.4.8; http://majestic12.co.uk/bot.php?+)',
    'SEMRushBot': 'Mozilla/5.0 (compatible; SEMRushBot/1.0; +http://www.semrush.com/bot.html)',
    'Applebot': 'Mozilla/5.0 (compatible; Applebot/0.3; +http://www.apple.com/go/applebot)',
    'GoogleImageBot': 'Googlebot-Image/1.0',
    'GoogleNewsBot': 'Googlebot-News',
    'Exabot': 'Mozilla/5.0 (compatible; Exabot/3.0; +http://www.exabot.com/go/robot)',
    'AlexaBot': 'ia_archiver (+http://www.alexa.com/site/help/webmasters; crawler@alexa.com)',
    'YetiBot': 'NaverBot/Yeti',
    'MailRuBot': 'Mozilla/5.0 (compatible; Mail.RU_Bot/2.0; +http://go.mail.ru/help/robots)',
    'SeznamBot': 'Mozilla/5.0 (compatible; SeznamBot/3.2; +http://napoveda.seznam.cz/en/seznambot-intro/)',
    'CoccocBot': 'Mozilla/5.0 (compatible; coccocbot-web/1.0; +http://help.coccoc.com/searchengine)',
    '360Spider': 'Mozilla/5.0 (compatible; 360Spider/2.0; +http://www.so.com/help/help_3_2.html)',
    'Wget': 'Wget/1.19.5 (linux-gnu)',
    'curl': 'curl/7.64.1',
    'ScreamingFrog': 'Mozilla/5.0 (compatible; Screaming Frog SEO Spider/13.0; +https://www.screamingfrog.co.uk/seo-spider/)',
    'SiteSucker': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0',
    'DotBot': 'Mozilla/5.0 (compatible; DotBot/1.1; +http://www.opensiteexplorer.org/dotbot)',
    'Site24x7': 'Site24x7',
    'UptimeRobot': 'Mozilla/5.0 (compatible; UptimeRobot/2.0; +http://www.uptimerobot.com/)',
    'Pingdom': 'Mozilla/5.0 (compatible; Pingdom.com_bot_version_1.4)',
    'GoogleFavicon': 'Mozilla/5.0 (compatible; Google-Site-Verification/1.0)',
    'WeiboBot': 'Mozilla/5.0 (compatible; WeiboBot/2.0; +http://www.weibo.com)',
    'WhatsApp': 'WhatsApp/2.21.5 Mozilla/5.0 (Linux; Android 9; PH-1 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36',
    'TelegramBot': 'Mozilla/5.0 (compatible; TelegramBot/1.0; +https://telegram.org/bots)',
    'Qwantify': 'Mozilla/5.0 (compatible; Qwantify/1.0; +https://www.qwant.com/)',
    'MegaIndexBot': 'Mozilla/5.0 (compatible; MegaIndex.ru/2.0; +http://megaindex.com/crawler)',
    'GlutenFreeBot': 'Mozilla/5.0 (compatible; GlutenFreeBot/1.0)',
    'GrapeshotCrawler': 'Mozilla/5.0 (compatible; GrapeshotCrawler/2.0; +http://www.grapeshot.co.uk/crawler.php)',
    'Barkrowler': 'Mozilla/5.0 (compatible; Barkrowler/0.9; +http://www.barkrowler.com)',
    'DeuSu': 'Mozilla/5.0 (compatible; DeuSu/0.1.0.12 +https://deusu.org)',
    'RobooBot': 'Mozilla/5.0 (compatible; RobooBot/1.0; +https://www.robometrics.co)',
    'Seekport': 'Seekport Crawler (http://seekport.com)',
    'RogerBot': 'Mozilla/5.0 (compatible; RogerBot/1.0; +https://moz.com/help/pro/what-is-rogerbot)',
    'CommonCrawler': 'CCBot/2.0 (https://commoncrawl.org/faq/)',
    'Google-Read-Aloud': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Google-Read-Aloud',
    'GoogleAdsBot-Mobile': 'AdsBot-Google-Mobile (+http://www.google.com/mobile/adsbot.html)'
}


# URL que deseas verificar
url = "https://www.brunorossi.cl"

# Verifica el estado HTTP para cada bot
for bot_name, user_agent in bots.items():
    headers = {
        'User-Agent': user_agent
    }
    
    try:
        # Realiza la solicitud HTTP
        response = requests.get(url, headers=headers)
        
        # Muestra el código de estado que recibe cada bot
        print(f"{response.status_code} | {bot_name} recibió un código {response.status_code} en {url}.")
        
    except requests.exceptions.RequestException as e:
        # Si hay algún problema de conexión, lo informa
        print(f"Error al intentar conectar {bot_name} a {url}: {e}")

