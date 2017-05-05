from gi.repository import Notify

Notify.init("This is a simple notification")

summary = "Meeting !!!"
body = "Meet Mr. XYZ at 10:00 am today"

notification = Notify.Notification.new(summary, body)

notification.show()
