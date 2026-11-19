with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_hdr = r'''      <!-- Header Right Action Group -->
      <div class="header-right-group">
        <!-- Godrej Cursive Script Logo -->
        <a href="/" class="header-script-link" aria-label="Godrej Group">
          <img src="assets/images/godrejsignature.svg" alt="Godrej" class="header-logo-script">
        </a>

        <!-- Search Button -->
        <button type="button" class="hdr-icon-circle" aria-label="Search Projects" data-open-modal="enquiryModal" data-prefill="Search Projects">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#141414" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
          </svg>
        </button>

        <!-- Hamburger Menu Toggle Button -->
        <button type="button" class="hdr-icon-circle" id="navToggleBtn" aria-label="Open Navigation Menu">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#141414" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="3" y1="6" x2="21" y2="6"></line>
            <line x1="3" y1="12" x2="21" y2="12"></line>
            <line x1="3" y1="18" x2="21" y2="18"></line>
          </svg>
        </button>
      </div>'''

new_hdr = r'''      <!-- Header Right Action Group (Exact: Search, Hamburger, Script) -->
      <div class="header-right-group">
        <!-- Search Button -->
        <button type="button" class="hdr-icon-circle" aria-label="Search Projects" data-open-modal="enquiryModal" data-prefill="Search Projects">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#141414" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
          </svg>
        </button>

        <!-- Hamburger Menu Toggle Button -->
        <button type="button" class="hdr-icon-circle" id="navToggleBtn" aria-label="Open Navigation Menu">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#141414" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="3" y1="6" x2="21" y2="6"></line>
            <line x1="3" y1="12" x2="21" y2="12"></line>
            <line x1="3" y1="18" x2="21" y2="18"></line>
          </svg>
        </button>

        <!-- Godrej Cursive Script Logo -->
        <a href="/" class="header-script-link" aria-label="Godrej Group">
          <img src="assets/images/godrejsignature.svg" alt="Godrej" class="header-logo-script">
        </a>
      </div>'''

html = html.replace(old_hdr, new_hdr)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated header icon order to Search, Hamburger, Script!")
