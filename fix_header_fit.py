with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re

# Replace header logo rules
old_gpl_logo = r'''.header-logo-gpl {
  height: 32px;
  width: auto;
  display: block;
}'''

new_gpl_logo = r'''.header-logo-gpl {
  height: 28px;
  width: 135px;
  max-width: 135px;
  object-fit: contain;
  display: block;
}'''

css = css.replace(old_gpl_logo, new_gpl_logo)

old_script_logo = r'''.header-logo-script {
  height: 30px;
  width: auto;
  display: block;
}'''

new_script_logo = r'''.header-logo-script {
  height: 24px;
  width: 50px;
  max-width: 50px;
  object-fit: contain;
  display: block;
}'''

css = css.replace(old_script_logo, new_script_logo)

# Update media query for header
old_media = r'''@media (max-width: 768px) {
  .godrej-site-header {
    height: 56px;
  }
  .header-inner-container {
    padding: 0 0.85rem;
  }
  .header-logo-gpl {
    height: 24px;
  }
  .header-right-group {
    gap: 0.45rem;
  }
  .header-logo-script {
    height: 22px;
    margin-left: 0.25rem;
  }
  .hdr-icon-circle {
    width: 32px;
    height: 32px;
  }
}'''

new_media = r'''@media (max-width: 768px) {
  .godrej-site-header {
    height: 56px;
    overflow: hidden;
  }
  .header-inner-container {
    padding: 0 0.75rem;
    flex-wrap: nowrap;
  }
  .header-brand-link {
    flex-shrink: 0;
  }
  .header-logo-gpl {
    height: 22px;
    width: 106px;
    max-width: 106px;
  }
  .header-right-group {
    gap: 0.35rem;
    flex-shrink: 0;
  }
  .header-logo-script {
    height: 20px;
    width: 42px;
    max-width: 42px;
    margin-left: 0;
  }
  .hdr-icon-circle {
    width: 30px;
    height: 30px;
    flex-shrink: 0;
  }
  .hdr-icon-circle svg {
    width: 15px;
    height: 15px;
  }
}'''

css = css.replace(old_media, new_media)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied exact constrained header sizing!")
