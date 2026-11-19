with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace mobile header gap and logo sizes
old_mobile_hdr = r'''@media (max-width: 768px) {
  .godrej-site-header {
    height: 56px;
  }
  .header-logo-gpl {
    height: 26px;
  }
  .header-logo-script {
    height: 24px;
  }
  .hdr-icon-circle {
    width: 34px;
    height: 34px;
  }
}'''

new_mobile_hdr = r'''@media (max-width: 768px) {
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

css = css.replace(old_mobile_hdr, new_mobile_hdr)

# Make sure hero card and plus button don't overlap on mobile
old_card_mobile = r'''@media (max-width: 768px) {
  .hero-floating-card-wrapper {
    bottom: 1.75rem;
    left: 1rem;
    right: 4.5rem;
    max-width: none;
  }
}'''

new_card_mobile = r'''@media (max-width: 768px) {
  .hero-floating-card-wrapper {
    bottom: 1.25rem;
    left: 0.75rem;
    right: 4.25rem;
    max-width: none;
  }
  .hero-action-circle-wrap {
    bottom: 1.25rem;
    right: 0.75rem;
    z-index: 10;
  }
  .hero-circle-plus-btn {
    width: 44px;
    height: 44px;
  }
}'''

css = css.replace(old_card_mobile, new_card_mobile)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated mobile styles successfully!")
