import tkinter as tk
from tkinter import messagebox
from plyer import notification
import threading

class DesktopNotifierApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Desktop Notifier")
        self.root.geometry("750x500")
        
        self.title_label = tk.Label(root, text="Notification Title:")
        self.title_label.pack()
        
        self.title_entry = tk.Entry(root)
        self.title_entry.pack()
        
        self.message_label = tk.Label(root, text="Notification Message:")
        self.message_label.pack()
        
        self.message_entry = tk.Entry(root)
        self.message_entry.pack()
        
        self.time_label = tk.Label(root, text="Time delay (seconds):")
        self.time_label.pack()
        
        self.time_entry = tk.Entry(root)
        self.time_entry.pack()
        
        self.notify_button = tk.Button(root, text="Notify", command=self.schedule_notification)
        self.notify_button.pack()
        
    def show_notification(self, title, message):
        notification.notify(
            title=title,
            message=message,
            app_icon=None,
            timeout=10,
            toast=False
        )
        
    def schedule_notification(self):
        title = self.title_entry.get()
        message = self.message_entry.get()
        try:
            delay = int(self.time_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid time delay. Please enter a valid number.")
            return
        
        if delay <= 0:
            messagebox.showerror("Error", "Time delay must be a positive number.")
            return
        
        self.root.withdraw()  # Hide the GUI
        
        def delayed_notification():
            import time
            time.sleep(delay)
            self.show_notification(title, message)
            self.root.deiconify()  # Show the GUI again
        
        threading.Thread(target=delayed_notification).start()

if __name__ == "__main__":
    root = tk.Tk()
    app = DesktopNotifierApp(root)
    
    # Original notification script
    title = 'Hello Dude, Please take a break 😄 !'
    message = 'Thank you for reading! Take care 😄!'
    notification.notify(
        title=title,
        message=message,
        app_icon=None,
        timeout=10,
        toast=False
    )
    
    root.mainloop()
