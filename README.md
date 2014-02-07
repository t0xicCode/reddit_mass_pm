reddit_mass_pm
==============

Sends mass reddit PMs from the command line


INSTALL
-------

It is recommended that you setup a virtualenv, but it isn't necessary.

Simply install praw or run pip:

    pip install -r requirements.txt

Then, you can run the python script:

    ./masspm.py
    # OR
    python masspm.py

USAGE
-----

The script will first prompt you for your username and password. Once logged in as you, it will prompt you for a subject, the message contents and a list of recipients. The format of the recipient list is a comma separate list (`recipient1,recipient2,...`). The script will then send the same message to all recipients and exit.
