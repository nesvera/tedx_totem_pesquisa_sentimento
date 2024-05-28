from enum import Enum

from .root import Root
from .confirmation import ConfirmationView
from .vote import VoteView
from .fim import FimView
from .not_found import NotFoundView
from .branco import BrancoView

class Frame_Name(Enum):
    VOTE = 1
    CONFIRMATION = 2
    END = 3
    NOT_FOUND = 4
    BRANCO = 5

class View:
    def __init__(self):
        self.root = Root()
        self.frame = None

    def _add_frame(self, frame, *args, **kwargs):
        new_frame = frame(self.root, *args, **kwargs)
        new_frame.grid(row=0, column=0, sticky="news")
        return new_frame

    def switch(self, frame_name, *args, **kwargs):
        if self.frame is not None:
            self.frame.erase()

        if frame_name == Frame_Name.VOTE:
            self.frame = self._add_frame(VoteView, *args, **kwargs)
        elif frame_name == Frame_Name.CONFIRMATION:
            self.frame = self._add_frame(ConfirmationView, *args, **kwargs)
        elif frame_name == Frame_Name.END:
            self.frame = self._add_frame(FimView, *args, **kwargs)
        elif frame_name == Frame_Name.NOT_FOUND:
            self.frame = self._add_frame(NotFoundView, *args, **kwargs)
        elif frame_name == Frame_Name.BRANCO:
            self.frame = self._add_frame(BrancoView, *args, **kwargs)
        else:
            self.frame = self._add_frame(VoteView, *args, **kwargs)

        self.frame.tkraise()

    def start_mainloop(self):
        self.root.mainloop()