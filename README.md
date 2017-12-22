# workJapanCodingAssignment

Assumptions:

Let mXn be the size of given matrix.

Algorithm:
Read the matrix from the file 'matrix.txt'.
For each and every element of matrix Four distinct ways can be drawn.
Lets consider for position x,y
Horizontal : right wards 
Vertical : downwards
RightDiagonal : diagonally right direction
LeftDiagonal : diagonally left direction 

Here we have to consider 4 directions instead of 8 because of remaining 4 ways have counted for some other points.

For each and every element 
	keep track on values of 4 directions
	Checking 4 consecutive points can be considered (around corner points consists of 2,3 elements but not 4)
	notedown the direction and the position

Finally it prints the maximum value along with the position and the direction of elements

For given matrix maximum value is 70600674 and the elements are 89,94,97,87

Time Complexity :
O(m*n)

Space Complexity :
O(m*n)
