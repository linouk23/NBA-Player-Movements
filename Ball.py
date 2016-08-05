class Ball:
    """A class for keeping info about the balls"""
    def __init__(self, ball):
        self.x = ball[2]
        self.y = ball[3]
        self.radius = ball[4]
        self.color = '#ff8c00'  # Hardcoded orange
