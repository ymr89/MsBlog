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

If you don’t already have Python 3.4, you can get it from [python.org](www.python.org). Alternatively, we recommend installing [Azure SDK for Python 3.4] (https://azure.microsoft.com/en-us/develop/python/) using the Web Platform installer, which will install Python, setuptools, pip and virtualenv.

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


## **Web App Creation on Portal**

The first step in creating your app is to create the web app via the [Azure Portal](https://portal.azure.com).

1. Log into the Azure Portal and click the **NEW** button in the bottom left corner.
3. In the search box, type "web app".
4. In the search results, select **Web App**, then click **Create**.
5. Configure the new app, such as creating a new App Service plan and a new resource group for it. Then, click **Create**.
6. Configure Git publishing for your newly created web app by following the instructions at [Local Git Deployment to Azure App Service](app-service-deploy-local-git.md).

## **Web App Development**

The next 3 sections describe how to proceed with the web app development under 3 different environments:

+	[Windows, with Python Tools for Visual Studio](https://github.com/ymr89/MsBlog/blob/master/WindowsVS.md)
+	[Windows, with command line](https://github.com/ymr89/MsBlog/blob/master/WindowsCLI.md)
+	[Mac/Linux, with command line](https://github.com/ymr89/MsBlog/blob/master/LinuxMac.md)

## **Troubleshooting**

If you have trouble with Django, please refer to this [Blog](https://blogs.msdn.microsoft.com/azureossds/2015/08/04/debug-django-web-application-in-azure-web-apps/).

If you have a problem creating the vistual enviroment, please refer to [this](https://github.com/Azure/azure-content/blob/master/includes/web-sites-python-troubleshooting-virtual-environment.md)

If you need more Django documentation, refer to [this](https://www.djangoproject.com/)

## **Maintainers**

**Microsoft**
+	[Andrea Lam] (andrela@microsoft.com)
+	[Meet Bhagdev] (meetb@microsoft.com)

**Independent**
+	[Yadi Reyes] (ymr89@uw.edu)















<a href="https://azuredeploy.net/" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>



