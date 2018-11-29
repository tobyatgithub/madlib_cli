# madlib_cli

**Author**: Toby  
**Version**: 1.0.0 

## Overview
<!-- Provide a high level overview of what this application is and why you are building it, beyond the fact that it's an assignment for a Code Fellows 401 class. (i.e. What's your problem domain?) -->
In this project, I created another command line game which takes advantage of Python’s built in capabilities for reading and writing files. This game is called madlib, where you ask users to input different types of words, and generate an interesting paragraph from those input. The output paragraph shall be printed on termnial screen and also saved into the directory.

## Getting Started
<!-- What are the steps that a user must take in order to build this app on their own machine and get it running? -->
To run the madlib_cli.py code on your machine, you only need python 3.6.  
To run the test_madlib_cli.py via pytest, you will need both python 3.6 and pytest.  


## Challenge
<!-- Provide a detailed description of the application design. What technologies (languages, libraries, etc) you're using, and any other relevant design information. This is also an area which you can include any visuals; flow charts, example usage gifs, screen captures, etc.-->

The most important chanllenge in this project is to extract specific words from a text according to a given pattern, and reformat the text into a new text according to user's input.  

I realize the extract part by using a for loop with a handler. The handler will search for starting indicator (in this case a '{'). Once the code finds this indicator, we start recording, until we find the close indicator (in this case a '}').  

## API
<!-- Provide detailed instructions for your applications usage. This should include any methods or endpoints available to the user/client/developer. Each section should be formatted to provide clear syntax for usage, example calls including input data requirements and options, and example responses or return values. -->
No API available yet.


## Change Log
<!-- Use this are to document the iterative changes made to your application as each feature is successfully implemented. Use time stamps. Here's an example:-->

11/28/18: First edition created. Have only one story embedded. 

