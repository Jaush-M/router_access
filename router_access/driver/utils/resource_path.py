import os
import sys


def resource_path(relative_path):
    base_path = None
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    finally:
        return os.path.join(base_path, relative_path)
