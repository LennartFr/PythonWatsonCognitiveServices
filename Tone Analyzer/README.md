## Synopsis

This repo wraps a few Python apps around the Watson Tone Analyzer service on Bluemix: https://www.ibm.com/watson/developercloud/tone-analyzer.html

The interface between Python and the Watson Tone Analyzer is the Python SDK https://github.com/watson-developer-cloud/python-sdk in the  Watson Developer Cloud: https://github.com/watson-developer-cloud 

## The steps to create the Python apps

### The first step is to sign up for the IBM Bluemix Cloud. 
For that you need to go to https://bluemix.net.
The process is quite simple, as shown in this video: https://www.youtube.com/watch?v=kUPwdfL8_oU

### The second step is to launch the Watson Tone Analyzer service.
It is hosted on the IBM Bluemix Cloud https://console.ng.bluemix.net/catalog/services/tone-analyzer
Launching it is as simple as going to the Bluemix Catalog, search for the Tone Analyzer service and clicking on the Create Button on this link: https://console.ng.bluemix.net/catalog/services/tone-analyzer?taxonomyNavigation=apps

The service will quickly be up and runing 

### The third step is to learn about the Watson Tone Analyzer service and its RESTful API.

![alt text](https://www.ibm.com/watson/developercloud/doc/tone-analyzer/images/tone-analyzer.png "Title Text 1")

* Overview of the Tone Analyzer service: https://www.ibm.com/watson/developercloud/doc/tone-analyzer/index.html
* API https://www.ibm.com/watson/developercloud/tone-analyzer/api/v3/#
* Demo: https://tone-analyzer-demo.mybluemix.net/

![alt text](https://c1.staticflickr.com/4/3936/33649744240_02238c084e_z.jpg "Title Text 1")
The key information we need to be able to access the Watson Tone Analyzer is the Credentials we get when we launch the Tone Analyzer service. We find this information in the Bluemix Dashboard https://console.ng.bluemix.net/dashboard/apps/
and the picture right above shows the Service Credentials Tabs and the Credentials-1 link we click on to get our credentials.
Which consists of "url": "https://gateway.watsonplatform.net/tone-analyzer/api",
  "username": "................",
  "password": "......" 

The username and password are private to you and should not be shared with others.

## Code Example
We are now ready to write our first client app.

We typically start with a cURL script that allows us to quickly exercise the Tone Analyzer API:
For the cURL script to run, all we have to do is to insert the credentials we get from the Tone Analyzer API,
as explained above, into the cURL script. Please note that the Userid and Password have been blanked out in the
curlTone.bat file in this repo.
https://github.com/LennartFr/PythonWatsonCognitiveServices/blob/master/Tone%20Analyzer/curlTone.bat








## Motivation

A short description of the motivation behind the creation and maintenance of the project. This should explain **why** the project exists.

## Installation

Provide code examples and explanations of how to get the project.

## API Reference

Depending on the size of the project, if it is small and simple enough the reference docs can be added to the README. For medium size to larger projects it is important to at least provide a link to where the API reference docs live.

## Tests

Describe and show how to run the tests with code examples.

## Contributors

Let people know how they can dive into the project, include important links to things like issue trackers, irc, twitter accounts if applicable.

## License

A short snippet describing the license (MIT, Apache, etc.)

