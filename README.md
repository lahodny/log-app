<h1 align="center"><img src="https://www.linkpicture.com/q/logo_199.png" alt="[YOUR_ALT]" width="250"/></h1>


<div align="center">
  <p align="center">
   <img src="https://www.linkpicture.com/q/iMac-iPad-and-iPhone-1.png" alt="[YOUR_ALT]"/>
  </p>
</div>
<div align="center">
  <strong>Web app for tracking workouts and personal bests</strong>
</div>
<div align="center">
  The final year school computer science project
</div>

<hr>

# 📙 Overview
This web app was created for athletes with an idea to help them with logging their workouts and performances. 
Thanks to modern technologies, we can visualize data in various ways. I tried to create an intuitive app which would show data in the most clear way possible.
Users can spot patterns that have remained unseen and be generally more self-aware. This helps them prevent injury and set more realistic goals. Also, seeing all your progress is of course very motivating.

## ⚙️ Development setup
### Prerequisites
Make sure you have 🐳Docker installed on your PC
### Setting Up a Project
```bash
git clone https://github.com/lahodny/log-app.git
cd log-app
docker-compose build
docker-compose run web python manage.py migrate
docker-compose run web python manage.py loaddata mydata.json
docker-compose up
```
> 🔔 **Please note:** You may need to use `docker stop` if you have any containers running.

## 🎨 Used technologies
### Frontend
- <a href="https://getbootstrap.com/">Bootstrap 5</a>
- <a href="https://www.chartjs.org/">Chart.js</a>
- <a href="https://jquery.com/">jQuery</a>
- <a href="https://fontawesome.com/">Font Awesome</a>
- <a href="https://micku7zu.github.io/vanilla-tilt.js/index.html">Tilt.js</a>
- <a href="https://michalsnik.github.io/aos/">AOS</a>
### Backend
- <a href="https://www.django-cms.org/">DjangoCMS</a>
- <a href="https://www.postgresql.org/">PostgreSQL</a>
- <a href="https://django-allauth.readthedocs.io/">django-allauth</a>
- <a href="https://pypi.org/project/django-colorfield/">django-colorfield</a>
- <a href="https://django-crispy-forms.readthedocs.io/">django-crispy-forms</a>

## ✨ Features
### Website structure
<img src="https://www.linkpicture.com/q/Screenshot-26_4.png" alt="[YOUR_ALT]"/>

### Calendar
Calendar shows logged trainings. It is made using python module HTMLCalendar. Users can create their own types of training and even pick a color for them. Colors keep data in the calendar readable.
### Graphs
Grahps visualize progress of your performances. User creates a discipline and then adds performances.
### Authentication
Everything here was created thanks to python package django-allauth. You can authanticate yourself also via third party apps - Google and Facebook.
### Database model

<div align="center">
  <img src="https://www.linkpicture.com/q/er-new_1.png" width="850" alt="[YOUR_ALT]"/>
</div>


## 🌏 Browser Support

| <img src="https://user-images.githubusercontent.com/1215767/34348387-a2e64588-ea4d-11e7-8267-a43365103afe.png" alt="Chrome" width="16px" height="16px" /> Chrome | <img src="https://user-images.githubusercontent.com/1215767/34348590-250b3ca2-ea4f-11e7-9efb-da953359321f.png" alt="IE" width="16px" height="16px" /> Internet Explorer | <img src="https://user-images.githubusercontent.com/1215767/34348380-93e77ae8-ea4d-11e7-8696-9a989ddbbbf5.png" alt="Edge" width="16px" height="16px" /> Edge | <img src="https://user-images.githubusercontent.com/1215767/34348394-a981f892-ea4d-11e7-9156-d128d58386b9.png" alt="Safari" width="16px" height="16px" /> Safari | <img src="https://user-images.githubusercontent.com/1215767/34348383-9e7ed492-ea4d-11e7-910c-03b39d52f496.png" alt="Firefox" width="16px" height="16px" /> Firefox |
| :---------: | :---------: | :---------: | :---------: | :---------: |
| Yes | 11+ | Yes | Yes | Yes |

## 📝 Project status 
In the very soon future, I would like to host the app online. I'm planning use platform Heroku.

## ✌️ Feedback
I would like to know what do you think about this! It's immensely important for the future of this app. 

<a href="https://github.com/lahodny/log-app/issues">Submit feedback</a>


**Like Appollog? Give this repo a star :star: :arrow_up:.**



