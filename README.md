# NWA
Discord Username's availability checker.

(This is a fork of the original Discord Username Checker. Please retain the original author's credits and review the license before using or redistributing it.)

---
- Checks for a specific list of usernames.
- Generates and checks for a specific given amount of usernames with a specific username length, (e.g 4 letters usernames.)
- Supports Multi-Tokens.
- Supports Webhooks.
- Completely customizable.
  
 > Check <a href =#notes >notes</a> for a very important information before using this tool, and for some FAQ. And BEFORE opening an issue.

# How to use
- Have <a href="https://www.python.org/">Python</a> installed.
- First clone the repository or download it as a zip.
- Install the required libraries, by running: ```pip install -r requirements.txt``` or ```pip3 install -r requirements.txt``` in your command line.
- Open `config.ini`.
- Paste your account's token in front of the equal symbol `TOKEN`.
- Configure NWA as you'd like (`config.ini`).
- Run `nwa.py`.

> - For adding a specific list of usernames, create a file named `usernames.txt` in the same running directory as `nwa.py` and list your usernames there, separating them by a new line.
> - For adding multiple tokens, open `config.ini` and enable `MULTI-TOKEN` by making it `true` and paste your tokens inside `tokens.txt` separating them by a new line.


# Images
![](./images/1.png)


# Notes
#### Disclaimer: I'm not responsible for/of any damage/results/returns/suspension made/resulted with/by this tool. It is your will to run, and once ran, it's your responsibility.


> - This repository is licensed under a **NON-COMMERCIAL USE.** <a href="https://github.com/suenerve/Discord-Username-Checker/blob/main/LICENSE">READ here.</a>

- Please retain credits to the original author wherever the code is used.
- Spamming Discord's API is against TOS, You may get your account suspended/rate limited and I am not responsible.
- You need to get your Discord's account authorization token and paste it inside the variable `TOKEN`. Use the tool only in accordance with Discord's Terms of Service.
- Make sure to have a decent delay or you may get your account disabled.
