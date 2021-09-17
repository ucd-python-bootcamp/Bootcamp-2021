## Day 3 Homework (Advanced)

Here is a csv file that contains all of the countires that medalled in the 2018 Winter Olympic games, their latitudes and longitudes, medals won, GDP (2014), and population (2014). Now we are going to create a multivariable fit and create a model 
[Day3CountryInfo2018_ADV.csv](https://ucd-python-bootcamp.github.io/Bootcamp-2021/HW_files/Day3CountryInfo2018_ADV.csv) 

### Initial Instructions:
  1. Download the csv file from the link above. 
  2. Open your Day 2 HW Colab notebook with the advanced solution (or the solutiion posted from Day 2 (ADV) if you were unable to complete it). Change the code to intake the new file.
  3. Click the file icon on the left toolbar, then click on the upload icon (the button on the left).
  4. Choose the new .csv file to upload in order to import the data.
  5. Here's the actual homework!
  
### Assignment
  - This part of the project is only meant to be completed once the [base homework for Day 3](https://ucd-python-bootcamp.github.io/Bootcamp-2021/HW3) has been completed. If you have not done so yet, go back and complete this. 
  - This assignment is not actually designed for students to finish in-person. This is an extra challenge for those that want to deepen their skills and understanding.
  - Your solution for Day 2 (ADV) should already be able to parse all of the data from the file. We will only be working with the data from the countries that medalled today.
  - In base homework, we looked at each variable independently, but now we want to fit a multivariable regression in the form of:
  ```
  medals = A*x + B*y + C*z + D
  ```
  - We will the `LinearRegression` class from `sklearn.linear_model`. To import only the desired class and not the entire library, use the following command:
  ```
  from sklearn.linear_model import LinearRegression
  ```
   - Here is the [documentation for LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
   - This is something called a class. It's a bit different from the functions we have used so far (see the resources on classes on the homepage). Basically it's a whole package of functions "wrapped-up" together.
   - To create an instance of the class, start with the following line:
   ```
   model = LinearRegression()
   ```
   - Now we can always call back to this instance with the `model` variable. This is called creating an object.
   - The documentation may be confusing, but in order to fit the data, you need to input the variables (GDP, populations and latitudes) and the output values (medal totals) into the function `model.fit()`.
   ```
   model.fit(X, medals)
   ``` 
   - However, the variables (X) must be input as an Nx3 array, where N is number of data points. Right now, we have the variables in three separate lists. See if you can figure out (Google is your friend!) how to transform this data into an Nx3 array.
      - The medal list is 1-dimensional so it can remain a list.
      
   - Once that bit is done your fit is complete! Everything has been calculated. To access the results, the following lines will retrieve the values we are want from the `model` object:
   ```
   R_squared = model.score(X, y)
   coefficients = model.coef_
   y-intercept = model.intercept_    
   ```
   - How does the R squared look compared to the single variable models?
   -------------------------------------------------
Finally, now that we have the coefficients and intercept, let's see if we can try to predict how many medals countries won at the 2014 Winter Olympics.
    
   - Downlaod the [Day3CountryInfo2014_ADV.csv](https://ucd-python-bootcamp.github.io/Bootcamp-2021/HW_files/Day3CountryInfo2014_ADV.csv).
   - To parse the data from this file there are two ways: the `with open` procedure we have done before or with a library called `pandas`. Overall pandas is faster and easier to use once learned but may be harder for new students. If you would like to see an example of how to use `pandas` read this [documentation](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) and take a peek at the answer key below.
   - Once you've parsed the data, calculate medal total and GDP per capita for the new data.
   - You can attempt this by either writing your own function manually, plugging in the coefficients and data for each country, or by using the `model.predict()` function.
     - `model.predict()` similar to `model.fit()` will take in an Nx3 array (X in example below) of variables and compute the medal totals. You'll need to get the 2014 data into the correct dimensions again.
     ```
     predictions = model.predict(X)
     ```
     - If you use pandas there is a different way to call the data into `model.predict()` see if you can figure it out yourself (with the help of the internet) or take a look at the answer key.
     - Now print out the predictions along with the actual medal totals and see how well the model works! (Russia was the host country in 2014 so their number might look quite skewed).
    
     - Congrats you have finished the most challenging part of this tutorial! Hopefully you have better understanding of libraries, classes, and how to teach yourself.
    
  
[.ipynb file](https://ucd-python-bootcamp.github.io/Bootcamp-2021/HW_solutions/HWDay3_ADV.ipynb)

[.py file](https://ucd-python-bootcamp.github.io/Bootcamp-2021/HW_solutions/HWDay3_ADV.py)
