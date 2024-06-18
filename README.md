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
- TradeHub uses a spread-sheet data model, allowing flexibility and real-time updates.
#### Structure
- The three worksheets are organized in two columns, the first column contains an heading ("item", first row) followed by a list of items. The second column contains an heading ("price", first row) followed by the related prices.
- The purchases worksheet is empty to start. When a purchase is made through TradeHub it will be displayed in similar fashion as the previous ones.Starting from the first column, the first row will contain "Name" on the left hand side, following we will have the second column with the unique order n.
The second row has been left empty to give some spacing.
The third row starting from the first column will contain the items, the more items purchased the more rows we will have. Every item is followed in the second column and same row, by the respective price value.
Once the items are finished we will have a "Total £" followed on same row by the sum of the prices previously displayed.
Under the Total £, we will have Rating (note that this is an optional value.) The value related to rating is calculate in an average of 5 numbers with a range from 0 to 5. If the cell on the right hand side of "Rating" is empty , it means that the user skipped the ratings at any moment.
- If the purchases worksheet will be too "populated" feel free to delete previous purchases. 

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

### Testing

TradeHub has been tested using the Python Linter provided by Code Institute.  
[Link to Linter](https://pep8ci.herokuapp.com/)
TradeHub has been tested in different platforms:
- VScode
- GitPod
- Heroku

I tested TradeHub from the deployed link by Heroku on:
- Chrome
- Microsoft Edge
- Mobile Devices
- Tablets
- Laptop

To note that I tried testing from `IOS` devices , but as tutors said ,it is a known issue that the pack provided from Code Institute does't work properly on this kind of operative system.
All I can see/say from IOS devices is that the terminal starts without issues.

#### Manual Testing
- As I wrote before TradeHub is very stubborn. I tried many times to follow prompts with incorrect answers of many kind. But in a good way TradeHub doesn't let the user get the upperhand following a simple but rigid flow.
- Here are some examples:

| Screenshot |Title| Explanation|
|---|---|---|
|[Wrong Username](/assets/img4rdm/manualTesting.png)![Wrong Username](/assets/img4rdm/manualTesting.png)|Username test|In this example we can see how the error handling gives a feedback anytime I tried to insert something that is not acceptable (numbers,spacing, symbols and mixed characters)|
|[Wrong Category](/assets/img4rdm/categorytest.png)![Wrong Category](/assets/img4rdm/categorytest.png)|Category test|As the example before nothing gets accepted except for the correct numbers|
|[Empty Basket](/assets/img4rdm/basketEmpty.png)![Empty Basket](/assets/img4rdm/basketEmpty.png)|Basket test|In here I tried to enter in the basket but being empty TradeHub realizes that and gives you a feedback about it.|
|[Wrong Items](/assets/img4rdm/itemsTest.png)![Wrong Items](/assets/img4rdm/itemsTest.png)|Items test|In this example as the previous tests I tried to insert various different characters , but "successfully" TradeHub reacted in the right way.In this case we also have the quantity tested succesfully.|
|[Basket Test](/assets/img4rdm/basketTest.png)![Basket Test](/assets/img4rdm/basketTest.png)|Basket test|Same as previous examples the test was successfull. Nothing passed except for the accepted values.|
|[Rating Test](/assets/img4rdm/ratingTest.png)![Rating Test](/assets/img4rdm/ratingTest.png)|Rating test|Here as well the error handlers do the right "job" giving access to the next step only entering the right values.|


### Bugs and Fixes

| Screenshot |Title| Explanation|
|---|---|---|
|[First Bug](/assets/img4rdm/bug1.png)![First Bug](/assets/img4rdm/bug1.png)|Wrong value|During the development a bug found was that in the worksheets the number values were being formatted in the wrong way. To solve this problem I changed the format to float so doesn't round the number giving the exact printed value.(To note that the value was just not displayed correctly, but the cell contained the right data.)|
|[Second Bug](/assets/img4rdm/Bug3.png)![Second Bug](/assets/img4rdm/Bug3.png)|Wrong Return|In this case I found the bug during the manual testing. I found the problem when I was tring to insert wrong values. For example when going for the basket and insterting on purpose a wrong value, I was getting redirected to the previous step instead of asking for the right value.What I did to solve this was returning different value or enhancing the error handling to return the wanted result|
|[Second Bug.1](/assets/img4rdm/bug4.png)![Second Bug.1](/assets/img4rdm/bug4.png)|2nd Bug.1|More examples|
|[Second Bug.2](/assets/img4rdm/bug5.png)![Second Bug.2](/assets/img4rdm/bug5.png)|2nd Bug.2|More examples|
|[Third Bug](/assets/img4rdm/bug6.png)![Third Bug](/assets/img4rdm/bug6.png)|Third Bug|The third bug found was that I wasn't updating correctly the purchase worksheet. Every new purchase was overriding the previous one, and that would be a big issue in a real world case.The solution was simple , I implemented in the code a way to find out if the columns were empty or already used. If already used we just simply needed to find the next empty spot|
- Some other bugs were related to indexing and updating the worksheets but nothing that needed major changes.

#### Fixes

- The only big fixes that have been done is the reformatting of huge function to smoller ones. Giving a better readability and more efficency.
- The other big fix that I did was moving around functions repositioning some functions where I thought was logically following the workflow.
- One small fix but not less important was the amount of item the user can purchase. Before I didn't insert a limit so the user could buy n^inf amount of items at once. This was giving hard time to TradeHub that was breaking down after 3/4 minutes. What I did  to fix this problem was giving the user a limit of 5 items at time. Solving the problem of processing too many items at once. 

### Remaining Bugs or fixes

- Something that need to be fixed is between the code and the spreadsheet. Basically is a size problem where once the columns are finished the program doesn't find anymore space where to record the new purchases. I increased the size of the spreadsheet manually to solve the initial problem.
- Same issue would be for the order number. I choose to give the user a 5 digit "reference n." that goes from 0 to 99999. It would be a problem to reach (even if large) that amount. Giving the program no way to continue after all numbers available are used.


### Validation

- To validate the code I used PEP8 [CI Python Linter](https://pep8ci.herokuapp.com/)
![Validation](/assets/img4rdm/pythonLinter.png)



