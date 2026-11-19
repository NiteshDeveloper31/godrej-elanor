with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re

old_mobile_hdr = r'''@media (max-width: 768px) {
  .godrej-site-header {
    height: 56px;
    overflow: hidden;
  }
  .header-inner-container {
    padding: 0 0.75rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
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
    display: flex;
    align-items: center;
    gap: 0.4rem;
    flex-shrink: 0;
  }
  .hdr-icon-circle {
    width: 32px;
    height: 32px;
    flex-shrink: 0;
  }
  .hdr-icon-circle svg {
    width: 16px;
    height: 16px;
  }
  .header-logo-script {
    height: 20px;
    width: 42px;
    max-width: 42px;
    margin-left: 0.2rem;
  }
}'''

new_mobile_hdr = r'''@media (max-width: 768px) {
  .godrej-site-header {
    height: 56px;
    width: 100%;
  }
  .header-inner-container {
    padding: 0 0.75rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    max-width: 100%;
  }
  .header-brand-link {
    flex-shrink: 0;
  }
  .header-logo-gpl {
    height: 20px;
    width: auto;
    max-width: 100px;
    object-fit: contain;
  }
  .header-right-group {
    display: flex;
    align-items: center;
    gap: 0.35rem;
    flex-shrink: 0;
  }
  .hdr-icon-circle {
    width: 28px;
    height: 28px;
    flex-shrink: 0;
  }
  .hdr-icon-circle svg {
    width: 14px;
    height: 14px;
  }
  .header-logo-script {
    height: 18px;
    width: auto;
    max-width: 40px;
    object-fit: contain;
    margin-left: 0.15rem;
  }
}'''

css = css.replace(old_mobile_hdr, new_mobile_hdr)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated mobile header CSS for ultra-responsive fit!")
