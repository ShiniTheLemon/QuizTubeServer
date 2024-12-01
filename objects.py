class multiplechoice:
    def __init__(self):
        self.question=None
        self.a=None
        self.b=None
        self.c=None
        self.d=None
        self.answer=None
    def set_question(self,question):
        self.question=question
    def set_a(self,a):
        self.a=a
    def set_b(self,b):
        self.b=b
    def set_c(self,c):
        self.c=c
    def set_d(self,d):
        self.d=d
    def set_answer(self,answer):
        self.answer=answer
    def get_question(self):
        return self.question
    def get_a(self):
        return self.a
    def get_b(self):
        return self.b
    def get_c(self):
        return self.c
    def get_d(self):
        return  self.d
    def ger_answer(self):
        return self.answer