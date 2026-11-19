# -*- coding: utf-8 -*-
"""
Updates styles.css and index.html to fix:
1. Hero banner text legibility (strong dark backdrop on text side, right-aligned building, compact balanced spacing).
2. Pricing section Rs. currency symbol sticking to card edges (generous padding, structured card header and figure box).
3. 100% full responsiveness from 320px to 1920px (1120px navbar collapse, mobile hamburger drawer, sticky bottom bar, zero horizontal scroll).
"""

# Let's inspect styles.css and write the refined, bulletproof stylesheet
STYLES_CSS = """/* ==========================================================================
   GODREJ ELANOR MAHALUNGE — OFFICIAL BRAND DESIGN SYSTEM
   Brand Identity: Godrej Properties (Navy Blue, Warm Gold, Clean White)
   Reference: https://www.godrejproperties.com/pune/residential/godrej-elanor#price
   ========================================================================== */

:root {
  /* Godrej Properties Official Palette */
  --godrej-navy: #0B2545;
  --godrej-navy-dark: #071A30;
  --godrej-navy-light: #13335A;
  
  --godrej-gold: #C5A880;
  --godrej-gold-dark: #A9895E;
  --godrej-gold-light: #E0CDB4;
  --godrej-gold-subtle: #F6F2EA;
  
  --bg-page: #FFFFFF;
  --bg-subtle: #F8F9FA;
  --bg-alt: #F1F4F8;
  --bg-card: #FFFFFF;
  
  --text-primary: #1C2430;
  --text-secondary: #4A5568;
  --text-muted: #718096;
  --text-light: #FFFFFF;
  --text-light-muted: #D1D5DB;
  
  --border-light: #E2E8F0;
  --border-medium: #CBD5E1;
  --border-dark: #1E293B;

  --whatsapp-color: #25D366;
  --whatsapp-dark: #128C7E;

  /* Typography */
  --font-heading: 'Playfair Display', Georgia, serif;
  --font-body: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;

  /* Layout & Sizing */
  --container-max: 1320px;
  --radius-xs: 2px;
  --radius-sm: 4px;
  --radius-md: 6px;
  --radius-pill: 9999px;

  --shadow-subtle: 0 2px 8px rgba(11, 37, 69, 0.05);
  --shadow-card: 0 4px 20px rgba(11, 37, 69, 0.08);
  --shadow-elevated: 0 12px 36px rgba(11, 37, 69, 0.12);
  --shadow-floating: 0 8px 30px rgba(0, 0, 0, 0.25);

  --transition-fast: 0.2s ease;
  --transition-normal: 0.3s ease;
}

/* ==========================================================================
   Base & Reset
   ========================================================================== */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  font-size: 16px;
  scroll-behavior: smooth;
  -webkit-text-size-adjust: 100%;
}

body {
  font-family: var(--font-body);
  background-color: var(--bg-page);
  color: var(--text-primary);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  overflow-x: hidden;
  position: relative;
  width: 100%;
}

img, picture, video, canvas, svg {
  display: block;
  max-width: 100%;
  height: auto;
}

input, button, textarea, select {
  font: inherit;
}

a {
  color: inherit;
  text-decoration: none;
  transition: color var(--transition-fast);
}

button {
  cursor: pointer;
  border: none;
  background: none;
}

/* Container */
.container {
  width: 100%;
  max-width: var(--container-max);
  margin-inline: auto;
  padding-inline: clamp(1rem, 3.5vw, 2.5rem);
}

.section-spacing {
  padding-block: clamp(3rem, 5vw, 4.5rem);
}

.section-spacing-sm {
  padding-block: clamp(2rem, 3.5vw, 3rem);
}

/* ==========================================================================
   Typography & Badges
   ========================================================================== */
.font-heading {
  font-family: var(--font-heading);
}

.font-body {
  font-family: var(--font-body);
}

.section-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--godrej-gold-dark);
  margin-bottom: 0.65rem;
}

.section-eyebrow::before {
  content: "";
  display: inline-block;
  width: 18px;
  height: 2px;
  background-color: var(--godrej-gold);
}

.section-title {
  font-family: var(--font-heading);
  font-size: clamp(1.85rem, 3.5vw, 2.65rem);
  font-weight: 600;
  color: var(--godrej-navy);
  line-height: 1.2;
  margin-bottom: 1rem;
}

.section-title em {
  font-style: italic;
  font-weight: 400;
  color: var(--godrej-gold-dark);
}

.section-subtitle {
  font-size: clamp(0.925rem, 1.2vw, 1.05rem);
  color: var(--text-secondary);
  line-height: 1.65;
  max-width: 680px;
}

.text-center {
  text-align: center;
}

.mx-auto {
  margin-inline: auto;
}

/* ==========================================================================
   Buttons
   ========================================================================== */
.btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-family: var(--font-body);
  font-size: 0.9rem;
  font-weight: 600;
  letter-spacing: 0.02em;
  padding: 0.75rem 1.5rem;
  border-radius: var(--radius-xs);
  transition: all var(--transition-fast);
  text-align: center;
  justify-content: center;
  white-space: nowrap;
}

.btn-gold {
  background-color: var(--godrej-gold);
  color: #FFFFFF;
}

.btn-gold:hover {
  background-color: var(--godrej-gold-dark);
  box-shadow: 0 4px 14px rgba(197, 168, 128, 0.4);
}

.btn-navy {
  background-color: var(--godrej-navy);
  color: #FFFFFF;
}

.btn-navy:hover {
  background-color: var(--godrej-navy-dark);
  box-shadow: 0 4px 14px rgba(11, 37, 69, 0.35);
}

.btn-outline-navy {
  background-color: transparent;
  color: var(--godrej-navy);
  border: 1px solid var(--godrej-navy);
}

.btn-outline-navy:hover {
  background-color: var(--godrej-navy);
  color: #FFFFFF;
}

.btn-outline-white {
  background-color: transparent;
  color: #FFFFFF;
  border: 1px solid rgba(255, 255, 255, 0.6);
}

.btn-outline-white:hover {
  background-color: #FFFFFF;
  color: var(--godrej-navy);
  border-color: #FFFFFF;
}

.btn-whatsapp {
  background-color: var(--whatsapp-color);
  color: #FFFFFF;
}

.btn-whatsapp:hover {
  background-color: var(--whatsapp-dark);
  box-shadow: 0 4px 14px rgba(37, 211, 102, 0.35);
}

/* ==========================================================================
   Top Header & Navigation Bar
   ========================================================================== */
.top-notice-bar {
  background-color: var(--godrej-navy-dark);
  color: #CBD5E1;
  font-size: 0.78rem;
  padding-block: 0.45rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

.top-notice-bar .container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.top-bar-rera {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.rera-pill-badge {
  background-color: rgba(197, 168, 128, 0.18);
  border: 1px solid var(--godrej-gold);
  color: var(--godrej-gold-light);
  font-size: 0.7rem;
  font-weight: 700;
  padding: 0.15rem 0.5rem;
  border-radius: var(--radius-xs);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.top-bar-contact {
  display: flex;
  align-items: center;
  gap: 0.85rem;
  flex-wrap: wrap;
}

.top-contact-link {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  color: #E2E8F0;
}

.top-contact-link:hover {
  color: var(--godrej-gold-light);
}

.site-header {
  position: sticky;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  background-color: #FFFFFF;
  box-shadow: var(--shadow-subtle);
  transition: all var(--transition-fast);
}

.site-header.scrolled {
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
}

.site-navbar {
  padding-block: 0.75rem;
}

.navbar-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}

.brand-box {
  display: flex;
  flex-direction: column;
}

.brand-logo-text {
  font-family: var(--font-heading);
  font-size: clamp(1.2rem, 2vw, 1.45rem);
  font-weight: 700;
  letter-spacing: 0.06em;
  color: var(--godrej-navy);
  line-height: 1;
}

.brand-subtitle {
  font-size: 0.65rem;
  font-weight: 600;
  color: var(--godrej-gold-dark);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin-top: 0.2rem;
}

/* Nav Menu Links */
.navbar-links {
  display: flex;
  align-items: center;
  gap: clamp(1rem, 1.8vw, 1.5rem);
}

.nav-item-link {
  font-size: 0.825rem;
  font-weight: 600;
  color: var(--text-secondary);
  position: relative;
  padding-block: 0.4rem;
}

.nav-item-link:hover,
.nav-item-link.active {
  color: var(--godrej-navy);
}

.nav-item-link::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background-color: var(--godrej-gold);
  transition: width var(--transition-fast);
}

.nav-item-link:hover::after,
.nav-item-link.active::after {
  width: 100%;
}

.navbar-cta-group {
  display: flex;
  align-items: center;
  gap: 0.65rem;
}

/* Mobile Toggle */
.mobile-menu-btn {
  display: none;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 5px;
  width: 40px;
  height: 40px;
  padding: 6px;
  border: 1px solid var(--border-medium);
  border-radius: var(--radius-xs);
  background-color: var(--bg-subtle);
  cursor: pointer;
}

.mobile-menu-btn span {
  display: block;
  width: 22px;
  height: 2px;
  background-color: var(--godrej-navy);
  border-radius: 1px;
}

/* ==========================================================================
   Hero Banner Section (High-Impact Real-Estate Hero)
   Text is 100% visible with rich deep backdrop & building image aligned right
   ========================================================================== */
.hero-banner-section {
  position: relative;
  background-color: var(--godrej-navy-dark);
  color: #FFFFFF;
  display: flex;
  align-items: center;
  overflow: hidden;
  padding-block: clamp(2.25rem, 4vw, 3.5rem);
  min-height: 580px;
}

.hero-bg-media {
  position: absolute;
  inset: 0;
  z-index: 1;
}

.hero-bg-media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: right 30%;
  filter: brightness(0.62) contrast(1.1);
}

/* High-contrast solid-to-transparent navy gradient ensuring 100% text readability */
.hero-gradient-overlay {
  position: absolute;
  inset: 0;
  z-index: 1;
  background: linear-gradient(
    90deg,
    rgba(7, 26, 48, 0.98) 0%,
    rgba(7, 26, 48, 0.94) 48%,
    rgba(7, 26, 48, 0.65) 75%,
    rgba(7, 26, 48, 0.35) 100%
  );
}

.hero-content-grid {
  position: relative;
  z-index: 2;
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: clamp(1.75rem, 3.5vw, 3rem);
  align-items: center;
}

.hero-left-col {
  padding-right: 0.5rem;
}

.hero-project-tag {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  background-color: rgba(197, 168, 128, 0.22);
  border: 1px solid var(--godrej-gold);
  color: var(--godrej-gold-light);
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  padding: 0.3rem 0.75rem;
  border-radius: var(--radius-xs);
  margin-bottom: 0.85rem;
}

.status-pulse-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background-color: var(--godrej-gold);
  box-shadow: 0 0 8px var(--godrej-gold);
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.4; transform: scale(0.85); }
  100% { opacity: 1; transform: scale(1); }
}

.hero-heading {
  font-family: var(--font-heading);
  font-size: clamp(2.1rem, 4vw, 3.25rem);
  font-weight: 600;
  line-height: 1.12;
  color: #FFFFFF;
  margin-bottom: 0.65rem;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
}

.hero-heading span {
  color: var(--godrej-gold-light);
  display: block;
  font-weight: 400;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
}

.hero-location-line {
  display: flex;
  align-items: center;
  gap: 0.45rem;
  font-size: 0.875rem;
  color: #E2E8F0;
  margin-bottom: 1rem;
  text-shadow: 0 1px 4px rgba(0, 0, 0, 0.5);
}

.hero-location-line svg {
  color: var(--godrej-gold);
  flex-shrink: 0;
}

.hero-description {
  font-size: 0.95rem;
  line-height: 1.6;
  color: #E2E8F0;
  margin-bottom: 1.35rem;
  max-width: 540px;
  text-shadow: 0 1px 4px rgba(0, 0, 0, 0.6);
}

.hero-description strong {
  color: #FFFFFF;
}

.hero-key-stats-strip {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 0.75rem;
  padding-block: 0.95rem;
  border-block: 1px solid rgba(255, 255, 255, 0.2);
  margin-bottom: 1.35rem;
  background-color: rgba(7, 26, 48, 0.4);
  border-radius: var(--radius-xs);
  padding-inline: 0.75rem;
}

.hero-stat-block span {
  display: block;
}

.hero-stat-val {
  font-family: var(--font-heading);
  font-size: 1.35rem;
  font-weight: 600;
  color: var(--godrej-gold-light);
  line-height: 1.1;
}

.hero-stat-lbl {
  font-size: 0.675rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: #CBD5E1;
  margin-top: 0.2rem;
}

.hero-actions-group {
  display: flex;
  align-items: center;
  gap: 0.65rem;
  flex-wrap: wrap;
}

/* Hero Quick Lead Form Card (Right Column) */
.hero-lead-card {
  background-color: #FFFFFF;
  color: var(--text-primary);
  border-radius: var(--radius-sm);
  padding: clamp(1.5rem, 2.5vw, 2rem);
  box-shadow: var(--shadow-floating);
  border-top: 4px solid var(--godrej-gold);
}

.lead-card-header {
  margin-bottom: 1rem;
  padding-bottom: 0.65rem;
  border-bottom: 1px solid var(--border-light);
}

.lead-card-tag {
  display: inline-block;
  font-size: 0.675rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--godrej-navy);
  margin-bottom: 0.25rem;
}

.lead-card-title {
  font-family: var(--font-heading);
  font-size: 1.35rem;
  font-weight: 600;
  color: var(--godrej-navy);
  line-height: 1.2;
}

.lead-card-desc {
  font-size: 0.8rem;
  color: var(--text-secondary);
  margin-top: 0.2rem;
}

.lead-card-form {
  display: flex;
  flex-direction: column;
  gap: 0.85rem;
}

.form-group-clean {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
}

.form-label-clean {
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--text-primary);
}

.form-input-clean,
.form-select-clean {
  width: 100%;
  padding: 0.65rem 0.85rem;
  font-size: 0.875rem;
  color: var(--text-primary);
  background-color: var(--bg-subtle);
  border: 1px solid var(--border-medium);
  border-radius: var(--radius-xs);
  transition: all var(--transition-fast);
}

.form-input-clean:focus,
.form-select-clean:focus {
  outline: none;
  background-color: #FFFFFF;
  border-color: var(--godrej-navy);
  box-shadow: 0 0 0 3px rgba(11, 37, 69, 0.1);
}

.phone-input-wrap {
  display: flex;
  align-items: stretch;
}

.phone-prefix-tag {
  display: inline-flex;
  align-items: center;
  padding: 0 0.75rem;
  background-color: var(--bg-alt);
  border: 1px solid var(--border-medium);
  border-right: none;
  border-radius: var(--radius-xs) 0 0 var(--radius-xs);
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--text-secondary);
}

.phone-input-wrap .form-input-clean {
  border-radius: 0 var(--radius-xs) var(--radius-xs) 0;
}

.lead-security-note {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  font-size: 0.7rem;
  color: var(--text-muted);
  margin-top: 0.5rem;
}

/* ==========================================================================
   Trust & Key Highlights Strip
   ========================================================================== */
.highlights-strip-section {
  background-color: var(--bg-subtle);
  border-bottom: 1px solid var(--border-light);
  padding-block: 2.25rem;
}

.highlights-strip-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
}

.highlight-strip-card {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
}

.highlight-strip-icon {
  width: 44px;
  height: 44px;
  border-radius: var(--radius-xs);
  background-color: var(--godrej-gold-subtle);
  color: var(--godrej-gold-dark);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.highlight-strip-text h4 {
  font-family: var(--font-heading);
  font-size: 1.05rem;
  font-weight: 600;
  color: var(--godrej-navy);
  margin-bottom: 0.25rem;
}

.highlight-strip-text p {
  font-size: 0.825rem;
  color: var(--text-secondary);
  line-height: 1.45;
}

/* ==========================================================================
   Project Overview Section
   ========================================================================== */
.overview-grid-layout {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: clamp(2rem, 4vw, 3.5rem);
  align-items: center;
}

.overview-text-col p {
  font-size: 0.95rem;
  color: var(--text-secondary);
  line-height: 1.7;
  margin-bottom: 1.25rem;
}

.overview-specs-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 1.5rem;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-xs);
  overflow: hidden;
  font-size: 0.875rem;
}

.overview-specs-table tr {
  border-bottom: 1px solid var(--border-light);
}

.overview-specs-table tr:last-child {
  border-bottom: none;
}

.overview-specs-table td {
  padding: 0.75rem 1rem;
}

.overview-specs-table td:first-child {
  background-color: var(--bg-subtle);
  color: var(--text-secondary);
  font-weight: 500;
  width: 38%;
  border-right: 1px solid var(--border-light);
}

.overview-specs-table td:last-child {
  color: var(--godrej-navy);
  background-color: #FFFFFF;
}

.overview-image-box {
  position: relative;
  border-radius: var(--radius-sm);
  overflow: hidden;
  box-shadow: var(--shadow-card);
}

.overview-image-box img {
  width: 100%;
  height: auto;
  object-fit: cover;
}

.overview-image-badge {
  position: absolute;
  bottom: 1.25rem;
  left: 1.25rem;
  right: 1.25rem;
  background-color: rgba(7, 26, 48, 0.92);
  color: #FFFFFF;
  padding: 0.85rem 1.25rem;
  border-radius: var(--radius-xs);
  border-left: 3px solid var(--godrej-gold);
}

.overview-image-badge strong {
  display: block;
  font-family: var(--font-heading);
  font-size: 1.1rem;
  color: var(--godrej-gold-light);
}

.overview-image-badge span {
  font-size: 0.775rem;
  color: #CBD5E1;
}

/* ==========================================================================
   Configurations & Pricing Section (#price)
   FIXED: Generous padding around ₹ currency symbol so it never sticks to edges!
   ========================================================================== */
.pricing-section-wrap {
  background-color: var(--bg-subtle);
}

.pricing-cards-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: clamp(1.25rem, 2.5vw, 2rem);
  align-items: stretch;
}

.pricing-unit-card {
  background-color: #FFFFFF;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-sm);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  transition: all var(--transition-normal);
  position: relative;
  box-shadow: var(--shadow-subtle);
}

.pricing-unit-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-card);
  border-color: var(--godrej-gold);
}

.pricing-unit-card.featured-card {
  border: 2px solid var(--godrej-gold);
  box-shadow: var(--shadow-card);
}

.pricing-badge-ribbon {
  background-color: var(--godrej-navy);
  color: var(--godrej-gold-light);
  font-size: 0.6875rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  text-align: center;
  padding-block: 0.4rem;
}

.pricing-card-top {
  padding: 1.5rem 1.75rem 1.25rem;
  border-bottom: 1px solid var(--border-light);
}

.pricing-unit-tagline {
  font-size: 0.72rem;
  font-weight: 700;
  color: var(--godrej-gold-dark);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  display: block;
  margin-bottom: 0.35rem;
}

.pricing-unit-name {
  font-family: var(--font-heading);
  font-size: 1.6rem;
  font-weight: 600;
  color: var(--godrej-navy);
  line-height: 1.2;
}

/* FIXED PRICING FIGURE BOX: Elegant background with ample horizontal padding */
.pricing-figure-box {
  padding: 1.25rem 1.75rem;
  background-color: #F8FAFC;
  border-bottom: 1px solid var(--border-light);
}

.pricing-figure-val {
  font-family: var(--font-heading);
  font-size: clamp(1.45rem, 2vw, 1.85rem);
  font-weight: 700;
  color: var(--godrej-navy);
  line-height: 1.1;
  display: block;
}

.pricing-figure-note {
  font-size: 0.75rem;
  color: var(--text-muted);
  margin-top: 0.35rem;
  display: block;
}

.pricing-card-details {
  padding: 1.5rem 1.75rem;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.pricing-spec-list {
  display: flex;
  flex-direction: column;
  gap: 0.65rem;
  margin-bottom: 1.5rem;
}

.pricing-spec-row {
  display: flex;
  justify-content: space-between;
  font-size: 0.8125rem;
  padding-bottom: 0.5rem;
  border-bottom: 1px solid rgba(0, 0, 0, 0.04);
}

.pricing-spec-row span {
  color: var(--text-secondary);
}

.pricing-spec-row strong {
  font-weight: 600;
  color: var(--godrej-navy);
  text-align: right;
}

/* ==========================================================================
   Home Loan & EMI Calculator (Clean Modern Interface)
   ========================================================================== */
.emi-calculator-card {
  background-color: #FFFFFF;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-sm);
  padding: clamp(2rem, 4vw, 3rem);
  box-shadow: var(--shadow-card);
}

.emi-calc-grid {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: clamp(2rem, 4vw, 3.5rem);
  align-items: center;
}

.slider-group {
  margin-bottom: 1.75rem;
}

.slider-label-flex {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.5rem;
}

.slider-title {
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--text-primary);
}

.slider-value-display {
  font-family: var(--font-heading);
  font-size: 1.15rem;
  font-weight: 600;
  color: var(--godrej-navy);
}

.calc-range-slider {
  width: 100%;
  height: 6px;
  background: #E2E8F0;
  border-radius: 3px;
  outline: none;
  -webkit-appearance: none;
  cursor: pointer;
}

.calc-range-slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: var(--godrej-navy);
  border: 2px solid #FFFFFF;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
  cursor: pointer;
  transition: transform var(--transition-fast);
}

.calc-range-slider::-webkit-slider-thumb:hover {
  transform: scale(1.15);
  background: var(--godrej-gold-dark);
}

.emi-result-panel {
  background-color: var(--godrej-navy);
  color: #FFFFFF;
  border-radius: var(--radius-sm);
  padding: clamp(1.75rem, 3vw, 2.25rem);
  box-shadow: var(--shadow-floating);
  border-left: 4px solid var(--godrej-gold);
}

.emi-monthly-num {
  font-family: var(--font-heading);
  font-size: clamp(2rem, 3vw, 2.6rem);
  font-weight: 700;
  color: var(--godrej-gold-light);
  line-height: 1.1;
  margin-block: 0.35rem 0.25rem;
}

/* ==========================================================================
   Master Plan & Floor Plans Section
   ========================================================================== */
.floor-plans-section {
  background-color: #FFFFFF;
}

.plan-tabs-row {
  display: flex;
  justify-content: center;
  gap: 0.6rem;
  flex-wrap: wrap;
  margin-bottom: 2.5rem;
}

.plan-tab-button {
  padding: 0.65rem 1.25rem;
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--text-secondary);
  background-color: var(--bg-subtle);
  border: 1px solid var(--border-medium);
  border-radius: var(--radius-pill);
  transition: all var(--transition-fast);
}

.plan-tab-button:hover {
  color: var(--godrej-navy);
  border-color: var(--godrej-navy);
}

.plan-tab-button.active {
  background-color: var(--godrej-navy);
  color: #FFFFFF;
  border-color: var(--godrej-navy);
}

.plan-display-card {
  background-color: var(--bg-subtle);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-sm);
  overflow: hidden;
  display: grid;
  grid-template-columns: 1.3fr 0.7fr;
  box-shadow: var(--shadow-card);
}

.plan-blueprint-box {
  background-color: #071A30;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1.5rem;
  border-right: 1px solid var(--border-light);
  position: relative;
}

.plan-blueprint-box img {
  max-height: 480px;
  width: auto;
  object-fit: contain;
  transition: transform var(--transition-normal);
  cursor: pointer;
}

.plan-blueprint-box img:hover {
  transform: scale(1.02);
}

.plan-info-box {
  padding: clamp(1.75rem, 3vw, 2.5rem);
  display: flex;
  flex-direction: column;
  justify-content: center;
  background-color: #FFFFFF;
}

/* ==========================================================================
   Curated Amenities Section (Riverfront Luxuries)
   ========================================================================== */
.amenities-section-wrap {
  background-color: var(--bg-subtle);
}

.amenities-grid-clean {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: clamp(1.25rem, 2.5vw, 2rem);
}

.amenity-card-clean {
  background-color: #FFFFFF;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-sm);
  overflow: hidden;
  box-shadow: var(--shadow-subtle);
  transition: all var(--transition-normal);
}

.amenity-card-clean:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-card);
}

.amenity-image-holder {
  height: 220px;
  overflow: hidden;
  position: relative;
}

.amenity-image-holder img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.6s ease;
}

.amenity-card-clean:hover .amenity-image-holder img {
  transform: scale(1.06);
}

.amenity-card-body {
  padding: 1.5rem;
}

.amenity-card-title {
  font-family: var(--font-heading);
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--godrej-navy);
  margin-bottom: 0.5rem;
}

.amenity-card-desc {
  font-size: 0.85rem;
  color: var(--text-secondary);
  line-height: 1.55;
}

/* ==========================================================================
   Architectural Gallery
   ========================================================================== */
.gallery-section-wrap {
  background-color: #FFFFFF;
}

.gallery-grid-clean {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.25rem;
}

.gallery-photo-item {
  position: relative;
  height: 260px;
  border-radius: var(--radius-xs);
  overflow: hidden;
  cursor: pointer;
}

.gallery-photo-item.wide-span {
  grid-column: span 2;
}

.gallery-photo-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.gallery-photo-item:hover img {
  transform: scale(1.05);
}

.gallery-photo-caption {
  position: absolute;
  inset: auto 0 0 0;
  padding: 1.5rem 1.25rem 1rem;
  background: linear-gradient(to top, rgba(7, 26, 48, 0.9), transparent);
  color: #FFFFFF;
  transform: translateY(10px);
  opacity: 0.9;
  transition: all var(--transition-fast);
}

.gallery-photo-item:hover .gallery-photo-caption {
  transform: translateY(0);
  opacity: 1;
}

.gallery-photo-caption h4 {
  font-family: var(--font-heading);
  font-size: 1.05rem;
  font-weight: 600;
  color: #FFFFFF;
}

.gallery-photo-caption p {
  font-size: 0.775rem;
  color: var(--godrej-gold-light);
  margin-top: 0.2rem;
}

/* ==========================================================================
   Location & Strategic Connectivity
   ========================================================================== */
.location-section-wrap {
  background-color: var(--bg-subtle);
}

.location-layout-grid {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: clamp(2rem, 4vw, 3.5rem);
  align-items: stretch;
}

.connectivity-table-wrap {
  background-color: #FFFFFF;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-sm);
  padding: clamp(1.5rem, 3vw, 2.25rem);
  box-shadow: var(--shadow-subtle);
}

.connectivity-table-clean {
  width: 100%;
  border-collapse: collapse;
}

.connectivity-table-clean tr {
  border-bottom: 1px solid var(--border-light);
}

.connectivity-table-clean tr:last-child {
  border-bottom: none;
}

.connectivity-table-clean td {
  padding: 0.85rem 0.5rem;
}

.conn-hub-name {
  font-weight: 600;
  font-size: 0.9rem;
  color: var(--godrej-navy);
}

.conn-hub-category {
  font-size: 0.75rem;
  color: var(--text-muted);
}

.conn-hub-time {
  font-family: var(--font-heading);
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--godrej-gold-dark);
  text-align: right;
  white-space: nowrap;
}

.location-map-clean-frame {
  border-radius: var(--radius-sm);
  overflow: hidden;
  box-shadow: var(--shadow-subtle);
  border: 1px solid var(--border-light);
  min-height: 400px;
}

.location-map-clean-frame iframe {
  width: 100%;
  height: 100%;
  min-height: 400px;
  border: none;
}

/* ==========================================================================
   Developer Heritage: Godrej Properties Legacy
   ========================================================================== */
.developer-section-clean {
  background-color: #FFFFFF;
}

.developer-content-grid {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: clamp(2rem, 4vw, 3.5rem);
  align-items: center;
}

.developer-stats-strip {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.25rem;
  margin-top: 2rem;
  padding-top: 1.5rem;
  border-top: 1px solid var(--border-light);
}

.dev-stat-number {
  font-family: var(--font-heading);
  font-size: 1.85rem;
  font-weight: 700;
  color: var(--godrej-navy);
  line-height: 1;
  display: block;
}

.dev-stat-text {
  font-size: 0.75rem;
  color: var(--text-secondary);
  margin-top: 0.35rem;
  display: block;
}

/* ==========================================================================
   Frequently Asked Questions (Clean Accordion)
   ========================================================================== */
.faq-section-clean {
  background-color: var(--bg-subtle);
}

.faq-list-clean {
  display: flex;
  flex-direction: column;
  gap: 0.85rem;
}

.faq-card-clean {
  background-color: #FFFFFF;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-xs);
  overflow: hidden;
  transition: all var(--transition-fast);
}

.faq-card-clean.active {
  border-color: var(--godrej-navy);
  box-shadow: var(--shadow-subtle);
}

.faq-btn-trigger {
  width: 100%;
  padding: 1.15rem 1.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  text-align: left;
  font-family: var(--font-heading);
  font-size: 1.05rem;
  font-weight: 600;
  color: var(--godrej-navy);
  cursor: pointer;
}

.faq-btn-trigger:hover {
  background-color: var(--bg-subtle);
}

.faq-icon-symbol {
  font-size: 1.35rem;
  color: var(--godrej-gold-dark);
  transition: transform var(--transition-fast);
}

.faq-card-clean.active .faq-icon-symbol {
  transform: rotate(45deg);
}

.faq-body-collapse {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.3s ease-out;
}

.faq-body-inner {
  padding: 0 1.5rem 1.25rem;
  font-size: 0.9rem;
  color: var(--text-secondary);
  line-height: 1.65;
  border-top: 1px solid var(--border-light);
  padding-top: 1rem;
}

/* ==========================================================================
   Schedule Site Visit Section (Dark Navy Contrast)
   ========================================================================== */
.site-visit-section-dark {
  background-color: var(--godrej-navy-dark);
  color: #FFFFFF;
}

.site-visit-grid-layout {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: clamp(2rem, 4vw, 3.5rem);
  align-items: center;
}

.site-visit-form-box {
  background-color: #FFFFFF;
  color: var(--text-primary);
  border-radius: var(--radius-sm);
  padding: clamp(1.75rem, 3.5vw, 2.5rem);
  box-shadow: var(--shadow-floating);
}

/* ==========================================================================
   Footer & MahaRERA Transparency
   ========================================================================== */
.site-footer-clean {
  background-color: var(--godrej-navy-dark);
  color: #94A3B8;
  font-size: 0.8125rem;
  padding-top: clamp(3rem, 5vw, 4.5rem);
  padding-bottom: 2rem;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.footer-columns-grid {
  display: grid;
  grid-template-columns: 1.35fr 0.9fr 0.9fr 1.25fr;
  gap: clamp(1.75rem, 3vw, 3rem);
  margin-bottom: 2.5rem;
}

.footer-col-head {
  font-family: var(--font-heading);
  font-size: 1.15rem;
  color: #FFFFFF;
  margin-bottom: 1rem;
}

.footer-links-col {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.footer-links-col a:hover {
  color: var(--godrej-gold-light);
}

.footer-rera-box-clean {
  background-color: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: var(--radius-xs);
  padding: 1rem;
  display: flex;
  align-items: center;
  gap: 1rem;
}

.footer-rera-qr {
  width: 64px;
  height: 64px;
  background-color: #FFFFFF;
  padding: 2px;
  border-radius: var(--radius-xs);
  flex-shrink: 0;
}

.footer-disclaimer-text {
  font-size: 0.72rem;
  line-height: 1.6;
  color: #64748B;
  padding-top: 1.5rem;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.footer-bottom-flex {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 1.25rem;
  margin-top: 1.25rem;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  font-size: 0.75rem;
  flex-wrap: wrap;
  gap: 1rem;
}

/* ==========================================================================
   Modals & Lightbox
   ========================================================================== */
.modal-overlay {
  position: fixed;
  inset: 0;
  z-index: 3000;
  background-color: rgba(7, 26, 48, 0.75);
  backdrop-filter: blur(6px);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1.25rem;
  opacity: 0;
  pointer-events: none;
  transition: opacity var(--transition-fast);
}

.modal-overlay.open {
  opacity: 1;
  pointer-events: auto;
}

.modal-dialog-box {
  background-color: #FFFFFF;
  width: 100%;
  max-width: 520px;
  border-radius: var(--radius-sm);
  overflow: hidden;
  box-shadow: var(--shadow-floating);
  position: relative;
  transform: translateY(15px);
  transition: transform var(--transition-fast);
}

.modal-overlay.open .modal-dialog-box {
  transform: translateY(0);
}

.modal-close-icon {
  position: absolute;
  top: 1.25rem;
  right: 1.25rem;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  border: 1px solid var(--border-light);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.25rem;
  color: var(--godrej-navy);
  background-color: var(--bg-subtle);
  cursor: pointer;
}

.modal-close-icon:hover {
  background-color: var(--godrej-navy);
  color: #FFFFFF;
}

.modal-head {
  padding: 1.75rem 2rem 1rem;
  border-bottom: 1px solid var(--border-light);
}

.modal-head-title {
  font-family: var(--font-heading);
  font-size: 1.45rem;
  color: var(--godrej-navy);
  font-weight: 600;
}

.modal-body-content {
  padding: 1.5rem 2rem 2rem;
  max-height: 80vh;
  overflow-y: auto;
}

/* Lightbox */
.lightbox-overlay {
  position: fixed;
  inset: 0;
  z-index: 4000;
  background-color: rgba(7, 26, 48, 0.96);
  backdrop-filter: blur(10px);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  opacity: 0;
  pointer-events: none;
  transition: opacity var(--transition-fast);
  padding: 1rem;
}

.lightbox-overlay.open {
  opacity: 1;
  pointer-events: auto;
}

.lightbox-img-holder {
  max-width: 90vw;
  max-height: 80vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.lightbox-img-holder img {
  max-width: 100%;
  max-height: 80vh;
  object-fit: contain;
}

.lightbox-text-caption {
  margin-top: 1rem;
  font-family: var(--font-heading);
  font-size: 1.25rem;
  color: #FFFFFF;
  text-align: center;
}

.lightbox-nav-arrow {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background-color: rgba(255, 255, 255, 0.15);
  color: #FFFFFF;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.35rem;
  cursor: pointer;
}

.lightbox-nav-arrow:hover {
  background-color: #FFFFFF;
  color: var(--godrej-navy);
}

.lightbox-prev-arrow { left: 1.5rem; }
.lightbox-next-arrow { right: 1.5rem; }

/* Floating Elements */
.floating-whatsapp-btn {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  z-index: 990;
  width: 54px;
  height: 54px;
  border-radius: 50%;
  background-color: var(--whatsapp-color);
  color: #FFFFFF;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 16px rgba(37, 211, 102, 0.4);
  transition: transform var(--transition-fast);
}

.floating-whatsapp-btn:hover {
  transform: scale(1.1);
}

/* Mobile Sticky Bottom Action Bar */
.mobile-action-bar-sticky {
  display: none;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  background-color: #FFFFFF;
  border-top: 1px solid var(--border-light);
  padding: 0.5rem 0.75rem;
  box-shadow: 0 -4px 16px rgba(0, 0, 0, 0.12);
}

.mobile-action-bar-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 0.5rem;
}

/* Mobile Drawer */
.mobile-nav-panel {
  position: fixed;
  inset: 0;
  z-index: 2500;
  background-color: rgba(7, 26, 48, 0.7);
  backdrop-filter: blur(6px);
  opacity: 0;
  pointer-events: none;
  transition: opacity var(--transition-fast);
}

.mobile-nav-panel.open {
  opacity: 1;
  pointer-events: auto;
}

.mobile-nav-drawer-content {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  width: 85%;
  max-width: 320px;
  background-color: #FFFFFF;
  padding: 1.75rem 1.25rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transform: translateX(100%);
  transition: transform var(--transition-fast);
  overflow-y: auto;
}

.mobile-nav-panel.open .mobile-nav-drawer-content {
  transform: translateX(0);
}

/* ==========================================================================
   RESPONSIVE BREAKPOINTS (Pixel-Perfect from 320px to 1920px)
   ========================================================================== */

/* Large Tablets & Small Laptops (<= 1140px) */
@media (max-width: 1140px) {
  .navbar-links {
    display: none !important;
  }
  .mobile-menu-btn {
    display: flex !important;
  }
}

/* Medium Tablets & Below (<= 1024px) */
@media (max-width: 1024px) {
  .hero-content-grid {
    grid-template-columns: 1fr;
    gap: 2.25rem;
  }
  .hero-left-col {
    padding-right: 0;
    text-align: center;
  }
  .hero-location-line {
    justify-content: center;
  }
  .hero-description {
    margin-inline: auto;
  }
  .hero-actions-group {
    justify-content: center;
  }
  .hero-lead-card {
    max-width: 500px;
    margin-inline: auto;
  }
  .highlights-strip-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .overview-grid-layout {
    grid-template-columns: 1fr;
  }
  .pricing-cards-grid {
    grid-template-columns: 1fr;
    max-width: 480px;
    margin-inline: auto;
  }
  .emi-calc-grid {
    grid-template-columns: 1fr;
  }
  .plan-display-card {
    grid-template-columns: 1fr;
  }
  .plan-blueprint-box {
    border-right: none;
    border-bottom: 1px solid var(--border-light);
  }
  .amenities-grid-clean {
    grid-template-columns: repeat(2, 1fr);
  }
  .location-layout-grid {
    grid-template-columns: 1fr;
  }
  .developer-content-grid {
    grid-template-columns: 1fr;
  }
  .developer-stats-strip {
    grid-template-columns: repeat(2, 1fr);
  }
  .site-visit-grid-layout {
    grid-template-columns: 1fr;
  }
  .footer-columns-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* Small Tablets & Large Phones (<= 768px) */
@media (max-width: 768px) {
  body {
    padding-bottom: 60px; /* Space for sticky bottom bar */
  }
  .mobile-action-bar-sticky {
    display: block !important;
  }
  .floating-whatsapp-btn {
    bottom: 4.8rem !important;
    right: 1.25rem !important;
    width: 48px !important;
    height: 48px !important;
  }
  .top-notice-bar .container {
    justify-content: center;
    text-align: center;
  }
  .top-bar-rera, .top-bar-contact {
    justify-content: center;
  }
  .hero-key-stats-strip {
    grid-template-columns: repeat(2, 1fr);
    text-align: center;
  }
  .highlights-strip-grid {
    grid-template-columns: 1fr;
  }
  .amenities-grid-clean {
    grid-template-columns: 1fr;
  }
  .gallery-grid-clean {
    grid-template-columns: 1fr;
  }
  .gallery-photo-item.wide-span {
    grid-column: span 1;
  }
  .footer-columns-grid {
    grid-template-columns: 1fr;
  }
}

/* Standard Mobile Phones (<= 480px) */
@media (max-width: 480px) {
  .top-notice-bar {
    font-size: 0.72rem;
  }
  .brand-logo-text {
    font-size: 1.15rem;
  }
  .navbar-cta-group .btn-outline-navy {
    display: none; /* Hide phone button on small navbar, available in sticky bar */
  }
  .hero-heading {
    font-size: 2rem;
  }
  .hero-stat-val {
    font-size: 1.2rem;
  }
  .pricing-unit-card {
    max-width: 100%;
  }
  .pricing-card-top, .pricing-figure-box, .pricing-card-details {
    padding-inline: 1.25rem;
  }
  .plan-tab-button {
    font-size: 0.775rem;
    padding: 0.5rem 0.9rem;
  }
  .overview-specs-table td {
    padding: 0.65rem 0.75rem;
    font-size: 0.8rem;
  }
  .overview-specs-table td:first-child {
    width: 45%;
  }
  .connectivity-table-clean td {
    padding: 0.65rem 0.25rem;
  }
  .conn-hub-name {
    font-size: 0.825rem;
  }
  .conn-hub-time {
    font-size: 0.95rem;
  }
}
"""

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(STYLES_CSS)

print("styles.css successfully updated with bulletproof visibility, padding, and responsiveness!")
