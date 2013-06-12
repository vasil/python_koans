#!/usr/bin/env python

import os
import sys
try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
    import re
    import time
except ImportError:
    os.system("python contemplate_koans.py")

class ModifyHandler(FileSystemEventHandler):
        @classmethod
        def is_about_file(filename):
            is_file = os.path.isfile(filename)
            matches_name_pattern = re.match("^.*about_.+\.py", filename)
            return is_file and matches_name_pattern
    
        def on_modified(self, event):
            #print event.event_type, event.src_path
            if (is_about_file(event.src_path)):
                from runner.mountain import Mountain
                Mountain().walk_the_path(".")

if __name__ == "__main__":
    observer = Observer()
    observer.schedule(ModifyHandler(), ".", recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
