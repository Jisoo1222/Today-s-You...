import schedule
import time

class EmotionReminder:
    def __init__(self):
        self.users = {}  # 사용자 정보를 저장할 딕셔너리

    def register_user(self, username, notification_time):
        if username not in self.users:
            self.users[username] = {"notification_time": notification_time}
            print(f"{username}님이 가입되었습니다. 알림 시간: {notification_time}")
        else:
            print(f"{username}님은 이미 가입되어 있습니다.")

    def send_emotion_reminder(self, username):
        if username in self.users:
            print(f"{username}님, 감정 기록을 해보세요!")
        else:
            print("사용자가 존재하지 않습니다.")

    def schedule_reminders(self):
        for username, notification_time in self.users.items():
            schedule.every().day.at(notification_time).do(self.send_emotion_reminder, username)

    def run_scheduler(self):
        while True:
            schedule.run_pending()
            time.sleep(1)

# 감정 리마인더 초기화
emotion_reminder = EmotionReminder()

# 사용자 등록 및 알림 설정
emotion_reminder.register_user("User1", "09:00")
emotion_reminder.register_user("User2", "12:30")

# 알림 스케줄링 및 실행
emotion_reminder.schedule_reminders()
emotion_reminder.run_scheduler()
