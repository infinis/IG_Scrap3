# IG_Scrap3
Selenium-Python script that allows user to scrape Instagram and save user's name and handle based on the given hashtag. 

<h1>Requirements</h1>
  selenium==3.141.0
  urllib3==1.24.1
  
<h1>How does it work</h1>
Script log you into Instagram account that you provided, searches Instagram posts by provided hashtag and exports handles and names of users.

<h1>How to set up</h1>
Run the command: pip install -r requirements.txt
Download latest <a href="https://chromedriver.chromium.org/downloads">chromedriver</>. Make sure you know the path to it.
Create userProfiles and hashtags files in the root directory (make sure they're empty).
Set **IG_USERNAME** and **IG_PASSWORD** variables. 
Run the script: python IGScrap3.py
