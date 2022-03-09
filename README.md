<!-- PROJECT SHIELDS -->
<!--
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

-->

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/Winkii/HoneyGain-Discord-Bot/">
    <img src="https://github.com/Winkii/HoneyGain-Discord-Bot/blob/main/Ressources/img/logo.jpg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">HoneyGain Discord Monitor</h3>

  <p align="center">
    Monitor your HoneyGain's balance
    <br />
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#requirements">Requirements</a>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li>
      <a href="#docker">Docker</a>
    </li>
    <li>
      <a href="#environment-variables">Environment Variables</a>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

It's an discord webhook for monitoring your Honeygain's balance.<br>

### What is Honeygain ?

It's an app that allows you to earn money simply by sharing your Internet. <br>
My referral link : https://bit.ly/HoneyGain_ref

<!-- GETTING STARTED -->
## Requirements
Language : Python3<br>
### Librairies required
   ```sh
pip install -r requirements.txt
   ```
### Configure the access token
Go on your dashboard : https://dashboard.honeygain.com/

To get your access token, open developer tools (or inspect element) on a chromium based browser and go to the console tab. Type in ```localStorage.getItem('JWT')``` into the console and press enter. The console with print your access token.

Copy and Paste this in the ```.env``` file
```txt
JWT_TOKEN=my_token
```
### Configure Discord Webhook
In Discord, select the Server, under Text Channels, select Edit Channel (gear icon)

Select Integrations > View Webhooks and click New Webhook.

Copy the Webhook URL and paste in the ```.env``` file.
```txt
DISCORD_CHANNEL=link_of_webhook
```

<!-- USAGE EXAMPLES -->
## Usage

Use this command for execute the HoneyGain Discord Monitor.
   ```sh
python3 launch.py
   ```

## Docker
### 🚧 Incoming...

## Environment Variables
 | Variable Name                               |   Description
 | ------------------------------------------- |:-----------------------------
 | JWT_TOKEN                                   | Authentication Token for link your HoneyGain account (<a href="#configure-the-access-token">Here</a>)
 | DISCORD_CHANNEL                             | Discord Webhook URL (<a href="#configure-discord-webhook">Here</a>)
 | BOT_USERNAME                                | Name of the Bot 



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
<!--[linkedin-url]: https://linkedin.com/in/github_username-->
