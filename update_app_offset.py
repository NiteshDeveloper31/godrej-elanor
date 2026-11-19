with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

import re

# Update smooth scroll offset
old_offset = r'''const headerHeight = 64 + (subNav ? subNav.offsetHeight : 48);'''
new_offset = r'''const headerHeight = 114;'''

js = js.replace(old_offset, new_offset)

# In initSubNavScroll, we no longer need to toggle .sticky since it's already cleanly fixed in CSS
old_scroll_sticky = r'''  // Toggle sticky class when scrolled past the white header
  window.addEventListener('scroll', () => {
    if (subNav) {
      if (window.scrollY > 50) {
        subNav.classList.add('sticky');
      } else {
        subNav.classList.remove('sticky');
      }
    }
  }, { passive: true });'''

new_scroll_sticky = r'''  // SubNav is fixed at top: 64px right under header'''

js = js.replace(old_scroll_sticky, new_scroll_sticky)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated app.js offset successfully!")
