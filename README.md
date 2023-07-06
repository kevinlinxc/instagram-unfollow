# instagram-unfollow
Unfollow everyone who doesn't follow you on Instagram


## Warning
First of all, using this script is not 100% safe. I've never been banned and I don't think you will be either, but if 
you do spam this script a bunch or unfollow 1000 people in 30 minutes, it's in the realm of possibility and I take no 
liability. Use at your own discretion.

Instagram WILL message you to confirm the login (for me, it says the device is "6T Dev"), that is expected. Sometimes, 
Instagram gets me to log in all over again on my phone too.

Second, this script uses [Instagrapi](https://github.com/adw0rd/instagrapi) and assumes that that library is not malicious. 
It has a lot of stars and no user-submitted issues related to security or stolen accounts, so I think it's safe, but again,
I'm not liable.

## How to use
1. Install Python, e.g. [Python 3.11.4](https://www.python.org/downloads/release/python-3114/). Scroll down and
choose an installer. While installing, make sure to check "Add Python 3.11 to PATH".
If you can open a terminal and run `python --version` and see `Python 3.11.4`, you're good to go, otherwise google
how to add Python to your PATH.
2. Clone this repository or just download and unzip the files (Green "Code" button in the top right of the repository 
page). Open a terminal in the directory where you downloaded `instagram-unfollow`
3. Install requirements by running `pip install instagrapi Pillow python-dotenv` in your terminal.
4. Create a file called `.env` in the same directory as `unfollow.py` and add the following lines (replacing the right
side of the `=` with your own info):
```
IG_USERNAME=your_username
IG_PASSWORD=your_password
IG_2FA=your_2fa_code
```

This assumes that you use an authenticator app for 2FA. If you use SMS, or don't use 2FA, delete the `IG_2FA` line.
5. Run `python unfollow.py` in your terminal (before your 2FA code expires!). If you get an error, read it and figure
out what went wrong. Your phone might ask you to confirm the login, so do that. The script will take some time
to run if you have a lot of followers/following, so be patient. After getting the list of followers/following, it will
prompt you to curate the list of people to unfollow. Follow the instructions, and you'll be good to go.

## Known issues
The script might not get all of your followers/following (e.g. when I was following 1700 people, the Instagrapi only
found ~1500. I'm not sure why; it might be rate-limiting or banned users or something, it's not a huge deal though.
Just wait a day and run the script again and it should get the rest of the users.