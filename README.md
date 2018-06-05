# Decision-Tree-Attribute-Selection-from-scratch

This code is being done as the assignment of CS 412- Intro to Data Mining (Spring 2018), University of Illinois at Urbana Champaign.

Rules for this assignment are mentioned below.

Given a training dataset with several categorical attributes and a target label, you have to identify the best attribute for splitting the dataset.

You have to choose the best attribute based on their information gain, gain ratio value and gini index.

For this problem, assume that gini index can be defined over a multi-valued attribute having  distinct attribute-values as,


Input Format

First line of the input contains the number of lines (1+ number of training instances). Second line contains the name of the attributes and the target label (last) comma separated. The following lines are training instances which are comma-separated: the first categorical attribute value, second categorical attribute, and so on and finally the target label value.

Example input,

6

income,age,buycomputer

high,mid,Yes

high,mid,No

high,young,Yes

low,young,Yes

low,old,Yes

Constraints

None

Output Format

The output will be the best attribute based on information gain followed by the best attribute based on gain ratio and gini index on separate lines.

Example output of the given input,

age

age

age

Sample Input 0

15
age,income,student,creditrating,buyscomputer?
l30,high,no,fair,no
l30,high,no,excellent,no
31to40,high,no,fair,yes
g40,medium,no,fair,yes
g40,low,yes,fair,yes
g40,low,yes,excellent,no
31to40,low,yes,excellent,yes
l30,medium,no,fair,no
l30,low,yes,fair,yes
g40,medium,yes,fair,yes
l30,medium,yes,excellent,yes
31to40,medium,no,excellent,yes
31to40,high,yes,fair,yes
g40,medium,no,excellent,no
Sample Output 0

age
age
age
 

