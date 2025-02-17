from flask import Flask, request, jsonify, render_template
import whois
import ssl
import socket
from urllib.parse import urlparse

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

def get_domain(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc

def check_ssl_certificate(url):
    try:
        if not url.startswith('http'):
            url = 'https://' + url
        domain = get_domain(url)

        context = ssl.create_default_context()
        conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=domain)
        conn.settimeout(3.0) #for timeout mostly increasing the speed of the results for ssl certficate
        conn.connect((domain, 443))
        ssl_info = conn.getpeercert()
        return True
    except Exception as e:
        return False

def check_misspelled_url(url):
    common_typos = [
    'gooogle', 'facebok', 'twittter', 'instagarm', 'linikedin', 'amzon', 'netfliix', 'youutube', 
    'ebbay', 'paypalx', 'reditt', 'disnney', 'goolge', 'micorsoft', 'applle', 'yahhoo', 'tumlr', 
    'pintrest', 'tikok', 'walmrat', 'costcoo', 'homedept', 'lowees', 'walgreenes', 'staplles', 
    'starubcks', 'mcdoonalds', 'burgerkingg', 'wenddies', 'domminos', 'subwy', 'kfcf', 'tacobelll', 
    'uberx', 'lyfft', 'expdeia', 'bookingscom', 'airbmb', 'tripadvsor', 'kayakx', 'hiltonn', 'marriottx', 
    'hyattt', 'holidayin', 'bestestern', 'southest', 'deltaxx', 'americanarline', 'unitedair', 
    'fedorai', 'chormium', 'mozillafirex', 'safariie', 'outlookx', 'gmial', 'yahomail', 'icould', 
    'protonmial', 'skpe', 'zoomus', 'tweeeter', 'snapcchat', 'linkdin', 'githubb', 'bitbuket', 
    'gitlabbb', 'stackovrflow', 'redditx', 'weehcat', 'whatspp', 'signalx', 'telegrammm', 'discordx', 
    'slackkk', 'skypeee', 'drpoobox', 'googledoccs', 'wordprss', 'shopifyy', 'woocommerces', 'bitcon', 
    'ethereumx', 'litcoin', 'dogeocoin', 'coinbass', 'binanace', 'krakenx', 'blockfi', 'poloniexx', 
    'metamsk', 'unisswap', 'coinmartketcap', 'robinhoood', 'etradee', 'fidelty', 'charlesschwab', 
    'vanguad', 'jporganchase', 'goldmansahcs', 'citiibank', 'bankofmreica', 'wellfsfargo', 'ameritradee', 
    'venmoe', 'cashappx', 'zellee', 'appleepay', 'googlepeay', 'squreup', 'strpie', 'shopiyfy', 
    'woocommmerce', 'bigcomerce', 'magnto', 'ebates', 'rakutenn', 'doordahh', 'ubereats', 'postmatesx', 
    'grubhbb', 'instacrt', 'amazonfressh', 'hellofresg', 'bluedapron', 'freshlyk', 'gooodrx', 'webmdx', 
    'healthlinee', 'medcapes', 'myfiitnesspal', 'fitbitx', 'stravax', 'mapmmyrun', 'pelotonx', 'roviae', 
    'garminconnct', 'nikeeplus', 'pinterestt', 'houzzex', 'zillwow', 'redfinex', 'truliaa', 'realtorxx', 
    'angiestlist', 'thumbtacc', 'taskrabitt', 'craigslst', 'nextdorr', 'neighbrhodd', 'meetupx', 'eventbrit', 
    'facebooklivee', 'twitchtt', 'youtueblive', 'dailmymotion', 'vimeoo', 'huluuu', 'disneyppplus', 'hbomaxx', 
    'crunchyrll', 'peacocck', 'slingg', 'rokuuu', 'firetick', 'chromcastt', 'nvidiai', 'amdgrapichs', 'intellx', 
    'seagatee', 'westernndigital', 'sandiskx', 'logitecch', 'corsairr', 'razr', 'steellseries', 'alienwarre', 
    'hpprintes', 'delllcomputers', 'lenovvo', 'toshibaee', 'acerrr', 'asuscom', 'samsug', 'oneplusx', 'xiaommi', 
    'huaweii', 'oppoe', 'sonyplaystationn', 'xboxss', 'nintindo', 'epixgames', 'steeam', 'originxx', 'blizzrd', 
    'bethesday', 'riotgamez', 'ubisoftt', 'eaaports', 'activison', 'rockstrar', 'mojanggg', 'googlplay', 
    'applestorre', 'fitbitx', 'wazeapp', 'mapquestt', 'goolgemaps', 'citymapp', 'tripeit', 'lonleyplanet', 
    'kayakxx', 'orbitzz', 'travelocityx', 'pricelineee', 'trivagggo', 'hotelstoday', 'ryanir', 'southwesst', 
    'alleginat', 'fronttier', 'turkshairline', 'aircanadaa', 'qunatas', 'virginatlanticc', 'baairways', 
    'finnairx', 'lufthansaa', 'icelanddair', 'emirattes', 'etihadairways', 'qatrairways', 'singaporeeair', 
    'airnz', 'anzx', 'americaneirlines', 'boeinggg', 'airbusss', 'spacexx', 'bluestarjets', 'golddstar', 
    'airasiia', 'cathayypacific', 'jalpanair', 'vietnammsairlines', 'philippineeairlines', 'telslaa', 'fararri', 
    'lambrginni', 'bugattti', 'mcclarenx', 'rollrsroyce', 'porschexx', 'maseratti', 'audiix', 'bmwxseries', 
    'mercdesbbenz', 'volkswaggon', 'volvoss', 'toyotaa', 'hondaa', 'forddx', 'chevyy', 'dodgexx', 'jeepxx', 
    'chryslerrr', 'genessis', 'hyuundii', 'acuraaa', 'lexuss', 'nissn', 'infinitix', 'subaruu', 'mitsubshhi', 
    'mazdaaa', 'tesclaxx', 'metropcsx', 'verizoon', 'attwireless', 'timmobile', 'sprintx', 'cricketx', 
    'boostt', 'goooglefi', 'mintmobilee', 'virgnmobile', 'xfinitymobilee', 'samsnggalaxy', 'appleeiphone', 
    'nokiasmartphone', 'sonyxperia', 'htccc', 'motorollaa', 'razerphhone', 'blackberyx', 'goprx', 'nvidiaax', 
    'nasaax', 'spacerxx', 'dragoncapsle', 'commericalcargo', 'inspration', 'spacewlk', 'spaceshtle', 'astronuat', 
    'venusmissoin', 'marsrvoer', 'pereservance', 'aploxo', 'skylnb', 'fiefoxx', 'googledocsx', 'evernotez', 
    'onennote', 'pdffillerx', 'dochubbs', 'wordpresxx', 'slackkk', 'discordxx', 'teslatechnix', 'solarciyy', 
    'neuraallink', 'theboringcommpany', 'startlinkx', 'holcytesky', 'gigaftory', 'autppilot', 'hyperlooppx', 
    'openaix', 'deeprmind', 'googlplex', 'alphabbet', 'applpewatch', 'musicx', 'spotiy', 'audubll', 'audacyx', 
    'soundclound', 'reverbnatt', 'bandccamp', 'soundcrrick', 'pandoraxx', 'iheartradix', 'tedddx', 'courseraax', 
    'edxorgg', 'khanacedemy', 'skillsshare', 'fivvrer', 'upwrks', 'tophatx', 'produccthunt', 'macrumrs', 
    'gogglesearch', 'googlenesw', 'thtaverge', 'wiredxx', 'slashdott', 'arsxtech', 'reecocde', '9to5goolgle', 
    'xdaa', 'androidcentralxx', 'macworldd', 'itscoop', 'tehcchrunch', 'venturebeatt', 'skpe', 'oulookxx', 
    'googldrivee', 'amazonwss', 'alibabaccloud', 'mocrosoftxx', 'zhoho', 'oraclee', 'blckchainx', 'minerexx', 
    'caffeex', 'etheruem', 'daggerscc', 'solananx', 'polkadott', 'vaporxxx', 'rednaxx', 'wavesxcoin', 'lightcoin', 
    'soildcoin', 'usdtetherx', 'hexcoin', 'tornadochahs', 'avlancex', 'harmonyyy', 'xmrmonero', 'manadecetraland', 
    'piicoinx', 'cadanaooxx', 'xlmripple', 'binananceee', 'bitconn', 'ethertum', 'litocooin', 'dogecoixn', 
    'cryptoxbx', 'powerminerxx', 'ethxchange', 'robinhoodx', 'binancenet', 'coinmatrket', 'bittradesx', 
    'orcidox', 'btcpoolll', 'gopayyc', 'cashapptx', 'venmosx', 'okcpid', 'plentyofff', 'chrstianmingl', 
    'bumblesx', 'tindrxx', 'matchtx', 'hingeapp', 'jointatxxx', 'okcupidxx', 'brsttax', 'grndrapp', 'likexxme', 
    'tossdfishx', 'gossssh', 'macysc', 'amazonprimevv', 'ecobbbbx', 'wholefodoos', 'gucciig', 'praddaa', 
    'channelll', 'louisvuitxx', 'tiffant', 'dolceeabc', 'monclerxxx', 'yyyeslaurent', 'lavchvkenne', 'carttier', 
    'vvvrxzzx', 'chanelperfume', 'hdozhs', 'giodxdet', 'bossccperfume', 'lvpurcheasesx', 'adidascx', 
    'nikeereacttt', 'trackfmomrsz', 'shpppingbaz', 'jcrewxx', 'oldnavy', 'gnpspxm', 'sportsappreal', 'wwpsxzzz'
]

    for typo in common_typos:
        if typo in url:
            return False
    return True

def check_https_protocol(url):
    return url.startswith('https://')

def check_domain_info(url):
    try:
        domain = get_domain(url)
        domain_info = whois.whois(domain)
        if domain_info and domain_info.creation_date:
            return True
        else:
            return False
    except Exception as e:
        return False  

@app.route('/check', methods=['POST'])
def check_website():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({"message": "Invalid URL", "isLegit": False}), 400

    https_valid = check_https_protocol(url)
    ssl_valid = check_ssl_certificate(url)
    misspelled_url = check_misspelled_url(url)
    domain_valid = check_domain_info(url)

    if https_valid and ssl_valid and misspelled_url and domain_valid:
        return jsonify({"message": "The website is legitimate.", "isLegit": True})
    else:
        if not https_valid:
            return jsonify({"message": "The website does not use HTTPS protocol.", "isLegit": False})
        if not ssl_valid:
            return jsonify({"message": "The website does not have a valid SSL certificate.", "isLegit": False})
        if not misspelled_url:
            return jsonify({"message": "The website URL appears to be misspelled.", "isLegit": False})
        if not domain_valid:
            return jsonify({"message": "The website domain information is suspicious.", "isLegit": False})

if __name__ == '__main__':
    app.run(debug=True)
