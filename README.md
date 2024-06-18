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
| Screenshot | Note | Explanation|
|---|---|---|
|[Welcome screen and user identification](/assets/img4rdm/home.png) ![Skeleton of landing page](/assets/img4rdm/home.png)|The landing screen|This is the first screen that you will see when landing. You are presented with the TradeHub's banner, this gives a simple but effective personalization to the app. Under it you have to insert a name to be able to continue. The name is stored with the complete purchase order enabling identification|
|[Category management](/assets/img4rdm/gotCategory.png)![Category list](/assets/img4rdm/gotCategory.png)|Following step after inserting the name,presents you categories|Here we have a list of categories, this list we fetched it from the "market_hub" spreadsheet. Each category is a worksheet with relative title. This allowes the user to select a category. |
|[Items management](/assets/img4rdm/items.png)![Items list](/assets/img4rdm/items.png)|After category selection we will have the items list|In here we can see the items list. From the spreadsheet prospective we have the items listed in a column followed by another column with related prices. Inside the app we can see the list and the prices with relative numbers on the left hand side. To select an item you'll need to insert the respective number , followed by the quantity that you like.|
|[Basket management](/assets/img4rdm/basket.png)![Basket screen](/assets/img4rdm/basket.png)|Basket is accessible from the options list at any moment with the only exception if the basket doesn't contains items| In the basket we will find the items that we would like to add to our purchase, we can see the items preceded by a number and followed by the quantity. In the basket we can choose also to remove items or comeback to where we were before entering it.|
|[Purchase processing](/assets/img4rdm/purchase.png)![Purchase screen](/assets/img4rdm/purchase.png)|Following step after inserting the name,presents you categories|The purchase takes count of all the items in the basket previously selected , provide a list of these items, the total price and a unique order number|
|Other features|||
|Interactive shopping flow||The aim here is to get the user to work out smoothly the navigation like it is in everyday life: get an item or more, put in the basket, remove it if we don't need it or was the wrong item, check the basket to see if we can proceed to the checkout. The program offers clear guidance throughout the entire process giving clear indications and redirecting if needed we simple feedbacks|
|Google Sheets||Google sheets provided me the way how to store our stock in different categories and different items for each category. It also allowed me to record/store the final purchase giving back real-time updates and retrievals|
|Error handling||My aim  here is to provide as much help as possible to the user cutting all the edges over wrong inputs. The user is presented with many prompts and I tried to make sure that anytime something goes sideways the program will be able to explain the user how to proceed correctly, we can say that TradeHub is a very "stubborn" application in a user friendly way|
|Unique order number||To ensure that the user "theoretically" will never have the chance to get the same "reference number" as another user , I implemented a simple random generation of 5 numbers adding some identification also over the purchase. Note I said theoretically because the written code goes from 00000 to 99999 so in this case if we go over that amount we could have an issue with processing due to number repetition|


### Data model
- TradeHub uses a spread-sheet data model, allowing flexibility and real-time updates

| Screenshot |Title| Explanation|
|---|---|---|
|[Clothes worksheet](/assets/img4rdm/clothes.png)![Clothes list](/assets/img4rdm/clothes.png)|Clothes category|In this worksheet named "clothes" we can find all the items related to this category|
|[Tech worksheet](/assets/img4rdm/techcategory.png)![Tech worksheet](/assets/img4rdm/techcategory.png)|Tech category|In this worksheet named "tech" we can find all the items related to this category|
|[Groceries worksheet](/assets/img4rdm/grocerycategory.png)![Groceries worksheet](/assets/img4rdm/grocerycategory.png)|Groceries category|In this worksheet named "groceries" we can find all the items related to this category|
|[Purchases worksheet](/assets/img4rdm/purchasesheet.png)![Purchases worksheet](/assets/img4rdm/purchasesheet.png)|Purchases|In this worksheet named "purchases" we have the processed purchases. It is recorded as two column expanding downwards depending on the amount of items purchased. As we can see in the screenshot at the top of the column we have the "username" and the order number. Following down we have the item on the left followed by the price on the right and so on for the other items. At the bottom of the items list we have the total price, and under the total price we can see the ratings. If the rating value is empty it mean that the user decided to skip the ratings. To note that if the user skips the ratings at any time ,the value will not be recorded.|

#### How the process works
The aim here was to have a simple but strong/powerful way to fetch and store data.  
I opted for the `A1 notation` with the `gspread`methods used in this kind of structures.
Having the first three categories filled in the worksheet makes it easy to target the cells needed in the program. 
Different way is used in the purchase process , where I created the 2 columns from within the code and uploaded them to the "purchases" worksheet.

| Screenshot |Title| Explanation|
|---|---|---|
|[Retrieve Titles](/assets/img4rdm/gspreadm1.png)![Retrieve Titles](/assets/img4rdm/gspreadm1.png)|Example 1|In this example we can see how the worksheets titles are retrieved or ignored using `gspread` library, in this case the tiles are used to print the category names.|
|[Retrieve Data](/assets/img4rdm/gspreadm2.png)![Retrieve Data](/assets/img4rdm/gspreadm2.png)|Example 2|In this second example we can see how we can select all values from a specific worksheet|
|[Inspecting worksheet](/assets/img4rdm/gspreadm3.png)![Inspecting worksheet](/assets/img4rdm/gspreadm3.png)|Example 3|In this third example I used methods to check if a specific cell (in this case the top row) contains data/values or is empty. The code in the example has been implemented to don't rewrite the previous purchase(I will get back to this in the bugs and fixes)|
|[Recording the purchase](/assets/img4rdm/gspreadm4.png)![Recording the purchase](/assets/img4rdm/gspreadm4.png)|Example 4|The fourth example it's the entire process that records the purchase in the "purchase" worksheet. It updates specific cells , for example iterating through the items in the basket and updating the cells starting from the third row (3+i). next_column from the previous example, and item[n] selects the chosen data/value. In simple words ,the first block of code updates the items, the second chunk updates the total price , the third block is getting the order number and the fifth chunk is about the average rating(everything works in a very similar way).(Note that the fourth block of code is printing in the terminal but nothing is affecting the spreadsheet)|
