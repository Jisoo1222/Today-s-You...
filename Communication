class SocialStoryManager:
    def __init__(self):
        self.users = {}  # 사용자 정보를 저장할 딕셔너리
        self.stories = []  # 스토리를 저장할 리스트

    def register_user(self, username):
        if username not in self.users:
            self.users[username] = {"followings": set()}
            print(f"{username}님이 가입되었습니다.")
        else:
            print(f"{username}님은 이미 가입되어 있습니다.")

    def follow_user(self, follower, following):
        if follower in self.users and following in self.users:
            self.users[follower]["followings"].add(following)
            print(f"{follower}님이 {following}님을 팔로우합니다.")
        else:
            print("사용자가 존재하지 않습니다.")

    def post_story(self, username, content):
        story = {"username": username, "content": content, "likes": 0}
        self.stories.append(story)
        print(f"{username}님이 새로운 스토리를 게시했습니다.")
        return story

    def like_story(self, liker, story):
        if liker in self.users and story in self.stories:
            if liker != story["username"]:
                story["likes"] += 1
                print(f"{liker}님이 {story['username']}님의 스토리를 좋아합니다.")
            else:
                print("자신의 스토리에는 좋아요를 누를 수 없습니다.")
        else:
            print("사용자 또는 스토리가 존재하지 않습니다.")

    def view_timeline(self, username):
        if username in self.users:
            timeline = [story for story in self.stories if story["username"] in self.users[username]["followings"]]
            for story in timeline:
                print(f"{story['username']}님의 스토리:")
                print(story["content"])
                print(f"좋아요 수: {story['likes']}")
                print("------------")

# 소셜 스토리 매니저 초기화
social_story_manager = SocialStoryManager()

# 사용자 등록, 팔로우 및 스토리 게시
social_story_manager.register_user("User1")
social_story_manager.register_user("User2")
social_story_manager.follow_user("User1", "User2")

story1 = social_story_manager.post_story("User1", "오늘은 새로운 책을 읽었어요!")
story2 = social_story_manager.post_story("User2", "맛있는 음식을 먹었어요!")

# 사용자 간 스토리 좋아요 및 타임라인 확인
social_story_manager.like_story("User2", story1)
social_story_manager.like_story("User1", story2)

social_story_manager.view_timeline("User1")
