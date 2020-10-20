# The Modern Post
#### News app that consumes the [News API](https://newsapi.org/) to serve news article from various sources.
#### By **Victor Maina**
#### [Heroku Deployment](https://the-modern-post-app.herokuapp.com/) | [Figma Link](https://www.figma.com/file/QL9rfOwNUnNPj4AbpJy7KH/The-Modern-Post?node-id=0%3A1)

---
## Description
The Modern Post is a simple Flask app that collects news articles from all around the world. On the homepage, a user can see various curated headlines from many news sources, and can also pick from the news outlet of their choice. All this is made possible by consuming the [News API](https://newsapi.org/).

## Setup/Installation Requirements

The app is deployed on Heroku, but you can also run it locally on your computer. First make sure Python3, pip, and Git are installed.
```
$ python3 --version
$ pip --version
$ git --version
```
If you don't have the above, install the like this:
```
$ sudo apt install python3 python3-pip git
```
Once installed, clone the app from this repository to you machine
```
$ git clone https://github.com/VictorKMaina/news-app.git
$ cd news-app/
```
This app requires Flask and some other dependencies to run, which are all installed in the virtual environment. To run the app, you need to activate the virtual environment. Make sure you're in the `news-app/` folder, then do
```
$ source virtual/bin/activate
```
If the virtual environment activated successfully, you should see something like this
```
(virtual) username@PC:~/../news-app$ 
```
You are now ready to run the app.
```
$ ./start.sh
```
After the Flask development server starts, open your browser and go to [the server link](http://127.0.0.1:5000/)

## Known Issues
Due to a routing bug, the app doesn't display the custom 404 page.

## Support and contact details
If you have any issues, questions, or ideas concerning the app, you can [email me](mailto:contact@victormaina.com).


## [LICENSE](./LICENSE)