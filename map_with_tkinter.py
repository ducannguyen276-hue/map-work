import tkinter
import tkintermapview


# create tkinter window
root_tk = tkinter.Tk()
root_tk.geometry(f"{800}x{600}")
root_tk.title("map_view_example.py")


# create map widget
map_widget = tkintermapview.TkinterMapView(root_tk, width=800, height=600, corner_radius=0)
map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# set current widget position and zoom
map_widget.set_position(43.4643, -80.5204)
map_widget.set_zoom(13)

def add_marker_event(coords):
    print("Add marker:", coords)
    new_marker = map_widget.set_marker(coords[0], coords[1], text="new marker")


map_widget.add_right_click_menu_command(label="Add Marker",
    command=add_marker_event,
    pass_coords=True)

map_widget.mainloop()