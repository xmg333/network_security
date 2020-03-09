from pykeyboard import PyKeyboard
k = PyKeyboard()


def output():
    k.press_key(k.control_key)
    for i in range(0,1000):
        k.tap_key("v")

        k.press_key(k.enter_key)
    k.release_key(k.control_key)


if __name__ == "__main__":
    output()