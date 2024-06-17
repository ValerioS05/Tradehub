![TradeHub](/assets/img4rdm/deviceMockup.png)

# TradeHub Readme

TradeHub is an interactive console based shopping application written in Python.
TradeHub interacts Google Sheet to manage inventory and record purchases.

## Links to main pages.
[TradeHub Spreadsheet ](https://docs.google.com/spreadsheets/d/1_wZuteOHdY8UPF8X3yymTwRSMhRYLE7cCkzrjmuUVsM/edit?gid=0#gid=0)

[TradeHub Application](https://tradehub-pj3-abd458db728b.herokuapp.com/)

### Let's explore TradeHub
- TradeHub has been built with a preset template offered from Code Institute.
- Folders modified for the project's realization are:
    - run.py 
        - Here is where the code for the application has been implemented
    - requirements.txt
        - Here we have the listed packages required to run the application smoothly once deployed or shared. 
        Making sure that everyone that works or will work on the project can install the exact samre requirements ,vital to run TradeHub.
    - README.md 
        - Here we have the guidance and explanation over the application.
    - Important mention is that credential have been added to get authorization and authentication (to read and write datas).
      Will be explained the "How to" later in this README.
    - Assets Folder
        - img4rdm Folder, contains .png files exclusively for this README.

### How it works
![Flowchart](/assets/img4rdm/Flowchartpj3.png)
- As we can see here , we have a flowchart explaining the application workflow.
- Important to mention is that the flowchart has been created before the application was built.

#### Walkthrough
- The "front page" of TradeHub will greet you! Welcoming you to the app and asks for a "username" to start.
- Inserting the right username will be key to pass through validation.
- Next step is selceting the category that you like to get into. The selection happens inserting the numbers appearing on the left side of the catery list.
- Once selecting the category TradeHub print you a list of items related to the category chosen. The items are listed in the same way as the category giving the app an easy understanding on how to continue navigating and a feeling of consistency.
- Once the item is selected you can choose the quantity. To mention that there's not a stock limit so you can have as many as you like.
To mention is that there's a limit per purchase so you can purchase a max of five items at time.
- Now that we set the quantity the items will be sent to the basket.
- This time you will be presented a list of options to continue shopping in the same category, change category, finish the purchase or view your basket.
- The basket is reachable in the same list as the categories, note that the basket is not accessible if the basket is empty.
When the basket contains items we have the chance to continue shopping or finishing the purchase(purchase will be explained later)
From within the basket you can also remove items if you like. Note that the removing process is one by one.
- If you want to continue to shop feel free to follow the previous steps.
- Finalizing the purchase is a simple step, you can select the final purchase from the option list or from the basket.
- When selecting to end the purchase you will be given the list of items that you selected, the total price and a unique order number.
- Ending the purchase will trigger a simple feedback survey, you can choose to skip it if you like. Leaving a feedback will let the dev improve the site and it is very quick!. 
- The purchase and the average feedback will be recorded in the "market_hub" spreadsheet.("Google spreadsheet") with your name, the unique order number, the list of items with relative prices , the total price and the average rating that you gave.
- Clit/tap on the Run program button if you like to start again. 


### Features
![HomePage](/assets/img4rdm/home.png)

