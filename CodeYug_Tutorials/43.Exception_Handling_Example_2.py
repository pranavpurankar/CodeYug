'''
Find the error and fix it 

def total_likes():
    reviews = [{'Image':3, 'Like':20, 'Comment':10},
                {'Like':15, 'Comment':8, 'Share':10},
                {'Image':7, 'Comment':16, 'Share':37},
                {'Image':6, 'Like':10, 'Comment':9}
                ]
    total = 0
    for review in reviews:
        total += reviews['Like']
        pass
    return total

print(total_likes())
'''


def total_likes():
    reviews = [{'Image': 3, 'Like': 20, 'Comment': 10},
               {'Like': 15, 'Comment': 8, 'Share': 10},
               {'Image': 7, 'Comment': 16, 'Share': 37},
               {'Image': 6, 'Like': 10, 'Comment': 9}]

    total = 0
    for review in reviews:
        try:
            total += reviews['Like']
            pass
        except Exception as var:
            print(var)
    return total


print(total_likes())
