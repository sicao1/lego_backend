# Capstone: The Lego Terrarium - Backend  #
This Django application manages Lego sets, allowing users to track details of their Lego collection, wishlist items, and more.

## Installing ##
* Fork this repository
* Clone your forked repository
* npm i

## Approach ##
This codebase has been crafted using Python in conjunction with the Django REST framework, leveraging SQLite3 as the underlying database storage solution. Prior to deployment, components such as CORS middleware and Gunicorn were installed. To ensure a robust separation of backend and frontend concerns, this codebase was deployed on Heroku, utilizing Heroku Postgres as an integrated add-on.

The model schema was designed to encompass key fields vital for Lego set management:

* Name: Identifies the Lego set.
* Image URL: Stores the web address of the Lego set's visual representation.
* Piece Count: Captures the total number of Lego pieces within the set.
* Theme: Categorizes the Lego set according to its thematic elements.
* Assembled Status (Built): Tracks whether the set has been assembled or remains unassembled.
* Wishlist: Indicates if the set is earmarked for future acquisition or ownership.
* Set Number (Item Number): Serves as a distinct identifier for each Lego set in the system.

The implementation of this schema reflects a deliberate and comprehensive approach to managing Lego set data, ensuring an organized and efficient system for users or developers interacting with the application.

## Screenshots ##
<img width="800" alt="Lego set display" src="https://i.imgur.com/uyXTyvP.png">
<img width="800" alt="Lego form to add new set" src="https://i.imgur.com/mk9vxV5.png">

## User Stories ##
* As a user I want to be able to keep track of all the lego sets I own and see them online in one place so that I can easily update, add and delete my collections list.
* As a user I want to easily be able to add new sets to the list.
* As a user I want to be able to edit the details of a set if needed.
* As a user I want to be able to sort the list.

## Planned Features ##
* Add a wishlist section
* Add user login
* Have the ability to share the collection list with other users of the app
* Have the ability to post on a community forum

## Helpful Links ##
Live site: https://jazzy-pothos-85e300.netlify.app/
