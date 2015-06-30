#!/usr/bin/python

import Tkinter as tk
import urllib
import json

class Application:
  def __init__(self,master):
    frame = tk.Frame(master, width=500, height=500, bd=2)
    frame.pack()
    
    self.textvariable = tk.StringVar()
    
    self.text = tk.Entry(frame, textvariable=self.textvariable, bg='white', width=30)
    self.textvariable.set('Enter the name of the article')
    self.text.pack(side='left')
    
    self.button = tk.Button(frame, text='Search', command=self.search)
    self.button.pack(side='left')
    
    self.textarea = tk.Text(frame, width=500, height=100, bg='white', state='disabled')
    self.textarea.pack(side='left')
    
  def search(self):
    search_result = self.textvariable.get()
    conv_quote = urllib.quote(search_result.encode('utf-8'))
    init_url = 'https://bn.wikipedia.org/w/api.php?action=query&prop=langlinks&format=json&lllang=en&'
    title_url = 'titles='+conv_quote
    complete_url = init_url+title_url
    read_data = urllib.urlopen(complete_url).read()
    json_data = json.loads(read_data)
    title_conv = json_data['query']['pages']['2730']['langlinks'][0]['*']
    self.textarea.config(state='normal')
    self.textarea.insert(1.0,title_conv)
    self.textarea.config(state='disabled')

root = tk.Tk()    
app = Application(root)
root.title("GeoPort")
root.mainloop()