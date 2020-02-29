# Introduction to APIs

Sam Maurer  
Guest lecture for UC Berkeley [CP255 Urban Informatics](https://github.com/ual/urban-informatics-and-visualization)  
October 9, 2017

This demo introduces [APIs](https://en.wikipedia.org/wiki/Application_programming_interface), which are code-based interfaces that allow outside developers to interact with a piece of software. We'll focus primarily on data-access APIs that operate over the web. In class we'll use Python to connect to a variety of APIs, from earthquake feeds and geocoders to public social media posts.


### Before class

1. **Save the demo files to your computer**

2. **From the command line, install this Python package for connecting to Twitter APIs:**  
   `pip install TwitterAPI`  
     
   There are several different package managers for Python. We're using "pip install" instead of "conda install" because Conda doesn't include this package in its index. 


### If not enrolled in the class

3. **Sign up for Twitter API credentials (5 minutes)**

    The latter part of the demo requires free Twitter API credentials. Rename `keys-example.py` to `keys.py` and follow these instructions:
     
   * Log into Twitter or create an account: http://twitter.com  
     
   * Register a new developer project: https://dev.twitter.com/apps/new  

     (The form is geared toward people making smartphone apps or web apps, but you still have to fill it out... You can call the app a learning exercise and give the URL of these demo instructions, for example)  
     
   * Submit the form, go to the "Keys and Access Tokens" tab, and click on "Create my access token" at the bottom of the page  
     
   * Copy these four codes into the `keys.py` file:  
     (a) consumer key, (b) consumer secret, (c) access token, (d) access token secret  
