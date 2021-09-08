from watcher.watcher import Watcher
import mouse


class MouseWatcher(Watcher):
    """Watches mouse inputs like movement and button activity.
    """

    def __init__(self):
        super().__init__("generic-mouse", 0)

        self.register_activity(
            "position-change", "JSON Object with parameter x and y describing the new absolute position of the pointer.", "Mouse is being moved.")

    def mouse_callback(self, event) -> None:
        print(event)

    def setup_hooks(self) -> None:
        """
        Sets up the necessary hooks for this Watcher.
        Triggered from the outside when Watcher is used.
        """
        mouse.hook(self.mouse_callback)

    def destroy_hooks(self) -> None:
        """
        Removes all registered hooks for this Watcher.
        Triggered from the outside when Watcher is used.
        """
        mouse.unhook(self.mouse_callback)
