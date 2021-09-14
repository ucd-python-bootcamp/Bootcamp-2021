## Day 2 Homework

Here is a csv file that contains all of the countires that medalled in the 2018 Winter Olympic games, their latitudes and longitudes, medals won, GDP (2018), and population (2018). This time, we are going to plot the countries that medalled and add more information to the plot.
[Day2CountryInfo2018.csv](https://ucd-python-bootcamp.github.io/Bootcamp-2021/HW_files/Day2CountryInfo2018.csv) 

### Initial Instructions:
  1. Download the csv file from the link above. 
  2. Open a new [Google Colab notebook](https://colab.research.google.com/) and click on "New Notebook" in the bottom right corner. (You may be able to modify your script from the Day 1 Homework instead)
  3. Click the file icon on the left toolbar, then click on the upload icon (the button on the left).
  4. Choose the new .csv file to upload in order to import the data.
  5. Here's the actual homework!
  
### Assignment
  - Open the csv file and examine what's in it. What variable types are in here? Strings, floats, or integers? 
  - In your Colab notebook, write a script that imports the data from the file to make a scatter plot.
  - As you parse the data, for each country you'll need to tally up the total medals. You will also need to calculate GDP per 5000 capita (GPD per 5000 people).
    - What techniques that we have reviewed can we do to accomplish these?
  - This time when you plot the data, color the countries according to number of medals won, and change the size of each point based on GPD per capita.
    - See the [plt.scatter documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html) to try to figure out how to implement this.
  - Add the equator to the plot as well.
  - Congrats! You are all done.
  - The plot will have fewer points this time without the countires that did not medal, but contain more information about those countries. If you want a challenge, the advanced homework will add more complexity and the other countries!
  - in Day 3 we will delve into using more libraries and do more data analysis.
  
## Answer
