from appJar import gui 
from paste_manager import PasteManager


app=gui("SCROLLABLE DEMO", "150x150")

app.startScrollPane("PANE")

pm = PasteManager()
rows = pm.get_value()
row = 0
for k, item in rows.iteritems():
    app.addLabel(str(k), item, row=row, column=1)
    row += 1
app.addMessage("1", "1", 11, 11)
app.stopScrollPane()
app.go()