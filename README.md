![TradeHub](/assets/img4rdm/deviceMockup.png)

# TradeHub Readme

TradeHub is an interactive console based shopping application written in Python.
TradeHub interacts with Google Sheet to manage inventory and record purchases.

## Links to main pages.

[TradeHub Spreadsheet ](https://docs.google.com/spreadsheets/d/1_wZuteOHdY8UPF8X3yymTwRSMhRYLE7cCkzrjmuUVsM/edit?gid=0#gid=0)

[TradeHub Application](https://tradehub-pj3-abd458db728b.herokuapp.com/)

## Readme content

1. [Exploring TradeHub](#lets-explore-tradehub)
2. [Features](#features)
3. [UI](#ui)
4. [UX](#ux)
5. [Data Model](#data-model)
6. [Testing](#testing)
7. [Bugs and Fixes](#bugs-and-fixes)
8. [Validartion](#validation)
9. [Deployment](#deployment)
10. [Techonologies](#technologies)
11. [Credits](#credits)
### Let's explore TradeHub

- TradeHub has been built with a preset template offered from **Code Institute**.
- **Folders** modified for the project's realization are:
    - **run.py**
        - Here is where the code for the application has been implemented
    - **requirements.txt**
        - Listing the packages required to run the application smoothly once deployed or shared. This ensures that everyone working on or joining the project can install the exact same requirements, which are vital for running TradeHub.
    - **README.md**
        - Here we have the guidance and explanation over the application.
    - **Important** It's important to mention that credentials have been added for authorization and authentication (to read and write data).
      Will be explained the "How to" later in this README.
    - **Assets Folder**
        - img4rdm Folder, contains .png files exclusively for this README.

### How it works

![Flowchart](/assets/img4rdm/Flowchartpj3.png)
- As we can see here , we have a **flowchart** explaining the application workflow.
- Important to mention is that the flowchart has been **created before** the application was built.
- Main thing that "diverge" from the flowchart presented above, is the basket accessibility. Now the basket can be accessed easily from different options.
Also when I created the flowchart, initially the idea was to have the basket in the spreadsheet, but during the deployment I opted to have the **basket "recorded" in a list** within the code.

#### Walkthrough

- The "front page" of TradeHub will greet you! Welcoming you to the app and asks for a **"username"** to start.
- Inserting the right username will be key to pass through **validation**.
- Next step is **selecting the category** that you like to get into. The selection happens inserting the numbers appearing on the left side of the category list.
- Once selected the category TradeHub prints you a **list of items** related to the category chosen. The items are listed in the same way as the category giving the app an **easy understanding** on how to continue navigating and a feeling of consistency.
- Once the item is selected, you can **choose the quantity**. It's worth mentioning that there's no stock limit, so you can purchase as many as you like."
To mention is that there's a limit per purchase so you can purchase a **max of five** items at time.
- Now that we've set the quantity, the items will be added to the basket.
- This time you will be presented a list of options to continue shopping in the **same category, change category, finish the purchase or view your basket**.
- The **basket** is reachable in the same list as the categories, note that the basket is not accessible if the basket is empty.
When the basket contains items we have the chance to continue shopping or finishing the purchase(purchase will be explained later)
From within the basket you can also **remove items** if you like. Note that the removing process is **one by one**.
- If you want to continue to shop feel free to follow the previous steps.
- Finalizing the **purchase** is a simple step, you can select the final purchase from the option list or from the basket.
- When selecting to end the purchase you will be given the list of items that you selected, the total price and a unique order number.
- Ending the purchase will trigger a simple **feedback survey**, you can choose to **skip** it if you like. Leaving a feedback will let the dev improve the site and it is very quick!. 
-The **purchase** and the **average feedback** will be **recorded** in the **"market_hub"** spreadsheet (Google Sheets) along with your **name, the unique order number, the list of items with their prices, the total price, and the average rating you provided**.
- Click/tap on the **Run program** button if you like to start again. 


### Features

| Screenshot | Note | Explanation|
|---|---|---|
|[Welcome screen and user identification](/assets/img4rdm/home.png) ![Skeleton of landing page](/assets/img4rdm/home.png)|The landing screen|This is the first screen that you will see when landing. You are presented with the TradeHub banner, this gives a simple but effective personalization to the app. Under it you have to insert a name to be able to continue. The name is stored with the complete purchase order enabling identification|
|[Category management](/assets/img4rdm/gotCategory.png)![Category list](/assets/img4rdm/gotCategory.png)|Following step after inserting the name,presents you categories|Here we have a list of categories, this list we fetched it from the "market_hub" spreadsheet. Each category is a worksheet with relative title. This allowes the user to select a category. |
|[Items management](/assets/img4rdm/items.png)![Items list](/assets/img4rdm/items.png)|After category selection we will have the items list|Here we can see the list of items.. From the spreadsheet prospective we have the items listed in a column followed by another column with related prices. Inside the app we can see the list and the prices with relative numbers on the left hand side. To select an item you'll need to insert the respective number , followed by the quantity that you like.|
|[Basket management](/assets/img4rdm/basket.png)![Basket screen](/assets/img4rdm/basket.png)|Basket is accessible from the options list at any moment with the only exception if the basket doesn't contains items| In the basket we will find the items that we would like to add to our purchase, we can see the items preceded by a number and followed by the quantity. In the basket we can choose also to remove items or comeback to where we were before entering it.|
|[Purchase processing](/assets/img4rdm/purchase.png)![Purchase screen](/assets/img4rdm/purchase.png)|Following step after inserting the name,presents you categories|The purchase takes count of all the items in the basket previously selected , provide a list of these items, the total price and a unique order number|
|**Other features**|||
|**Interactive shopping flow**||The aim here is to get the user to work out smoothly the navigation like it is in everyday life: get an item or more, put in the basket, remove it if we don't need it or was the wrong item, check the basket to see if we can proceed to the checkout. The program offers clear guidance throughout the entire process giving clear indications and redirecting if needed we simple feedbacks|
|**Google Sheets**||Google sheets provided me the way how to store our stock in different categories and different items for each category. It also allowed me to record/store the final purchase giving back real-time updates and retrievals|
|**Error handling**||My aim  here is to provide as much help as possible to the user cutting all the edges over wrong inputs. The user is presented with many prompts and I tried to make sure that anytime something goes sideways the program will be able to explain the user how to proceed correctly, we can say that TradeHub is a very "stubborn" application in a user friendly way|
|**Unique order number**||To ensure that the user "theoretically" will never have the chance to get the same "reference number" as another user , I implemented a simple random generation of 5 numbers adding some identification also over the purchase. Note I said theoretically because the written code goes from 00000 to 99999 so in this case if we go over that amount we could have an issue with processing due to number repetition|

### Future features

| Feature | Present | Future |
|---|---|---|
|**Specifics ratings**|At the moment when the user insert ratings feedbacks at the end of the purchase the only thing that we get is the average rating. This gives an overall performance review based on user preferences|What I would like to see a score for each prompt giving the chance to improve over a specific TradeHub aspect.|
|**Stock**|In this moment the user can buy an infinite number of items|I would like to implement stock management so the user experience is enhanced even more making TradeHub more real-time/real life based.Also the items avalilability would be increased and more categories will be added.|
|**Shipping**|Once the purchase has been made TradeHub cuts off with an order recorded to a spreadsheet| As a feature I would like to insert a "form" to implement shipping methods.|
|**Payments**|Currently, the user can buy as much as the user likes without any restrictions.|I would like to implement payment methods and budgets, so the user can make sure to don't go overbudget and choose how to pay(obviously at the moment this is a project so no payment methods will be added or any charge will be applied).|
|**User class/Recognition**|In this moment a returning user starts TradeHub like a first time user due to a simple "username" prompt.|I would like to implement credentials to recognize the user when coming back. This would allow to track user preferences and details(if we count the future features as well), making the user experience even better and TradeHub more trustworthy.|
|**Database Reset/Rewrite**|At the moment the worksheet is getting populated everytime someone makes a purchase, making the database overpopulated|Implementing from within the code , a function that regolates the amount of purchases , or replacing overtime dated purchases with new ones|
|**Security measure**| At the moment the only "security measure" that is implemented its the locked worksheets (categories only, purchase is open), making sure that TradeHub works properly.| I would like to implement security measures over confidential details and the data structure that is easily accessible|
- Overall the future features will be a great improvement for both sides (user/admin), making the user journey much easier and stright forward , and the admin more in control over the platform and analytics.|


### UI

- TradeHub uses **ASCII art with pyfiglet** and **colored** text with **colorama** enhancing the visual design. The colors are:
    - Mainly green for general text and **positive** feedbacks.
    - Promts are standard color detaching them from plain text.
    - **Negative** feedback for example from error handling are colored red giving the user an understanding of what is going on making it user friendly even for a first timer.

Overall the coloring gives **consistency** even in a simple application like TradeHub.

### UX

- As discussed before in the Features the User Experience is focused on **functionalities, navigation , feedbacks and interaction**
- The user can move around TradeHub wihtout losing the sense of position or getting lost in infinite loops. 
- The **feedbacks** are helping the user to move freely and **improve the experience**. 
- We can speak also about the **ratings** that the user can give at the end of the purchase, showing that TradeHub cares and wants to **improve** for the user **satisfaction**. 
- The purchase process also makes sure that the user gets a **confirmation** of what has been processed, receving a **detailed summary** of their purchase enhancing **transparency and identification**(unique order n.).
- By focusing on these **UX elements**, TradeHub builds trust with its users. Trust is critical in online marketplaces, where users need **assurance** that their transactions are **secure**, their feedback is **valued**, and their overall **experience is positive**.

### User Stories

- As new user
    - I want to **easily navigate** and **explore** TradeHub without feeling overwhelmed.
        -   TradeHub gives a simple "registration" process and makes it easy to navigate with **clear instructions** how to get through.
- As a shopper
    - I want to browse different categories and items, i want to know prices and see my basket to have everything **under control**.
        - Each category displays a range of different items related to the selected category. Every item its followed by a price.
        Giving the user the chance to review the basket removing or adding items to it. Resembling a seamless **shopping experience**.
### As developer

- As "admin" of TradeHub , I wanted to **manage** categories , **update** inventory and **view sales analytics** to ensure the platform operates smoothly and **improves overtime** in different aspects, giving a **great experience** to the user and chances to improve to the developer.
    - TradeHub is **built to record** user interaction over purchases and ratings. Enabling me to **retrieve datas** over user preferences(TradeHub perfomances) and where to **improve the platform** reviewing ratings.
#### Real user feedback

- During the TredeHub development, I was giving to people close to me the chance to try TradeHub, giving me different views and opinions. This helped also the implementation of some feature like the order n. and the ratings and some other small details like adding the chance to purchase directly from the basket.
### Data model

- TradeHub uses a **spread-sheet data model**, allowing flexibility and real-time updates.
#### Structure

- The **three worksheets** are organized in two columns, the first column contains an heading ("item", first row) followed by a **list of items**. The second column contains an heading ("price", first row) followed by the **related prices**.
- The purchases worksheet is empty to start. When a purchase is made through TradeHub it will be displayed in similar fashion as the previous ones.Starting from the first column, the first row will contain **"Name"** on the left hand side, following we will have the second column with the **unique order n.**
The second row has been left empty to give some spacing.
The third row starting from the first column will contain the items, the more items purchased the more rows we will have. Every item is followed in the second column and same row, by the respective price value.
Once the items are finished we will have a **"Total £"** followed on same row by the **sum of the prices** previously displayed.
Under the Total £, we will have **Rating** (note that this is an optional value.) The value related to rating is calculate in an **average of 5** numbers with a range from 0 to 5. If the cell on the right hand side of "Rating" is empty , it means that the user skipped the ratings at any moment.
> If the purchases worksheet will be too "populated" feel free to delete previous purchases. 

| Screenshot |Title| Explanation|
|---|---|---|
|[Clothes worksheet](/assets/img4rdm/clothes.png)![Clothes list](/assets/img4rdm/clothes.png)|Clothes category|In this worksheet named "clothes" we can find all the items related to this category|
|[Tech worksheet](/assets/img4rdm/techcategory.png)![Tech worksheet](/assets/img4rdm/techcategory.png)|Tech category|In this worksheet named "tech" we can find all the items related to this category|
|[Groceries worksheet](/assets/img4rdm/grocerycategory.png)![Groceries worksheet](/assets/img4rdm/grocerycategory.png)|Groceries category|In this worksheet named "groceries" we can find all the items related to this category|
|[Purchases worksheet](/assets/img4rdm/purchasesheet.png)![Purchases worksheet](/assets/img4rdm/purchasesheet.png)|Purchases|In this worksheet named "purchases" we have the processed purchases. It is recorded as two column expanding downwards depending on the amount of items purchased. As we can see in the screenshot at the top of the column we have the "username" and the order number. Following down we have the item on the left followed by the price on the right and so on for the other items. At the bottom of the items list we have the total price, and under the total price we can see the ratings. If the rating value is empty it mean that the user decided to skip the ratings. To note that if the user skips the ratings at any time ,the value will not be recorded.|

#### How the process works

The aim here was to have a simple but strong/powerful way to fetch and store data.  
I opted for the **A1 notation** with the **gspread** methods used in this kind of structures.
Having the first three categories filled in the worksheet makes it easy to target the cells needed in the program. 
Different way is used in the purchase process , where I created the 2 columns from within the code and uploaded them to the "purchases" worksheet.

| Screenshot |Title| Explanation|
|---|---|---|
|[Retrieve Titles](/assets/img4rdm/gspreadm1.png)![Retrieve Titles](/assets/img4rdm/gspreadm1.png)|Example 1|In this example we can see how the worksheets titles are retrieved or ignored using **gspread** library, in this case the tiles are used to print the category names.|
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
- Mozilla Firefox
- Opera
- Safari
- Mobile Devices(Android/IOS)
- Tablets(Android/IOS)
- Laptop(Windows/Mac)

To note that I tried testing from **IOS** devices , but as tutors said ,it is a known issue that the pack provided from Code Institute does't work properly on this kind of operative system.
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
- Another small fix that was done, was about the length of some lines of code/comments. Some of the lines reached 120 characters where the limit is much lower. Now all the file has been redacted to follow this standards with the help of PEP8 linter.

### Remaining Bugs or fixes

- Something that need to be fixed is between the code and the spreadsheet. Basically is a size problem where once the columns are finished the program doesn't find anymore space where to record the new purchases. I increased the size of the spreadsheet manually to solve the initial problem.
- Same issue would be for the order number. I choose to give the user a 5 digit "reference n." that goes from 0 to 99999. It would be a problem to reach (even if large) that amount. Giving the program no way to continue after all numbers available are used.


### Validation

- To validate the code I used PEP8 [CI Python Linter](https://pep8ci.herokuapp.com/)
![Validation](/assets/img4rdm/pythonLinter.png)

- To have a "second opinion is also used [Pythonium syntax checker](https://pythonium.net/linter)
![Second Validation](/assets/img4rdm/secondValidation.png)

### Deployment

- TradeHub is hosted in:
    - **Heroku**
    - **GitHub**
- Data side is currently in **Google Sheets**.
- TradeHub has been built on **Gitpod**.

#### How to deploy on Github

1. Go to **Github**
2. Access the **Repository**
3. Select **Settings**
4. On the left side you need to get into **Pages**
5. You will see **Build and deployment**.
6. Under the **Branch** select **main**
7. Click **save**
8. If correctly executed the page will indicate the succesful **deployment** and the link related.

#### Cloning
1. From repository on Github click the green button **Code** .
2. After clicking you will see **Clone**.
3. You can **download Zip** and extract files to run locally via browser.
4. Or cloning via **Git** with **HTTPS**.
5. To clone via Git, make sure you select the directory where you want to store your repository.
6. Use **git clone** followed by the HTTPS seen on previous steps.
7. Once you run the command you will see **example**: Cloning into **My-repo**...
8. To verify if succesful you can use in the terminal the command **ls**.
9. This will show you the list of folders and files in the directory.

#### Heroku deployment
1. Ensure that all your dependencies are listed in the requirements.txt file by running the command: **pip3 freeze > requirements.txt** in your Python **terminal**. This will add all your requirements to the **requirements.txt** file.
2. Visit the **Heroku** website, sign up by clicking the button in the top right corner, then **log in**.
3. Click on **New** in the top right corner and select **Create new app**.
4. Choose a unique name for your app, set your region to for example "Europe"(you can choose the region that you are in), and click **Create app**.
5. Go to the **Settings** tab, then click **Reveal Config Vars** under **Config Vars**.
6. Enter **CREDS** as the first **KEY**, and paste the entire contents of your **creds.json** file (including the curly braces) into the **VALUE** field, then click **Add**.
7. Enter **PORT** as the second **KEY**, set **8000** as the **VALUE**, and click **Add**.
8. Scroll down to the Buildpacks section, click **Add buildpack**, and select Python. Then add another buildpack and select **Node.js**. Ensure that Python is listed above Node.js.
9. Scroll back up and go to the **Deploy** tab.
Under **Deployment method**, select **GitHub**, search for your GitHub repository by name, and select the correct one.
10. Scroll down to **Automatic deploy**, choose the **main branch** so that any changes pushed to GitHub will **automatically update** the Heroku app.
11. Scroll down to **Manual deploy** and click **Deploy Branch**.
Once the deployment is complete, click on **View** to open a new tab and display your program.


#### Google API set up
1. Create a **Google account** and a **Google Sheet**, naming it preferably the same as your GitHub repository.
2. Visit **Google Cloud Platform**, click **Select a project**, then **New project**, and name it, matching your GitHub repository and Google Sheets name, then click **Create**.
3. Select your newly created project from the **Select project** menu.
4. On your project dashboard, go to **"API & Services" > "Library"**.
5. Enable the **Google Drive API** by searching for it and clicking **Enable**.
6. Click **Create credentials**, select **Google Drive API** for the API, **Application Data** for data access, and answer **No** to using it with Compute Engine, Kubernetes Engine, App Engine, or Cloud Functions. Click **Next** and then **Done**.
7. Enter a service account name, matching your Google Cloud project name if available, and click **Create**.
8. In **Grant this service account access to project**, select the role **"Basic" > "Editor"** and click **Continue**. Skip **Grant users access** and click **Done**.
9. Click on the newly created service account, go to the **Keys** tab, and click **"Add Key" > "Create New Key"**. Select **JSON** and click **Create** to download the .json file.
10. Return to **"API & Services" > "Library"**, search for **Google Sheets API**, and click **Enable**.

#### Linking API to Gitpod
1. Drag and drop the downloaded .json file into your **Gitpod workspace** and rename it to **creds.json**.
2. Open the **creds.json** file and copy the email address next to **client_email** (without quotes).
3. Open your **Google Sheets** file, click the **Share** button, and paste the copied email address.
4. Ensure **Editor** is selected, untick **Notify People**, and click **Share**.
> We need to make sure that **creds.json** is added to **.gitignore** because it contains private credentials.

### Technologies
- TradeHub was built using **Python** and libraries
- Packages
    - **Gspread**
    - **Colorama**
    - **Pyfiglet**
- For deployment was used **Heroku**.
- **Gitpod** as editor.
- **Google sheet** as database.
- **Github** is hosting the repository


### Credits

- [Miro.com](https://miro.com/app/dashboard/) was used to create the flowchart
- Template create by Code Institute for Deployment Terminal.