# SFHacks_2021
Contains the source code to our project that we did for the Hackathon at the San Francisco State University (https://sfhacks.io/) - 2021 edition.

## Inspiration
COVID has affected our lives a lot over the past year.  Being the victims, we wanted to help our family, especially the young kids and senior citizens from the difficulties caused through technology with our **KinShield** app.
 
## What it does
The KinShield app helps protect your family from COVID. Depending on the age, people would get notified if there is a vaccine appointment available with respect to the local government regulations. Notifications are sent to give alerts when the appointment is available.
Kids are monitored by parents using the app. Daily safety activities (washing hands, daily monitor check, etc)  are logged and reminders are sent if they missed out on one. 

## How we built it
**Android App:** We built it on **Kotlin** using **Android Studio**. We used material-design for the UI/UX. Google's **Firebase** Realtime database was used to store data. We used Notivize to send notifications for users to keep track of the healthy habits. We integrated Notivize with **Google Cloud Messaging**. The **Notivize** API is also used to send alert notifications to the users when they meet the criteria to get vaccines in their nearby region and when there is an appointment available.

**Website:** The website has been built using HTML, CSS & JavaScript. It has been connected with Firebase project as well. Python scripts were used to scrape data from the websites - _RiteAid_ and _Walgreens_. The Notivize app is used to send alert notifications to the users when they meet the criteria to get vaccines in their nearby region and is integrated with Python.


## Challenges we ran into
Scraping from Walgreens and RiteAid websites was not simple since they did not pass the location information through URL. Instead, this was the first time we worked on scraping websites that used XHR requests. It was fun inspecting the network activity and finally end up scraping.

Another major difficulty we faced was with firebase since we had not used it before. Integrating it with the website's form took us some time. 

We dockerized our Python scripts but couldn't end up deploying them on GCP CloudFunction, as per our plan.

## Accomplishments that we're proud of
The app gave us happiness as we are working on protecting families from COVID. The satisfaction derived from using our technical skills to help society is unmatched!

## What we learned
So many things - working with Google Firebase, scraping XHR requests, hosting on Domain.com, using Notivize API.

## What's next for KinShield
We would like to complete a few of the targets that we couldn't- have the web app on a GKE and scale it to consumer needs; complete the GCP Cloud Function integration and finally release it to the well-being of society :)

