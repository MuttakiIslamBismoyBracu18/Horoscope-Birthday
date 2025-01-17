from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app, resources={r"/*":{'origins':"*"}})
DEBUG = True
app.config.from_object(__name__)

birthstones = {
    1: ('Garnet', 'https://en.wikipedia.org/wiki/Garnet'),
    2: ('Amethyst', 'https://en.wikipedia.org/wiki/Amethyst'),
    3: ('Aquamarine', 'https://en.wikipedia.org/wiki/Aquamarine_(gemstone)'),
    4: ('Diamond', 'https://en.wikipedia.org/wiki/Diamond'),
    5: ('Emerald', 'https://en.wikipedia.org/wiki/Emerald'),
    6: ('Pearl', 'https://en.wikipedia.org/wiki/Pearl'),
    7: ('Ruby', 'https://en.wikipedia.org/wiki/Ruby'),
    8: ('Peridot', 'https://en.wikipedia.org/wiki/Peridot'),
    9: ('Sapphire', 'https://en.wikipedia.org/wiki/Sapphire'),
    10: ('Opal', 'https://en.wikipedia.org/wiki/Opal'),
    11: ('Topaz', 'https://en.wikipedia.org/wiki/Topaz'),
    12: ('Turquoise', 'https://en.wikipedia.org/wiki/Turquoise')
}

zodiac_dates = {
    'Capricorn': ((12, 22), (1, 19)),
    'Aquarius': ((1, 20), (2, 18)),
    'Pisces': ((2, 19), (3, 20)),
    'Aries': ((3, 21), (4, 19)),
    'Taurus': ((4, 20), (5, 20)),
    'Gemini': ((5, 21), (6, 20)),
    'Cancer': ((6, 21), (7, 22)),
    'Leo': ((7, 23), (8, 22)),
    'Virgo': ((8, 23), (9, 22)),
    'Libra': ((9, 23), (10, 22)),
    'Scorpio': ((10, 23), (11, 21)),
    'Sagittarius': ((11, 22), (12, 21))
}

zodiac_signs = [
    ('Capricorn', (datetime(1, 12, 22), datetime(1, 1, 19))),
    ('Aquarius', (datetime(1, 1, 20), datetime(1, 2, 18))),
    ('Pisces', (datetime(1, 2, 19), datetime(1, 3, 20))),
    ('Aries', (datetime(1, 3, 21), datetime(1, 4, 19))),
    ('Taurus', (datetime(1, 4, 20), datetime(1, 5, 20))),
    ('Gemini', (datetime(1, 5, 21), datetime(1, 6, 20))),
    ('Cancer', (datetime(1, 6, 21), datetime(1, 7, 22))),
    ('Leo', (datetime(1, 7, 23), datetime(1, 8, 22))),
    ('Virgo', (datetime(1, 8, 23), datetime(1, 9, 22))),
    ('Libra', (datetime(1, 9, 23), datetime(1, 10, 22))),
    ('Scorpio', (datetime(1, 10, 23), datetime(1, 11, 21))),
    ('Sagittarius', (datetime(1, 11, 22), datetime(1, 12, 21))),
    ('Capricorn', (datetime(1, 12, 22), datetime(1, 12, 31))),
]

horoscopes = {
    'Capricorn': "Conserve your energy today as you might face some tough decisions.",
    'Aquarius': "Creativity will be your best ally today.",
    'Pisces': "Pay attention to the dreams you have; they might tell you something important.",
    'Aries': "Your energy and drive will help you deal with any challenge today.",
    'Taurus': "Take a moment to appreciate the beauty in the world around you.",
    'Gemini': "Your adaptability will serve you well today; be ready for sudden changes.",
    'Cancer': "Emotional security is important, but don't be afraid to step out of your comfort zone.",
    'Leo': "Let your natural leadership qualities shine, but remember to listen to others.",
    'Virgo': "Your attention to detail will lead you to success.",
    'Libra': "Balance is key today—avoid extremes in work or play.",
    'Scorpio': "A mystery may be revealed to you today.",
    'Sagittarius': "Adventure is out there; don't be afraid to explore."
}

facts_about_signs = {
    'Capricorn': "Capricorns are known for their discipline and management skills.",
    'Aquarius': "Aquarius-born are shy and quiet but highly intellectual.",
    'Pisces': "Pisces are very friendly, often finding themselves in a company of very different people.",
    'Aries': "Aries loves to be number one, so it’s no surprise that these audacious rams are the first sign of the zodiac.",
    'Taurus': "Taurus is an earth sign represented by the bull.",
    'Gemini': "Gemini represents two different personalities in one and you will never be sure which one you will face.",
    'Cancer': "Cancer is one of the most challenging zodiac signs to get to know.",
    'Leo': "Leos love to be surrounded by modern and trendy things.",
    'Virgo': "Virgos are always paying attention to the smallest details and their deep sense of humanity makes them one of the most careful signs of the zodiac.",
    'Libra': "Libras are fascinated by balance and symmetry, they are in a constant chase for justice and equality.",
    'Scorpio': "Scorpio-born are passionate and assertive people.",
    'Sagittarius': "Curious and energetic, Sagittarius is one of the biggest travelers among all zodiac signs."
}


@app.route('/', methods=['GET'])
def greetings():
    return("Hello, World!!")

@app.route('/calculate', methods=['POST'])
@cross_origin(origin="localhost:8080")
def calculate_age():
    if not request.is_json:
        print("Request is not JSON!")
        return jsonify({"error": "Missing JSON in request"}), 400

    data = request.get_json()
    print("Received data:", data)
    from_date = datetime.strptime(data['fromDate'], '%Y-%m-%d')
    to_date = datetime.strptime(data['toDate'], '%Y-%m-%d')
    delta = to_date - from_date
    
    age_years = to_date.year - from_date.year - ((to_date.month, to_date.day) < (from_date.month, from_date.day))
    age_months = age_years * 12 + to_date.month - from_date.month
    age_weeks = delta.days // 7
    age_days = delta.days
    leap_years = count_leap_years(from_date.year, to_date.year)

    zodiac_info = get_zodiac_info(from_date)

    extra_months = to_date.month - from_date.month - (to_date.day < from_date.day)
    extra_days = to_date.day - from_date.day

    if extra_days < 0:
        days_in_prev_month = (to_date - timedelta(days=to_date.day)).day
        extra_days += days_in_prev_month

    if extra_months < 0:
        extra_months += 12

    generation = "Unknown"
    if from_date.year < 1946:
        generation = "The Silent Generation"
    elif from_date.year < 1965:
        generation = "Baby Boomer"
    elif from_date.year < 1981:
        generation = "Generation X"
    elif from_date.year < 1997:
        generation = "Millennials"
    elif from_date.year < 2013:
        generation = "Generation Z"

    
    birth_month = from_date.month
    birthstone_name, birthstone_url = birthstones[birth_month]
    
    return jsonify({
        'age': age_years,
        'months': age_months,
        'weeks': age_weeks,
        'days': age_days,
        'leapYears': leap_years,
        'generation': generation,
        'extra_months': extra_months,
        'extra_days': extra_days,
        'birthstone': {
            'name': birthstone_name,
            'url': birthstone_url
        },
        'zodiac': zodiac_info
    })


def count_leap_years(year1, year2):
    leap_years = 0
    for year in range(year1, year2 + 1):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            leap_years += 1
    return leap_years

def get_zodiac_sign(month, day):
    for zodiac, (start_date, end_date) in zodiac_dates.items():
        if (month == start_date[0] and day >= start_date[1]) or \
           (month == end_date[0] and day <= end_date[1]):
            return zodiac
    return "Unknown"

def get_zodiac_info(birth_date):
    month = birth_date.month
    day = birth_date.day
    year = birth_date.year
    zodiac_sign = get_zodiac_sign(month, day)
    life_path_number = calculate_life_path_number(month, day, year)
    compatibility_info = get_zodiac_compatibility(zodiac_sign)

    if zodiac_sign:
        horoscope = horoscopes.get(zodiac_sign, "No horoscope available.")
        facts = facts_about_signs.get(zodiac_sign, "No facts available.")
        more_info_url = f"https://en.wikipedia.org/wiki/{zodiac_sign}_(astrology)"

        return {
            'sign': zodiac_sign,
            'horoscope': horoscope,
            'facts': facts,
            'more_info_url': more_info_url,
            'life_path_number': life_path_number,
            'compatibility': compatibility_info
        }
    else:
        return {
            'sign': "Unknown",
            'horoscope': "No horoscope available.",
            'facts': "No facts available.",
            'more_info_url': "https://en.wikipedia.org/wiki/Zodiac"
        }
        
def calculate_life_path_number(month, day, year):
    digits = [int(i) for i in str(month) + str(day) + str(year)]
    while len(digits) > 1:
        digits = [int(i) for i in str(sum(digits))]
    return digits[0]

def get_zodiac_compatibility(sign):
    compatibility_chart = {
        'Aries': {
            'Aquarius': 'High - Both love independence and are driven.',
            'Gemini': 'High - A dynamic and energetic pairing.',
            'Leo': 'High - Both signs are fiery and share a zest for life.',
            'Sagittarius': 'High - Both love adventures and have an optimistic outlook.',
            'Aries': 'Medium - Passionate but potentially competitive relationships.',
            'Virgo': 'Medium - If they respect each other’s strengths, the relationship can flourish.',
            'Libra': 'Medium - Attracts as opposites, but may face challenges in the long run.',
            'Pisces': 'Medium - They complement each other if they find balance.',
            'Taurus': 'Low - Aries is spontaneous, Taurus seeks stability.',
            'Cancer': 'Low - Potential for friction and misunderstanding.',
            'Scorpio': 'Low - Power struggles likely.',
            'Capricorn': 'Low - Different values and attitudes.',  
        },
        'Taurus': {
            'Taurus': 'High - Comfortable and harmonious, sharing similar values.',
            'Cancer': 'High - Both signs are nurturing and value home life.',
            'Virgo': 'High - Both Earth signs, they have a natural understanding of each other.',
            'Capricorn': 'High - Both appreciate and strive for security and stability.',
            'Pisces': 'High - Taurus offers grounding, Pisces brings emotional depth.',
            'Gemini': 'Medium - If Taurus offers security and Gemini provides variety, it can work.',
            'Leo': 'Medium - If mutual respect is maintained, it’s a steady pairing.',
            'Libra': 'Medium - They share a love of beauty and culture but may struggle with indecisiveness.',
            'Scorpio': 'Medium - A relationship of intensity and depth.',
            'Sagittarius': 'Low - Taurus may find Sagittarius too flighty.',
            'Aries': 'Low - Taurus values harmony, which conflicts with Aries’ boldness.',
            'Aquarius': 'Low - Taurus is traditional, Aquarius is unconventional.',
            
        },
        'Gemini': {
            'Aries': 'High - Mutual appreciation for spontaneity and adventure.',
            'Leo': 'High - Both enjoy social life and excitement; a vibrant match.',
            'Libra': 'High - Both are air signs and have a strong intellectual connection.',
            'Sagittarius': 'High - Both are curious and love freedom, forming a creative pair.',
            'Aquarius': 'High - Both are intellectual, independent, and sociable.',
            'Taurus': 'Medium - If Gemini can offer variety within Taurus’ need for comfort, it can work.',
            'Gemini': 'Medium - Can be a stimulating relationship as long as they manage their mutual inconsistency.',
            'Pisces': 'Medium - Gemini brings intellectual stimulation, and Pisces brings creativity.',
            'Cancer': 'Low - Gemini’s need for independence clashes with Cancer’s need for emotional connection.',
            'Virgo': 'Low - Different approaches to life; Virgo is methodical, Gemini is spontaneous.',
            'Scorpio': 'Low - Gemini is light-hearted and social, while Scorpio is intense and private.',
            'Capricorn': 'Low - Gemini may find Capricorn too serious and unadventurous.',  
        },
        'Cancer': {
            'Taurus': 'High - Both enjoy comfort and stability, forming a loyal bond.',
            'Cancer': 'High - Deep understanding of each other’s emotional needs.',
            'Virgo': 'High - Both signs are caring and nurturing, often forming a stable relationship.',
            'Scorpio': 'High - Both are emotional and intuitive, creating a deeply connected relationship.',
            'Pisces': 'High - Both are sensitive and empathetic, often feeling a strong, emotional connection.',
            'Leo': 'Medium - If Leo can respect Cancer’s emotions and Cancer can appreciate Leo’s expressiveness, it can work.',
            'Libra': 'Medium - Cancer’s need for a cozy home life may be at odds with Libra’s sociable nature.',
            'Capricorn': 'Medium - Opposites that can complement each other with effort: Cancer’s warmth with Capricorn’s ambition.',
            'Aries': 'Low - Cancer’s sensitivity may conflict with Aries’ directness.',
            'Gemini': 'Low - Cancer’s need for closeness might overwhelm Gemini’s need for space.',
            'Sagittarius': 'Low - Cancer may find Sagittarius too restless, and Sagittarius may find Cancer too clingy.',    
            'Aquarius': 'Low - Cancer’s traditionalism contrasts with Aquarius’ rebellion.',
            
        },
        'Leo': {
            'Aries': 'High - Both are fiery and dynamic, leading to a passionate and energetic relationship.',
            'Taurus': 'Medium - Leo’s flair can dazzle Taurus, but they must manage differences in their need for attention versus stability.',
            'Gemini': 'High - Social and adventurous, they enjoy an active and engaging relationship.',
            'Cancer': 'Medium - Leo’s boldness can complement Cancer’s nurturing nature, if they understand each other’s needs.',
            'Leo': 'High - A regal partnership full of drama and passion, though they must avoid competing for the spotlight.',
            'Virgo': 'Low - Leo’s extravagance may clash with Virgo’s meticulousness, unless they appreciate their differences.',
            'Libra': 'High - Both appreciate aesthetics and luxury, sharing a love of social activities.',
            'Scorpio': 'Medium - Magnetic attraction can lead to a powerful bond, but power struggles are possible.',
            'Sagittarius': 'High - Both love freedom and exploration, making for an exciting relationship.',
            'Capricorn': 'Low - Leo’s lavishness conflicts with Capricorn’s practicality, requiring compromise.',
            'Aquarius': 'Medium - Intriguing to each other, but Leo’s need for adoration may not match Aquarius’ independence.',
            'Pisces': 'High - Leo protects and Pisces dreams, creating a nurturing and supportive relationship.'
        },
        'Virgo': {
            'Aries': 'Low - Aries’ impulsiveness can be at odds with Virgo’s cautious nature.',
            'Taurus': 'High - Both earth signs, they share a practical approach to life and a deep sense of loyalty.',
            'Gemini': 'Medium - Intellectual compatibility is strong, but Virgo’s need for order may clash with Gemini’s free spirit.',
            'Cancer': 'High - A supportive and caring relationship, with each valuing home and family.',
            'Leo': 'Low - Virgo’s modesty contrasts with Leo’s flamboyance, though they can offer each other balance.',
            'Virgo': 'High - A harmonious and understanding relationship, with a shared approach to life and love of order.',
            'Libra': 'Medium - Shared intellectual interests, but Virgo’s practicality may clash with Libra’s indecisiveness.',
            'Scorpio': 'High - A strong bond with mutual respect, both valuing privacy and depth in their relationships.',
            'Sagittarius': 'Low - Virgo’s detail-oriented nature may stifle Sagittarius’ love of freedom and adventure.',
            'Capricorn': 'High - Both value hard work and ambition, creating a strong and practical partnership.',
            'Aquarius': 'Medium - Shared intellectual pursuits, but may struggle with emotional connection.',
            'Pisces': 'High - Virgo offers grounding, while Pisces adds a touch of magic and romance.'
        },
        'Libra': {
            'Aries': 'Medium - A dynamic attraction with potential for balance, but requires effort to harmonize Aries’ directness with Libra’s diplomacy.',
            'Taurus': 'Medium - Shared love for beauty and art, but Taurus’ stubbornness may clash with Libra’s indecision.',
            'Gemini': 'High - Both are air signs with a love for socializing, communication, and intellectual stimulation.',
            'Cancer': 'Low - Libra’s sociability may feel superficial to Cancer, who seeks emotional depth.',
            'Leo': 'High - Shared appreciation for the finer things in life and social events, making a glamorous pair.',
            'Virgo': 'Medium - Respect for each other’s intellect, but may struggle with different approaches to life.',
            'Libra': 'High - A harmonious and aesthetically pleasing relationship, but may lack depth without effort.',
            'Scorpio': 'Low - Libra’s light-heartedness conflicts with Scorpio’s intensity and need for deep connections.',
            'Sagittarius': 'High - Both love adventure and exploration, though Sagittarius’ bluntness may hurt Libra’s sensitivities.',
            'Capricorn': 'Low - Different values, with Capricorn’s seriousness contrasting with Libra’s love of harmony and social life.',
            'Aquarius': 'High - Both air signs, sharing intellectual interests and a forward-looking perspective.',
            'Pisces': 'Medium - A romantic connection is possible, but Pisces’ emotional depth may overwhelm Libra’s need for harmony.'
        },
        'Scorpio': {
            'Aries': 'Medium - Both have strong personalities, leading to passionate but potentially conflict-ridden interactions.',
            'Taurus': 'High - A strong physical and emotional connection, though stubbornness can lead to challenges.',
            'Gemini': 'Low - Scorpio’s depth contrasts with Gemini’s lighter approach to life.',
            'Cancer': 'High - Emotional and intuitive, both value deep connections and loyalty.',
            'Leo': 'Medium - Magnetic attraction, but their strong wills might clash.',
            'Virgo': 'High - Mutual respect for each other’s strengths, leading to a strong and supportive relationship.',
            'Libra': 'Low - Scorpio’s intensity might overwhelm Libra’s need for harmony.',
            'Scorpio': 'High - Intensely rewarding but also challenging, with a need for mutual respect and understanding.',
            'Sagittarius': 'Low - Scorpio’s need for emotional depth may conflict with Sagittarius’ love of freedom.',
            'Capricorn': 'High - Both are determined and value security, leading to a strong foundation.',
            'Aquarius': 'Low - Scorpio’s emotional intensity is at odds with Aquarius’ independence.',
            'Pisces': 'High - A deep, empathetic connection with mutual respect and understanding.'
        },
        'Sagittarius': {
            'Aries': 'High - Both love adventure and have a great enthusiasm for life.',
            'Taurus': 'Low - Sagittarius’ need for freedom clashes with Taurus’ need for stability.',
            'Gemini': 'High - Both are curious and enjoy a relationship full of variety and excitement.',
            'Cancer': 'Low - Sagittarius’ frankness may hurt sensitive Cancer.',
            'Leo': 'High - A mutual love for adventure and a strong creative bond.',
            'Virgo': 'Low - Sagittarius’ spontaneity conflicts with Virgo’s need for order.',
            'Libra': 'High - Both enjoy exploring new ideas and cultures, leading to a dynamic relationship.',
            'Scorpio': 'Low - Sagittarius’ love of freedom clashes with Scorpio’s need for depth and intimacy.',
            'Sagittarius': 'High - An adventurous and freedom-loving partnership, though they may need to work on commitment.',
            'Capricorn': 'Low - Sagittarius’ spontaneity is at odds with Capricorn’s structured approach.',
            'Aquarius': 'High - Both value independence and intellectual pursuits, making for an exciting relationship.',
            'Pisces': 'Medium - Sagittarius’ optimism can complement Pisces’ dreaminess, but they may struggle with practical matters.'
        },
        'Capricorn': {
            'Aries': 'Low - Capricorn’s methodical approach conflicts with Aries’ impulsiveness.',
            'Taurus': 'High - Both value stability and have a practical approach to life, creating a strong bond.',
            'Gemini': 'Low - Capricorn’s seriousness contrasts with Gemini’s sociability and need for variety.',
            'Cancer': 'High - Both are caring and value security, leading to a nurturing relationship.',
            'Leo': 'Low - Capricorn’s pragmatism may dampen Leo’s exuberance.',
            'Virgo': 'High - A shared approach to life that values diligence and practicality.',
            'Libra': 'Low - Capricorn’s focus on practicality may conflict with Libra’s idealistic nature.',
            'Scorpio': 'High - Both are determined and value depth in relationships, creating a strong connection.',
            'Sagittarius': 'Low - Capricorn’s need for structure clashes with Sagittarius’ need for freedom.',
            'Capricorn': 'High - A strong, ambitious partnership, though they may need to work on flexibility and spontaneity.',
            'Aquarius': 'Low - Capricorn’s traditionalism conflicts with Aquarius’ unconventional nature.',
            'Pisces': 'High - Capricorn offers grounding, while Pisces brings emotional depth and creativity.'
        },
        'Aquarius': {
            'Aries': 'High - A dynamic duo that thrives on adventure and new experiences.',
            'Taurus': 'Low - Taurus’ need for stability may clash with Aquarius’ love for freedom.',
            'Gemini': 'High - Both air signs, they share a strong intellectual connection and love for social activities.',
            'Cancer': 'Low - Cancer’s emotional depth might be overwhelming for the more detached Aquarius.',
            'Leo': 'High - Both enjoy creativity and can have a dynamic, if sometimes competitive, relationship.',
            'Virgo': 'Medium - If they can appreciate their differences, they can form a relationship based on mutual respect.',
            'Libra': 'High - Both air signs, they enjoy intellectual discussions and share a love of social justice.',
            'Scorpio': 'Low - Scorpio’s intensity can clash with Aquarius’ need for space and freedom.',
            'Sagittarius': 'High - Both value independence and have a mutual love for adventure and exploration.',
            'Capricorn': 'Low - Capricorn’s traditional approach can be at odds with Aquarius’ unconventional ways.',
            'Aquarius': 'High - They understand each other’s need for independence and can have a harmonious relationship.',
            'Pisces': 'Medium - Pisces’ emotional depth can either drown or enchant Aquarius, depending on mutual understanding and respect.'
        },
        'Pisces': {
            'Aries': 'Medium - Aries’ boldness can either fascinate or overwhelm Pisces’ sensitivity.',
            'Taurus': 'High - Taurus provides the stability Pisces craves, and Pisces brings a touch of magic to Taurus’ life.',
            'Gemini': 'Low - Gemini’s need for intellectual stimulation might not always meet Pisces’ emotional depth.',
            'Cancer': 'High - Both water signs, they share a deep emotional connection and intuitive understanding of each other.',
            'Leo': 'Medium - Leo’s warmth and generosity can light up Pisces’ world, as long as Leo is patient with Pisces’ emotional needs.',
            'Virgo': 'High - Their differences complement each other; Virgo provides grounding, while Pisces adds creativity and intuition.',
            'Libra': 'Medium - Libra’s charm and social grace can be attractive to Pisces, but they need to navigate their differing approaches to decision-making.',
            'Scorpio': 'High - Both are water signs, sharing an intense emotional bond and deep understanding.',
            'Sagittarius': 'Low - Sagittarius’ love for freedom and adventure might clash with Pisces’ need for closeness and security.',
            'Capricorn': 'Medium - Capricorn provides stability and structure, which Pisces finds comforting, but their emotional expressions differ.',
            'Aquarius': 'Medium - Aquarius’ innovative spirit intrigues Pisces, though their emotional wavelengths might not always align.',
            'Pisces': 'High - They share a profound emotional and spiritual connection, understanding each other’s depths like no other.'
        },
    }
    return compatibility_chart.get(sign, {})


if __name__ == "__main__":
    app.run(debug=True)