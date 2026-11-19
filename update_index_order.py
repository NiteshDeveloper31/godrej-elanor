# -*- coding: utf-8 -*-
"""
Production builder update for Godrej Elanor Mahalunge landing page.
Aligns structure 100% to official Godrej Properties portal:
Banner -> Overview -> Floor Plans & Pricing -> Amenities -> Gallery (Exact 6-column asymmetric grid) -> Location -> Footer.
Client Credentials:
- Phone: +91 84593 96466
- Email: enquiryinfinitee@gmail.com
- Project RERA: PR1260002602617
- Agent RERA: A52100040088
"""

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
  <title>Godrej Elanor Mahalunge, Pune | Luxury 3 & 4 BHK Riverfront Residences | Godrej Properties</title>
  
  <meta name="description" content="Welcome to Godrej Elanor Mahalunge, Pune by Godrej Properties. French-inspired luxury 3 & 4 BHK riverside residences starting at ₹ 1.89 Cr*. MahaRERA: PR1260002602617.">
  <meta name="keywords" content="Godrej Elanor, Godrej Elanor Mahalunge, Godrej Properties Pune, Godrej Hinjewadi Baner, Luxury 3 BHK Pune, Flats in Mahalunge">
  <meta name="author" content="Authorized Channel Partner: A52100040088">
  <meta name="theme-color" content="#0B2545">

  <!-- Open Graph Meta Tags -->
  <meta property="og:title" content="Godrej Elanor Mahalunge, Pune | Luxury Riverfront Residences">
  <meta property="og:description" content="French-inspired riverside living by Godrej Properties. 3 & 4 BHK residences starting ₹ 1.89 Cr*. EOI booking window open.">
  <meta property="og:image" content="assets/images/godrej-cdn/hero-banner-main.webp">
  <meta property="og:type" content="website">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="favicon.svg">
  
  <!-- Google Fonts: Playfair Display + Plus Jakarta Sans -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">

  <!-- Stylesheet -->
  <link rel="stylesheet" href="styles.css">
</head>
<body>

  <!-- ==========================================================================
       TOP NOTICE & RERA STATUS BAR
       ========================================================================== -->
  <div class="top-notice-bar">
    <div class="container">
      <div class="top-bar-rera">
        <span class="rera-pill-badge">MahaRERA Approved</span>
        <span>Project RERA: <strong>PR1260002602617</strong></span>
        <span class="sep-bullet" aria-hidden="true">•</span>
        <span>Agent RERA: <strong>A52100040088</strong></span>
        <a href="https://maharera.mahaonline.gov.in" target="_blank" rel="noopener" class="top-contact-link" style="text-decoration: underline; margin-left: 6px;">Verify on MahaRERA</a>
      </div>
      <div class="top-bar-contact">
        <a href="tel:+918459396466" class="top-contact-link">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
          <span>Sales Desk: <strong>+91 84593 96466</strong></span>
        </a>
        <span class="sep-bullet" aria-hidden="true">•</span>
        <a href="mailto:enquiryinfinitee@gmail.com" class="top-contact-link">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="16" x="2" y="4" rx="2"></rect><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"></path></svg>
          <span>enquiryinfinitee@gmail.com</span>
        </a>
      </div>
    </div>
  </div>

  <!-- ==========================================================================
       MAIN BRAND NAVBAR
       ========================================================================== -->
  <header class="site-header">
    <nav class="site-navbar">
      <div class="container navbar-inner">
        <!-- Brand Logo -->
        <a href="#" class="brand-box" aria-label="Godrej Elanor Home">
          <span class="brand-logo-text">GODREJ PROPERTIES</span>
          <span class="brand-subtitle">GODREJ ELANOR · MAHALUNGE, PUNE</span>
        </a>

        <!-- Desktop Navigation Links (Official Section Order) -->
        <div class="navbar-links" role="navigation">
          <a href="#hero" class="nav-item-link">Home</a>
          <a href="#overview" class="nav-item-link">Overview</a>
          <a href="#floor-plans" class="nav-item-link">Floor Plans</a>
          <a href="#price" class="nav-item-link">Price &amp; Units</a>
          <a href="#amenities" class="nav-item-link">Amenities</a>
          <a href="#gallery" class="nav-item-link">Gallery</a>
          <a href="#location" class="nav-item-link">Location</a>
          <a href="#faqs" class="nav-item-link">FAQs</a>
        </div>

        <!-- Action Buttons -->
        <div class="navbar-cta-group">
          <a href="tel:+918459396466" class="btn btn-outline-navy" style="padding: 0.55rem 1rem; font-size: 0.85rem;">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
            <span>+91 84593 96466</span>
          </a>
          <button type="button" class="btn btn-gold" data-open-modal="enquiryModal" data-prefill="Brochure Request" style="padding: 0.55rem 1.15rem; font-size: 0.85rem;">
            <span>Enquire Now</span>
          </button>
          
          <!-- Mobile Menu Toggle Button -->
          <button type="button" class="mobile-menu-btn mobile-nav-toggle" id="mobileNavToggle" aria-label="Toggle navigation menu">
            <span></span>
            <span></span>
            <span></span>
          </button>
        </div>
      </div>
    </nav>
  </header>

  <!-- ==========================================================================
       SECTION 1: HERO BANNER (Widescreen Render + High-Contrast Lead Form)
       ========================================================================== -->
  <section class="hero-banner-section" id="hero">
    <div class="hero-bg-media">
      <img src="assets/images/godrej-cdn/hero-banner-main.webp" alt="Godrej Elanor Mahalunge Luxury Towers" loading="eager" width="1920" height="900">
    </div>
    <div class="hero-gradient-overlay"></div>

    <div class="container hero-content-grid">
      <!-- Left Content Column (High Contrast & Clear Typography) -->
      <div class="hero-left-col">
        <div class="hero-project-tag">
          <span class="status-pulse-dot"></span>
          <span>NEW LAUNCH · MAHALUNGE, PUNE</span>
        </div>

        <h1 class="hero-heading">
          Godrej Elanor
          <span>Mahalunge, Pune</span>
        </h1>

        <div class="hero-location-line">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"></path><circle cx="12" cy="10" r="3"></circle></svg>
          <span>Opposite Hinjawadi IT Hub, Baner-Mahalunge Smart City, Pune - 411045</span>
        </div>

        <p class="hero-description">
          Experience timeless French-inspired riverside living by Godrej Properties. Masterfully planned across <strong>8.5 acres</strong> with <strong>~5 acres of landscaped open greens</strong> and over <strong>1,00,000 sq. ft. of riverfront lifestyle amenities</strong>. Offering bespoke 3 &amp; 4 BHK residences with expansive running decks and scenic river views.
        </p>

        <!-- Key Project Highlights Badges Strip -->
        <div class="hero-key-stats-strip">
          <div class="hero-stat-block">
            <span class="hero-stat-val">8.5 Acres</span>
            <span class="hero-stat-lbl">Land Parcel</span>
          </div>
          <div class="hero-stat-block">
            <span class="hero-stat-val">B+G+3P+35</span>
            <span class="hero-stat-lbl">Tower Elevation</span>
          </div>
          <div class="hero-stat-block">
            <span class="hero-stat-val">1 Lakh Sq. Ft.</span>
            <span class="hero-stat-lbl">Riverfront Luxuries</span>
          </div>
          <div class="hero-stat-block" style="border-left: 2px solid var(--godrej-gold); padding-left: 0.75rem;">
            <span class="hero-stat-val" style="color: var(--godrej-gold-light);">₹ 1.89 Cr*</span>
            <span class="hero-stat-lbl">Starting Price Onwards</span>
          </div>
        </div>

        <!-- CTA Buttons -->
        <div class="hero-actions-group">
          <button type="button" class="btn btn-gold" data-open-modal="enquiryModal" data-prefill="Instant Cost Sheet">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
            <span>Download Brochure &amp; Price Sheet</span>
          </button>

          <button type="button" class="btn btn-outline-white" data-open-modal="siteVisitModal">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="4" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
            <span>Book Site Tour &amp; Cab</span>
          </button>

          <a href="https://wa.me/918459396466?text=Hi%2C%20I%20am%20interested%20in%20Godrej%20Elanor%20Mahalunge%20Pune.%20Please%20share%20the%20price%20sheet%20and%20project%20brochure." target="_blank" rel="noopener" class="btn btn-whatsapp" aria-label="Chat on WhatsApp">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
            <span>WhatsApp Enquiry</span>
          </a>
        </div>
      </div>

      <!-- Right Column: Instant High-Conversion Lead Capture Card -->
      <div class="hero-right-col">
        <div class="hero-lead-card">
          <div class="lead-card-header">
            <span class="lead-card-tag">OFFICIAL SALES DESK</span>
            <h2 class="lead-card-title">Get Instant Price Sheet &amp; Brochure</h2>
            <p class="lead-card-desc">Direct builder pricing, floor plans, and priority launch invitations.</p>
          </div>

          <form data-lead-form class="lead-card-form" id="heroLeadForm">
            <div class="form-group-clean">
              <label for="heroName" class="form-label-clean">Full Name *</label>
              <input type="text" id="heroName" name="name" class="form-input-clean" placeholder="Enter your full name" required autocomplete="name">
            </div>

            <div class="form-group-clean">
              <label for="heroPhone" class="form-label-clean">Mobile Number *</label>
              <div class="phone-input-wrap">
                <span class="phone-prefix-tag">+91</span>
                <input type="tel" id="heroPhone" name="phone" class="form-input-clean" placeholder="10-digit mobile number" required pattern="[0-9]{10}" maxlength="10" autocomplete="tel">
              </div>
            </div>

            <div class="form-group-clean">
              <label for="heroConfig" class="form-label-clean">Configuration Preferred</label>
              <select id="heroConfig" name="configuration" class="form-select-clean">
                <option value="3 BHK Premium (1270-1280 Sq. Ft.)">3 BHK Premium (1,270 – 1,280 Sq. Ft.) · ₹ 1.90 Cr*</option>
                <option value="3 BHK Luxe (1310 Sq. Ft.)" selected>3 BHK Luxe (1,310 Sq. Ft.) · ₹ 1.96 Cr*</option>
                <option value="4 BHK Duplex (Bespoke Area)">4 BHK Duplex Penthouse · Price On Request</option>
                <option value="General Enquiry">Need Configuration Guidance</option>
              </select>
            </div>

            <div class="form-checkbox-wrap" style="display: flex; align-items: flex-start; gap: 0.5rem; margin-bottom: 1.25rem;">
              <input type="checkbox" id="heroConsent" checked required style="margin-top: 3px; accent-color: var(--godrej-gold);">
              <label for="heroConsent" style="font-size: 0.75rem; color: var(--text-secondary); line-height: 1.4;">
                I authorize Godrej Properties &amp; authorized channel partner to contact me via Call/WhatsApp/SMS regarding project updates.
              </label>
            </div>

            <button type="submit" class="btn btn-gold btn-block" style="width: 100%; justify-content: center; padding: 0.85rem 1rem; font-size: 0.95rem; font-weight: 600;">
              <span>Unlock Pricing &amp; Download Brochure</span>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </button>

            <div class="lead-security-note">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="11" x="3" y="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
              <span>100% Privacy Protected · Zero Spam · Verified RERA: PR1260002602617</span>
            </div>
          </form>
        </div>
      </div>
    </div>
  </section>

  <!-- ==========================================================================
       SECTION 2: OVERVIEW SECTION (Exact Official Builder Copy & Sanction Data)
       ========================================================================== -->
  <section class="section-spacing overview-section-wrap" id="overview">
    <div class="container">
      <div class="overview-grid-layout">
        <!-- Text & Specs Column -->
        <div class="overview-text-col">
          <span class="section-eyebrow">PROJECT OVERVIEW</span>
          <h2 class="section-title">Overview of <em>Godrej Elanor</em></h2>
          <p class="section-subtitle" style="font-size: 1.05rem; font-weight: 500; color: var(--godrej-navy); line-height: 1.7; margin-bottom: 1rem;">
            Welcome to Godrej Elanor, where French-inspired elegance meets the promise of a thoughtfully curated lifestyle. Set within the expansive 119+ hectare (approx. 295+ Acres) Mahalunge Township in Pune, Godrej Elanor brings together the charm of refined living.
          </p>

          <p>
            With access to approximately <strong>8 hectares (approx. 20 Acres) of public greens</strong> and a vibrant <strong>Retail Street</strong> within the township, every day brings opportunities to experience more, connect more and live better.
          </p>
          <p>
            The project parcel itself spans <strong>8.5 acres</strong> with <strong>~5 acres of dedicated open spaces</strong> and an extraordinary <strong>1,00,000 sq. ft. riverfront promenade</strong>. Featuring 5 high-rise towers rising across 3 podium levels to 35 residential floors, low-density planning guarantees supreme privacy with only 8 residences per floor served by 7 high-speed passenger elevators.
          </p>

          <!-- Specifications Table -->
          <table class="overview-specs-table" aria-label="Godrej Elanor Project Specifications">
            <tbody>
              <tr>
                <td>Development Type</td>
                <td><strong>French-Inspired Luxury Riverside Residences</strong></td>
              </tr>
              <tr>
                <td>Total Land Parcel</td>
                <td><strong>8.5 Acres (within 295+ Acres Integrated Township)</strong></td>
              </tr>
              <tr>
                <td>Open &amp; Green Spaces</td>
                <td><strong>Approx. 5 Acres (~60% open to sky) + 20 Acres Public Greens</strong></td>
              </tr>
              <tr>
                <td>Building Elevation</td>
                <td><strong>Basement + Ground + 3 Podiums + 35 Residential Floors</strong></td>
              </tr>
              <tr>
                <td>Towers &amp; Phasing</td>
                <td><strong>5 Residential Towers (Phase 1 launch: 2 Towers)</strong></td>
              </tr>
              <tr>
                <td>Density &amp; Core</td>
                <td><strong>Low-density design with only 8 units/floor &amp; 7 high-speed lifts</strong></td>
              </tr>
              <tr>
                <td>Lifestyle Spaces</td>
                <td><strong>1 Lakh Sq. Ft. Riverfront Amenities + 30,000 Sq. Ft. Twin Clubhouses</strong></td>
              </tr>
              <tr>
                <td>MahaRERA Registration</td>
                <td><strong>PR1260002602617</strong> (Registered with MahaRERA Maharashtra)</td>
              </tr>
            </tbody>
          </table>

          <div style="margin-top: 1.75rem; display: flex; gap: 1rem; flex-wrap: wrap;">
            <button type="button" class="btn btn-navy" data-open-modal="enquiryModal" data-prefill="Project Factsheet">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
              <span>Download Project Factsheet</span>
            </button>
            <button type="button" class="btn btn-outline-navy" data-open-modal="siteVisitModal">
              <span>Book Guided Site Tour</span>
            </button>
          </div>
        </div>

        <!-- Visual / Image Column -->
        <div class="overview-visual-col">
          <div class="overview-image-box">
            <img src="assets/images/about/About.webp" alt="Godrej Elanor Mahalunge Masterplan Architecture" loading="lazy" width="600" height="520">
            <div class="overview-image-badge">
              <strong>8.5 Acres Riverside Sanctuary</strong>
              <span>5 Towers · B+G+3P+35 Floors · 1 Lakh Sq. Ft. Amenities</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ==========================================================================
       SECTION 3: FLOOR PLANS & CONFIGURATIONS (#floor-plans & #price)
       ========================================================================== -->
  <section class="section-spacing floor-plans-section" id="floor-plans">
    <div class="container">
      <div class="text-center" style="max-width: 780px; margin-inline: auto; margin-bottom: 2.5rem;">
        <span class="section-eyebrow">ARCHITECTURAL BLUEPRINTS &amp; INVENTORY</span>
        <h2 class="section-title">Master Layout &amp; <em>Floor Plans</em></h2>
        <p class="section-subtitle">
          Explore the master layout and high-definition floor plans. Every residence features thoughtful room zoning, dedicated foyers, and French running decks.
        </p>
      </div>

      <!-- Tab Switcher Navigation -->
      <div class="plan-tabs-row" role="tablist">
        <button type="button" class="plan-tab-button plan-pill-btn active" data-tab="tabMasterPlan" role="tab" aria-selected="true">
          Master Layout (8.5 Acres)
        </button>
        <button type="button" class="plan-tab-button plan-pill-btn" data-tab="tab3BhkPrem" role="tab" aria-selected="false">
          3 BHK Premium (1,270 – 1,280 Sq. Ft.)
        </button>
        <button type="button" class="plan-tab-button plan-pill-btn" data-tab="tab3BhkLuxe" role="tab" aria-selected="false">
          3 BHK Luxe (1,310 Sq. Ft.)
        </button>
        <button type="button" class="plan-tab-button plan-pill-btn" data-tab="tab4BhkDuplex" role="tab" aria-selected="false">
          4 BHK Duplex Penthouse
        </button>
      </div>

      <!-- Tab 1: Master Plan -->
      <div class="plan-tab-pane active" id="tabMasterPlan" style="display: block;">
        <div class="plan-display-card">
          <div class="plan-blueprint-box">
            <img src="assets/images/floor-plan/MasterPlan.webp" alt="Godrej Elanor Mahalunge 8.5 Acres Master Plan Layout" loading="lazy" width="800" height="500" data-lightbox-src="assets/images/floor-plan/MasterPlan.webp" data-title="Godrej Elanor Mahalunge - 8.5 Acres Master Layout">
            <span style="position: absolute; bottom: 1rem; left: 1rem; background: rgba(11, 37, 69, 0.85); color: #FFFFFF; font-size: 0.75rem; padding: 0.35rem 0.75rem; border-radius: 2px;">
              Click image to enlarge blueprint
            </span>
          </div>
          <div class="plan-info-box">
            <span class="section-eyebrow" style="margin-bottom: 0.5rem;">GATED COMMUNITY LAYOUT</span>
            <h3 style="font-family: var(--font-heading); font-size: 1.5rem; color: var(--godrej-navy); margin-bottom: 0.75rem;">
              8.5 Acres Riverfront Master Plan
            </h3>
            <p style="font-size: 0.875rem; color: var(--text-secondary); line-height: 1.6; margin-bottom: 1.5rem;">
              The master plan integrates 5 residential towers rising along the pristine riverbank with dedicated pedestrian pathways, central vehicle-free podiums, 2 twin clubhouses, and approx. 5 acres of open green sanctuary.
            </p>

            <div class="pricing-spec-list" style="margin-bottom: 1.75rem;">
              <div class="pricing-spec-row">
                <span>Access Corridors</span>
                <strong>36m DP Main Road &amp; 15m Internal Road</strong>
              </div>
              <div class="pricing-spec-row">
                <span>Vehicle-Free Podiums</span>
                <strong>3 Dedicated Levels of Secure Parking</strong>
              </div>
              <div class="pricing-spec-row">
                <span>Riverfront Frontage</span>
                <strong>1,00,000 Sq. Ft. Continuous Promenade</strong>
              </div>
              <div class="pricing-spec-row">
                <span>Central Green Spines</span>
                <strong>~5 Acres of Lush Landscaped Gardens</strong>
              </div>
            </div>

            <button type="button" class="btn btn-navy" data-open-modal="enquiryModal" data-prefill="Master Plan High-Res PDF">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
              <span>Download Master Plan PDF</span>
            </button>
          </div>
        </div>
      </div>

      <!-- Tab 2: 3 BHK Premium -->
      <div class="plan-tab-pane" id="tab3BhkPrem" style="display: none;">
        <div class="plan-display-card">
          <div class="plan-blueprint-box">
            <img src="assets/images/floor-plan/UnitPlan.webp" alt="Godrej Elanor 3 BHK Premium Floor Plan Unit Layout" loading="lazy" width="800" height="500" data-lightbox-src="assets/images/floor-plan/UnitPlan.webp" data-title="Godrej Elanor - 3 BHK Premium Floor Plan (1,270 - 1,280 Sq. Ft.)">
            <span style="position: absolute; bottom: 1rem; left: 1rem; background: rgba(11, 37, 69, 0.85); color: #FFFFFF; font-size: 0.75rem; padding: 0.35rem 0.75rem; border-radius: 2px;">
              Click image to enlarge blueprint
            </span>
          </div>
          <div class="plan-info-box">
            <span class="section-eyebrow" style="margin-bottom: 0.5rem;">UNIT BLUEPRINT</span>
            <h3 style="font-family: var(--font-heading); font-size: 1.5rem; color: var(--godrej-navy); margin-bottom: 0.75rem;">
              3 BHK Premium (1,270 – 1,280 Sq. Ft.)
            </h3>
            <p style="font-size: 0.875rem; color: var(--text-secondary); line-height: 1.6; margin-bottom: 1.5rem;">
              Thoughtfully optimized floor design featuring a formal entrance foyer, grand dining area, separate dry balcony for utilities, and large French sliding windows connecting the living hall to the river deck.
            </p>

            <div class="pricing-spec-list" style="margin-bottom: 1.75rem;">
              <div class="pricing-spec-row">
                <span>Carpet Area</span>
                <strong>1,270 to 1,280 Sq. Ft.</strong>
              </div>
              <div class="pricing-spec-row">
                <span>Living &amp; Dining Hall</span>
                <strong>Spacious 22 ft × 12 ft Salon</strong>
              </div>
              <div class="pricing-spec-row">
                <span>Master Bedroom</span>
                <strong>14 ft × 12 ft with En-Suite Bath</strong>
              </div>
              <div class="pricing-spec-row">
                <span>Deck Dimension</span>
                <strong>6 ft Wide Running Riverfront Balcony</strong>
              </div>
            </div>

            <button type="button" class="btn btn-gold" data-open-modal="enquiryModal" data-prefill="3 BHK Premium Floor Plan PDF">
              <span>Request Detailed Dimensions PDF</span>
            </button>
          </div>
        </div>
      </div>

      <!-- Tab 3: 3 BHK Luxe -->
      <div class="plan-tab-pane" id="tab3BhkLuxe" style="display: none;">
        <div class="plan-display-card">
          <div class="plan-blueprint-box">
            <img src="assets/images/floor-plan/UnitPlan.webp" alt="Godrej Elanor 3 BHK Luxe Floor Plan Unit Layout" loading="lazy" width="800" height="500" data-lightbox-src="assets/images/floor-plan/UnitPlan.webp" data-title="Godrej Elanor - 3 BHK Luxe Floor Plan (1,310 Sq. Ft.)">
            <span style="position: absolute; bottom: 1rem; left: 1rem; background: rgba(11, 37, 69, 0.85); color: #FFFFFF; font-size: 0.75rem; padding: 0.35rem 0.75rem; border-radius: 2px;">
              Click image to enlarge blueprint
            </span>
          </div>
          <div class="plan-info-box">
            <span class="section-eyebrow" style="margin-bottom: 0.5rem;">PREMIUM RIVERFRONT UNIT</span>
            <h3 style="font-family: var(--font-heading); font-size: 1.5rem; color: var(--godrej-navy); margin-bottom: 0.75rem;">
              3 BHK Luxe (1,310 Sq. Ft.)
            </h3>
            <p style="font-size: 0.875rem; color: var(--text-secondary); line-height: 1.6; margin-bottom: 1.5rem;">
              The signature configuration offering direct front-row river views. Boasts dual balconies including an exclusive private deck attached to the master suite, walk-in closet space, and premium bathroom specifications.
            </p>

            <div class="pricing-spec-list" style="margin-bottom: 1.75rem;">
              <div class="pricing-spec-row">
                <span>Carpet Area</span>
                <strong>1,310 Sq. Ft.</strong>
              </div>
              <div class="pricing-spec-row">
                <span>Master Suite</span>
                <strong>Luxury Suite + Private Deck + Wardrobe Niche</strong>
              </div>
              <div class="pricing-spec-row">
                <span>Kitchen Layout</span>
                <strong>L-Shaped Granite Platform + Utility Store</strong>
              </div>
              <div class="pricing-spec-row">
                <span>Balconies</span>
                <strong>2 Private Balconies with Glass Railings</strong>
              </div>
            </div>

            <button type="button" class="btn btn-gold" data-open-modal="enquiryModal" data-prefill="3 BHK Luxe Floor Plan PDF">
              <span>Request Detailed Dimensions PDF</span>
            </button>
          </div>
        </div>
      </div>

      <!-- Tab 4: 4 BHK Duplex Penthouse -->
      <div class="plan-tab-pane" id="tab4BhkDuplex" style="display: none;">
        <div class="plan-display-card">
          <div class="plan-blueprint-box">
            <img src="assets/images/godrej-cdn/overview-hero.webp" alt="Godrej Elanor 4 BHK Duplex Penthouse Sky Residence" loading="lazy" width="800" height="500" data-lightbox-src="assets/images/godrej-cdn/overview-hero.webp" data-title="Godrej Elanor - 4 BHK Duplex Sky Residence">
            <span style="position: absolute; bottom: 1rem; left: 1rem; background: rgba(11, 37, 69, 0.85); color: #FFFFFF; font-size: 0.75rem; padding: 0.35rem 0.75rem; border-radius: 2px;">
              Click image to enlarge
            </span>
          </div>
          <div class="plan-info-box">
            <span class="section-eyebrow" style="margin-bottom: 0.5rem;">PENTHOUSE COLLECTION</span>
            <h3 style="font-family: var(--font-heading); font-size: 1.5rem; color: var(--godrej-navy); margin-bottom: 0.75rem;">
              4 BHK Duplex Penthouse Residences
            </h3>
            <p style="font-size: 0.875rem; color: var(--text-secondary); line-height: 1.6; margin-bottom: 1.5rem;">
              Crowning the top 4 floors (Floors 32 to 35) of Godrej Elanor. These expansive duplex penthouses feature soaring double-height living ceilings, private sky lounges, domestic staff quarters, and 270-degree skyline views.
            </p>

            <div class="pricing-spec-list" style="margin-bottom: 1.75rem;">
              <div class="pricing-spec-row">
                <span>Configuration</span>
                <strong>4 BHK Double-Height Duplex</strong>
              </div>
              <div class="pricing-spec-row">
                <span>Levels</span>
                <strong>Lower &amp; Upper Duplex Floors (32 to 35)</strong>
              </div>
              <div class="pricing-spec-row">
                <span>Special Features</span>
                <strong>Internal Designer Staircase &amp; Sky Lounge</strong>
              </div>
              <div class="pricing-spec-row">
                <span>Allotment Mode</span>
                <strong>Personalized Presentation by Invitation</strong>
              </div>
            </div>

            <button type="button" class="btn btn-navy" data-open-modal="enquiryModal" data-prefill="4 BHK Duplex VIP Floor Plan">
              <span>Request Private VIP Presentation</span>
            </button>
          </div>
        </div>
      </div>

      <!-- Pricing Cards 3-Column Grid (#price) -->
      <div id="price" style="margin-top: 4.5rem; padding-top: 2rem;">
        <div class="text-center" style="max-width: 780px; margin-inline: auto; margin-bottom: 2.5rem;">
          <span class="section-eyebrow">VERIFIED BUILDER PRICING &amp; INVENTORY</span>
          <h2 class="section-title">Configurations &amp; <em>Pricing Sheet</em></h2>
          <p class="section-subtitle">
            Direct builder pre-launch prices for Godrej Elanor Mahalunge. Priority allotment active with ₹ 1 Lakh* EOI token.
          </p>
        </div>

        <div class="pricing-cards-grid">
          <!-- Card 1: 3 BHK Premium -->
          <div class="pricing-unit-card">
            <div class="pricing-card-top">
              <span class="pricing-unit-tagline">SMART LUXURY RESIDENCE</span>
              <h3 class="pricing-unit-name">3 BHK Premium</h3>
            </div>
            <div class="pricing-figure-box">
              <span class="pricing-figure-val"><span style="color: var(--godrej-gold-dark); font-weight: 600; margin-right: 3px;">₹</span>1.90 – 2.03 Cr*</span>
              <span class="pricing-figure-note">All Inclusive · Exclusive Pre-Launch Price</span>
            </div>
            <div class="pricing-card-details">
              <div class="pricing-spec-list">
                <div class="pricing-spec-row">
                  <span>RERA Carpet Area</span>
                  <strong>1,270 – 1,280 Sq. Ft.</strong>
                </div>
                <div class="pricing-spec-row">
                  <span>Balcony / Outdoor</span>
                  <strong>Expansive Running Deck</strong>
                </div>
                <div class="pricing-spec-row">
                  <span>Floor Level</span>
                  <strong>Floors 4 to 30</strong>
                </div>
                <div class="pricing-spec-row">
                  <span>Ventilation</span>
                  <strong>3-Side Open French Windows</strong>
                </div>
                <div class="pricing-spec-row">
                  <span>EOI Booking Amount</span>
                  <strong style="color: var(--godrej-gold-dark);">₹ 1,00,000* Only</strong>
                </div>
              </div>

              <div>
                <button type="button" class="btn btn-navy btn-block" style="width: 100%; justify-content: center;" data-open-modal="enquiryModal" data-prefill="3 BHK Premium (1270-1280 Sq. Ft.)">
                  <span>Request Cost Sheet &amp; Floor Plan</span>
                </button>
              </div>
            </div>
          </div>

          <!-- Card 2: 3 BHK Luxe (Featured) -->
          <div class="pricing-unit-card featured-card">
            <div class="pricing-badge-ribbon">MOST POPULAR CHOICE</div>
            <div class="pricing-card-top">
              <span class="pricing-unit-tagline">PANORAMIC RIVERFRONT FACING</span>
              <h3 class="pricing-unit-name">3 BHK Luxe</h3>
            </div>
            <div class="pricing-figure-box">
              <span class="pricing-figure-val"><span style="color: var(--godrej-gold-dark); font-weight: 600; margin-right: 3px;">₹</span>1.96 – 2.09 Cr*</span>
              <span class="pricing-figure-note">All Inclusive · Direct River Views</span>
            </div>
            <div class="pricing-card-details">
              <div class="pricing-spec-list">
                <div class="pricing-spec-row">
                  <span>RERA Carpet Area</span>
                  <strong>1,310 Sq. Ft.</strong>
                </div>
                <div class="pricing-spec-row">
                  <span>Balcony / Outdoor</span>
                  <strong>Dual Panoramic Balconies</strong>
                </div>
                <div class="pricing-spec-row">
                  <span>Master Suite</span>
                  <strong>King Suite with Walk-In Dresser</strong>
                </div>
                <div class="pricing-spec-row">
                  <span>View Guarantee</span>
                  <strong>Unobstructed River &amp; Garden View</strong>
                </div>
                <div class="pricing-spec-row">
                  <span>EOI Booking Amount</span>
                  <strong style="color: var(--godrej-gold-dark);">₹ 1,00,000* Only</strong>
                </div>
              </div>

              <div>
                <button type="button" class="btn btn-gold btn-block" style="width: 100%; justify-content: center;" data-open-modal="enquiryModal" data-prefill="3 BHK Luxe (1310 Sq. Ft.)">
                  <span>Unlock Special Launch Offer</span>
                </button>
              </div>
            </div>
          </div>

          <!-- Card 3: 4 BHK Duplex Penthouse -->
          <div class="pricing-unit-card">
            <div class="pricing-card-top">
              <span class="pricing-unit-tagline">CROWNING FLOORS 32 TO 35</span>
              <h3 class="pricing-unit-name">4 BHK Duplex</h3>
            </div>
            <div class="pricing-figure-box">
              <span class="pricing-figure-val">Price On Request*</span>
              <span class="pricing-figure-note">Ultra-Luxury Penthouse Inventory</span>
            </div>
            <div class="pricing-card-details">
              <div class="pricing-spec-list">
                <div class="pricing-spec-row">
                  <span>RERA Carpet Area</span>
                  <strong>Bespoke Duplex Layout</strong>
                </div>
                <div class="pricing-spec-row">
                  <span>Living Room</span>
                  <strong>Double-Height Grand Salon</strong>
                </div>
                <div class="pricing-spec-row">
                  <span>Terrace Deck</span>
                  <strong>Private Sky Deck &amp; Lounge</strong>
                </div>
                <div class="pricing-spec-row">
                  <span>Exclusivity</span>
                  <strong>Limited to Top 4 Floors Only</strong>
                </div>
                <div class="pricing-spec-row">
                  <span>Allotment Mode</span>
                  <strong style="color: var(--godrej-gold-dark);">By Private Invitation Only</strong>
                </div>
              </div>

              <div>
                <button type="button" class="btn btn-navy btn-block" style="width: 100%; justify-content: center;" data-open-modal="enquiryModal" data-prefill="4 BHK Duplex (Bespoke Area)">
                  <span>Inquire for Duplex Penthouse</span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ==========================================================================
       SECTION 4: AMENITIES SHOWCASE
       ========================================================================== -->
  <section class="section-spacing amenities-section-wrap" id="amenities">
    <div class="container">
      <div class="text-center" style="max-width: 780px; margin-inline: auto; margin-bottom: 3.5rem;">
        <span class="section-eyebrow">WORLD-CLASS RECREATION</span>
        <h2 class="section-title">Over 1,00,000 Sq. Ft. of <em>Riverfront &amp; Clubhouse Luxuries</em></h2>
        <p class="section-subtitle">
          Indulge in a holistic lifestyle curated for health, leisure, and family recreation across twin designer clubhouses and riverside nature trails.
        </p>
      </div>

      <!-- Amenities Grid (6 Clean Cards) -->
      <div class="amenities-grid-clean">
        <!-- Amenity 1: Riverfront Promenade -->
        <div class="amenity-card-clean">
          <div class="amenity-image-holder">
            <img src="assets/images/amenities/riverfront-promenade.webp" alt="Godrej Elanor 1 Lakh Sq Ft Riverfront Promenade and Boardwalk" loading="lazy" width="400" height="260">
          </div>
          <div class="amenity-card-body">
            <h3 class="amenity-card-title">1 Lakh Sq. Ft. Riverfront Promenade</h3>
            <p class="amenity-card-desc">
              A serene waterfront walking trail lined with native flora, shaded pavilions, yoga pavilions, and uninterrupted sunset river views.
            </p>
          </div>
        </div>

        <!-- Amenity 2: Twin Clubhouses -->
        <div class="amenity-card-clean">
          <div class="amenity-image-holder">
            <img src="assets/images/amenities/clubhouse.webp" alt="Godrej Elanor 30,000 Sq Ft Twin Designer Clubhouses" loading="lazy" width="400" height="260">
          </div>
          <div class="amenity-card-body">
            <h3 class="amenity-card-title">Twin Clubhouses (30,000 Sq. Ft.)</h3>
            <p class="amenity-card-desc">
              Two grand clubhouses (18,000 &amp; 12,000 sq. ft.) featuring French salons, banquet halls, library lounge, and indoor games facilities.
            </p>
          </div>
        </div>

        <!-- Amenity 3: Infinity Pool -->
        <div class="amenity-card-clean">
          <div class="amenity-image-holder">
            <img src="assets/images/amenities/infinity-pool.webp" alt="Godrej Elanor Infinity Edge Swimming Pool with Sun Deck" loading="lazy" width="400" height="260">
          </div>
          <div class="amenity-card-body">
            <h3 class="amenity-card-title">Infinity-Edge Swimming Pool</h3>
            <p class="amenity-card-desc">
              Semi-Olympic temperature-controlled infinity pool overlooking the river, accompanied by a kids' splash pool and poolside cabanas.
            </p>
          </div>
        </div>

        <!-- Amenity 4: Gym & Crossfit -->
        <div class="amenity-card-clean">
          <div class="amenity-image-holder">
            <img src="assets/images/amenities/gym.webp" alt="Godrej Elanor World Class Fitness Center and Crossfit Arena" loading="lazy" width="400" height="260">
          </div>
          <div class="amenity-card-body">
            <h3 class="amenity-card-title">High-Tech Gymnasium &amp; CrossFit</h3>
            <p class="amenity-card-desc">
              Fully equipped fitness centre with imported cardio and strength equipment, personal training zones, and pilates studio.
            </p>
          </div>
        </div>

        <!-- Amenity 5: Badminton Court -->
        <div class="amenity-card-clean">
          <div class="amenity-image-holder">
            <img src="assets/images/amenities/badminton-court.webp" alt="Godrej Elanor Professional Wooden Badminton Court" loading="lazy" width="400" height="260">
          </div>
          <div class="amenity-card-body">
            <h3 class="amenity-card-title">Indoor Badminton Court</h3>
            <p class="amenity-card-desc">
              Championship-standard indoor wooden-floored badminton courts designed with tournament-grade lighting and spectator seating.
            </p>
          </div>
        </div>

        <!-- Amenity 6: Squash Court -->
        <div class="amenity-card-clean">
          <div class="amenity-image-holder">
            <img src="assets/images/amenities/squash-court.webp" alt="Godrej Elanor Glass Back Squash Court Arena" loading="lazy" width="400" height="260">
          </div>
          <div class="amenity-card-body">
            <h3 class="amenity-card-title">Glass-Back Squash Court</h3>
            <p class="amenity-card-desc">
              Air-conditioned glass-back squash court providing an intense racquet workout for residents of all ages and skill levels.
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ==========================================================================
       SECTION 5: ARCHITECTURAL GALLERY (100% Matching Official Godrej Portal)
       Reference: https://www.godrejproperties.com/pune/residential/godrej-elanor/gallery
       Asymmetric 6-Column Grid (.parent-div & .children-dev) + Interactive Lightbox
       ========================================================================== -->
  <section class="gallery-section-wrap" id="gallery">
    <div class="container">
      <!-- Official Header with Elegant Double Gradient Separator Lines -->
      <div class="gallery-intro-heading">
        <div class="line before"></div>
        <h2>Gallery</h2>
        <div class="line after"></div>
      </div>

      <p class="text-center section-subtitle mx-auto" style="margin-bottom: 2.5rem;">
        Take an immersive visual tour through Godrej Elanor's show residences, elegant living salons, master bedroom suites, and riverfront decks.
      </p>

      <!-- Exact Official Godrej Asymmetric 6-Column Gallery Grid -->
      <div class="parent-div">
        <!-- div-1: Large Hero Visual (Col 1 to 4, Row 1 to 2) -->
        <div class="children-dev div-1" data-lightbox-src="assets/images/gallery/living-room.webp" data-title="Grand Living & Dining Salon - French Decks">
          <img src="assets/images/gallery/living-room.webp" alt="Godrej Elanor Grand Living Salon with French Balcony Decks" loading="lazy" width="1200" height="700">
          <div class="image-caption">
            <span>Grand Living &amp; Dining Salon</span>
          </div>
        </div>

        <!-- div-2: Tall Riverfront Deck (Col 5 to 6, Row 1 to 2) -->
        <div class="children-dev div-2" data-lightbox-src="assets/images/gallery/deck.webp" data-title="Riverfront Running Balcony Deck - Panoramic Views">
          <img src="assets/images/gallery/deck.webp" alt="Godrej Elanor Riverfront Running Balcony Deck" loading="lazy" width="600" height="700">
          <div class="image-caption">
            <span>Riverfront Running Deck</span>
          </div>
        </div>

        <!-- div-3: Master Bedroom Suite (Col 1 to 2, Row 3 to 4) -->
        <div class="children-dev div-3" data-lightbox-src="assets/images/gallery/bedroom.webp" data-title="Master Bedroom Suite with En-Suite Deck">
          <img src="assets/images/gallery/bedroom.webp" alt="Godrej Elanor Master Bedroom Suite" loading="lazy" width="600" height="600">
          <div class="image-caption">
            <span>Master Bedroom Suite</span>
          </div>
        </div>

        <!-- div-4: Gourmet Modular Kitchen (Col 3 to 4, Row 3) -->
        <div class="children-dev div-4" data-lightbox-src="assets/images/gallery/kitchen.webp" data-title="Gourmet Modular Kitchen with Utility">
          <img src="assets/images/gallery/kitchen.webp" alt="Godrej Elanor Modular Kitchen" loading="lazy" width="600" height="300">
          <div class="image-caption">
            <span>Gourmet Modular Kitchen</span>
          </div>
        </div>

        <!-- div-5: Designer Bathroom (Col 3 to 4, Row 4) -->
        <div class="children-dev div-5" data-lightbox-src="assets/images/gallery/bathroom.webp" data-title="European Restroom with Glass Partitions">
          <img src="assets/images/gallery/bathroom.webp" alt="Godrej Elanor European Designer Bathroom" loading="lazy" width="600" height="300">
          <div class="image-caption">
            <span>European Restrooms</span>
          </div>
        </div>

        <!-- div-6: Family Lounge & Living 2 (Col 5 to 6, Row 3 to 4) -->
        <div class="children-dev div-6" data-lightbox-src="assets/images/gallery/living-room-2.webp" data-title="Family Entertainment Lounge">
          <img src="assets/images/gallery/living-room-2.webp" alt="Godrej Elanor Family Entertainment Lounge" loading="lazy" width="600" height="600">
          <div class="image-caption">
            <span>Family Entertainment Lounge</span>
          </div>
        </div>
      </div>

      <!-- Gallery CTA -->
      <div class="text-center" style="margin-top: 2.5rem;">
        <button type="button" class="btn btn-navy" data-open-modal="enquiryModal" data-prefill="Complete 24-Image Gallery Portfolio">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect><circle cx="9" cy="9" r="2"></circle><path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path></svg>
          <span>Request High-Definition Gallery Lookbook (PDF)</span>
        </button>
      </div>
    </div>
  </section>

  <!-- ==========================================================================
       SECTION 6: LOCATION & STRATEGIC CONNECTIVITY
       ========================================================================== -->
  <section class="section-spacing location-section-wrap" id="location">
    <div class="container">
      <div class="text-center" style="max-width: 780px; margin-inline: auto; margin-bottom: 3.5rem;">
        <span class="section-eyebrow">STRATEGIC MAHALUNGE IT HUB</span>
        <h2 class="section-title">Location &amp; <em>Neighborhood Connectivity</em></h2>
        <p class="section-subtitle">
          Situated on the Hinjawadi-Baner growth corridor, Godrej Elanor offers unmatched commute times to Pune's leading IT parks, international schools, hospitals, and highways.
        </p>
      </div>

      <!-- Location Grid -->
      <div class="location-layout-grid">
        <!-- Commute Times Table (Verified from Godrej Data) -->
        <div class="connectivity-table-wrap">
          <h3 style="font-family: var(--font-heading); font-size: 1.35rem; color: var(--godrej-navy); margin-bottom: 1.25rem;">
            Nearby Landmarks &amp; Travel Times
          </h3>

          <table class="connectivity-table-clean" aria-label="Distance from Key Pune Landmarks">
            <tbody>
              <tr>
                <td>
                  <div class="conn-hub-name">Hinjawadi IT Park (Phase 1)</div>
                  <div class="conn-hub-category">TCS, Infosys, Wipro, Cognizant Tech Hub</div>
                </td>
                <td><span class="conn-hub-time">9 Mins</span></td>
              </tr>
              <tr>
                <td>
                  <div class="conn-hub-name">Mumbai - Bangalore Highway (NH 48)</div>
                  <div class="conn-hub-category">Direct arterial gateway to Mumbai &amp; Western Pune</div>
                </td>
                <td><span class="conn-hub-time">12 Mins</span></td>
              </tr>
              <tr>
                <td>
                  <div class="conn-hub-name">Balewadi Metro Station</div>
                  <div class="conn-hub-category">Pune Metro Line 3 (Hinjawadi - Shivajinagar)</div>
                </td>
                <td><span class="conn-hub-time">14 Mins</span></td>
              </tr>
              <tr>
                <td>
                  <div class="conn-hub-name">Ruby Hall Clinic Hinjawadi</div>
                  <div class="conn-hub-category">Multi-speciality tertiary healthcare hospital</div>
                </td>
                <td><span class="conn-hub-time">11 Mins</span></td>
              </tr>
              <tr>
                <td>
                  <div class="conn-hub-name">Mahindra International School</div>
                  <div class="conn-hub-category">Acclaimed world-class educational institution</div>
                </td>
                <td><span class="conn-hub-time">14 Mins</span></td>
              </tr>
              <tr>
                <td>
                  <div class="conn-hub-name">Chandani Chowk / Pune - Paud Road</div>
                  <div class="conn-hub-category">Key junction connecting Kothrud and Bavdhan</div>
                </td>
                <td><span class="conn-hub-time">18 Mins</span></td>
              </tr>
              <tr>
                <td>
                  <div class="conn-hub-name">Pune International Airport</div>
                  <div class="conn-hub-category">Direct transit via NH 48 Ring Road bypass</div>
                </td>
                <td><span class="conn-hub-time">35 Mins</span></td>
              </tr>
            </tbody>
          </table>

          <div style="margin-top: 1.5rem;">
            <a href="https://maps.app.goo.gl/g3ppuziWzUjwYWQX6" target="_blank" rel="noopener" class="btn btn-navy" style="font-size: 0.85rem;">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="3 11 22 2 13 21 11 13 3 11"></polygon></svg>
              <span>View On Google Maps</span>
            </a>
          </div>
        </div>

        <!-- Embedded Interactive Map -->
        <div class="location-map-clean-frame">
          <iframe 
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d15128.913508605273!2d73.74313271738283!3d18.563721300000004!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc2bc21a4f0bb03%3A0xe54e6ff1b312384a!2sMahalunge%2C%20Pune%2C%20Maharashtra!5e0!3m2!1sen!2sin!4v1700000000000!5m2!1sen!2sin" 
            width="100%" 
            height="100%" 
            style="border:0;" 
            allowfullscreen="" 
            loading="lazy" 
            referrerpolicy="no-referrer-when-downgrade" 
            title="Godrej Elanor Mahalunge Location Map">
          </iframe>
        </div>
      </div>
    </div>
  </section>

  <!-- ==========================================================================
       SECTION 7: FREQUENTLY ASKED QUESTIONS (Accordion)
       ========================================================================== -->
  <section class="section-spacing faq-section-clean" id="faqs">
    <div class="container">
      <div class="text-center" style="max-width: 780px; margin-inline: auto; margin-bottom: 3rem;">
        <span class="section-eyebrow">CLEAR TRANSPARENCY</span>
        <h2 class="section-title">Frequently Asked <em>Questions</em></h2>
        <p class="section-subtitle">
          Verified answers regarding MahaRERA registration, pricing, unit sizes, booking process, and site visits.
        </p>
      </div>

      <!-- FAQ Accordion List -->
      <div class="faq-list-clean" style="max-width: 860px; margin-inline: auto;">
        <!-- Question 1 -->
        <div class="faq-card-clean faq-item-editorial active">
          <button type="button" class="faq-btn-trigger faq-trigger-editorial" aria-expanded="true">
            <span>What is the MahaRERA registration number for Godrej Elanor?</span>
            <span class="faq-icon-symbol" aria-hidden="true">+</span>
          </button>
          <div class="faq-body-collapse faq-answer-editorial">
            <div class="faq-body-inner">
              Godrej Elanor Mahalunge is an officially registered residential project under MahaRERA with registration number <strong>PR1260002602617</strong>. The authorized channel partner registration number is <strong>A52100040088</strong>. All project details, approvals, and verified sanction plans can be reviewed on the official MahaRERA website (<a href="https://maharera.mahaonline.gov.in" target="_blank" rel="noopener" style="text-decoration: underline; color: var(--godrej-navy);">maharera.mahaonline.gov.in</a>).
            </div>
          </div>
        </div>

        <!-- Question 2 -->
        <div class="faq-card-clean faq-item-editorial">
          <button type="button" class="faq-btn-trigger faq-trigger-editorial" aria-expanded="false">
            <span>What configurations and carpet areas are available?</span>
            <span class="faq-icon-symbol" aria-hidden="true">+</span>
          </button>
          <div class="faq-body-collapse faq-answer-editorial">
            <div class="faq-body-inner">
              Godrej Elanor offers ultra-spacious 3 BHK and 4 BHK residences:
              <ul style="margin-top: 0.5rem; margin-left: 1.25rem;">
                <li><strong>3 BHK Premium:</strong> 1,270 to 1,280 Sq. Ft. RERA Carpet Area.</li>
                <li><strong>3 BHK Luxe:</strong> 1,310 Sq. Ft. RERA Carpet Area (Riverfront Facing).</li>
                <li><strong>4 BHK Duplex Penthouses:</strong> Bespoke layouts on the crowning top 4 floors (Floors 32 to 35).</li>
              </ul>
            </div>
          </div>
        </div>

        <!-- Question 3 -->
        <div class="faq-card-clean faq-item-editorial">
          <button type="button" class="faq-btn-trigger faq-trigger-editorial" aria-expanded="false">
            <span>What is the starting price and EOI amount?</span>
            <span class="faq-icon-symbol" aria-hidden="true">+</span>
          </button>
          <div class="faq-body-collapse faq-answer-editorial">
            <div class="faq-body-inner">
              Pre-launch prices start from <strong>₹ 1.89 Cr* / ₹ 1.90 Cr* (All Inclusive)</strong> for 3 BHK Premium residences, and <strong>₹ 1.96 Cr* (All Inclusive)</strong> for 3 BHK Luxe riverfront residences. The Expression of Interest (EOI) window is active with an initial booking token of <strong>₹ 1,00,000*</strong>, which grants priority inventory selection.
            </div>
          </div>
        </div>

        <!-- Question 4 -->
        <div class="faq-card-clean faq-item-editorial">
          <button type="button" class="faq-btn-trigger faq-trigger-editorial" aria-expanded="false">
            <span>What amenities are included in the development?</span>
            <span class="faq-icon-symbol" aria-hidden="true">+</span>
          </button>
          <div class="faq-body-collapse faq-answer-editorial">
            <div class="faq-body-inner">
              Residents enjoy over <strong>1,00,000 sq. ft. of riverfront recreation</strong> and <strong>30,000 sq. ft. of twin clubhouses</strong>. Key facilities include an infinity-edge swimming pool, riverfront promenade, badminton and squash courts, gymnasium &amp; crossfit studio, banquet hall, landscaped reflexology paths, yoga deck, and children’s play parks.
            </div>
          </div>
        </div>

        <!-- Question 5 -->
        <div class="faq-card-clean faq-item-editorial">
          <button type="button" class="faq-btn-trigger faq-trigger-editorial" aria-expanded="false">
            <span>Are home loans pre-approved for this project?</span>
            <span class="faq-icon-symbol" aria-hidden="true">+</span>
          </button>
          <div class="faq-body-collapse faq-answer-editorial">
            <div class="faq-body-inner">
              Yes, Godrej Elanor is pre-approved by all leading nationalized and private financial institutions including State Bank of India (SBI), HDFC Bank, ICICI Bank, Axis Bank, and Bank of Baroda. Special low-interest rates and doorstep loan processing are available.
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ==========================================================================
       SECTION 8: SITE FOOTER & MAHARERA TRANSPARENCY
       ========================================================================== -->
  <footer class="site-footer-clean">
    <div class="container">
      <div class="footer-columns-grid">
        <!-- Col 1: Brand Info -->
        <div>
          <div style="font-family: var(--font-heading); font-size: 1.35rem; color: #FFFFFF; font-weight: 700; margin-bottom: 0.35rem;">
            GODREJ ELANOR
          </div>
          <div style="font-size: 0.75rem; letter-spacing: 0.1em; color: var(--godrej-gold); text-transform: uppercase; margin-bottom: 1rem;">
            Mahalunge, Pune · By Godrej Properties
          </div>
          <p style="font-size: 0.8125rem; line-height: 1.6; color: #94A3B8; margin-bottom: 1.25rem;">
            A premier 8.5-acre riverside residential landmark in Mahalunge, Pune. Masterfully crafted with European architecture, 1 Lakh sq. ft. riverfront recreation, and twin clubhouses.
          </p>
          <div style="font-size: 0.8125rem; color: #CBD5E1;">
            <div><strong>Marketing Office:</strong> Godrej Experience Galleria, Hinjawadi, Pune - 411057</div>
            <div style="margin-top: 0.35rem;"><strong>Site Address:</strong> Godrej Elanor, Riverfront Road, Mahalunge, Pune - 411045</div>
            <div style="margin-top: 0.35rem;"><strong>Sales Desk:</strong> <a href="tel:+918459396466" style="color: #FFFFFF; font-weight: 600;">+91 84593 96466</a></div>
            <div style="margin-top: 0.35rem;"><strong>Official Email:</strong> <a href="mailto:enquiryinfinitee@gmail.com" style="color: #FFFFFF;">enquiryinfinitee@gmail.com</a></div>
          </div>
        </div>

        <!-- Col 2: Navigation Links -->
        <div>
          <h4 class="footer-col-head">Project Sections</h4>
          <div class="footer-links-col">
            <a href="#hero">Home Banner</a>
            <a href="#overview">Project Overview</a>
            <a href="#floor-plans">Floor Plans &amp; Blueprints</a>
            <a href="#price">Configurations &amp; Pricing</a>
            <a href="#amenities">Riverfront Amenities</a>
            <a href="#gallery">Photo Gallery</a>
            <a href="#location">Location &amp; Commute</a>
            <a href="#faqs">Project FAQs</a>
          </div>
        </div>

        <!-- Col 3: Residences -->
        <div>
          <h4 class="footer-col-head">Configurations</h4>
          <div class="footer-links-col">
            <a href="#price">3 BHK Premium (1,270 – 1,280 Sq. Ft.)</a>
            <a href="#price">3 BHK Luxe (1,310 Sq. Ft.)</a>
            <a href="#price">4 BHK Duplex Penthouse (Floors 32 – 35)</a>
            <a href="#" data-open-modal="enquiryModal" data-prefill="Brochure Download">Download Official Brochure</a>
            <a href="#" data-open-modal="siteVisitModal">Book Chauffeur Cab Pickup</a>
          </div>
        </div>

        <!-- Col 4: MahaRERA QR & Official Transparency -->
        <div>
          <h4 class="footer-col-head">MahaRERA Registration</h4>
          <div class="footer-rera-box-clean">
            <img src="assets/images/qr-code/6aeaebed56bba-PR1260002602617.png" alt="MahaRERA QR Code PR1260002602617" class="footer-rera-qr" width="64" height="64">
            <div style="font-size: 0.775rem; line-height: 1.5;">
              <div>Project MahaRERA:</div>
              <strong style="color: #FFFFFF; font-size: 0.85rem;">PR1260002602617</strong>
              <div style="margin-top: 0.35rem;">Agent MahaRERA:</div>
              <strong style="color: var(--godrej-gold); font-size: 0.85rem;">A52100040088</strong>
            </div>
          </div>
          <p style="font-size: 0.75rem; color: #64748B; margin-top: 0.75rem; line-height: 1.4;">
            Available at official website: <a href="https://maharera.mahaonline.gov.in" target="_blank" rel="noopener" style="color: var(--godrej-gold-light); text-decoration: underline;">maharera.mahaonline.gov.in</a> under registered projects.
          </p>
        </div>
      </div>

      <!-- Legal Disclaimer Text -->
      <div class="footer-disclaimer-text">
        <p>
          <strong>Disclaimer:</strong> This website is maintained by an authorized channel partner (MahaRERA: A52100040088) for marketing and informational purposes regarding Godrej Elanor (MahaRERA: PR1260002602617). The content, visual representations, specifications, amenities, and dimensions presented herein are indicative and subject to approvals from competent authorities. Real-estate prices mentioned are indicative starting prices and subject to change without prior notice. Government taxes, stamp duty, registration charges, and other statutory levies are applicable over and above the base prices. The official website of Godrej Properties Limited is www.godrejproperties.com.
        </p>
      </div>

      <div class="footer-bottom-flex">
        <div>
          &copy; 2026 Godrej Elanor Mahalunge, Pune. All Rights Reserved.
        </div>
        <div>
          Authorized Channel Partner MahaRERA: <strong>A52100040088</strong> · Project RERA: <strong>PR1260002602617</strong>
        </div>
      </div>
    </div>
  </footer>

  <!-- ==========================================================================
       FLOATING ACTIONS & MOBILE STICKY BAR
       ========================================================================== -->
  <!-- Floating WhatsApp Action -->
  <a href="https://wa.me/918459396466?text=Hi%2C%20I%20am%20interested%20in%20Godrej%20Elanor%20Mahalunge%20Pune.%20Please%20share%20the%20price%20sheet%20and%20project%20brochure." target="_blank" rel="noopener" class="floating-whatsapp-btn" aria-label="Chat on WhatsApp">
    <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
  </a>

  <!-- Mobile Bottom Sticky Action Bar -->
  <div class="mobile-action-bar-sticky">
    <div class="mobile-action-bar-grid">
      <a href="tel:+918459396466" class="btn btn-outline-navy" style="padding: 0.65rem 0.5rem; font-size: 0.8rem; justify-content: center;">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
        <span>Call Now</span>
      </a>

      <a href="https://wa.me/918459396466?text=Hi%2C%20I%20am%20interested%20in%20Godrej%20Elanor%20Mahalunge%20Pune.%20Please%20share%20the%20price%20sheet%20and%20project%20brochure." target="_blank" rel="noopener" class="btn btn-whatsapp" style="padding: 0.65rem 0.5rem; font-size: 0.8rem; justify-content: center;">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
        <span>WhatsApp</span>
      </a>

      <button type="button" class="btn btn-gold" data-open-modal="enquiryModal" data-prefill="Price Sheet" style="padding: 0.65rem 0.5rem; font-size: 0.8rem; justify-content: center;">
        <span>Price Sheet</span>
      </button>
    </div>
  </div>

  <!-- Mobile Drawer Menu -->
  <div class="mobile-nav-panel" id="mobileDrawer">
    <div class="mobile-nav-drawer-content">
      <div>
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem;">
          <div>
            <div style="font-family: var(--font-heading); font-size: 1.25rem; font-weight: 700; color: var(--godrej-navy);">GODREJ ELANOR</div>
            <div style="font-size: 0.75rem; color: var(--godrej-gold-dark); text-transform: uppercase;">Mahalunge, Pune</div>
          </div>
          <button type="button" id="mobileCloseBtn" class="modal-close-icon" aria-label="Close menu">&times;</button>
        </div>

        <div style="display: flex; flex-direction: column; gap: 1.25rem; font-size: 1.05rem; font-weight: 500;">
          <a href="#hero" style="color: var(--godrej-navy);">Home Banner</a>
          <a href="#overview" style="color: var(--godrej-navy);">Project Overview</a>
          <a href="#floor-plans" style="color: var(--godrej-navy);">Floor Plans &amp; Blueprints</a>
          <a href="#price" style="color: var(--godrej-navy);">Configurations &amp; Pricing</a>
          <a href="#amenities" style="color: var(--godrej-navy);">Curated Amenities</a>
          <a href="#gallery" style="color: var(--godrej-navy);">Photo Gallery</a>
          <a href="#location" style="color: var(--godrej-navy);">Location &amp; Commute</a>
          <a href="#faqs" style="color: var(--godrej-navy);">Project FAQs</a>
        </div>
      </div>

      <div style="margin-top: 2rem; border-top: 1px solid var(--border-light); padding-top: 1.5rem;">
        <div style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 0.75rem;">
          Sales Desk: <strong>+91 84593 96466</strong>
        </div>
        <button type="button" class="btn btn-gold btn-block" style="width: 100%; justify-content: center;" data-open-modal="enquiryModal" data-prefill="Brochure Request">
          <span>Enquire Now</span>
        </button>
      </div>
    </div>
  </div>

  <!-- ==========================================================================
       MODALS SYSTEM
       ========================================================================== -->
  <!-- 1. General Enquiry & Pricing Modal -->
  <div class="modal-overlay" id="enquiryModal" role="dialog" aria-modal="true" aria-labelledby="modalTitle1">
    <div class="modal-dialog-box">
      <button type="button" class="modal-close-icon modal-close-btn" aria-label="Close modal">&times;</button>
      <div class="modal-head">
        <span class="lead-card-tag">GODREJ PROPERTIES SALES DESK</span>
        <h3 class="modal-head-title" id="modalTitle1">Request Pricing &amp; Brochure</h3>
      </div>
      <div class="modal-body-content">
        <p style="font-size: 0.875rem; color: var(--text-secondary); margin-bottom: 1.25rem;">
          Please enter your contact details to receive the official Godrej Elanor Mahalunge cost sheet, floor plan blueprints, and launch discounts.
        </p>

        <form data-lead-form id="modalLeadForm">
          <div class="form-group-clean">
            <label for="modalName" class="form-label-clean">Full Name *</label>
            <input type="text" id="modalName" name="name" class="form-input-clean" placeholder="Enter your full name" required>
          </div>

          <div class="form-group-clean">
            <label for="modalPhone" class="form-label-clean">Mobile Number *</label>
            <div class="phone-input-wrap">
              <span class="phone-prefix-tag">+91</span>
              <input type="tel" id="modalPhone" name="phone" class="form-input-clean" placeholder="10-digit mobile number" required pattern="[0-9]{10}" maxlength="10">
            </div>
          </div>

          <div class="form-group-clean">
            <label for="modalConfig" class="form-label-clean">Configuration of Interest</label>
            <select id="modalConfig" name="configuration" class="form-select-clean">
              <option value="3 BHK Premium (1270-1280 Sq. Ft.)">3 BHK Premium (1,270 – 1,280 Sq. Ft.) · ₹ 1.90 Cr*</option>
              <option value="3 BHK Luxe (1310 Sq. Ft.)" selected>3 BHK Luxe (1,310 Sq. Ft.) · ₹ 1.96 Cr*</option>
              <option value="4 BHK Duplex (Bespoke Area)">4 BHK Duplex Penthouse · Price On Request</option>
              <option value="General Enquiry">All Configurations &amp; Investment Guidance</option>
            </select>
          </div>

          <button type="submit" class="btn btn-gold btn-block" style="width: 100%; justify-content: center; padding: 0.85rem; margin-top: 1.25rem;">
            <span>Get Cost Sheet on WhatsApp &amp; SMS</span>
          </button>

          <div class="lead-security-note">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="11" x="3" y="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
            <span>RERA: PR1260002602617 · Agent: A52100040088 · Zero Spam</span>
          </div>
        </form>
      </div>
    </div>
  </div>

  <!-- 2. Site Visit Modal -->
  <div class="modal-overlay" id="siteVisitModal" role="dialog" aria-modal="true" aria-labelledby="modalTitle2">
    <div class="modal-dialog-box">
      <button type="button" class="modal-close-icon modal-close-btn" aria-label="Close modal">&times;</button>
      <div class="modal-head">
        <span class="lead-card-tag">VIP SITE EXPERIENCE</span>
        <h3 class="modal-head-title" id="modalTitle2">Book Guided Site Visit</h3>
      </div>
      <div class="modal-body-content">
        <p style="font-size: 0.875rem; color: var(--text-secondary); margin-bottom: 1.25rem;">
          Enjoy a complimentary AC cab pickup &amp; drop service from anywhere in Pune. Select your date and time below.
        </p>

        <form data-lead-form id="modalSiteVisitForm">
          <div class="form-group-clean">
            <label for="visitModalName" class="form-label-clean">Full Name *</label>
            <input type="text" id="visitModalName" name="name" class="form-input-clean" placeholder="Enter your full name" required>
          </div>

          <div class="form-group-clean">
            <label for="visitModalPhone" class="form-label-clean">Mobile Number *</label>
            <div class="phone-input-wrap">
              <span class="phone-prefix-tag">+91</span>
              <input type="tel" id="visitModalPhone" name="phone" class="form-input-clean" placeholder="10-digit mobile number" required pattern="[0-9]{10}" maxlength="10">
            </div>
          </div>

          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem;">
            <div class="form-group-clean">
              <label for="visitModalDate" class="form-label-clean">Visit Date</label>
              <input type="date" id="visitModalDate" name="visit_date" class="form-input-clean">
            </div>
            <div class="form-group-clean">
              <label for="visitModalTime" class="form-label-clean">Time Slot</label>
              <select id="visitModalTime" name="visit_time" class="form-select-clean">
                <option value="10:00 AM - 12:00 PM">10:00 AM – 12:00 PM</option>
                <option value="12:00 PM - 02:00 PM">12:00 PM – 02:00 PM</option>
                <option value="02:00 PM - 04:00 PM" selected>02:00 PM – 04:00 PM</option>
                <option value="04:00 PM - 06:00 PM">04:00 PM – 06:00 PM</option>
              </select>
            </div>
          </div>

          <button type="submit" class="btn btn-navy btn-block" style="width: 100%; justify-content: center; padding: 0.85rem; margin-top: 1.25rem;">
            <span>Schedule Free Cab &amp; Site Tour</span>
          </button>
        </form>
      </div>
    </div>
  </div>

  <!-- 3. Success Confirmation Modal -->
  <div class="modal-overlay" id="successModal" role="dialog" aria-modal="true">
    <div class="modal-dialog-box" style="text-align: center; max-width: 460px;">
      <button type="button" class="modal-close-icon modal-close-btn" aria-label="Close modal">&times;</button>
      <div class="modal-body-content" style="padding: 2.5rem 2rem;">
        <div style="width: 60px; height: 60px; border-radius: 50%; background-color: #DEF7EC; color: #0E9F6E; display: flex; align-items: center; justify-content: center; margin: 0 auto 1.25rem;">
          <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
        </div>

        <h3 style="font-family: var(--font-heading); font-size: 1.5rem; color: var(--godrej-navy); margin-bottom: 0.5rem;">
          Request Received Successfully!
        </h3>
        <p style="font-size: 0.875rem; color: var(--text-secondary); line-height: 1.6; margin-bottom: 1.5rem;">
          Thank you, <strong id="successLeadName" style="color: var(--godrej-navy);">Valued Customer</strong>. Our official project relationship manager has received your inquiry for Godrej Elanor Mahalunge and will reach out shortly on <strong id="successLeadPhone" style="color: var(--godrej-navy);">your number</strong>.
        </p>

        <div style="background-color: var(--bg-subtle); border: 1px dashed var(--border-medium); border-radius: var(--radius-xs); padding: 0.85rem; margin-bottom: 1.5rem; font-size: 0.8rem; color: var(--text-secondary);">
          Booking Reference ID: <strong style="color: var(--godrej-navy);" id="successRefId">GE-84593</strong><br>
          Sent to sales desk: <span style="color: var(--godrej-navy); font-weight: 600;">enquiryinfinitee@gmail.com</span>
        </div>

        <div style="display: flex; gap: 0.75rem; justify-content: center;">
          <button type="button" class="btn btn-navy modal-close-btn" style="padding: 0.65rem 1.25rem;">
            <span>Close Window</span>
          </button>
          <a href="https://wa.me/918459396466?text=Hi%2C%20I%20have%20submitted%20an%20enquiry%20for%20Godrej%20Elanor%20Mahalunge.%20Please%20share%20the%20cost%20sheet%20now." target="_blank" rel="noopener" class="btn btn-whatsapp" style="padding: 0.65rem 1.25rem;">
            <span>Chat on WhatsApp</span>
          </a>
        </div>
      </div>
    </div>
  </div>

  <!-- 4. Architectural Lightbox Modal -->
  <div class="lightbox-overlay" id="lightboxModal" role="dialog" aria-modal="true">
    <button type="button" id="lightboxCloseBtn" class="lightbox-nav-arrow" style="top: 1.5rem; right: 1.5rem; transform: none;" aria-label="Close lightbox">&times;</button>
    <button type="button" class="lightbox-nav-arrow lightbox-prev-arrow lightbox-prev" aria-label="Previous image">&#10094;</button>
    <button type="button" class="lightbox-nav-arrow lightbox-next-arrow lightbox-next" aria-label="Next image">&#10095;</button>
    
    <div class="lightbox-img-holder">
      <img src="" alt="Enlarged Architectural Preview" id="lightboxImg">
    </div>
    <div class="lightbox-text-caption" id="lightboxCaption">
      Godrej Elanor Mahalunge
    </div>
  </div>

  <!-- JavaScript Controller -->
  <script src="app.js"></script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

print("Updated index.html successfully with exact requested sequence!")
