# Documents Test Driven refactoring of the kata


## 1. Run default test
   
![Default test Fails](img/01.png)

**Fix: Correct method name 'fixme' to 'foo'**

**1. Check Item Name is constant always**

![Default test pass](img/02.png)

## 2. Add test cases for base requirements
**2. Check Item SellIn** <br>
**3. Check Item Quality** 

![Tests for base Req](img/03.png)

## 3. Add test cases for Finer Constraints
**4. Check Item Quality is never Negative** <br>
**5. Check Item Quality is never more than 50** <br>
**6. Check Item Quality degrade after SellIn**

![Tests for Finer Constraints](img/04.png)

## 4. Major refactor of glided_rose and test_glided_rose
**1.Refactor GlidedRose Class to python function as the Class only has behavior and data is not native(instantied by a different class i.e. Item)** <br>
**2. Move Item class to a seperate .py file for easier maintenance** <br>
**3. Adding Type Hints for better readability on 1 and 2** <br>
**4. Refactor test_glided_rose to adapt to changes from 1 to 3**

![Tests after refactoring ](img/05.png)

