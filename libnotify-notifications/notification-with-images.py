#This time import the GdkPixbuf module
from gi.repository import Notify, GdkPixbuf

Notify.init("Test App")
notification = Notify.Notification.new("Alert!")

# Use GdkPixbuf to create the proper image type
image = GdkPixbuf.Pixbuf.new_from_file("logo-new.png")

# Use the GdkPixbuf image
notification.set_icon_from_pixbuf(image)
notification.set_image_from_pixbuf(image)

notification.show()
