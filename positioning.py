def screen_size(window):
    screen_height = window.winfo_screenheight()
    screen_width = window.winfo_screenwidth()
    return screen_width, screen_height


def get_form_size(window):
    # Upadating windows form size
    window.update()
    window_width = (window.winfo_reqwidth())
    window_height = (window.winfo_reqheight())

    # finding the middle width & height of form to set it in middle of screen
    width_middle = round(window_width / 2)
    height_middle = round(window_height / 2)

    # to prevent sticking widget with edge of the form , width incresed by 3px.
    return window_width + 3, window_height, width_middle, height_middle


def centeralize_window(window):
    window.geometry(
        "{}x{}+{}+{}".format(get_form_size(window)[0], get_form_size(window)[1],
                             round(screen_size(window)[0] / 2)-get_form_size(window)[2],
                             round(screen_size(window)[1] / 2)-get_form_size(window)[3]))


if __name__ == "__main__":
    pass
