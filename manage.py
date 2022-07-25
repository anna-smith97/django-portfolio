#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    os.environ['DATABASE_URL'] = 'postgres://efqgkwzznvwfoo:459634ff2a72793f32ec3e1ea693b9f5a24f4ec6a8b8b590f3e02fc24dbd5861@ec2-54-87-179-4.compute-1.amazonaws.com:5432/dfamuneg8ram38'

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
