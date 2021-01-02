import keyboard, os, time

PASSWORD = "hello123"
SECONDS_BEFORE_LOGOFF = 10

class gaurd(object):
    def __init__(self):
        self.set_password = ""
        self.password = PASSWORD
        self.wait = True
        keyboard.on_press(self.get_char)

    def get_char(self, char):
        if self.wait:
            self.set_password += char.name

    def run_fun(self):
        self.first = time.time()
        while self.wait:
            time.sleep(0.9)
            if self.password in self.set_password:
                self.wait = False
            else:
                if time.time() - self.first > SECONDS_BEFORE_LOGOFF:
                    os.system("logoff")

    def run(self):
        self.run_fun()


my_gaurd = gaurd()
my_gaurd.run()
