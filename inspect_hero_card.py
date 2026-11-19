with open('godrej_godrej-elanor.html', encoding='utf-8') as f:
    html = f.read()

pos = html.find('property-details-hero-section')
print(html[pos+1000:pos+4500])
