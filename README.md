# Selenium integrated pytest framework

A framework is the skeleton on which a project is built, just like a good foundation, having 
a solid test framework always ensures the quality of the delivery, increases team collaboration, reduces effort
by creating more usable blocks/chunks of code and finally it may even increase the test coverage.

Salient features:
1. Cross Browser testing incorporated
2. Simplified Page Object Modelling
3. Component wrapping approach for page level methods
4. Reports incorporated through pytest html1
5. Possibility to include API automations

### System setup

This framework comes with integrated requirements.txt file which includes all the required libraries for the project.
Use the commands given below respectively to have all libraries installed.

pip install -r requirement.txt
playwright install

To update the requirements.txt file with libraries that are added later, simply run the below command:

pip freeze > requirements.txt

### Cross Browser testing 

This framework has multiple browser support which can be accessed by the following command:

pytest --browser_name "browsername"

as of 1st match 2025, this supports chrome and firefox but can easily be extended with other browsers.
if the browsername is not provided, the default browser taken will be chrome.


### Simplified POM

While we have certain textbook methods of creating the pagelocator classes, I've always found that keeping the locators 
simply as strings worked the best for me.

There are certain techniques in modifying an xpath which can save us a lot of lines of code, for instance, if there is a
form of demographics, and just by changing a class name, we can switch between elements,
I've found it more efficient to write a string as xpath and simply modify it while calling by adding the necessary text, 
this approach has saved me a lot of lines previously and was well accepted by the team as well.

To add more to the cause, there are certain operations that may not be done only through one type of locator. So having it as
string and later casting it into a type of locator of our liking is another flexibility
this framework provides.

This is easier to implement, learn and modify.

### Component Wrapping Method Development

