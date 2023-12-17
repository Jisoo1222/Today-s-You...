# user.py
class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def sign_up(self):
        print(f"{self.username} 회원 가입을 진행합니다.")

# survey.py
def content_preference_survey():
    print("선호하시는 콘텐츠를 선택해 주세요.")
    print("1. 시")
    print("2. 소설")
    print("3. 드라마")
    print("4. 영화")
    print("5. 노래")

def user_emotion_survey():
    print("오늘 당신의 기분은?")
    print("1. 즐거움")
    print("2. 기쁨")
    print("3. 지루함")
    print("4. 화남")
    print("5. 우울함")

    choice = input("번호를 선택하세요: ")
    emotions = ["즐거움", "기쁨", "지루함", "화남", "우울함"]

    try:
        selected_emotion = emotions[int(choice) - 1]
        return selected_emotion
    except (ValueError, IndexError):
        print("올바른 번호를 선택하세요.")
        return None

# diary.py
def write_diary_entry():
    print("\n오늘의 하루를 기록해보세요:")
    diary_entry = input("일기 내용을 입력하세요: ")
    return diary_entry

# recommendation.py
def recommend_content(emotion):
    recommendations = {
        "즐거움": ["시1", "소설1", "드라마1", "영화1", "노래1"],
        "기쁨": ["시2", "소설2", "드라마2", "영화2", "노래2"],
        "지루함": ["시3", "소설3", "드라마3", "영화3", "노래3"],
        "화남": ["시4", "소설4", "드라마4", "영화4", "노래4"],
        "우울함": ["시5", "소설5", "드라마5", "영화5", "노래5"]
    }

    return recommendations.get(emotion, [])

# main.py
from user import User
from survey import content_preference_survey, user_emotion_survey
from diary import write_diary_entry
from recommendation import recommend_content

user = User("OurPreciousLife", "OurPreciousLife@gmail.com", "OurPreciousLife1234")
user.sign_up()

content_preference_survey()

# 사용자 감정 분석
emotion = user_emotion_survey()

# 추천 콘텐츠 출력
recommendations = recommend_content(emotion)
print(recommendations)
