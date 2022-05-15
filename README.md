# IG_Scrap3
Selenium-Python script that allows user to scrape Instagram and save user's name and handle based on the given hashtag. 

<h1>Requirements</h1>
  selenium==3.141.0
  urllib3==1.24.1
  
<h1>How does it work</h1>
Script log you into Instagram account that you provided, searches Instagram posts by provided hashtag and exports handles and names of users.

<h1>How to set up</h1>
Run the command: pip install -r requirements.txt
Download latest <a href="https://chromedriver.chromium.org/downloads">chromedriver</a>. <br>Make sure you know the path to it.
Create userProfiles and hashtags files in the root directory (make sure they're empty).<br>
Set IG_USERNAME and IG_PASSWORD variables. <br>
Run the script: python IGScrap3.py<br>

<h1>Development roadmap</h1>
<ul>
  <li>1.)Add a new feature that will download user's profile picture and store all the info into a single folder (Profile picture + Full name + Username).</li>
  <li>2.)Integrate proxies.</li>
  <li>3.)Make the whole program interactive, ask user for their input etc...</li>
