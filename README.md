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

**Git Repository Contents** 

Here is an overview of the folders you’ll find in the Git repository, which you’ll clone in the next section.

+ Main sources for the application. Consists of 4 pages (index, about, blog, contact) with a master layout. Static content and scripts include bootstrap, jquery and respond.  
![1](https://github.com/ymr89/MsBlog/blob/master/Images-README/1.jpg)
![2](https://github.com/ymr89/MsBlog/blob/master/Images-README/2.jpg)

+ Local management and development server support. Use this to run the application locally, synchronize the database, and create super user.  
![3](https://github.com/ymr89/MsBlog/blob/master/Images-README/3.png)

+ Default database. Includes the necessary tables for the application to run, but it doesn’t contain any users (we will synchronize with a PostgreSQL or MySQL database and create a user).  
![4](https://github.com/ymr89/MsBlog/blob/master/Images-README/4.png)

+ External packages needed by this application. The deployment script will pip install the packages listed in this file.  
![5](https://github.com/ymr89/MsBlog/blob/master/Images-README/5.png)

+ IIS configuration files. The deployment script will use the appropriate web.config script.  
![6](https://github.com/ymr89/MsBlog/blob/master/Images-README/6.png)

The next 3 sections describe how to proceed with the web app development under 3 different environments:

+	Windows, with Python Tools for Visual Studio
+	Windows, with command line
+	Mac/Linux, with command line

## **Web App Creation on Portal**

The first step in creating your app is to create the web app via the [Azure Portal](https://portal.azure.com).

1. Log into the Azure Portal and click the **NEW** button in the bottom left corner.
3. In the search box, type "web app".
4. In the search results, select **Web App**, then click **Create**.
5. Configure the new app, such as creating a new App Service plan and a new resource group for it. Then, click **Create**.
6. Configure Git publishing for your newly created web app by following the instructions at [Local Git Deployment to Azure App Service](app-service-deploy-local-git.md).

## **Web App Development**

**Windows – Python Tools for Visual Studio** 

+	Clone the repository.  
First, clone the repository using the URL provided on development section.  
Open the solution file (.sln) that is included in the root of the repository.  
![7](https://github.com/ymr89/MsBlog/blob/master/Images-README/7.png)

+ Change the requirements file.  
Double-click on requirements.txt. If you’re using a PostgreSQL database, add _psycopg2==2.6.2_.  
If you’re using a MySQL database, add _MySQL-python==1.2.3_. By default, requirements.txt contains the driver for a PostgreSQL database.  
![8](https://github.com/ymr89/MsBlog/blob/master/Images-README/8.png)

+ Create a virtual environment.  
Right-click on Python Environments and select Add Virtual Environment. Make sure the name is _env_. Click Create, this will create the virtual environment and the dependencies listed in requirenments.txt.  
![9](https://github.com/ymr89/MsBlog/blob/master/Images-README/9.png)

+	Change the information on the database.  
Open the folder MsBlog and double-click on settings.py.  
![10](https://github.com/ymr89/MsBlog/blob/master/Images-README/10.png)  
Scroll down until you find the DATABASES. Change the information according to your database. Save.   
Engine for PostgreSQL: _'django.db.backends.postgresql_psycopg2'_  
Engine for MySQL: _'django.db.backends.mysql'_  
![11](https://github.com/ymr89/MsBlog/blob/master/Images-README/11.png)

+	Migrate and create a superuser.  
To migrate the information into the new database, right-click on the root project, select python and click-on migrate.  
![12](https://github.com/ymr89/MsBlog/blob/master/Images-README/12.png)  
Now, create the super user. As before, right-click on the root project, select python and select Create Superuser.
![13](https://github.com/ymr89/MsBlog/blob/master/Images-README/13.png)  
Django will prompt a command-line to set the superuser. Follow the instructions. 

+	Run using developer server.  
Press F5 to start debugging, and your web browser will open automatically to the page running locally.  
![14](https://github.com/ymr89/MsBlog/blob/master/Images-README/14.png) 

+	Make changes.  
Now you can experiment by making changes to the application sources and/or templates.  
To access the admin page to add users, or add new posts, access through _/admin/_.  
![15](https://github.com/ymr89/MsBlog/blob/master/Images-README/15.png)  
Once you have logged in, you can either add posts through the admins page or in the website as _/posts/create/_.  
After you’ve tested your changes, commit to the Git repository. 

+	Deploy to Azure.  
If you need help with git, please refer to [Local Git Deployment to Azure App Service] (https://github.com/Azure/azure-content/blob/master/articles/app-service-web/app-service-deploy-local-git.md).


**Windows – Command Line**

+	Clone the repository.  
First, clone the repository using the URL provided in development section. If you need more information, see [Local Git Deployment to Azure App Service] (https://github.com/Azure/azure-content/blob/master/articles/app-service-web/app-service-deploy-local-git.md).   
```
git clone <repo-url>  
cd <repo-folder>  
git remote add azure <repo-url>  
```

+	Create a virtual environment.  
We will create a new virtual environment for development purposes (do not add it to the repository). Virtual environments in Python are not relocatable, so every developer working on the application will create their own locally.  
Make sure to have the same Python version selected for the web app.  
```
python -m venv env 
```

+	Change the requirements file. 
In the command line, type requirements.txt. 
```
requirements.txt
```  
If you’re using a PostgreSQL database, add _psycopg2==2.6.2_. If you’re using a MySQL database, add _MySQL-python==1.2.3_. By default, requirements.txt contains the driver for a PostgreSQL database.  

Install any external packages required by the application. 

```
env\Scripts\pip install -r requirements.txt
``` 

+	Change the information on the database.  
Cd into the MsBlog folder, and open the settings.py file. 

```
cd MsBlog  
idle settings.py  
```  

Scroll down until you find the DATABASES. Change the information according to your database. Save.   
Engine for PostgreSQL: _'django.db.backends.postgresql_psycopg2'_  
Engine for MySQL: _'django.db.backends.mysql'_  

![11](https://github.com/ymr89/MsBlog/blob/master/Images-README/11.png)

Don’t forget to _cd .._ to go back into the main folder after you saved the changes in your setting.py file. 

```
cd ..
```

+ Migrate and create a super user.  
Run this from the command-line from your project folder to migrate the information: 

```
python manage.py migrate
```  
Then, run this from the command-line to create a superuser: 

```
python manage.py createsuperuser
```  
Follow the prompts to set the user name, password, etc. 

+ Run using development server.  
You can launch the application running the following command:  
```
python manage.py runserver
```  
Then, you can open the browser to the URL. 

![14](https://github.com/ymr89/MsBlog/blob/master/Images-README/14.png)

+ Make changes.  
Now you can experiment by making changes to the application sources and/or templates. To access the admin page to add users, or add new posts, access through _/admin/_.

![15](https://github.com/ymr89/MsBlog/blob/master/Images-README/15.png) 

Once you have logged in, you can either add posts through the admins page or in the website as _/posts/create/_.

After you’ve tested your changes, commit them to the Git repository:

``` 
git add <modified-file>  
git commit -m "<commit-message>" 
```  

+ Deploy to azure.  
To trigger a deployment, push the changes to Azure. 

```
git push azure master
```

**Mac/Linux – Command Line**

## **Troubleshoot**
`https://blogs.msdn.microsoft.com/azureossds/2015/08/04/debug-django-web-application-in-azure-web-apps/`

## **Maintainers**

**Microsoft**
+	[Andrea Lam] (andrela@microsoft.com)
+	[Meet Bhagdev] (meetb@microsoft.com)

**Independent**
+	[Yadi Reyes] (ymr89@uw.edu)















<a href="https://azuredeploy.net/" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>



