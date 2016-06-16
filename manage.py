#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

    reload(sys)  # Reload does the trick!
    sys.setdefaultencoding('UTF-8')

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pympm.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
