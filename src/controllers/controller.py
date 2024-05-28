from controllers.sound import Sound
from controllers.buttons import Buttons, BUTTON_LABEL
from views.view import Frame_Name
from models.votes import VoteModel
from enum import Enum
import json

class FSM_States(Enum):
    VOTE = 1
    VOTE_WAITING = 2
    CONFIRM = 3
    FIM = 4
    NOT_FOUND = 5
    BRANCO = 6

class Controller:
    update_fsm_period = 100
    ticks_state_vote_wating = 20
    ticks_state_fim = 40
    ticks_state_not_found = 40
    ticks_state_branco = 40

    def __init__(self, view):
        self.view = view
        self.vote_model = VoteModel()

        self.sound = Sound()
        self.buttons = Buttons()

        self.fsm_state = FSM_States.VOTE
        self.fsm_ticks_count = 0

        self.candidate_found = False
        self.candidate_number = ""
        self.view.switch(Frame_Name.VOTE, candidate_number=self.candidate_number)

        self.candidate_info  = {}
        with open("../etc/candidates.json", "r") as f:
            candidate_file = json.load(f)
            self.candidate_info = candidate_file.get("candidates", {})


    def update_fsm(self):
        button_pressed = self.buttons.check_buttons()
        #print("pressed: ", button_pressed)
        #print("state: ", self.fsm_state)

        # events based on time
        if self.fsm_state == FSM_States.VOTE:
            if button_pressed in (BUTTON_LABEL.BTN_0,
                                  BUTTON_LABEL.BTN_1,
                                  BUTTON_LABEL.BTN_2,
                                  BUTTON_LABEL.BTN_3,
                                  BUTTON_LABEL.BTN_4,
                                  BUTTON_LABEL.BTN_5,
                                  BUTTON_LABEL.BTN_6,
                                  BUTTON_LABEL.BTN_7,
                                  BUTTON_LABEL.BTN_8,
                                  BUTTON_LABEL.BTN_9):
                self.candidate_number += button_pressed
                self.view.switch(Frame_Name.VOTE, candidate_number=self.candidate_number)
                self.sound.play_click()

                if len(self.candidate_number) == 2:
                    self.candidate_found = False
                    for candidate in self.candidate_info:
                        if candidate.get("number") == self.candidate_number:
                            self.candidate_name = candidate.get("name")
                            self.candidate_party = "Equipe TEDxBlumenau"
                            self.candidate_image = "../img/" + candidate.get("image")
                            self.candidate_found = True
                            break

                    if self.candidate_found:
                        self.fsm_state = FSM_States.VOTE_WAITING
                    else:
                        self.fsm_state = FSM_States.VOTE_WAITING

            elif button_pressed == BUTTON_LABEL.BTN_CORRIGE:
                self.candidate_number = ""
                self.view.switch(Frame_Name.VOTE, candidate_number=self.candidate_number)

            elif button_pressed == BUTTON_LABEL.BTN_BRANCO:
                self.fsm_state = FSM_States.BRANCO

                self.view.switch(Frame_Name.BRANCO)
                self.vote_model.write_vote("branco")

        elif self.fsm_state == FSM_States.VOTE_WAITING:
            if button_pressed == BUTTON_LABEL.BTN_CORRIGE:
                self.candidate_number = ""
                self.fsm_state = FSM_States.VOTE

                self.view.switch(Frame_Name.VOTE, candidate_number=self.candidate_number)
                self.buttons.flush_queue()

            if self.fsm_ticks_count >= self.ticks_state_vote_wating:
                self.fsm_ticks_count = 0

                if self.candidate_found:
                    self.fsm_state = FSM_States.CONFIRM
                    self.view.switch(Frame_Name.CONFIRMATION,
                                    candidate_number = self.candidate_number,
                                    candidate_name = self.candidate_name,
                                    candidate_party = self.candidate_party,
                                    candidate_image = self.candidate_image)
                    self.buttons.flush_queue()

                else:
                    self.fsm_state = FSM_States.NOT_FOUND
                    self.view.switch(Frame_Name.NOT_FOUND)

            self.fsm_ticks_count += 1

        elif self.fsm_state == FSM_States.CONFIRM:
            if button_pressed == BUTTON_LABEL.BTN_CORRIGE:
                self.candidate_number = ""
                self.fsm_state = FSM_States.VOTE

                self.view.switch(Frame_Name.VOTE, candidate_number=self.candidate_number)
                self.buttons.flush_queue()

            elif button_pressed ==  BUTTON_LABEL.BTN_CONFIRMA:
                self.fsm_state = FSM_States.FIM

                self.view.switch(Frame_Name.END)
                self.sound.play_confirm()

                self.vote_model.write_vote(self.candidate_number)
                self.candidate_number = ""

        elif self.fsm_state == FSM_States.FIM:
            if self.fsm_ticks_count >= self.ticks_state_fim:
                self.fsm_ticks_count = 0
                self.fsm_state = FSM_States.VOTE

                self.candidate_number = ""
                self.view.switch(Frame_Name.VOTE, candidate_number=self.candidate_number)
                self.buttons.flush_queue()

            self.fsm_ticks_count += 1

        elif self.fsm_state == FSM_States.NOT_FOUND:
            if self.fsm_ticks_count >= self.ticks_state_not_found:
                self.fsm_ticks_count = 0
                self.fsm_state = FSM_States.VOTE

                self.candidate_number = ""
                self.view.switch(Frame_Name.VOTE, candidate_number=self.candidate_number)
                self.buttons.flush_queue()

            self.fsm_ticks_count += 1

        elif self.fsm_state == FSM_States.BRANCO:
            if self.fsm_ticks_count >= self.ticks_state_branco:
                self.fsm_ticks_count = 0
                self.fsm_state = FSM_States.VOTE

                self.candidate_number = ""
                self.view.switch(Frame_Name.VOTE, candidate_number=self.candidate_number)
                self.buttons.flush_queue()

            self.fsm_ticks_count += 1

        self.view.root.after(self.update_fsm_period, self.update_fsm)

    def start(self):
        self.view.root.after(self.update_fsm_period, self.update_fsm)
        self.view.start_mainloop()
