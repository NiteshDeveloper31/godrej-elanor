with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add overflow-x: hidden to html and body
old_body = r'''html {
  scroll-behavior: smooth;
  font-size: 16px;
}

body {
  font-family: var(--gpl-font-sans);
  color: var(--gpl-text-body);
  background-color: #FFFFFF;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}'''

new_body = r'''html {
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

css = css.replace(old_body, new_body)

# Fix subnav overflow on mobile
old_subnav_media = r'''@media (max-width: 768px) {
  .subnav-links-list {
    gap: 1.15rem;
    overflow-x: auto;
    white-space: nowrap;
    -webkit-overflow-scrolling: touch;
  }
}'''

new_subnav_media = r'''@media (max-width: 768px) {
  .hero-subnav-bar {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
  }
  .subnav-inner-container {
    width: max-content;
    min-width: 100%;
    justify-content: flex-start;
    gap: 1.25rem;
    padding: 0 0.85rem;
  }
  .subnav-back-link {
    flex-shrink: 0;
  }
  .subnav-links-list {
    gap: 1.15rem;
    flex-shrink: 0;
  }
}'''

css = css.replace(old_subnav_media, new_subnav_media)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Added overflow constraints and fixed subnav mobile scrolling!")
