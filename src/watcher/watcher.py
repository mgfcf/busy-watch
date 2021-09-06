class Watcher:
    """
    Defines generic property watcher. Hooks into a specific system parameter
    and converts it into single snippets that can be analysed.
    """

    def hooks_setup(self) -> None:
        """
        Sets up the necessary hooks for this Watcher.
        Triggered from the outside when Watcher is used.
        """
        pass

    def hook_destroy(self) -> None:
        """
        Removes all registered hooks for this Watcher.
        Triggered from the outside when Watcher is used.
        """
        pass

    def get_available_activities(self) -> list:
        """
        @return List containing all the potential activities from this Watcher.
        """
        pass
