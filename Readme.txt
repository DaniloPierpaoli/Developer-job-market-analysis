
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

Datasets:
 -Findings: 
   • PostegreSQL is the database most used by respondents and the database they want to work with the most. . We can see an opposite trend in MySQL. SQLite has a larger number of participants that wish to work with than MySQL. Also, Redis seems to be on a growing trend. Overall PostegreSQL seems to become even more dominant than it currently is among respondents. 
   • MySQL is currently the second most used database and it's the number 4 respondents want to work with. 
   • More participants want to work with PostegreSQL and Redis than there are already working with
