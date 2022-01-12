# Game Hut
My project online store called Game hub, inspired by my own pasion for gaming this online store aims to sell all things gaming.
 
## UX
### Targeted User
* This website is targeted at gamers that are interested in video games and its lore.
* People of all ages.
* Have an interest in gaming culture.
* People who like to have game merchandise.
### User Story
1. As a new user to this Website, I want to easily navigate the website so i can find 
the information i need.
2. As a new user to this Website, I want important information I need on the home page so
I can make a decision quicker.
3. As a new user to this Website, I want to be able to know what this website is about and what it can do.
4. As a new user to this Website, I want to be able to make a purchase.
5. As a new user to this Website, I want to be able to create an account. 
6. As a new user to this Website, I want to know when a purchase has been successful.

### Wireframes
My wireframes can be found within my files as seen bellow.

#### Wireframe 
Stored in this repository as "ms4-wireframe.pdf"

## Features
* Each page features the same navigation bar to create consistency
throughout the webpage.
* Each page is also reponsive.
* The home page features a hero image with overlayed text, this hero image is the first thing 
you see when you load up the webpage and it is supposed to grab the users attention and tell the user what the website is about.
* There is a "shop now" button that brings the user straight to the store.
* User can create a profile straight throught the profile button in the nav bar
*Site uses toasts so the user is confident that the just took action. for example when they add something too their basket a toast will pop up confirming it.
 
### Existing Features
* Navigation Bar - allows user to easily navigate the entire website. Exists on every page 
* Home Page  - Allows user to get all information that they would need in order 
to either go to the shop or to make their own profile
* Site uses Toasts everywhere ffor the users benefit and so they have feedback on what they are doing. 
* User can make their own profile.
*User can add add to their basket, edit and change any information aout themselves or the order they are making
*Real emails are being used to send confirmation emails to the user.

### Features Left to Implement
* More products on the site
*More user interaction,  a little more animation perhaps.
## Technologies Used
* This website uses HTML programming language.
* This website uses CSS programming language.
* This website uses Javascript programming language.
*This website uses Django.
*This website uses JSON
*This website uses font awsome
*This website uses Amazon Web Service
*This website uses Heroku
* This website uses Bootstrap CDN. bootstrap was used to ensure a responsive and consistent 
website. [https://www.bootstrapcdn.com/] 

## Testing
W3C Markup Validation and W3C CSS Validation were used to validate the code of the website.
* [https://validator.w3.org/]
* [https://jigsaw.w3.org/css-validator/]


### Testing User Stories
1. As a new user to this Website, I want to easily navigate the website so i can find 
the information i need.
* The navigation bar can be easily found on every page of the website.
* When you hover on the links in the navigation bar, the links change color to let the user know what they are about to click. Links also say way the user will be going.

2. As a new user to this Website, I want important information I need on the home page so
I can make a decision quicker.
* The hero image has a Shop now button that bring you to all products sold
* The user is presented with all information needed to make a decision on wheter to continue or not.

3. As a new user to this Website, I want to be able to know what this website is about and what it can do.
* The Home page has all information imediately available to the user.

4. As a new user to this Website, I want to be able to make a purchase.
* Once the shop now button s clicked the user is offered all the products that we sell
* Once an item is chosen and they put it in their basket all the have to do is continue to checkout and fill in their information.

5. As a new user to this Website, I want to be able to create an account.
* Every new user only needs to click the profile button where they will be able to make an account, by filling in a form.
6. As a new user to this Website, I want to know when a purchase has been successful.
* User will recieve a toast to confirm their order and also an email.

### Manually testing functionality of the website
#### Home Page:
1. Navigation Bar:
* Go to the homepage with a desktop screen size.
* Click on each link in the nav and hero button making sure that you arive to the correct destination.
*Ensure the search bar is working correctly
* Change screen size from desktop to tablet to make sure the navigation bar is responsive and
that there is no overflow issues.
* Change screensize from tablet to mobile and repeat the above step.
* Repeat these steps again using a mobile device and a tablet.

2. Hero image / button:
* Go to the homepage with a desktop screen size
* Make sure image take up 100% of the width.
* Ensure shop now button is in the correct position and is easy to read
* Change screen size from desktop to tablet checking responsiveness of the image and the text.
* Change screen size from tablet to mobile and repeat the above step. 
* Repeat these steps again using a mobile device and a tablet.

3. products page:
* Go to the products page with a desktop screen size
* change all the categories
* Search for a product
* Ensure all products are clickable.
* Ensure filter features work
* Change screen size from desktop to tablet to make sure the all content responds properly and
that there is no overflow issues with padding or margins.
* Change screen size from tablet to mobile and repeat the above step.
* Repeat these steps again using a mobile device and a tablet.

#### Login Page:
1. Navigation Bar:
* Repeat the same steps for navigation bar on Home Page
* Ensure the code is identical

2. Form:
* Ensure required information has to be entered
*Ensure toast pops up on form completion
* Change screen size from tablet to mobile and repeat the above step.
* Repeat these steps again using a mobile device and a tablet

### Log out page:
1. Navigation Bar:
* Repeat the same steps for navigation bar on Home Page
* Ensure the code is identical

2. Form:
* Ensure required information has to be entered
*Ensure toast pops up on form completion
* Change screen size from tablet to mobile and repeat the above step.
* Repeat these steps again using a mobile device and a tablet

###Profile page:
* Repeat the same steps for navigation bar on Home Page
*Ensure all required feilds must be entered
*Ensure correct toast appears on form completion
*order history should be displayed and easy to read.

###Product managment page:
* Repeat the same steps for navigation bar on Home Page
*Only the superuser can have access to this page
*Ensure all required feilds must be entered
*superuser should receive correct toast on form completion.
*superuser should be able to add products to the webpage

###Super User:
*Ensure they can do everything a normal user can do.
*Ensure that they can edit and delete products from products page and product details page.

### More Testing
1. Asked family and friends to look at the site to see if they could find any bugs. 
(This happened after I had done all my own testing and they were unable to find any bugs)

## Deployment
### This project was deployed using Heruko using github repositories
1. Ensure your project dependencies and requirements are included in a requirements.txt file
in your project folder.
2. To complete this you will need to enter the following code into your terminal
"pip3 freeze --local > requirements.txt"
3. Create a Procfile 
4. Commit and push these changes to your repository
5. Create and acccount on Heroku 
6. Once logged in select new the create new app.
7. Create a project name that is completely unique and select your region
8. Click on the option that will connect you directly to your github acount
9. Ensure it is your account that is displayed and then search for your project.
10. After this Input all of your config vars in the settings tab.
11. You may now go back to the deploy tab and "Enabe automatic deploy"
12. Then click deploy branch just underneath.
13. Your app should start to build and within a few moments youll be given an 
option to view what you deployed.
### How to run this project locally
You will need a Github account and a browser (chrome)
1. Install the gitpod chrome extension to your browser. 
[https://www.gitpod.io/docs/browser-extension/]
2. After installation, go to github.com and find this project repository.
[https://github.com/Robertl231/mileston-2-v3] 
3. Click on the green "Gitpod Button" in the top right above the repository.
4. Once this is done the site will create a new workspace for this project.
5. Enter these commands in the order for everything to work correctly.
*pip3 freeze > unins.txt && pip3 uninstall -y -r unins.txt && rm unins.txt

*pip3 install -r requirements.txt


## Credits
### Content
All Content is my own unless stated otherwise here or in the form of comments in the html 
code or here.
*Toasts were heavily inspired and taken from Boutique ado project.

### Media
#### The photos used in this site were obtained from sources listed below:
1. ACV.png - https://www.ubisoft.com/en-us/
2.bulbasaur.png - https://www.popfigures.com/
3. ghost.jpg - https://www.suckerpunch.com/category/ghost-of-tsushima/
4. gow.jpg - https://sms.playstation.com/
5. miles.png - https://www.popfigures.com/
6. pikachu.png - https://www.popfigures.com/
7. TLOU.png - https://www.naughtydog.com/
8. Uncharted.png - https://www.naughtydog.com/
9. witcher.jpg - https://thewitcher.com/en/witcher3
### Acknowledgements

I would like to thank my Mentor Miguel for all his help and guidance, aswell as my friends and family.