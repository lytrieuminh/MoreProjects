# Let's code a social media notifier that tells a user about the latest activity on their social media.

action = "reply"

if action == "like":
    print("Someone has liked your post")
elif action == "comment":
    print("Someone has commented on your post")
elif action == "reply":
    print("Someone has replied to your post")
else:
    print("There is an activity on your page")
