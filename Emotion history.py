from datetime import datetime

class EmotionHistoryManager:
    def __init__(self):
        self.users = {}  # 사용자 정보를 저장할 딕셔너리

    def register_user(self, username):
        if username not in self.users:
            self.users[username] = {"emotions": {}}
            print(f"{username}님이 가입되었습니다.")
        else:
            print(f"{username}님은 이미 가입되어 있습니다.")

    def record_emotion(self, username, emotion):
        current_date = datetime.now()
        current_month = current_date.strftime("%Y-%m")
        current_year = current_date.strftime("%Y")

        if username in self.users:
            if current_month not in self.users[username]["emotions"]:
                self.users[username]["emotions"][current_month] = {"daily_emotions": {}}

            if current_year not in self.users[username]["emotions"]:
                self.users[username]["emotions"][current_year] = {"monthly_emotions": {}}

            current_day = current_date.strftime("%d")

            # 월별 기록
            self.users[username]["emotions"][current_month]["daily_emotions"][current_day] = emotion

            # 연간 기록
            if current_month not in self.users[username]["emotions"][current_year]["monthly_emotions"]:
                self.users[username]["emotions"][current_year]["monthly_emotions"][current_month] = {}

            self.users[username]["emotions"][current_year]["monthly_emotions"][current_month][current_day] = emotion

            print(f"{username}님의 {current_month}의 감정이 성공적으로 기록되었습니다.")
        else:
            print(f"{username}님은 가입되어 있지 않습니다.")

    def view_emotion_history(self, username, period):
        if username in self.users:
            if period.count("-") == 1:  # 월별 감정 기록 조회
                self._view_monthly_emotion_history(username, period)
            elif period.count("-") == 0:  # 연간 감정 기록 조회
                self._view_yearly_emotion_history(username, period)
            else:
                print("올바른 기간 형식이 아닙니다. (예: '2023-12' 또는 '2023')")
        else:
            print(f"{username}님은 가입되어 있지 않습니다.")

    def _view_monthly_emotion_history(self, username, month):
        if month in self.users[username]["emotions"]:
            monthly_emotions = self.users[username]["emotions"][month]["daily_emotions"]
            print(f"\n{username}님의 {month}의 감정 기록:")
            for day, emotion in monthly_emotions.items():
                print(f"{month}-{day}: {emotion}")
            
            self._plot_emotion_distribution(monthly_emotions)
        else:
            print(f"{username}님의 {month}에 대한 감정 기록이 없습니다.")

    def _view_yearly_emotion_history(self, username, year):
        if year in self.users[username]["emotions"]:
            yearly_emotions = self.users[username]["emotions"][year]["monthly_emotions"]
            print(f"\n{username}님의 {year}의 감정 기록:")
            for month, daily_emotions in yearly_emotions.items():
                print(f"{month}: {', '.join([f'{day}: {emotion}' for day, emotion in daily_emotions.items()])}")
            
            self._plot_emotion_distribution(yearly_emotions)
        else:
            print(f"{username}님의 {year}에 대한 감정 기록이 없습니다.")

    def _plot_emotion_distribution(self, emotions):
        emotion_counts = {}
        for emotion in emotions.values():
            emotion_counts[emotion] = emotion_counts.get(emotion, 0) + 1

        print("\n감정 분포:")
        for emotion, count in emotion_counts.items():
            print(f"{emotion}: {count}")

# 감정 히스토리 매니저 초기화
emotion_history_manager = EmotionHistoryManager()

# 사용자 등록
emotion_history_manager.register_user("OurPreciousLife")

# 월별 및 연간 감정 기록
emotion_history_manager.record_emotion("OurPreciousLife", "기쁨")
emotion_history_manager.record_emotion("OurPreciousLife", "우울함")
emotion_history_manager.record_emotion("OurPreciousLife", "즐거움")

# 이전 월 및 연간의 감정 히스토리 확인
emotion_history_manager.view_emotion_history("OurPreciousLife", "2023-12")
emotion_history_manager.view_emotion_history("OurPreciousLife", "2023")
