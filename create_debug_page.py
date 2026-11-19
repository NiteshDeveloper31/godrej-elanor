# Let's inspect by creating a test html file with an inline script that writes rects to localStorage or document.title!
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

debug_script = """
<script>
window.addEventListener('load', () => {
  const gpl = document.querySelector('.header-logo-gpl')?.getBoundingClientRect();
  const grp = document.querySelector('.header-right-group')?.getBoundingClientRect();
  const search = document.querySelector('.hdr-icon-circle')?.getBoundingClientRect();
  const menu = document.getElementById('navToggleBtn')?.getBoundingClientRect();
  const scriptLogo = document.querySelector('.header-logo-script')?.getBoundingClientRect();
  const container = document.querySelector('.header-inner-container')?.getBoundingClientRect();
  
  const report = {
    windowInnerWidth: window.innerWidth,
    container: container ? {left: container.left, right: container.right, width: container.width} : null,
    gpl: gpl ? {left: gpl.left, right: gpl.right, width: gpl.width} : null,
    grp: grp ? {left: grp.left, right: grp.right, width: grp.width} : null,
    search: search ? {left: search.left, right: search.right, width: search.width} : null,
    menu: menu ? {left: menu.left, right: menu.right, width: menu.width} : null,
    scriptLogo: scriptLogo ? {left: scriptLogo.left, right: scriptLogo.right, width: scriptLogo.width} : null,
  };
  document.title = 'DEBUG:' + JSON.stringify(report);
});
</script>
"""

html_with_debug = html.replace('</head>', debug_script + '</head>')
with open('debug.html', 'w', encoding='utf-8') as f:
    f.write(html_with_debug)

print("Created debug.html")
