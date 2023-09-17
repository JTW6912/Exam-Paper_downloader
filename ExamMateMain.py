import re
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from lxml import etree
import requests




window = tk.Tk()
window.title('ExamMate Paper Downloader Made By Timmy')

Frame = tk.Frame(window)
Frame.grid()

def Search_Button_Clicked():
    Link = LinkEntry.get()

    if Link == '': #if empty
        tk.messagebox.showerror(title='error Message',message='Cant leave the link Entry blank')
    elif 'exam-mate.com/topicalpastpapers' not in Link:
        tk.messagebox.showerror(title='error Message', message='pls enter the valid link')
    else:
        url = Link
        header = {'Cookie':'_ga=GA1.2.120463541.1693557306; _gid=GA1.2.1243640465.1693557306; _gcl_au=1.1.1185577029.1693557307; _ga_EJZVNZHW6H=GS1.2.1693630751.3.1.1693630752.0.0.0; XSRF-TOKEN=eyJpdiI6IkZsS0VtNGVuSlJJcEVyam41UGJOd0E9PSIsInZhbHVlIjoiMEZKM28yV1M1eVRsQkhCZTArRWhuSkM3S0tiVkEzU1AzRDU5RU9sdTJhbDYrZzhIU212MG9FMi9qWnR4RnRmditnVTBKUFJGcStrQndicDZKSmVXbCtEY3dEZmJTazdvWWpRdFBEd0ZaOFI1TCttUGNkelg0OW5xOGNsMXZpTkwiLCJtYWMiOiJkMzQzOWY5ZDYwMzBhOTYzZGEwZmYxMzg4YTA4MzYwMDc0ODhkYzE1OWUyNWEzZDRlMmNjMjcyOTQyMzc0NjRiIiwidGFnIjoiIn0%3D; exam_mate_session=eyJpdiI6Ii8zZGRxbkh3UjhkRStlaVpmNEM4eVE9PSIsInZhbHVlIjoiV0duMTNIVFpTYTRZQXljdUk4ZGZoNzlaU3BrSERrSzlzTStCNTBwdDJUOW1EWklybkdKSWFyeTNEaWgwR1BzVHFUVWMvcGN6WXIrajRoeWpUakVkNG1UNTJQOWtsRy9pOUR3a1p5L3V0NmlqcTFwWHhrQ2dFbXdrQWx4T3FKOVQiLCJtYWMiOiJiMTIwZmM1ZThmNDY0YTRiMjc3MTlkZjEzMGNkZTZmNWMyNzlhZTZhZTc3ODljMjkzYWUyMDBjMDg3NDM2OTI3IiwidGFnIjoiIn0%3D'
                  ,'User-Agent':'ozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
        resp = requests.get(url=url,headers=header)
        tree = etree.HTML(resp.text)
        PaperInfoList = tree.xpath('//div[@class="question-list"]//ul[@class="list-group results-box"]/li')
        #/html/body/div[1]/div[5]/div[2]/div[2]/div[1]/div/div[2]/div[1]/ul/li[1]/span[1]
        for Paper_Info in PaperInfoList:
            title = Paper_Info.xpath('./span/text()')
            title = title[0].replace('\n','')
            PaperContent = Paper_Info.xpath('./@onclick')
            PaperContent=PaperContent[0]
            #解析 成列表
            Qregex = '{"question_images":(?P<QuestionList>.*?),"a'
            QuestionPaper_List = re.findall(Qregex,PaperContent)[0]
            QuestionPaper_List = QuestionPaper_List.replace('[','')
            QuestionPaper_List = QuestionPaper_List.replace('\"', '')
            QuestionPaper_List = QuestionPaper_List.replace(']', '')
            QuestionPaper_List = QuestionPaper_List.split(',')

            # print(QuestionPaper_List)

            Aregex = '"answer_images":(.*?),"'
            AnswerPaper_List = re.findall(Aregex, PaperContent)[0]
            AnswerPaper_List = AnswerPaper_List.replace('[', '')
            AnswerPaper_List = AnswerPaper_List.replace('\"', '')
            AnswerPaper_List = AnswerPaper_List.replace(']', '')
            AnswerPaper_List = AnswerPaper_List.split(',')


            print(title, AnswerPaper_List)


        # print(len(PaperInfoList))


#main Area F
MainAreaFrame = tk.LabelFrame(Frame,text='ExamMate Hack')
MainAreaFrame.grid(row=0,column=0,pady=10,padx = 10)

LinkLabel = tk.Label(MainAreaFrame,text='Link:')
LinkEntry = tk.Entry(MainAreaFrame,width=50)
LinkLabel.grid(row=0,column=0)
LinkEntry.grid(row=1,column=0,pady=5,padx=10)

LinkEntry.insert(0,'https://www.exam-mate.com/topicalpastpapers?cat=5&sub=47&page=2')

#searchoption Frame
Search_Option_Frame = tk.LabelFrame(Frame,text = 'Advance Option')
Search_Option_Frame.grid(row=1,sticky='news',pady=10,padx=10)

#page limit
PageLimit_Label = tk.Label(Search_Option_Frame,text='PageLimit:')
PageLimit_Label.grid(row=0,column=0)

PageLimit_SpinBox = ttk.Spinbox(Search_Option_Frame,from_=1, to=1000,width=3)
PageLimit_SpinBox.grid(row=0,column=1)

PageLimit_SpinBox.set(3)

#slow mode
Slow_Mode_var = tk.StringVar()
Slow_Mode_Label = tk.Label(Search_Option_Frame,text='Slow Mode')

Slow_Mode_CheckButton = tk.Checkbutton(Search_Option_Frame,variable=Slow_Mode_var,onvalue='on',offvalue='off')
Slow_Mode_Label.grid(row=1,column=0)
Slow_Mode_CheckButton.grid(row=1,column=1)

Slow_Mode_var.set('on')

#with premiere acc




Search_Button = tk.Button(Frame,text='Download',command=Search_Button_Clicked)
Search_Button.grid(row=2,column=0,pady=10)
#Button














window.mainloop()