### 110. 平衡二叉树

        110. Balanced Binary Tree

给定一个二叉树，判断它是否是高度平衡的二叉树。

Given a binary tree, determine if it is height-balanced.

本题中，一棵高度平衡二叉树定义为：

For this problem, a height-balanced binary tree is defined as:

        一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

        a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

示例 1:

给定二叉树 `[3,9,20,null,null,15,7]`:

Given the following tree `[3,9,20,null,null,15,7]`:

```
    3
   / \
  9  20
    /  \
   15   7
```

Return true.

Example 2:

Given the following tree `[1,2,2,3,3,null,null,4,4]`:

```
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
 ```

 Return false.