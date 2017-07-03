import webbrowser
class Movie:
    def __init__(self, m_title, m_storyline, m_poster, youtube_trailer):
        self.title = m_title
        self.storyline = m_storyline
        self.poster = m_poster
        self.trail_url = youtube_trailer
    def trailer(self):
        webbrowser.open('self.trail_url')
