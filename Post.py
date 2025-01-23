class Post:
    def __init__(self, username, location, description, likes_counter, comments):
        self.username = username
        self.location = location
        self.description = description
        self.likes_counter = likes_counter
        self.comments = comments
    def add_like(self):
        self.likes_counter += 1
    def add_comment_text(self, text):
        if isinstance(comment, text):
            self.comments.append(text)

