#   This file contains constants and paths used
#   in the downloads_sifter project

from os import path

#   ***** OS Paths *****

DEFAULT_HOME_PATH = path.expanduser("~")

DEFAULT_DOWNLOADS_PATH = path.join(DEFAULT_HOME_PATH, "Downloads")

DEFAULT_PICTURES_PATH = path.join(DEFAULT_HOME_PATH, "Pictures")

DEFAULT_DOCUMENTS_PATH = path.join(DEFAULT_HOME_PATH, "Documents")
