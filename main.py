import tkinter as tk
from tkinter import ttk

window = tk.Tk()
Frame = tk.Frame(master=window)
Frame.pack()

#Course Option Choose Frame
CourseOptionFrame = tk.LabelFrame(Frame,text='Course Option')
CourseOptionFrame.grid(padx=10,sticky='news')

CurriculumOptionLabel = tk.Label(CourseOptionFrame,text='curriculum:')
#un
CurriculumOptionComboBox = ttk.Combobox(CourseOptionFrame,values=[''],width=15)
CurriculumOptionLabel.grid(row=0,column=0)
CurriculumOptionComboBox.grid(row=0,column = 1)

#Subject

SubjectOptionLabel = tk.Label(CourseOptionFrame,text='Subject:')
#un
SubjectOptionComboBox = ttk.Combobox(CourseOptionFrame,values=[''],width=15)
SubjectOptionLabel.grid(row=0,column=2)
SubjectOptionComboBox.grid(row=0,column = 3)

for widget in CourseOptionFrame.winfo_children():
    widget.grid_configure(pady=5,padx=5)


#second Frame
Second_CourseFrame = tk.LabelFrame(master=Frame)
Second_CourseFrame.grid(row=1,column=0,sticky='news',pady=10,padx=10)

#topic
TopicOptionLabel = tk.Label(Second_CourseFrame,text='Topic:')
#un
TopicOptionComboBox = ttk.Combobox(Second_CourseFrame,values=[''],width=10)
TopicOptionLabel.grid(row=0,column=0)
TopicOptionComboBox.grid(row=0,column = 1)

#paper
paperOptionLabel = tk.Label(Second_CourseFrame,text='paper:')
#un
paperOptionComboBox = ttk.Combobox(Second_CourseFrame,values=[''],width=10)
paperOptionLabel.grid(row=0,column=2)
paperOptionComboBox.grid(row=0,column = 3)

#Years
YearsOptionLabel = tk.Label(Second_CourseFrame,text='Years:')
#un
YearsOptionComboBox = ttk.Combobox(Second_CourseFrame,values=[''],width=10)
YearsOptionLabel.grid(row=0,column=4)
YearsOptionComboBox.grid(row=0,column = 5)

#Season
SeasonOptionLabel = tk.Label(Second_CourseFrame,text='Season:')
#un
SeasonOptionComboBox = ttk.Combobox(Second_CourseFrame,values=[''],width=10)
SeasonOptionLabel.grid(row=1,column=0)
SeasonOptionComboBox.grid(row=1,column = 1)

#Zone
ZoneOptionLabel = tk.Label(Second_CourseFrame,text='Zone:')
#un
ZoneOptionComboBox = ttk.Combobox(Second_CourseFrame,values=[''],width=10)
ZoneOptionLabel.grid(row=1,column=2)
ZoneOptionComboBox.grid(row=1,column = 3)


ButtonFrame = tk.LabelFrame(Frame)
ButtonFrame.grid(row=2,sticky='news',pady=10,padx=10)
# SearchButton
SearchButton = tk.Button(ButtonFrame,text='Search',width=10)
SearchButton.grid()


window.mainloop()