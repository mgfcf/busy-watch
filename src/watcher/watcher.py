class Watcher:
    """
    Defines generic property watcher. Hooks into a specific system parameter
    and converts it into single snippets that can be analysed.
    """

    def __init__(self, watcher_id: str, version: int):
        """Basic setup for Watcher.

        Args:
            watcher_id (str): Unique Watcher identifier, ideally human-readable. Dots and spaces will be replaced by dashes.
            version (int): Should be increased with every important version chang, to mark compatibility.
        """
        super().__init__()

        self.watcher_id = self.escape_ids(watcher_id)
        self.version = version

        self.activities = {}
        self.callbacks = []

    def setup_hooks(self) -> None:
        """
        Sets up the necessary hooks for this Watcher.
        Triggered from the outside when Watcher is used.
        """
        pass

    def destroy_hooks(self) -> None:
        """
        Removes all registered hooks for this Watcher.
        Triggered from the outside when Watcher is used.
        """
        pass

    def get_unique_activity_id(self, activity_id: str) -> str:
        """Creates an id for a given activity, that is unique application wide.

        Args:
            activity_id (str): Activity id that is unique in the scope of this Watcher.

        Returns:
            str: Application wide unique activity id.
        """
        return f'{self.watcher_id}.{self.escape_ids(activity_id)}'

    def escape_ids(self, unescaped_id: str) -> str:
        """Removes any special character from an id.

        Args:
            id (str): Unsanatized id.

        Returns:
            str: Escaped id.
        """
        return unescaped_id.replace(".", "-").replace(" ", "-")

    def register_activity(self, activity_id: str, format_description: str, trigger_description: str) -> None:
        """Activities have to be registered to be to be logged.

        Args:
            activity_id (str): Watcher-wide unique id for this event. Ideally humand-readable. Dots and spaces will be replaced by dashes.
            format_description (str): In what format will the data be stored.
            trigger_description (str): What triggers the activity.
        """
        unique_id = self.get_unique_activity_id(activity_id)

        self.activities[unique_id] = {
            "watcher_id": self.watcher_id,
            "watcher_version": self.version,
            "activity_id": self.escape_ids(activity_id),
            "format": format_description,
            "trigger": trigger_description
        }

    def _store_activity(self, activity: str, activity_id: str) -> None:
        """Takes an activity and processes it.

        Args:
            activity (str): Content of the activity, packed into a string. Can be a JSON Object.
            activity_id (str): Watcher-wide unique activity id.
        """
        # Notify callbacks
        for cb in self.callbacks:
            cb()

    def add_callback(self, cb) -> None:
        """Registers a callback for activies and hooks all activities.

        Args:
            cb (function): The function to call when an activity occurres.
        """
        if len(self.callbacks) <= 0:
            self.setup_hooks()

        self.callbacks.append(cb)
    
    def remove_callback(self, cb) -> None:
        """Removes a callback for activies and eventually removes all hooks.

        Args:
            cb (function): The function to remove from the registered callbacks.
        """
        self.callbacks.remove(cb)

        if len(self.callbacks) <= 0:
            self.destroy_hooks()
