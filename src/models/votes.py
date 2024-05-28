from datetime import datetime
import os

class VoteModel:
    filepath = os.path.abspath("../result/votes.csv")

    def __init__(self):
        pass

    def write_vote(self, vote):
        vote_time = datetime.now()
        vote_str = f"{vote_time},{vote},\n"

        with open(self.filepath, "a") as f:
            f.write(vote_str)
