from gi.repository import Notify

Notify.init("Test App")

# Define a callback function
def my_callback_func():
    pass

notification = Notify.Notification.new("Hi!")
# The notification will have a button that says
# "Reply to Message". my_callback_func is something
# We will have to define
notification.add_action(
    "action_click",
    "Reply to Message",
    my_callback_func,
    None # Arguments
)

# Clear all actions with clear_actions()
