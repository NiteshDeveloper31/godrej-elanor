with open('godrej_godrej-elanor.html', encoding='utf-8') as f:
    html = f.read()

pos = html.find('Property Banner Image')
end_fig = html.find('</figure>', pos)
print("After figure:")
print(html[end_fig:end_fig+2000])
