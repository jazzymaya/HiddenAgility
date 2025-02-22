# SymCheck File Structure
Our application is structured as follows:
| File Name   | Description                                                            |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ProjectDocs      | This folder contains all the Project Deliverable files featured on the project Wiki page.                                                                                                                                                        |
| ebdjango     | This is the Django application folder where important files such as views.py, admin.py, and the migrations folder are housed.                                                                                                                                             |
| TeamPhotos   | This folder contains the photos of each team member that are used on the project Wiki page.                                                                                                                              |
| media | This folder houses all the user-uploaded images submitted via the image upload page. If this folder is deleted, a new one will be automatically generated when a user uploads another image. 
| models | This folder contains our machine learning model in .h5 format.
| templates | This folder contains the HTML code files for our homepage, image upload page, and results page. 
| db.sqlite3 | This is the default Django database file created during the creation of an application. We did not use a database in our implementation, however, this file is still needed to keep all dependencies intact.
| manage.py | This is a command-line utility that allows us to run our Django application. The command to run the server is: "python manage.py runserver".

For more information about running our application, please see our [Installation Manual](https://github.com/jazzymaya/HiddenAgility/blob/master/ProjectDocs/Artifacts/SymCheck%20Installation%20Manual.pdf) and [User Manual](https://github.com/jazzymaya/HiddenAgility/blob/master/ProjectDocs/Artifacts/SymCheck%20User%20Manual.pdf)
