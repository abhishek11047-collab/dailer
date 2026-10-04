from plyer import call

def make_call(self, button):
    if self.number.text:
        call.makecall(tel=self.number.text)
