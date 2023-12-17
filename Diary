from datetime import datetime

class DiaryManagerWithCalendar:
    def __init__(self):
        self.users = {}  # 사용자 정보를 저장할 딕셔너리

    def register_user(self, username):
        if username not in self.users:
            self.users[username] = {"diaries": {}}
            print(f"{username}님이 가입되었습니다.")
        else:
            print(f"{username}님은 이미 가입되어 있습니다.")

    def write_diary(self, username, emotion, diary_entry):
        current_date = datetime.now().strftime("%Y-%m-%d")

        if username in self.users:
            self.users[username]["diaries"][current_date] = {"emotion": emotion, "entry": diary_entry}
            print(f"{username}님의 일기가 성공적으로 작성되었습니다.")
        else:
            print(f"{username}님은 가입되어 있지 않습니다.")

    def view_diary_by_date(self, username, date):
        if username in self.users and date in self.users[username]["diaries"]:
            entry = self.users[username]["diaries"][date]
            print(f"\n{date}의 감정: {entry['emotion']}")
            print("일기 내용:")
            print(entry['entry'])
        else:
            print(f"{date}에 작성된 일기가 없습니다.")

# 일기 관리기와 캘린더 기능을 함께 사용
diary_manager_with_calendar = DiaryManagerWithCalendar()

# 사용자 등록
diary_manager_with_calendar.register_user("OurPreciousLife")

# 감정 일기 작성
diary_manager_with_calendar.write_diary("OurPreciousLife", "기쁨", "오늘은 정말 행복한 날이었습니다.")
diary_manager_with_calendar.write_diary("OurPreciousLife", "우울함", "하루가 힘들었어요.")

# 특정 날짜의 감정 일기 확인
diary_manager_with_calendar.view_diary_by_date("OurPreciousLife", "2023-12-17")
