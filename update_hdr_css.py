with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_mobile_hdr = r'''@media (max-width: 768px) {
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

new_mobile_hdr = r'''@media (max-width: 768px) {
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

css = css.replace(old_mobile_hdr, new_mobile_hdr)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated styles.css with perfect mobile header spacing!")
