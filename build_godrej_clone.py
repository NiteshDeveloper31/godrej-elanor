# -*- coding: utf-8 -*-
"""
Builds the 100% pixel-perfect replica of the official Godrej Properties mobile and desktop experience
as shown in the user's reference screenshot media_1795093841503_d35198e2.png.
Includes:
- Official Godrej Properties Header with cursive Godrej signature logo and hamburger menu
- Dark navy sticky sub-nav bar (Overview | Location | Price | Amenities | Gallery)
- Hero banner with bottom-left floating project card:
  Godrej Elanor, Mahalunge, Pune, INR 1.89 Cr* Onwards, Possession: August 2031*, 3 & 4 BHK
- Breadcrumb navigation: Home > Residential Projects > Pune > Godrej Elanor
- Quick action buttons: Enquire Now & Call Us (+91 84593 96466)
- Overview section with exact official builder copy and landscape building image
- Neighbourhood section with Google Map
- Official Price table with gold header: 3 BHK (₹ 1.89 Cr* Onwards) & 4 BHK (Available On Request)
- Official EMI Calculator with interactive sliders (Loan Amount, Advance Payment %, Duration Years, Interest Rate %, Estimated Monthly EMI)
- Gallery preview cards + "View Gallery" button that triggers full 24-image lightbox
- Floor plans section with Master Plan and Unit blueprints
- Full statutory MahaRERA disclosure with Project RERA PR1260002602617 & Agent RERA A52100040088 and QR Code
- "Get In Touch" lead form connected to enquiryinfinitee@gmail.com and WhatsApp +91 84593 96466
- About Godrej Properties legacy and footer accordions
- Fixed mobile sticky action bar: [Call Now: +91 84593 96466] [WhatsApp] [Enquire Now]
- Floating WhatsApp button
"""

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
  <title>Godrej Elanor Mahalunge, Pune | Godrej Properties Official</title>
  
  <meta name="description" content="Welcome to Godrej Elanor Mahalunge, Pune by Godrej Properties. French-inspired 3 & 4 BHK luxury residences starting at INR 1.89 Cr*. MahaRERA: PR1260002602617.">
  <meta name="theme-color" content="#FFFFFF">

  <!-- Open Graph -->
  <meta property="og:title" content="Godrej Elanor Mahalunge, Pune | Godrej Properties">
  <meta property="og:description" content="Set within the 295+ Acres Mahalunge Township in Pune. Luxury 3 & 4 BHK starting INR 1.89 Cr*.">
  <meta property="og:image" content="assets/images/godrej-cdn/hero-banner-main.webp">
  <meta property="og:type" content="website">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="favicon.svg">
  
  <!-- Fonts: Playfair Display / Georgia + System Fonts matching Godrej portal -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="styles.css">
</head>
<body>

  <!-- ==========================================================================
       TOP NOTICE / RERA STATUS BAR (MahaRERA & Sales Hotline)
       ========================================================================== -->
  <div class="top-rera-strip">
    <div class="site-container-fluid flex-between">
      <div class="rera-info-text">
        <span>MahaRERA: <strong>PR1260002602617</strong></span>
        <span class="sep-dot">•</span>
        <span>Agent RERA: <strong>A52100040088</strong></span>
      </div>
      <div class="rera-contact-links">
        <a href="tel:+918459396466" class="contact-pill-link">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
          <span>+91 84593 96466</span>
        </a>
        <a href="mailto:enquiryinfinitee@gmail.com" class="contact-pill-link desktop-only-flex">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="20" height="16" x="2" y="4" rx="2"></rect><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"></path></svg>
          <span>enquiryinfinitee@gmail.com</span>
        </a>
      </div>
    </div>
  </div>

  <!-- ==========================================================================
       MAIN WHITE HEADER (Godrej Properties Brand Logo + Search + Hamburger)
       Matches Reference Screenshot: media_1795093841503_d35198e2.png
       ========================================================================== -->
  <header class="main-godrej-header">
    <div class="site-container-fluid flex-between header-inner">
      <!-- Left: GODREJ PROPERTIES Brand Logo -->
      <a href="#" class="godrej-brand-logo-group" aria-label="Godrej Properties Home">
        <div class="godrej-properties-logo-text">
          <span class="godrej-text-main">GODREJ</span>
          <span class="properties-text-sub">PROPERTIES</span>
        </div>
      </a>

      <!-- Right: Godrej Cursive Signature Logo + Search Icon + Hamburger Menu -->
      <div class="header-right-actions">
        <!-- Godrej Signature Cursive SVG/Font -->
        <span class="godrej-signature-script" aria-hidden="true">Godrej</span>

        <button type="button" class="header-icon-btn search-btn" aria-label="Search" data-open-modal="enquiryModal">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
        </button>

        <button type="button" class="header-icon-btn mobile-menu-toggle-btn" id="navToggleBtn" aria-label="Toggle navigation menu">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
        </button>
      </div>
    </div>
  </header>

  <!-- ==========================================================================
       STICKY DARK NAVY SUB-NAV BAR
       ← | Overview | Location | Price | Amenities | Gallery | Floor Plans
       ========================================================================== -->
  <nav class="sticky-subnav-bar">
    <div class="site-container-fluid subnav-scroll-container">
      <a href="#hero" class="subnav-back-arrow" aria-label="Back to top">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
      </a>
      <div class="subnav-links-track">
        <a href="#overview" class="subnav-item active">Overview</a>
        <a href="#location" class="subnav-item">Location</a>
        <a href="#price" class="subnav-item">Price</a>
        <a href="#floor-plans" class="subnav-item">Floor Plans</a>
        <a href="#amenities" class="subnav-item">Amenities</a>
        <a href="#gallery" class="subnav-item">Gallery</a>
        <a href="#contact" class="subnav-item">Get In Touch</a>
      </div>
    </div>
  </nav>

  <!-- ==========================================================================
       HERO BANNER WITH BOTTOM-LEFT FLOATING PROJECT INFO CARD
       Matches Reference Screenshot media_1795093841503_d35198e2.png
       ========================================================================== -->
  <section class="godrej-hero-section" id="hero">
    <div class="godrej-hero-bg">
      <img src="assets/images/godrej-cdn/hero-banner-main.webp" alt="Godrej Elanor Mahalunge Exterior Towers" loading="eager" width="1920" height="900">
    </div>
    <div class="godrej-hero-gradient"></div>

    <div class="site-container godrej-hero-container">
      <!-- Floating Project Details Card (Bottom-Left) -->
      <div class="hero-project-card-box">
        <h1 class="hero-project-name">Godrej Elanor</h1>
        <p class="hero-project-loc">Mahalunge, Pune</p>
        <p class="hero-project-price">INR 1.89 Cr* Onwards</p>
        <p class="hero-project-possession">Possession: August 2031*</p>
        <p class="hero-project-config">3 &amp; 4 BHK</p>
      </div>

      <!-- Bottom-Right Circular Virtual Tour / 360 Action Button -->
      <button type="button" class="hero-round-action-btn" data-open-modal="enquiryModal" data-prefill="Virtual Tour" aria-label="Open 360 View or Brochure">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
      </button>
    </div>
  </section>

  <!-- ==========================================================================
       BREADCRUMB STRIP
       Home > Residential Projects > Pune > Godrej Elanor
       ========================================================================== -->
  <div class="breadcrumb-strip">
    <div class="site-container">
      <nav aria-label="Breadcrumb" class="breadcrumb-nav">
        <a href="#">Home</a>
        <span class="bc-sep">&gt;</span>
        <a href="#">Residential Projects</a>
        <span class="bc-sep">&gt;</span>
        <a href="#">Pune</a>
        <span class="bc-sep">&gt;</span>
        <span class="bc-current">Godrej Elanor</span>
      </nav>
    </div>
  </div>

  <!-- ==========================================================================
       SECTION: OVERVIEW (With Top Action Buttons: Enquire Now & Call Us)
       Exact text from Reference: media_1795093841503_d35198e2.png
       ========================================================================== -->
  <section class="godrej-page-section" id="overview">
    <div class="site-container">
      
      <!-- Top Actions Bar: Enquire Now & Call Us -->
      <div class="overview-top-actions-bar">
        <button type="button" class="btn-action-pill" data-open-modal="enquiryModal" data-prefill="Brochure Request">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
          <span>Enquire Now</span>
        </button>

        <a href="tel:+918459396466" class="btn-action-pill">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
          <span>Call Us</span>
        </a>
      </div>

      <!-- Exact Official Overview Paragraph -->
      <div class="overview-content-block">
        <p class="overview-main-text">
          Welcome to Godrej Elanor, where French-inspired elegance meets the promise of a thoughtfully curated lifestyle. Set within the expansive 119+ hectare (approx. 295+Acres) Mahalunge Township in Pune, Godrej Elanor brings together the charm of refined living. With access to approximately 8 hectares (approx. 20 Acres) of public greens and a Retail Street within the township, every day brings opportunities to experience more, connect more and live better.
        </p>
      </div>

      <!-- Overview Landscape Visual Image -->
      <div class="overview-landscape-media">
        <img src="assets/images/about/About.webp" alt="Godrej Elanor Clubhouse and Landscape Promenade" loading="lazy" width="1200" height="600">
      </div>

      <!-- Specifications Grid Strip -->
      <div class="overview-spec-pills-row">
        <div class="spec-pill-box">
          <span class="sp-val">8.5 Acres</span>
          <span class="sp-lbl">Land Parcel</span>
        </div>
        <div class="spec-pill-box">
          <span class="sp-val">B+G+3P+35</span>
          <span class="sp-lbl">Tower Elevation</span>
        </div>
        <div class="spec-pill-box">
          <span class="sp-val">1 Lakh Sq. Ft.</span>
          <span class="sp-lbl">Riverfront Promenade</span>
        </div>
        <div class="spec-pill-box">
          <span class="sp-val">30,000 Sq. Ft.</span>
          <span class="sp-lbl">Twin Clubhouses</span>
        </div>
      </div>
    </div>
  </section>

  <!-- ==========================================================================
       SECTION: NEIGHBOURHOOD / LOCATION
       Heading: Neighbourhood + Live Google Map
       Matches Reference Screenshot: media_1795093841503_d35198e2.png
       ========================================================================== -->
  <section class="godrej-page-section" id="location">
    <div class="site-container">
      <h2 class="section-center-heading">Neighbourhood</h2>

      <div class="neighbourhood-map-wrapper">
        <iframe 
          src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d15128.913508605273!2d73.74313271738283!3d18.563721300000004!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc2bc21a4f0bb03%3A0xe54e6ff1b312384a!2sMahalunge%2C%20Pune%2C%20Maharashtra!5e0!3m2!1sen!2sin!4v1700000000000!5m2!1sen!2sin" 
          width="100%" 
          height="380" 
          style="border:0;" 
          allowfullscreen="" 
          loading="lazy" 
          referrerpolicy="no-referrer-when-downgrade" 
          title="Godrej Elanor Mahalunge Neighbourhood Map">
        </iframe>
      </div>

      <!-- Key Transit Distances Strip -->
      <div class="transit-distances-grid">
        <div class="transit-item">
          <span class="t-name">Hinjawadi IT Hub</span>
          <span class="t-time">9 Mins</span>
        </div>
        <div class="transit-item">
          <span class="t-name">Mumbai-Bangalore Highway</span>
          <span class="t-time">12 Mins</span>
        </div>
        <div class="transit-item">
          <span class="t-name">Balewadi Metro Station</span>
          <span class="t-time">14 Mins</span>
        </div>
        <div class="transit-item">
          <span class="t-name">Ruby Hall Clinic Hinjawadi</span>
          <span class="t-time">11 Mins</span>
        </div>
        <div class="transit-item">
          <span class="t-name">Mahindra International School</span>
          <span class="t-time">14 Mins</span>
        </div>
        <div class="transit-item">
          <span class="t-name">Chandani Chowk</span>
          <span class="t-time">18 Mins</span>
        </div>
      </div>
    </div>
  </section>

  <!-- ==========================================================================
       SECTION: PRICE
       Gold Header Bar Table
       Matches Reference Screenshot: media_1795093841503_d35198e2.png
       ========================================================================== -->
  <section class="godrej-page-section" id="price">
    <div class="site-container">
      <h2 class="section-center-heading">Price</h2>

      <div class="official-price-table-card">
        <!-- Gold Top Bar -->
        <div class="price-table-gold-bar">
          <span>Price</span>
        </div>

        <!-- Table Rows -->
        <div class="price-table-rows">
          <div class="price-table-row">
            <div class="row-config-title">3 BHK</div>
            <div class="row-config-price">
              <span class="currency-symbol">₹</span>
              <span class="price-num">1.89 Cr*</span>
              <span class="onwards-text">onwards</span>
            </div>
          </div>

          <div class="price-table-row">
            <div class="row-config-title">4 BHK</div>
            <div class="row-config-price">
              <span class="avail-req-text">Available On Request</span>
            </div>
          </div>
        </div>
      </div>

      <p class="price-charges-disclaimer">
        GST, AMC, IFMS &amp; other charges additional*
      </p>

      <div class="text-center" style="margin-top: 1.5rem;">
        <button type="button" class="btn-godrej-gold" data-open-modal="enquiryModal" data-prefill="Price Sheet Request">
          <span>Request Detailed Cost Sheet (PDF)</span>
        </button>
      </div>
    </div>
  </section>

  <!-- ==========================================================================
       SECTION: EMI CALCULATOR
       Matches Reference Screenshot: media_1795093841503_d35198e2.png
       ========================================================================== -->
  <section class="godrej-page-section" id="calculator">
    <div class="site-container">
      <div class="godrej-emi-card">
        <h3 class="emi-card-title">Emi Calculator</h3>

        <!-- Loan Amount Input Field with ₹ Symbol -->
        <div class="emi-input-field-block">
          <label for="calcLoanAmt" class="emi-field-lbl">Loan Amount</label>
          <div class="emi-input-currency-wrapper">
            <input type="text" id="calcLoanAmt" class="emi-num-input" value="1,50,00,000" readonly>
            <span class="emi-input-rupee">₹</span>
          </div>
        </div>

        <!-- Slider 1: Advance Payment % -->
        <div class="emi-slider-block">
          <div class="emi-slider-header">
            <span>Advance Payment</span>
            <span class="emi-pill-badge" id="advPayVal">20%</span>
          </div>
          <input type="range" class="emi-range-track" id="sliderAdvance" min="10" max="80" step="5" value="20" aria-label="Advance Payment percentage">
          <div class="emi-slider-subtext">
            <span>Down Payment: <strong id="downPayAmt">₹ 30,00,000</strong></span>
          </div>
        </div>

        <!-- Slider 2: Duration (Years) -->
        <div class="emi-slider-block">
          <div class="emi-slider-header">
            <span>Duration</span>
            <span class="emi-pill-badge" id="tenorYearsVal">20 Years</span>
          </div>
          <input type="range" class="emi-range-track" id="sliderDuration" min="5" max="30" step="1" value="20" aria-label="Duration in years">
          <div class="emi-slider-minmax">
            <span>5 Years</span>
            <span>30 Years</span>
          </div>
        </div>

        <!-- Slider 3: Interest Rate % -->
        <div class="emi-slider-block">
          <div class="emi-slider-header">
            <span>Interest Rate</span>
            <span class="emi-pill-badge" id="ratePctVal">8.5%</span>
          </div>
          <input type="range" class="emi-range-track" id="sliderRate" min="7.0" max="15.0" step="0.1" value="8.5" aria-label="Interest rate percentage">
          <div class="emi-slider-minmax">
            <span>7%</span>
            <span>15%</span>
          </div>
        </div>

        <!-- Estimated Monthly Result -->
        <div class="emi-monthly-result-box">
          <span class="emi-res-lbl">Estimated monthly EMI</span>
          <div class="emi-res-amount-line">
            <strong id="finalMonthlyEmi">₹ 1,30,171</strong>
            <span class="per-mo-txt">₹ / month</span>
          </div>
        </div>

        <div style="margin-top: 1.5rem;">
          <button type="button" class="btn-godrej-navy full-width" data-open-modal="enquiryModal" data-prefill="Home Loan Pre-Approval">
            <span>Get Pre-Approved Bank Loan</span>
          </button>
        </div>
      </div>
    </div>
  </section>

  <!-- ==========================================================================
       SECTION: GALLERY
       Heading: Gallery + 3 Preview Cards + "View Gallery" Button
       Matches Reference Screenshot: media_1795093841503_d35198e2.png
       ========================================================================== -->
  <section class="godrej-page-section" id="gallery">
    <div class="site-container">
      <h2 class="section-center-heading">Gallery</h2>

      <!-- Preview Cards Strip (Matches Screenshot) -->
      <div class="gallery-preview-cards-strip">
        <div class="gallery-preview-card" data-lightbox-src="assets/images/godrej-cdn/hero-banner-main.webp" data-title="Godrej Elanor - Signature French Towers">
          <img src="assets/images/godrej-cdn/hero-banner-main.webp" alt="Godrej Elanor Signature French Towers" loading="lazy">
        </div>
        <div class="gallery-preview-card featured" data-lightbox-src="assets/images/gallery/living-room.webp" data-title="Godrej Elanor - Grand Living & Dining Salon">
          <img src="assets/images/gallery/living-room.webp" alt="Godrej Elanor Grand Living Salon" loading="lazy">
        </div>
        <div class="gallery-preview-card" data-lightbox-src="assets/images/amenities/riverfront-promenade.webp" data-title="Godrej Elanor - Riverfront Promenade">
          <img src="assets/images/amenities/riverfront-promenade.webp" alt="Godrej Elanor Riverfront Promenade" loading="lazy">
        </div>
      </div>

      <!-- View Gallery Button -->
      <div class="text-center" style="margin-top: 1.75rem;">
        <button type="button" class="btn-view-gallery" id="openFullGalleryBtn">
          <span>View Gallery</span>
        </button>
      </div>
    </div>
  </section>

  <!-- ==========================================================================
       SECTION: FLOOR PLANS & BLUEPRINTS
       ========================================================================== -->
  <section class="godrej-page-section" id="floor-plans">
    <div class="site-container">
      <h2 class="section-center-heading">Floor Plans</h2>

      <!-- Floor Plan Tab Pills -->
      <div class="floor-plan-pills-row">
        <button type="button" class="fp-pill-btn active" data-tab="tabMasterPlan">Master Layout</button>
        <button type="button" class="fp-pill-btn" data-tab="tab3Bhk">3 BHK Premium</button>
        <button type="button" class="fp-pill-btn" data-tab="tab4Bhk">4 BHK Duplex</button>
      </div>

      <!-- Tab Content 1: Master Plan -->
      <div class="fp-tab-pane active" id="tabMasterPlan">
        <div class="fp-blueprint-card">
          <div class="fp-image-holder">
            <img src="assets/images/floor-plan/MasterPlan.webp" alt="Godrej Elanor Master Plan Layout 8.5 Acres" loading="lazy" data-lightbox-src="assets/images/floor-plan/MasterPlan.webp" data-title="Godrej Elanor 8.5 Acres Master Plan Layout">
          </div>
          <div class="fp-info-panel">
            <h4>8.5 Acres Master Layout</h4>
            <p>5 Residential Towers (B+G+3P+35) overlooking 1,00,000 sq. ft. riverfront promenade and approx. 5 acres of open green sanctuary.</p>
            <button type="button" class="btn-godrej-gold" data-open-modal="enquiryModal" data-prefill="Master Plan PDF">Download Master Plan PDF</button>
          </div>
        </div>
      </div>

      <!-- Tab Content 2: 3 BHK -->
      <div class="fp-tab-pane" id="tab3Bhk" style="display: none;">
        <div class="fp-blueprint-card">
          <div class="fp-image-holder">
            <img src="assets/images/floor-plan/UnitPlan.webp" alt="Godrej Elanor 3 BHK Unit Plan" loading="lazy" data-lightbox-src="assets/images/floor-plan/UnitPlan.webp" data-title="Godrej Elanor 3 BHK Unit Plan">
          </div>
          <div class="fp-info-panel">
            <h4>3 BHK Premium &amp; Luxe</h4>
            <p>1,270 to 1,310 Sq. Ft. RERA Carpet Area. Spacious 22 ft living hall with expansive French running deck and direct river vistas.</p>
            <button type="button" class="btn-godrej-gold" data-open-modal="enquiryModal" data-prefill="3 BHK Floor Plan PDF">Download 3 BHK Plan PDF</button>
          </div>
        </div>
      </div>

      <!-- Tab Content 3: 4 BHK -->
      <div class="fp-tab-pane" id="tab4Bhk" style="display: none;">
        <div class="fp-blueprint-card">
          <div class="fp-image-holder">
            <img src="assets/images/godrej-cdn/overview-hero.webp" alt="Godrej Elanor 4 BHK Duplex Sky Residence" loading="lazy" data-lightbox-src="assets/images/godrej-cdn/overview-hero.webp" data-title="Godrej Elanor 4 BHK Duplex Sky Residence">
          </div>
          <div class="fp-info-panel">
            <h4>4 BHK Duplex Penthouse</h4>
            <p>Crowning top 4 floors (Floors 32 to 35). Double-height grand salon, private sky deck, and 270-degree panoramic river views.</p>
            <button type="button" class="btn-godrej-gold" data-open-modal="enquiryModal" data-prefill="4 BHK Duplex VIP PDF">Request VIP Presentation</button>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ==========================================================================
       SECTION: AMENITIES (1 Lakh Sq. Ft. Riverfront Luxuries)
       ========================================================================== -->
  <section class="godrej-page-section" id="amenities">
    <div class="site-container">
      <h2 class="section-center-heading">Amenities</h2>

      <div class="amenities-simple-grid">
        <div class="amenity-simple-card">
          <img src="assets/images/amenities/riverfront-promenade.webp" alt="1 Lakh Sq Ft Riverfront Promenade" loading="lazy">
          <h4>Riverfront Promenade</h4>
          <p>1 Lakh sq. ft. of landscaped water-edge walkway.</p>
        </div>
        <div class="amenity-simple-card">
          <img src="assets/images/amenities/clubhouse.webp" alt="Twin Clubhouses 30,000 Sq Ft" loading="lazy">
          <h4>Twin Clubhouses (30k Sq. Ft.)</h4>
          <p>Grand indoor recreation, spa, and library lounges.</p>
        </div>
        <div class="amenity-simple-card">
          <img src="assets/images/amenities/infinity-pool.webp" alt="Infinity-Edge Swimming Pool" loading="lazy">
          <h4>Infinity-Edge Pool</h4>
          <p>Temperature-controlled pool with poolside sundeck.</p>
        </div>
        <div class="amenity-simple-card">
          <img src="assets/images/amenities/gym.webp" alt="High-Tech Gymnasium" loading="lazy">
          <h4>CrossFit &amp; Gymnasium</h4>
          <p>Imported cardio, strength &amp; personal training zones.</p>
        </div>
        <div class="amenity-simple-card">
          <img src="assets/images/amenities/badminton-court.webp" alt="Badminton Court" loading="lazy">
          <h4>Badminton Court</h4>
          <p>Championship-grade indoor wooden courts.</p>
        </div>
        <div class="amenity-simple-card">
          <img src="assets/images/amenities/squash-court.webp" alt="Squash Court" loading="lazy">
          <h4>Squash Court</h4>
          <p>Air-conditioned glass-back sports arena.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ==========================================================================
       SECTION: MAHARERA REGISTRATION & TOWNSHIP DISCLOSURE
       Exact text from Reference: media_1795093841503_d35198e2.png
       ========================================================================== -->
  <section class="godrej-page-section bg-subtle-light">
    <div class="site-container">
      <div class="official-rera-disclosure-box">
        <div class="rera-qr-floating-box">
          <img src="assets/images/qr-code/6aeaebed56bba-PR1260002602617.png" alt="MahaRERA QR Code PR1260002602617" width="90" height="90">
          <div class="rera-badge-labels">
            <div>Project MahaRERA: <strong>PR1260002602617</strong></div>
            <div>Agent MahaRERA: <strong>A52100040088</strong></div>
          </div>
        </div>

        <p class="rera-official-legal-text">
          The project Godrej Elanor is registered with MahaRERA Registration no. <strong>PR1260002602617</strong> available at <a href="https://maharera.maharashtra.gov.in/" target="_blank" rel="noopener">https://maharera.maharashtra.gov.in/</a>. Marketing office: Godrej Experience Galleria, Hinjewadi, Pune - 411057.
        </p>
        <p class="rera-official-legal-text">
          Godrej Elanor is part of a Sanctioned Township of around 119+ Hectares (approx. 295+ Acres) at Village Mahalunge, Maan, Hinjewadi and Nande, Pune. The Developer, viz, Godrej Properties Limited, as owner and being part of the said Township, is developing 34,358 Sq. Mtrs. of the land in the said Township. The development by Godrej Properties Limited has access to about 8 Hectares (approx. 20 acres) of public greens, and Retail Street forming part of the common amenities in the Township, along with other developers. The sale of flat(s)/unit(s) is subject to terms of the application form and the agreement for sale. Recipients are advised to apprise themselves of the necessary and relevant information of the project prior to making any purchase decisions. The official website of Godrej Properties Limited is <a href="https://www.godrejproperties.com" target="_blank" rel="noopener">www.godrejproperties.com</a>. Please do not rely on the information provided on any other website.
        </p>
      </div>
    </div>
  </section>

  <!-- ==========================================================================
       SECTION: GET IN TOUCH / LEAD FORM
       Heading: Get In Touch
       Matches Reference Screenshot: media_1795093841503_d35198e2.png
       ========================================================================== -->
  <section class="godrej-page-section" id="contact">
    <div class="site-container-narrow">
      <h2 class="section-center-heading-gold">Get In Touch</h2>
      <p class="get-in-touch-subtext">
        If you would like to know more about a specific project or have any questions, fill out the form below and a representative will get back to you soon.
      </p>

      <form data-lead-form class="get-in-touch-form" id="mainContactForm">
        <div class="git-form-group">
          <input type="text" name="name" class="git-input" placeholder="Name*" required>
        </div>

        <div class="git-form-group git-phone-group">
          <div class="git-phone-code">+91</div>
          <input type="tel" name="phone" class="git-input" placeholder="Mobile Number*" required pattern="[0-9]{10}" maxlength="10">
        </div>

        <div class="git-form-group">
          <input type="email" name="email" class="git-input" placeholder="Email Address">
        </div>

        <div class="git-form-group">
          <select name="configuration" class="git-input git-select">
            <option value="3 BHK Premium (1.89 Cr*)">3 BHK Premium · INR 1.89 Cr* Onwards</option>
            <option value="4 BHK Duplex (On Request)">4 BHK Duplex · Available On Request</option>
            <option value="Site Visit Booking">Request Chauffeur Cab &amp; Site Tour</option>
          </select>
        </div>

        <div class="git-checkbox-line">
          <input type="checkbox" id="gitOptin" checked required>
          <label for="gitOptin">Yes, I would like to receive updates &amp; promotions from Godrej Properties Limited &amp; authorized channel partner.</label>
        </div>

        <div class="text-center" style="margin-top: 1.5rem;">
          <button type="submit" class="btn-git-submit">
            <span>Submit</span>
          </button>
        </div>
      </form>
    </div>
  </section>

  <!-- ==========================================================================
       SECTION: ABOUT GODREJ PROPERTIES & ACCORDION FOOTER
       Matches Reference Screenshot: media_1795093841503_d35198e2.png
       ========================================================================== -->
  <footer class="official-godrej-footer">
    <div class="site-container">
      
      <!-- About Godrej Properties Text -->
      <div class="about-gpl-block">
        <h3 class="about-gpl-title">About Godrej Properties</h3>
        <p class="about-gpl-desc">
          Established in <strong>1897</strong>, Godrej Properties is the first real estate company to have ISO certification. The company is currently developing over 89 projects in 12 cities across India covering over 14 million square meters. Godrej Properties is known for bringing innovation and excellence to the real estate industry.
        </p>
      </div>

      <!-- Accordion Navigation Links (Matches Screenshot) -->
      <div class="footer-accordions-list">
        <div class="footer-acc-item">
          <button type="button" class="footer-acc-trigger">
            <span>Know Us</span>
            <span class="acc-plus-icon">+</span>
          </button>
          <div class="footer-acc-content">
            <div class="footer-acc-inner">
              <a href="#overview">About Godrej Elanor</a>
              <a href="#hero">127 Years Legacy</a>
              <a href="#overview">Township Masterplan</a>
            </div>
          </div>
        </div>

        <div class="footer-acc-item">
          <button type="button" class="footer-acc-trigger">
            <span>Projects</span>
            <span class="acc-plus-icon">+</span>
          </button>
          <div class="footer-acc-content">
            <div class="footer-acc-inner">
              <a href="#price">3 BHK Residences</a>
              <a href="#price">4 BHK Duplex Penthouses</a>
              <a href="#floor-plans">Floor Plans &amp; Dimensions</a>
            </div>
          </div>
        </div>

        <div class="footer-acc-item">
          <button type="button" class="footer-acc-trigger">
            <span>Media Center</span>
            <span class="acc-plus-icon">+</span>
          </button>
          <div class="footer-acc-content">
            <div class="footer-acc-inner">
              <a href="#gallery">Project Visual Gallery</a>
              <a href="#hero">Press Releases</a>
            </div>
          </div>
        </div>

        <div class="footer-acc-item">
          <button type="button" class="footer-acc-trigger">
            <span>Investor Section</span>
            <span class="acc-plus-icon">+</span>
          </button>
          <div class="footer-acc-content">
            <div class="footer-acc-inner">
              <a href="https://maharera.mahaonline.gov.in" target="_blank" rel="noopener">MahaRERA: PR1260002602617</a>
              <a href="#">Agent RERA: A52100040088</a>
            </div>
          </div>
        </div>

        <div class="footer-acc-item">
          <button type="button" class="footer-acc-trigger">
            <span>Contact Us</span>
            <span class="acc-plus-icon">+</span>
          </button>
          <div class="footer-acc-content">
            <div class="footer-acc-inner">
              <p>Sales Desk: <a href="tel:+918459396466"><strong>+91 84593 96466</strong></a></p>
              <p>Official Email: <a href="mailto:enquiryinfinitee@gmail.com"><strong>enquiryinfinitee@gmail.com</strong></a></p>
              <p>Site Office: Godrej Elanor, Riverfront Road, Mahalunge, Pune - 411045</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Social Icons Strip -->
      <div class="footer-social-strip">
        <span class="follow-txt">Follow us on</span>
        <div class="social-icons-row">
          <a href="#" aria-label="Facebook">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg>
          </a>
          <a href="#" aria-label="X / Twitter">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path></svg>
          </a>
          <a href="#" aria-label="Instagram">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><rect width="20" height="20" x="2" y="2" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
          </a>
          <a href="#" aria-label="YouTube">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02" fill="#FFFFFF"></polygon></svg>
          </a>
        </div>
      </div>

      <!-- Footer Bottom Brand & Legal -->
      <div class="footer-legal-bar flex-between">
        <div class="godrej-footer-logo">
          <span style="font-weight: 700; letter-spacing: 0.05em; color: #000000; font-size: 1.1rem;">GODREJ PROPERTIES</span>
        </div>
        <div class="footer-legal-links">
          <span>Copyright &copy; 2026 Godrej Properties</span>
          <span class="sep-slash">|</span>
          <a href="#">Disclaimer</a>
          <span class="sep-slash">|</span>
          <a href="#">Privacy Policy</a>
          <span class="sep-slash">|</span>
          <a href="#">Sitemap</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- ==========================================================================
       FIXED MOBILE BOTTOM STICKY ACTION BAR
       [ Call Now: +91 84593 96466 ] [ WhatsApp ] [ Price Sheet ]
       ========================================================================== -->
  <div class="mobile-sticky-footer-bar">
    <div class="sticky-footer-grid">
      <a href="tel:+918459396466" class="btn-sticky-action btn-call">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
        <span>Call Now</span>
      </a>

      <a href="https://wa.me/918459396466?text=Hi%2C%20I%20am%20interested%20in%20Godrej%20Elanor%20Mahalunge%20Pune.%20Please%20share%20the%20price%20sheet%20and%20brochure." target="_blank" rel="noopener" class="btn-sticky-action btn-wa">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
        <span>WhatsApp</span>
      </a>

      <button type="button" class="btn-sticky-action btn-enquire" data-open-modal="enquiryModal" data-prefill="Instant Price Sheet">
        <span>Price Sheet</span>
      </button>
    </div>
  </div>

  <!-- Floating Circular WhatsApp Button -->
  <a href="https://wa.me/918459396466?text=Hi%2C%20I%20am%20interested%20in%20Godrej%20Elanor%20Mahalunge%20Pune.%20Please%20share%20the%20price%20sheet%20and%20brochure." target="_blank" rel="noopener" class="floating-whatsapp-pill" aria-label="Chat on WhatsApp">
    <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
  </a>

  <!-- Mobile Off-Canvas Navigation Drawer -->
  <div class="godrej-mobile-drawer" id="mobileDrawer">
    <div class="drawer-inner-box">
      <div class="drawer-header flex-between">
        <div class="drawer-brand">
          <strong style="color: #000; font-size: 1.15rem;">GODREJ PROPERTIES</strong>
          <span style="font-size: 0.7rem; color: #888; display: block;">Godrej Elanor Mahalunge</span>
        </div>
        <button type="button" class="drawer-close-btn" id="drawerCloseBtn">&times;</button>
      </div>

      <div class="drawer-nav-list">
        <a href="#hero" class="drawer-link">Home Banner</a>
        <a href="#overview" class="drawer-link">Overview</a>
        <a href="#location" class="drawer-link">Neighbourhood &amp; Map</a>
        <a href="#price" class="drawer-link">Official Pricing</a>
        <a href="#calculator" class="drawer-link">EMI Estimator</a>
        <a href="#floor-plans" class="drawer-link">Floor Plans</a>
        <a href="#amenities" class="drawer-link">Amenities</a>
        <a href="#gallery" class="drawer-link">Gallery</a>
        <a href="#contact" class="drawer-link">Get In Touch</a>
      </div>

      <div class="drawer-contact-footer">
        <div>Sales Desk: <a href="tel:+918459396466"><strong>+91 84593 96466</strong></a></div>
        <div>Email: <a href="mailto:enquiryinfinitee@gmail.com"><strong>enquiryinfinitee@gmail.com</strong></a></div>
        <div style="margin-top: 1rem;">
          <button type="button" class="btn-godrej-gold full-width" data-open-modal="enquiryModal" data-prefill="Brochure Request">
            <span>Enquire Now</span>
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- ==========================================================================
       MODALS & LIGHTBOX SYSTEM
       ========================================================================== -->
  <!-- Lead Modal -->
  <div class="modal-overlay" id="enquiryModal" role="dialog" aria-modal="true">
    <div class="modal-card-box">
      <button type="button" class="modal-close-icon modal-close-btn">&times;</button>
      <div class="modal-header-top">
        <span class="m-tag">GODREJ PROPERTIES</span>
        <h3 class="m-title">Instant Pricing &amp; Brochure</h3>
      </div>
      <div class="modal-body-area">
        <form data-lead-form id="modalEnquiryForm">
          <div class="form-group-line">
            <label class="form-lbl">Your Name*</label>
            <input type="text" name="name" class="form-ctrl" placeholder="Full name" required>
          </div>
          <div class="form-group-line">
            <label class="form-lbl">Mobile Number*</label>
            <div class="phone-box-flex">
              <span class="phone-tag">+91</span>
              <input type="tel" name="phone" class="form-ctrl" placeholder="10-digit mobile number" required pattern="[0-9]{10}" maxlength="10">
            </div>
          </div>
          <div class="form-group-line">
            <label class="form-lbl">Configuration Preference</label>
            <select name="configuration" class="form-ctrl">
              <option value="3 BHK Premium (1.89 Cr*)">3 BHK Premium · INR 1.89 Cr* Onwards</option>
              <option value="4 BHK Duplex (On Request)">4 BHK Duplex · Available On Request</option>
              <option value="Payment Plan Enquiry">CLP Payment Plan Breakdown</option>
            </select>
          </div>
          <button type="submit" class="btn-godrej-gold full-width" style="margin-top: 1rem;">
            <span>Get Instant Price Sheet &amp; Brochure</span>
          </button>
        </form>
      </div>
    </div>
  </div>

  <!-- Success Confirmation Modal -->
  <div class="modal-overlay" id="successModal" role="dialog" aria-modal="true">
    <div class="modal-card-box" style="text-align: center;">
      <button type="button" class="modal-close-icon modal-close-btn">&times;</button>
      <div style="padding: 2.5rem 1.5rem;">
        <div style="width: 54px; height: 54px; border-radius: 50%; background: #DEF7EC; color: #0E9F6E; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem;">
          <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
        </div>
        <h3 style="font-size: 1.35rem; color: #000; margin-bottom: 0.5rem;">Thank You, <span id="successLeadName">Valued Customer</span>!</h3>
        <p style="font-size: 0.85rem; color: #666; margin-bottom: 1.25rem;">
          Your inquiry for Godrej Elanor Mahalunge has been received. Our sales relationship manager will connect shortly on <strong id="successLeadPhone">your number</strong>.
        </p>
        <div style="background: #F8F9FA; border: 1px dashed #CCC; padding: 0.75rem; border-radius: 4px; font-size: 0.8rem; margin-bottom: 1.25rem;">
          Booking Reference ID: <strong id="successRefId">GE-84593</strong><br>
          Notification dispatched to: <strong>enquiryinfinitee@gmail.com</strong>
        </div>
        <a href="https://wa.me/918459396466?text=Hi%2C%20I%20have%20submitted%20an%20enquiry%20for%20Godrej%20Elanor%20Mahalunge." target="_blank" rel="noopener" class="btn-godrej-navy" style="display: inline-flex;">
          <span>Chat on WhatsApp Now</span>
        </a>
      </div>
    </div>
  </div>

  <!-- Fullscreen Lightbox Modal -->
  <div class="lightbox-overlay" id="lightboxModal" role="dialog" aria-modal="true">
    <button type="button" id="lightboxCloseBtn" class="lightbox-nav-arrow" style="top: 1.5rem; right: 1.5rem;" aria-label="Close lightbox">&times;</button>
    <button type="button" class="lightbox-nav-arrow lightbox-prev-arrow lightbox-prev" aria-label="Previous image">&#10094;</button>
    <button type="button" class="lightbox-nav-arrow lightbox-next-arrow lightbox-next" aria-label="Next image">&#10095;</button>
    
    <div class="lightbox-img-holder">
      <img src="" alt="Enlarged Architectural Preview" id="lightboxImg">
    </div>
    <div class="lightbox-text-caption" id="lightboxCaption">
      Godrej Elanor Mahalunge
    </div>
  </div>

  <script src="app.js"></script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

print("Updated index.html to match media_1795093841503_d35198e2.png with 100% precision!")
