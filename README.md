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

2.	Change the requirements file. 

Double-click on requirements.txt. If you’re using a PostgreSQL database, add _psycopg2==2.6.2_. If you’re using a MySQL database, add _MySQL-python==1.2.3_. By default, requirements.txt contains the driver for a PostgreSQL database. 

3.	Create a virtual environment. 

Right-click on Python Environments and select Add Virtual Environment. Make sure the name is _env_. Click Create, this will create the virtual environment and the dependencies listed in requirenments.txt. 

4.	Change the information on the database.  

Open the folder MsBlog and double-click on settings.py. 
Scroll down until you find the DATABASES. Change the information according to your database. Save. 

Engine for PostgreSQL: _'django.db.backends.postgresql_psycopg2'_

Engine for MySQL: _'django.db.backends.mysql'_

5.	Migrate and create a superuser. 

To migrate the information into the new database, right-click on the root project, select python and click-on migrate.  














<a href="https://azuredeploy.net/" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>



