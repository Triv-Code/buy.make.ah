This is a make/buy comparison tool for commonly used potions in World of Warcraft. Using Blizzard's API (WoW's Developer Company) the script gathers auction house data on the matieral cost to craft and the cost of buying the potion itself. Comparing the cost, the script determines if you should buy or craft, as well as, how much you'll save (converted to WoW's currency). 

Features: 

    ⦿ Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program
        • I have two lists (herbs / potions) both of which contain multiple dictionaries. All of the directionaries are updated from the API with either a cost or buy_cost key:value pair. These are eventually used for the comparison function. 

    ⦿ Create and call at least 3 functions or methods, at least one of which must return a value that is used somewhere else in your code. To clarify, at least one function should be called in your code, that function should calculate, retrieve, or otherwise set the value of a variable or data structure, return a value to where it was called, and use that value somewhere else in your code.
        • Two functions are used to filter the api and update my dictionaries in herbs/potions. Another four functions are used to convert the currency into gold/silver/copper. The final function called is the comparison function, giving us the final print out. 

    ⦿ Build a conversion tool that converts user input to another type and displays it (ex: converts cups to grams).
        • WoW's in game currency is done in Gold, Silver, and Copper. The API uses a separate currency as a single integer. Using a function for each, I convert the integer into the in game currency. 
    
    ⦿ Connect to an external/3rd party API and read data into your app.
        • Blizzard's API is used to retrieve all of the prices used in my comparison.

    ⦿ Read data from an external file, such as text, JSON, CSV, etc and use that data in your application.
        • The API call returns a JSON file, that is read from in order to update the dictionaries. 

!!! Code Louisville !!! 
The API uses OAuth and requires a new Token every 24 hours. Reach out to me on slack and I can use my credentials to supply you with an up to date token. The token itself is at the end of the URL. Once you have the updated Token, just run ```python api.py``` from the command line and you're good to go. 
