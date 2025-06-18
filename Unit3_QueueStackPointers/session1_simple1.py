'''
Problem 1: Post Format Validator
You are managing a social media platform and need to ensure that posts are properly formatted. 

Each post must have balanced and correctly nested tags, such as () for mentions, [] for hashtags, 
and {} for links. You are given a string representing a post's content, 
and your task is to determine if the tags in the post are correctly formatted.

A post is considered valid if:

Every opening tag has a corresponding closing tag of the same type.
Tags are closed in the correct order.

Example Output:
True
True
False
'''
def is_valid_post_format(posts):
    pass

'''
Problem 2: Reverse User Comments Queue
On your platform, comments on posts are displayed in the order they are received. 
However, for a special feature, you need to reverse the order of comments before displaying them. 

Given a queue of comments represented as a list of strings, reverse the order using a stack.


Example Output:
['Thanks for sharing.', 'Love it!', 'Great post!']
['Well written.', 'Interesting read.', 'First!']
'''
def reverse_comments_queue(comments):
    # initalize stack
    stack = []
  
  # push everything to stack using for loop
    for each in comments:
        stack.append(each)
    
    new_comment = []
    
    while len(stack) != 0:
        new_comment.append(stack.pop())

    return new_comment

print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))
print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))

'''
Problem 4: Engagement Boost
You track your daily engagement rates as a list of integers, sorted in non-decreasing order. 
To analyze the impact of certain strategies, you decide to square each engagement rate 
and then sort the results in non-decreasing order.

Given an integer array engagements sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.

Your Task:

Read through the existing solution and add comments so that everyone in your pod understands how it works.
Modify the solution below to use the two-pointer technique.


Example Usage:

Example Output:

[0, 1, 9, 16, 100]
[4, 9, 9, 49, 121]
'''
def engagement_boost(engagements):
    squared_engagements = []
    
    # initialize two pointers
    left = 0
    right = len(engagements) -1
    
    while left <= right:
        if left == right:
            left_squared = engagements[left] * engagements[left]
            squared_engagements.append(left_squared)
        else: 
            left_squared = engagements[left] * engagements[left]
            right_squared = engagements[right] * engagements[right]
            squared_engagements.append(left_squared)
            squared_engagements.append(right_squared)

        left += 1
        right -= 1
    
    squared_engagements.sort(reverse=True)
    
    return squared_engagements


print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))