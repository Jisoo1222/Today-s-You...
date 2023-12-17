import random
from collections import Counter
import time

class RealTimeEmotionMonitor:
    def __init__(self):
        self.users = {}  # 사용자 정보를 저장할 딕셔너리

    def register_user(self, username):
        if username not in self.users:
            self.users[username] = {"emotions": []}
            print(f"{username}님이 가입되었습니다.")
        else:
            print(f"{username}님은 이미 가입되어 있습니다.")

    def generate_random_emotion(self, username):
        emotions = ["즐거움", "기쁨", "지루함", "화남", "우울함"]
        random_emotion = random.choice(emotions)
        self.users[username]["emotions"].append(random_emotion)
        print(f"{username}님의 감정: {random_emotion}")

    def monitor_realtime_emotions(self):
        while True:
            time.sleep(5)  # 5초마다 실시간 감정 업데이트
            all_emotions = [emotion for user in self.users.values() for emotion in user["emotions"]]
            if all_emotions:
                most_common_emotion = Counter(all_emotions).most_common(1)[0][0]
                print(f"실시간 가장 많이 나타나는 감정: {most_common_emotion}")
            else:
                print("현재 사용자의 감정이 없습니다.")

# 실시간 감정 모니터 초기화
realtime_emotion_monitor = RealTimeEmotionMonitor()

# 사용자 등록 및 감정 생성
realtime_emotion_monitor.register_user("User1")
realtime_emotion_monitor.register_user("User2")

# 5초마다 감정 생성 및 실시간 모니터링
for _ in range(10):  # 10번 반복 (50초 동안)
    for username in realtime_emotion_monitor.users.keys():
        realtime_emotion_monitor.generate_random_emotion(username)

realtime_emotion_monitor.monitor_realtime_emotions()

