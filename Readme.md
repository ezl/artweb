
# Sms2Url

Receives SMS message from Twilio phone number, and replies with URLs to all sites that use the sent image.

## Installation

1. Ensure Firefox is installed: sudo apt-get -y install firefox
2.  Login to your Twilio account, Phone Numbers -&gt; Manage menu, and check the web hook URL for desired phone number to"  https://domain.com/sms2url/receive
3.  Ensure Python 3 is installed with one clena mySQL database
4. Copy .env.example file to artweb/.env and modify as necessary.
5.  Run setup.sh in this directory.
6.  Setup uwgsi + Nginx, and start HTTP server.

That's it, begin sending SMS messages of images to the Twilio number, everything will be logged in database, and SMS will be sent back with links to all sites containing the image.

Admin panel with stats and history of all received SMS messages is located at:
    https://domain.com/admin/



