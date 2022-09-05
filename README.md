# wines_ETL

## Overview:
The goal of this weekend project was to extract, transform and load information about Spanish wines. To that end I will be using the knowledge and tools I have to my disposal at the present moment.

## The Project:
### First source of data: Kaggle csv

On this project I will use three different sources of data being this one the first. The database contained 7500 rows and the following columns:

1.	winery: Winery name
2.	wine: Name of the wine
3.	year: Year in which the grapes were harvested
4.	rating: Average rating given to the wine by the users [from 1-5]
5.	num_reviews: Number of users that reviewed the wine
6.	country: Country of origin [Spain]
7.	region: Region of the wine
8.	price: Price in euros [€]
9.	type: Wine variety
10.	body: Body score, defined as the richness and weight of the wine in your mouth [from 1-5]
11.	acidity: Acidity score, defined as wine's “pucker” or tartness; it's what makes a wine refreshing and your tongue salivate and want another sip [from 1-5]

After I removed the duplicates, which were many, I was left with only 2048 different wines. Credits on the original database go to:

fedesoriano. (April 2022). Spanish Wine Quality Dataset. Retrieved [Date Retrieved] from https://www.kaggle.com/datasets/fedesoriano/spanish-wine-quality-dataset

### Second source of data: web scraping vivino.com

With selenium I scraped this popular wine website. I used a link that showed me Spanish wines with a rating over 3.6 so that most data was new since the kaggle database only included wines from 4.2 till 5. In the Vivino.py file you can find the code I used to extract all the individual links to these wines. After 1200 wines the website didnt let me go further. This is something I would have tried to solve if I had more time.

Now that I have the list of links (linksv1.txt) I scraped each link for information to expand my database. I vivino_data.py you can find the code. Most variables present in the kaggle database were here as well except the data on flavours. I had limited time so I had to make due wit that. Scraping with 6 open tabs at the same time took more than 2 hours. I removed a few wines that had "year" over 2022 or under 1900. I also had to fix some data types and names to join this table with the previous one of kaggle. My new database had 3241 rows.

### Third source of data: web scraping decantalo.com

To end my information gatherinf phase I scraped 40 more wines which had the prestigious parker score. The code can be found in the decantalo_parker_ratings.py file. Some cleaning of the data had to be made specially for long names and wines with no year. One wine had incorrect information whixh was sorted out manually with a google search. The information on this website wasnt as vast as in the previous one so a lot of null values were introduced.

### Cleaning

All the cleaning takes place in the databases_cleaning.py file. The column "country" was dropped since all wines are from Spain and for the second adn third source of data columns were added to ressemble the kaggle databse and join all three in a single table. You can find that table in the data folder under the name final_data.csv. Most wines added on the third step were not present in the combined table but three of them had to be updated manually.

### Loading

Since all the information is contained in one table I decided to upload it to SQL. The creation query can be found in the folder of the same name.

## Conclusions

Some insights on the data can be found in some_conclusions.py




