from core import filters, detectors, process

class CommentAnalyser:
    def __init__(self):
        self.hate_comments = []
        self.vulgar_comments = []
        self.shout_comments = []

        with open("comments.txt", "r") as f:
            self.comments = f.readlines()

    def filter_comments(self):
        return detectors.spam_detector(filters.spam, self.comments)

    def process_comments(self, comments):
        # del len(word) < 3
        spam_comments = detectors.spam_detector(filters.spam, comments)
        # clean space in comments
        space_comments = list(map(process.space, spam_comments))
        # add tags
        tags_comments = list(map(process.add_tags, space_comments))
        # censorship of profanity
        masking_comments = list(map(process.word_masking, tags_comments))
        return masking_comments

    def pipeline(self):
        filtered_comments = self.filter_comments()
        return self.process_comments(filtered_comments)
    
if __name__ == '__main__':
    forum_comments = CommentAnalyser().pipeline()
    print(*forum_comments, sep="\n")