
EXECUTIVE SUMMARY 
• Subset of Stack Overflow public dataset resulting of annual survey had been analyzed from row data. 
• The report shows a very dynamic and changing market for techs used by developers:
• PostegreSQL seems to affirm more and more its dominance in database field.
• Python is replacing Javascript in popularity among developers. 
• Microsoft Azure and Amazon Web Services (AWS) share nearly the entire market for platforms. 
• Spring Boot and React are increasing in dominance in their web framework market. 
• A significant amount of developer hold a college degree. 
• The dataset is biased towards US, Germany and UK.


INTRODUCTION 

• Stack Overlflow conducts surveys among its users. These surveys allow the collection of structure data that can provide very useful insights into the current situation of the developer job, the tech stack currently used and the one that is projected to be used.
• The data is cleaning appropriately and processed to visualize the databases and programming languages currently used and that are projected to be used. •We make some assumption in this analysis: • The dataset is representative of the entire market of techs used and will be used worldwide 
• The projected value for next year is assumed to be the tech that respondents of the survey reported they wish to work with.

METHODOLOGY 
• The dataset is in the form of csv file that can be accessed online or downloaded. 
• The data wrangling – the process of cleaning, process and transforming the data for the purpose of data analysis- is done using Python programming language.  • Missing values are handled here either by removing entire rows, or replacing the values for a statistical index, such us mode for qualitative values, or median/average for quantitative values. • For the programming languages and database columns that are analyzed the data is processed into these steps: • For each value of these columns is split for each tech listed and placed into a new PandasSeries object . 
• The techs listed in the series are counted and bar plots are then created.


RESULTS: 

Datasets trends:
 -Findings: 
   • PostegreSQL is the database most used by respondents and the database they want to work with the most. . We can see an opposite trend in MySQL. SQLite has a larger number of participants that wish to work with than MySQL. Also, Redis seems to be on a growing trend. Overall PostegreSQL seems to become even more dominant than it currently is among respondents. 
   • MySQL is currently the second most used database and it's the number 4 respondents want to work with. 
   • More participants want to work with PostegreSQL and Redis than there are already working with

 -Implications:
   • PostegreSQL is projected to increase in usage further and reinforce its dominance among database use 
   • MySQL will be likely overtaken by Sqlite and Redis in the upcoming years. 
   • MySQL has the largest downward trend among top used databases while PostegreSQL and Redis have the largest upward trend

Programming langiages trends:
 - Findings: 
    • Javascript is currently the most used programming language, but will probably become number 3, according to these findings. 
    • Python will become number one language used, according to these findings 
    • There are more respondents that work with certain languages in the top 10 than the ones that want to work with them Implications 
 - Implications:
    • Python will be used more and more compared to JavaScript and HTML/CSS 
    • Nearly all languages in the Top 10, with the exception of Rust, seem to be in a downward trend overall. 
    • Javascript seems to be in a larger downward trend than other languages

DiSCUSSION AND CONCLUSION:
Some technologies rapidly increase in popularity, making the tech stack used by developers very dynamic and changing on a yearly basis. A few techs, especially PostegreSQL database, Microsoft Azure and AWS platforms seem to have a significant dominance in their respective market, that doesn't seem to be changing in the short term. A large amount of respondents are from either the US, UK or Germany, making the results possibly biased or skewed towards certain niche.
To encapsulate all in a few key points:
  •PostegreSQL seems to assert dominance among databases.
  •Microsoft Azure and AWS currently dominate and will probably keep dominating the platform tech. 
  •Programming languages usage instead seems to be more dynamic andcan change quickly 
  •Web framework techs seems to have a low concentration in current and future usage, 
  although the current and future short term most used ones are Spring Boot and React.
   

