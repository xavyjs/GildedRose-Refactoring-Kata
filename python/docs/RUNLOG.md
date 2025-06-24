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

## 5. Adding Tests for straight forward cases
**1. Aged Brie** <br>
**2. Sulfuras** 

![Test for straight forward cases](img/06.png)

## 6. Adding Tests for backstage

**1. Increase in Quality w.r.t SellIn** <br>
**2. Quality +2 when days leq 10** <br>
**3. Quality +3 when days leq 5** <br>
**4. Quality drops to 0 post concert**

![Test for backstage](img/07.png)

## 7. Refactoring gilded_rose

**1. Seperating loops and iter instance** <br>
![Tests 7](img/08.png)

**2. Re-ordering setters for sell in and quality** <br>
![Tests 9](img/09.png)

**3. Replacing Item Strings by Constants to avoid frequent typos** <br>
![Test 10](img/10.png)

**4. Refactor nested item quality checks with functions** <br>
![Test 11](img/11.png)

**5. Increase readability of conditionals with inversion of condition** <br>
![Test 12](img/12.png)

**6. Simplify conditionals by collapsing logic** <br>
![Test 13](img/13.png)


