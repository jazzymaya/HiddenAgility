# SymCheck File Structure
Our application is structed as follows:
| File Name   | Description                                                            |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| .idea | This is a folder that contains the project files for the JetBrains PyCharm Python IDE. If you wish to run our application using the IDE or Intellij IDEA, you should keep this folder. If you don't, it completely is safe to delete it. |
| ProjectDocs      | This folder contains all the Project Deliverable files used on the Wiki page.                                                                                                                                                        |
| SymCheck     | This is the Django application folder where important files such as view.py, admin.py and the migrations folder are held.                                                                                                                                             |
| TeamPhotos   | This folder contains the images of each team member that is used on the Wiki page.                                                                                                                              |
| pycache | This folder contains bytecode-compiled and optimized bytecode-compiled versions of our program's files.
| djangoProject1 | This folder contains important Django files such as settings.py, urls.py, and our static folder.
| media | This folder holds all the user uploaded images that was submitted via the imageuploadpage. If you delete this folder, a new one will automatically generate when a user uploads another image. 
| models | This folder contains our Machine Learning model in .h5 format.
| templates | This folder contains the HTML files for our homepage, imageuploadpage, and resultspage. 
| db.sqlite3 | This is the default Django database file created during the creation of an application. We did not use a database in our implementation, however, this file is still needed to keep dependencies intact.
| manage.py | This is a command-line utility that allows us to run our Django application. The command to run the server is: "python manage.py runserver".
| requirements.txt | This is a text file that lists all python packages used for this application. This file was created as preparation for deploying our application in the cloud. _(Coming soon in CS692!)_ 

For more information about running our application, please visit our [Installation Manual](https://github.com/jazzymaya/HiddenAgility/blob/master/ProjectDocs/Sprint%204/HiddenAgilitySymCheck%20Installation%20Manual.pdf) and [User Manual](https://github.com/jazzymaya/HiddenAgility/blob/master/ProjectDocs/Sprint%204/SymCheck%20User%20Manual.pdf)
