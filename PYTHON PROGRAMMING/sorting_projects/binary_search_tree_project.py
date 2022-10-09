"""
BINARY SEARCH TREE    

Binary Search Tree is a node-based binary tree data structure which has the following properties:

• The left subtree of a node contains only nodes with keys lesser than the node’s key.
• The right subtree of a node contains only nodes with keys greater than the node’s key.
• The left and right subtree each must also be a binary search tree.

[7, 5, 1, 8, 3, 6, 0, 9, 4, 2]                     

(-1-) Write the Binary-Search-Tree stages of the above sequence.


1)                      7                  LEVEL 0 (ROOT)

---------------------------------------------------------------------------------------------------

2)                      7
                      /             
                    5                      LEVEL 1

---------------------------------------------------------------------------------------------------  

3)                      7                      
                      /                  
                    5       
                  /   
                1                          LEVEL 3

---------------------------------------------------------------------------------------------------  

4)                      7                      
                      /   \              
                    5       8              LEVEL 4
                  /   
                1     

---------------------------------------------------------------------------------------------------  

5)                      7                      
                      /   \              
                    5       8              
                  /   
                1 
                  \  
                    3                      LEVEL 5

---------------------------------------------------------------------------------------------------

6)                      7                      
                      /   \              
                    5       8              
                  /   \ 
                1       6                  LEVEL 6
                  \  
                    3  

---------------------------------------------------------------------------------------------------

7)                      7                      
                      /   \              
                    5       8              
                  /   \ 
                1       6                  
              /   \  
            0       3                      LEVEL 7

---------------------------------------------------------------------------------------------------

8)                      7                      
                      /   \              
                    5       8              
                  /   \       \ 
                1       6       9          LEVEL 8          
              /   \  
            0       3

---------------------------------------------------------------------------------------------------

9)                      7                       
                      /   \              
                    5       8              
                  /   \       \ 
                1       6       9                   
              /   \  
            0       3
                      \ 
                        4                  LEVEL 9  

---------------------------------------------------------------------------------------------------

10)                     7                       
                      /   \              
                    5       8              
                  /   \       \ 
                1       6       9                   
              /   \  
            0       3
                  /   \ 
                2       4                  LEVEL 10
"""