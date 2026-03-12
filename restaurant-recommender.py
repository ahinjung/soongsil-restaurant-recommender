import turtle
import random

# 숭실대 주변 맛집 리스트 전체
soongsil_restaurants = [
    "명태촌 숭실대점", "명품고향삼계탕 숭실대", "취향 숭실대", "황새골손칼국수 상도동",
    "면식당 숭실대점", "긴자료코 숭실대입구역점", "초밥이야기 숭실대본점", "왕돈까스왕냉면 숭실대점",
    "더코네 숭실대", "쑝쑝돈까스 숭실대점", "신의주찹쌀순대 숭실대점", "연래춘 숭실대", "크라이치즈버거 숭실대점",
    "청년다방 숭실대점", "스톤504 스테이크하우스 숭실대입구역", "프랭크버거 숭실대점", "찌개대학부대과 숭실대",
    "철탄 함바그 텐동 숭실대", "마루스시 숭실대", "가야성 숭실대", "내가찜한닭 숭실대점", "은화수식당 숭실대",
    "맘스터치 숭실대입구역점", "샤로스톤 숭실대입구역", "멘동 숭실대", "슬로우캘리 숭실대점", "써브웨이 숭실대점",
    "밀플랜비 숭실대점", "샹츠마라 숭실대점", "준호네즉석떡볶이 숭실대", "신전떡볶이 숭실대", "아리랑컵밥 숭실대점"
]

# 가격 (원)
price_info = {
    "명태촌 숭실대점": 16000,
    "명품고향삼계탕 숭실대": 15000,
    "취향 숭실대": 7000,
    "황새골손칼국수 상도동": 12000,
    "면식당 숭실대점": 8000,
    "긴자료코 숭실대입구역점": 13000,
    "초밥이야기 숭실대본점": 14000,
    "왕돈까스왕냉면 숭실대점": 9000,
    "더코네 숭실대": 7000,
    "쑝쑝돈까스 숭실대점": 10500,
    "신의주찹쌀순대 숭실대점": 9000,
    "연래춘 숭실대": 7000,
    "크라이치즈버거 숭실대점": 10900,
    "청년다방 숭실대점": 9000,
    "스톤504 스테이크하우스 숭실대입구역": 29900,
    "프랭크버거 숭실대점": 89000,
    "찌개대학부대과 숭실대": 9000,
    "철탄 함바그 텐동 숭실대": 9900,
    "마루스시 숭실대": 20000,
    "가야성 숭실대": 11000,
    "내가찜한닭 숭실대점": 12000,
    "은화수식당 숭실대": 12500,
    "맘스터치 숭실대입구역점": 8500,
    "샤로스톤 숭실대입구역": 18000,
    "멘동 숭실대": 7500,
    "슬로우캘리 숭실대점": 12500,
    "써브웨이 숭실대점": 8700,
    "밀플랜비 숭실대점": 6000,
    "샹츠마라 숭실대점": 12000,
    "준호네즉석떡볶이 숭실대": 6500,
    "신전떡볶이 숭실대": 6000,
    "아리랑컵밥 숭실대점": 4700
}

# 식당 지도 URL
url_info = {
    "명태촌 숭실대점": "https://map.kakao.com/?q=명태촌+숭실대점",
    "명품고향삼계탕 숭실대": "https://map.kakao.com/?q=명품고향삼계탕+숭실대",
    "취향 숭실대": "https://map.kakao.com/?q=취향+숭실대",
    "황새골손칼국수 상도동": "https://map.kakao.com/?q=황새골손칼국수+상도동",
    "면식당 숭실대점": "https://map.kakao.com/?q=면식당+숭실대점",
    "긴자료코 숭실대입구역점": "https://map.kakao.com/?q=긴자료코+숭실대입구역점",
    "초밥이야기 숭실대본점": "https://map.kakao.com/?q=초밥이야기+숭실대본점",
    "왕돈까스왕냉면 숭실대점": "https://map.kakao.com/?q=왕돈까스왕냉면+숭실대점",
    "더코네 숭실대": "https://map.kakao.com/?q=더코네+숭실대",
    "쑝쑝돈까스 숭실대점": "https://map.kakao.com/?q=쑝쑝돈까스+숭실대점",
    "신의주찹쌀순대 숭실대점": "https://map.kakao.com/?q=신의주찹쌀순대+숭실대점",
    "연래춘 숭실대": "https://map.kakao.com/?q=연래춘+숭실대",
    "크라이치즈버거 숭실대점": "https://map.kakao.com/?q=크라이치즈버거+숭실대점",
    "청년다방 숭실대점": "https://map.kakao.com/?q=청년다방+숭실대점",
    "스톤504 스테이크하우스 숭실대입구역": "https://map.kakao.com/?q=스톤504+스테이크하우스+숭실대입구역",
    "프랭크버거 숭실대점": "https://map.kakao.com/?q=프랭크버거+숭실대점",
    "찌개대학부대과 숭실대": "https://map.kakao.com/?q=찌개대학부대과+숭실대",
    "철탄 함바그 텐동 숭실대": "https://map.kakao.com/?q=철탄+함바그+텐동+숭실대",
    "마루스시 숭실대": "https://map.kakao.com/?q=마루스시+숭실대",
    "가야성 숭실대": "https://map.kakao.com/?q=가야성+숭실대",
    "내가찜한닭 숭실대점": "https://map.kakao.com/?q=내가찜한닭+숭실대점",
    "은화수식당 숭실대": "https://map.kakao.com/?q=은화수식당+숭실대",
    "맘스터치 숭실대입구역점": "https://map.kakao.com/?q=맘스터치+숭실대입구역점",
    "샤로스톤 숭실대입구역": "https://map.kakao.com/?q=샤로스톤+숭실대입구역",
    "멘동 숭실대": "https://map.kakao.com/?q=멘동+숭실대",
    "슬로우캘리 숭실대점": "https://map.kakao.com/?q=슬로우캘리+숭실대점",
    "써브웨이 숭실대점": "https://map.kakao.com/?q=써브웨이+숭실대점",
    "밀플랜비 숭실대점": "https://map.kakao.com/?q=밀플랜비+숭실대점",
    "샹츠마라 숭실대점": "https://map.kakao.com/?q=샹츠마라+숭실대점",
    "준호네즉석떡볶이 숭실대": "https://map.kakao.com/?q=준호네즉석떡볶이+숭실대",
    "신전떡볶이 숭실대": "https://map.kakao.com/?q=신전떡볶이+숭실대",
    "아리랑컵밥 숭실대점": "https://map.kakao.com/?q=아리랑컵밥+숭실대점"
}


# 날씨별 분류
hot_weather = [
    "취향 숭실대", "슬로우캘리 숭실대점", "초밥이야기 숭실대본점", "마루스시 숭실대", "아리랑컵밥 숭실대점"
]
rainy_weather = [
    "신의주찹쌀순대 숭실대점", "명품고향삼계탕 숭실대", "명태촌 숭실대점", "찌개대학부대과 숭실대", "더코네 숭실대", "신전떡볶이 숭실대"
]
cold_weather = [
    "황새골손칼국수 상도동", "철탄 함바그 텐동 숭실대", "스톤504 스테이크하우스 숭실대입구역",
    "쑝쑝돈까스 숭실대점", "취향 숭실대", "샹츠마라 숭실대점"
]
mild_weather = [
    "연래춘 숭실대", "프랭크버거 숭실대점", "크라이치즈버거 숭실대점", "더코네 숭실대"
]
humid_weather = [
    "샹츠마라 숭실대점", "내가찜한닭 숭실대점", "신전떡볶이 숭실대", "찌개대학부대과 숭실대", "취향 숭실대"
]

# 기분별 분류
happy = [
    "스톤504 스테이크하우스 숭실대입구역", "샤로스톤 숭실대입구역", "쑝쑝돈까스 숭실대점",
    "초밥이야기 숭실대본점", "마루스시 숭실대", "긴자료코 숭실대입구역점", "내가찜한닭 숭실대점", "청년다방 숭실대점"
]
depressed = [
    "명품고향삼계탕 숭실대", "신의주찹쌀순대 숭실대점", "명태촌 숭실대점", "찌개대학부대과 숭실대",
    "면식당 숭실대점", "멘동 숭실대"
]
stressed = [
    "샹츠마라 숭실대점", "취향 숭실대", "신전떡볶이 숭실대", "내가찜한닭 숭실대점"
]
blank_mind = [
    "연래춘 숭실대", "가야성 숭실대", "프랭크버거 숭실대점", "써브웨이 숭실대점", "크라이치즈버거 숭실대점",
    "왕돈까스왕냉면 숭실대점", "은화수식당 숭실대", "아리랑컵밥 숭실대점", "밀플랜비 숭실대점"
]
romantic = [
    "스톤504 스테이크하우스 숭실대입구역", "샤로스톤 숭실대입구역", "철탄 함바그 텐동 숭실대",
    "긴자료코 숭실대입구역점", "쑝쑝돈까스 숭실대점"
]

weather_dict = {
    "1": hot_weather,
    "2": rainy_weather,
    "3": cold_weather,
    "4": mild_weather,
    "5": humid_weather
}

mood_dict = {
    "1": happy,
    "2": depressed,
    "3": stressed,
    "4": blank_mind,
    "5": romantic
}

# 가격대별 최대 가격 설정 (1~4)
budget_dict = {
    "1": 10000,
    "2": 15000,
    "3": 20000,
    "4": 100000
}

# 터틀 초기 설정
screen = turtle.Screen()
screen.title("오늘 뭐 먹지? - 식당 추천 프로그램")
screen.bgcolor("lightyellow")
screen.setup(width=800, height=600)
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

def write_center(text, y, font_size=24):
    pen.goto(0, y)
    pen.write(text, align="center", font=("Arial", font_size, "bold"))

def write_question(y_pos, question, choices):
    pen.goto(-350, y_pos)
    pen.write(question, font=("Arial", 16, "bold"))
    pen.goto(-300, y_pos - 30)
    for choice in choices:
        pen.write(choice, font=("Arial", 14, "normal"))
        pen.goto(-300, pen.ycor() - 25)

# 1. 날씨 입력
pen.clear()
write_center("오늘 뭐 먹지?", 250)
write_question(30, "오늘 날씨는 어떤가요? (숫자 입력)", [
    "1. 맑고 더운 날",
    "2. 비 오는 날",
    "3. 추운 날",
    "4. 선선한 날",
    "5. 습하거나 축축한 날"
])
weather = screen.textinput("날씨 입력", "1~5 중 선택하세요:")

# 2. 기분 입력
pen.clear()
write_center("오늘 뭐 먹지?", 250)
write_question(30, "지금 기분은 어떤가요? (숫자 입력)", [
    "1. 기분 좋고 활기참",
    "2. 우울하거나 처짐",
    "3. 스트레스 받음",
    "4. 아무 생각 없음",
    "5. 설렘/데이트"
])
mood = screen.textinput("기분 입력", "1~5 중 선택하세요:")

# 3. 예산 입력
pen.clear()
write_center("오늘 뭐 먹지?", 250)
write_question(30, "원하는 가격대는?", [
    "1. ~10,000원",
    "2. 10,000 ~ 15,000원",
    "3. 15,000 ~ 20,000원",
    "4. 20,000원~"
])
budget = screen.textinput("가격대 입력", "1~4 중 선택하세요:")

pen.clear()
write_center("입력 완료! 식당을 추천 중입니다...", 0, 20)

pen.clear()
def filter_by_budget(restaurants, max_price):
    return [r for r in restaurants if price_info.get(r, 1000000) <= max_price]

def draw_recommendation(restaurant, price, url):
    turtle.clear()
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.write("오늘의 추천 식당!", font=("Arial", 18, "bold"))
    turtle.goto(-200, 60)
    turtle.write(f"이름: {restaurant}", font=("Arial", 14, "normal"))
    turtle.goto(-200, 30)
    turtle.write(f"가격: {price}원", font=("Arial", 14, "normal"))
    turtle.goto(-200, 0)
    turtle.write(f"위치: {url}", font=("Arial", 10, "normal"))
    turtle.hideturtle()
    turtle.done()

def recommend_restaurant_with_turtle(weather, mood, budget):
    weather_candidates = weather_dict.get(weather, soongsil_restaurants)
    mood_candidates = mood_dict.get(mood, soongsil_restaurants)
    max_budget = budget_dict.get(budget, 1000000)
    budget_candidates = filter_by_budget(soongsil_restaurants, max_budget)

    final_candidates = set(budget_candidates) & set(weather_candidates) & set(mood_candidates)

    if not final_candidates:
        final_candidates = set(weather_candidates) & set(mood_candidates)
        if not final_candidates:
            final_candidates = set(budget_candidates)
        if not final_candidates:
            final_candidates = set(soongsil_restaurants)

    restaurant = random.choice(list(final_candidates))
    price = price_info.get(restaurant, "가격 정보 없음")
    url = url_info.get(restaurant, "URL 없음")

    draw_recommendation(restaurant, price, url)

recommend_restaurant_with_turtle(weather, mood, budget)

