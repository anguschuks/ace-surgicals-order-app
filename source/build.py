import os
H=os.path.dirname(os.path.abspath(__file__))
import json,base64,re
s=open(os.path.join(H,'template.html')).read()
s=s.replace('<symbol id="i-search"','<symbol id="i-image" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="10" r="2"/><path d="M21 17l-5-5-9 8"/></symbol>\n<symbol id="i-search"',1)

d=json.load(open(os.path.join(H,'products.json')))
CATS=["Ward Equipment","General Medical Equipment","Maternity & Gynecology","Surgical & Theatre","Surgical Instrument","Radiology & Imaging","Laboratory & Diagnostics","Ophthalmology","Dental & ENT","Apparel & Linens","Consumables & Supplies","Physiotherapy","Models & Charts","Laboratory Glassware","Reagents and Chemicals"]
data=[[i['id'],CATS.index(i['c']),i['n'],i['d'],i['p']] for i in d]
logo='data:image/webp;base64,'+base64.b64encode(open(os.path.join(H,'logo.webp'),'rb').read()).decode()
s=s.replace('__DATA__',json.dumps(data,ensure_ascii=True,separators=(',',':'))).replace('__LOGO__',logo)
# make the whole file pure ASCII so no device can mis-read the encoding
def js_esc(t): return ''.join(c if ord(c)<128 else ''.join('\\u%04x'%u for u in __import__('struct').unpack('<%dH'%(len(c.encode('utf-16-le'))//2),c.encode('utf-16-le'))) for c in t)
def html_esc(t): return ''.join(c if ord(c)<128 else '&#x%x;'%ord(c) for c in t)
out=[];pos=0
for m in re.finditer(r'(<script>)(.*?)(</script>)|(<style>)(.*?)(</style>)',s,re.S):
    out.append(html_esc(s[pos:m.start()]))
    if m.group(1): out.append('<script>'+js_esc(m.group(2))+'</script>')
    else:
        css=m.group(5); assert all(ord(c)<128 for c in re.sub(r'/\*.*?\*/','',css,flags=re.S)), 'non-ascii css'
        out.append('<style>'+re.sub(r'[^\x00-\x7f]','-',css)+'</style>')
    pos=m.end()
out.append(html_esc(s[pos:]))
page=''.join(out)
assert all(ord(c)<128 for c in page)

head='<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
i=page.index('<svg width="0"')
site=head+page[:i]+'<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n</head>\n<body>\n'+page[i:]+'\n</body>\n</html>\n'
open(os.path.join(H,'..','index.html'),'w',encoding='ascii').write(site)
