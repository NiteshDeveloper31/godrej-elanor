with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Make sure html and body NEVER scroll horizontally
old_html_body = r'''html {
  scroll-behavior: smooth;
  font-size: 16px;
  overflow-x: hidden;
  max-width: 100vw;
}

body {
  font-family: var(--gpl-font-sans);
  color: var(--gpl-text-body);
  background-color: #FFFFFF;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  overflow-x: hidden;
  max-width: 100vw;
  position: relative;
}'''

new_html_body = r'''html {
  scroll-behavior: smooth;
  font-size: 16px;
  overflow-x: hidden !important;
  width: 100%;
  max-width: 100%;
}

body {
  font-family: var(--gpl-font-sans);
  color: var(--gpl-text-body);
  background-color: #FFFFFF;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  overflow-x: hidden !important;
  width: 100%;
  max-width: 100%;
  position: relative;
}'''

css = css.replace(old_html_body, new_html_body)

# Fix hero-subnav-bar and subnav-inner-container
old_subnav_base = r'''.hero-subnav-bar {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  z-index: 10;
  background: rgba(0, 0, 0, 0.35);
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  transition: all 0.3s ease;
}'''

new_subnav_base = r'''.hero-subnav-bar {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  width: 100%;
  max-width: 100%;
  z-index: 10;
  background: rgba(0, 0, 0, 0.35);
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  transition: all 0.3s ease;
  overflow-x: auto;
  overflow-y: hidden;
}'''

css = css.replace(old_subnav_base, new_subnav_base)

# Make sure header-inner-container is strictly 100% and doesn't overflow
old_hdr_inner = r'''.header-inner-container {
  width: 100%;
  max-width: 1320px;
  margin: 0 auto;
  padding: 0 1.25rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
}'''

new_hdr_inner = r'''.header-inner-container {
  width: 100%;
  max-width: 1320px;
  margin: 0 auto;
  padding: 0 1.25rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-sizing: border-box;
}'''

css = css.replace(old_hdr_inner, new_hdr_inner)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied strict width and overflow controls to styles.css!")
