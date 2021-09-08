from watcher.mouse_watcher import MouseWatcher
from time import sleep


watcher = MouseWatcher()

print(watcher.activities)
watcher.setup_hooks()

sleep(1000)
