# Microsoft Blog

## **Description**
Microsoft Blog is a cross platform in which full time employees or interns can share experiences working at Microsoft. These stories will be available for all prospect hires and interns.  The experiences will come as a blog post by-weekly. Readers will be able to like the stories and comment through Facebook. 

The web application aims to open a different perspective for prospective employees to see a different side of the company through the stories. 

## **Features**

**Admin**: Administration is totally accessible. Administrator can create users which can access to create, modify or delete posts without continuous confirmation from the admin. 

**Contact Form**: Employees or interns interested in share their experience can contact the team and attach their stories in a contact form that will be email to the administrators. 

**Facebook comments**: People reading the posts can like, share and comment on the posts. The feature enables the comments to be recognized by user, in case some comments are inappropriate the admin will be able to remove them. 

## **Stack**

Python 3.4 (see requirements.txt for a list of python packages)

Django 1.9.7

PostgreSQL 9.5 or MySQL on Azure

## **Development**

To develop Microsoft Blog website, download or clone the repository 
[MsBlog](https://github.com/ymr89/MsBlog).


## **Prerequisites**

+	Windows, Mac or Linux
+	Python 3.4
+	Setuptools, pip, virtualenv
+	Git
+	Python Tools for Visual Studio (PTVS) This is optional. 

**Windows** 

If you don’t already have Python 3.4, you can get it from python.org. Alternatively, we recommend installing [Azure SDK for Python 3.4] (https://azure.microsoft.com/en-us/develop/python/) using the Web Platform installer, which will install Python, setuptools, pip and virtualenv.

For Git, we recommend GitHub for Windows. If you use Visual Studio, you can use the integrated Git Support with the [Python Tools 2.2 for Visual Studio] (https://github.com/Microsoft/PTVS/releases/v2.2.4).

**Mac/Linux**

You should have Python and Git already installed, make sure the version is at least 3.4. 

## **Application Overview**

**Git repository contents** 

Here is an overview of the folders you’ll find in the Git repository, which you’ll clone in the next section.

+ Main sources for the application. Consists of 4 pages (index, about, blog, contact) with a master layout. Static content and scripts include bootstrap, jquery and respond.

![1](C://Users/t-yareye/Pictures/MsBlog Documentation/1.jpg)

+ Local management and development server support. Use this to run the application locally, synchronize the database, and create super user.

+ Default database. Includes the necessary tables for the application to run, but it doesn’t contain any users (we will synchronize with a PostgreSQL or MySQL database and create a user).

+ External packages needed by this application. The deployment script will pip install the packages listed in this file. 

+ IIS configuration files. The deployment script will use the appropriate web.config script.

The next 3 sections describe how to proceed with the web app development under 3 different environments:

+	Windows, with Python Tools for Visual Studio
+	Windows, with command line
+	Mac/Linux, with command line

## **Web app development**

**Windows – Python Tools for Visual Studio** 

1.	Clone the repository.  
First, clone the repository using the URL provided on development section.  
Open the solution file (.sln) that is included in the root of the repository. 

[2.](#2) Change the requirements file.  
    Double-click on requirements.txt. If you’re using a PostgreSQL database, add _psycopg2==2.6.2_.  
    If you’re using a MySQL database, add _MySQL-python==1.2.3_. By default, requirements.txt contains the driver for a PostgreSQL database. 

3. Create a virtual environment.  
Right-click on Python Environments and select Add Virtual Environment. Make sure the name is _env_. Click Create, this will create the virtual environment and the dependencies listed in requirenments.txt. 

4.	Change the information on the database.  
Open the folder MsBlog and double-click on settings.py. 

Scroll down until you find the DATABASES. Change the information according to your database. Save. 

Engine for PostgreSQL: _'django.db.backends.postgresql_psycopg2'_  
Engine for MySQL: _'django.db.backends.mysql'_

5.	Migrate and create a superuser.  
To migrate the information into the new database, right-click on the root project, select python and click-on migrate.  

Now, create the super user. As before, right-click on the root project, select python and select Create Superuser.

Django will prompt a command-line to set the superuser. Follow the instructions. 

6.	Run using developer server.  
Press F5 to start debugging, and your web browser will open automatically to the page running locally. 
 

7.	Make changes.  
Now you can experiment by making changes to the application sources and/or templates.  
To access the admin page to add users, or add new posts, access through _/admin/_. 
 
Once you have logged in, you can either add posts through the admins page or in the website as _/posts/create/_. 

After you’ve tested your changes, commit to the Git repository. 

8.	Deploy to Azure.  
If you need help with git, please refer to [Local Git Deployment to Azure App Service] (https://github.com/Azure/azure-content/blob/master/articles/app-service-web/app-service-deploy-local-git.md).


**Windows – command line**

1.	Clone the repository.  
First, clone the repository using the URL provided in development section. If you need more information, see [Local Git Deployment to Azure App Service] (https://github.com/Azure/azure-content/blob/master/articles/app-service-web/app-service-deploy-local-git.md).

```
git clone <repo-url>  
cd <repo-folder>  
git remote add azure <repo-url>  
```
 

2.	Create a virtual environment.  
We will create a new virtual environment for development purposes (do not add it to the repository). Virtual environments in Python are not relocatable, so every developer working on the application will create their own locally.  
Make sure to have the same Python version selected for the web app. 

```
python -m venv env 
```

3.	Change the requirements file. 
Please refer to step 2 – web app development for Windows – Python Tools for Visual Studio. In the command line, just type requirements.txt.

```
requirements.txt
```
 
Install any external packages required by the application. 

```
env\Scripts\pip install -r requirements.txt
``` 

4.	Change the information from the database.  
Cd into the MsBlog folder, and open the settings.py file. To change the database settings, please refer to step 4 – web app development for Windows – Python Tools for Visual Studio. 

```
cd MsBlog  
idle settings.py  
```

Don’t forget to cd .. back after you saved the changes in your setting.py file. 

```
cd ..
```

5.	Migrate and create a super user.  
Run this from the command-line from your project folder to migrate the information: 

```
python manage.py migrate
```
 
Then, run this from the command-line to create a superuser: 

```
python manage.py createsuperuser
```
 
Follow the prompts to set the user name, password, etc. 

6.	Run using development server.  
You can launch the application running the following command: 

```
python manage.py runserver
```

Then, you can open the browser to that URL. 

7.	Make changes.  
Please refer to step 7 – web app development for Windows – Python Tools for Visual Studio.  
After you’ve tested your changes, commit them to the Git repository:

``` 
git add <modified-file>  
git commit -m "<commit-message>" 
```
 
8.	Deploy to azure.  
To trigger a deployment, push the changes to Azure. 

```
git push azure master
```
 
**Mac/Linux – command line **

## **Troubleshoot **
`https://blogs.msdn.microsoft.com/azureossds/2015/08/04/debug-django-web-application-in-azure-web-apps/`

## **Maintainers **

**Microsoft**
+	[Andrea Lam] (andrela@microsoft.com)
+	[Meet Bhagdev] (meetb@microsoft.com)

**Independent**
+	[Yadi Reyes] (ymr89@uw.edu)















<a href="https://azuredeploy.net/" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>



