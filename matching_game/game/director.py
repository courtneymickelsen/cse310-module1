class Director:
    """ You have to start and finish drawing in arcade using start_render() and finish_render().
    open_window()
    draw_rectangle() expects the x and y coordinates of the center of the rectangle, the width, and the height.
    Keyboard Input: .on_key_press(), .on_key_release()
Mouse Input: .on_mouse_press(), .on_mouse_release(), .on_mouse_motion()
Updating Game Object: .on_update()
Drawing: .on_draw()"""

    def __init__(self, cast, script):
        self._cast = cast
        self._script = script
        self._keep_playing = True

