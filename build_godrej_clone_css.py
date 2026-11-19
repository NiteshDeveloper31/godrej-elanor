# -*- coding: utf-8 -*-
"""
Writes styles.css to exactly match media_1795093841503_d35198e2.png
Official Godrej Properties Mobile & Desktop Design System
"""

STYLES_CSS = """/* ==========================================================================
   OFFICIAL GODREJ PROPERTIES DESIGN SYSTEM
   Matches Reference: media_1795093841503_d35198e2.png
   ========================================================================== */

:root {
  --gpl-navy: #0B2545;
  --gpl-navy-dark: #071A30;
  --gpl-gold: #B89D6C;
  --gpl-gold-dark: #A08352;
  --gpl-gold-light: #DFC8A2;
  
  --gpl-text: #222222;
  --gpl-text-muted: #666666;
  --gpl-text-light: #888888;
  --gpl-bg: #FFFFFF;
  --gpl-bg-subtle: #F8F9FA;
  --gpl-bg-alt: #F1F4F8;
  --gpl-border: #E5E9ED;
  --gpl-border-light: #EFEFEF;

  --wa-green: #25D366;
  --wa-green-dark: #128C7E;

  --font-serif: 'Playfair Display', Georgia, serif;
  --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  
  --max-w: 1140px;
  --max-w-narrow: 680px;
}

/* ==========================================================================
   Reset & Base Styles
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
  font-family: var(--font-sans);
  background-color: var(--gpl-bg);
  color: var(--gpl-text);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  overflow-x: hidden;
  position: relative;
  width: 100%;
}

img {
  display: block;
  max-width: 100%;
  height: auto;
}

a {
  color: inherit;
  text-decoration: none;
}

button {
  cursor: pointer;
  border: none;
  background: none;
  font: inherit;
}

input, select, textarea {
  font: inherit;
}

/* Containers */
.site-container {
  width: 100%;
  max-width: var(--max-w);
  margin-inline: auto;
  padding-inline: 1.25rem;
}

.site-container-narrow {
  width: 100%;
  max-width: var(--max-w-narrow);
  margin-inline: auto;
  padding-inline: 1.25rem;
}

.site-container-fluid {
  width: 100%;
  padding-inline: 1.25rem;
}

.flex-between {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.text-center {
  text-align: center;
}

.full-width {
  width: 100%;
}

/* ==========================================================================
   Top Notice / RERA Strip
   ========================================================================== */
.top-rera-strip {
  background-color: var(--gpl-navy-dark);
  color: #CBD5E1;
  font-size: 0.75rem;
  padding-block: 0.35rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

.rera-info-text {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  flex-wrap: wrap;
}

.rera-contact-links {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.contact-pill-link {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  color: #FFFFFF;
  font-weight: 500;
}

.contact-pill-link:hover {
  color: var(--gpl-gold-light);
}

.sep-dot {
  opacity: 0.4;
}

/* ==========================================================================
   Main White Header (Matches media_1795093841503_d35198e2.png)
   ========================================================================== */
.main-godrej-header {
  background-color: #FFFFFF;
  border-bottom: 1px solid var(--gpl-border);
  position: sticky;
  top: 0;
  z-index: 1000;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.04);
}

.header-inner {
  height: 60px;
}

.godrej-brand-logo-group {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.godrej-properties-logo-text {
  display: flex;
  flex-direction: column;
}

.godrej-text-main {
  font-weight: 800;
  letter-spacing: 0.06em;
  font-size: 1.2rem;
  color: #000000;
  line-height: 1;
}

.properties-text-sub {
  font-size: 0.58rem;
  letter-spacing: 0.16em;
  color: #000000;
  font-weight: 600;
  margin-top: 1px;
}

.header-right-actions {
  display: flex;
  align-items: center;
  gap: 1.15rem;
}

/* Godrej Cursive Script Logo */
.godrej-signature-script {
  font-family: 'Brush Script MT', cursive, Georgia, serif;
  font-size: 1.65rem;
  color: #000000;
  font-weight: normal;
  letter-spacing: -0.02em;
  margin-right: 0.35rem;
  user-select: none;
}

.header-icon-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  color: #27262E;
  padding: 4px;
}

/* ==========================================================================
   Sticky Sub-Navigation Bar (Dark Navy)
   ← | Overview | Location | Price | Amenities | Gallery
   ========================================================================== */
.sticky-subnav-bar {
  background-color: var(--gpl-navy);
  color: #FFFFFF;
  position: sticky;
  top: 60px;
  z-index: 990;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.subnav-scroll-container {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  overflow-x: auto;
  scrollbar-width: none;
  -webkit-overflow-scrolling: touch;
}

.subnav-scroll-container::-webkit-scrollbar {
  display: none;
}

.subnav-back-arrow {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: #FFFFFF;
  padding: 0.75rem 0.65rem 0.75rem 0;
  flex-shrink: 0;
  border-right: 1px solid rgba(255, 255, 255, 0.15);
  margin-right: 0.5rem;
}

.subnav-links-track {
  display: flex;
  align-items: center;
  gap: 1.25rem;
  white-space: nowrap;
}

.subnav-item {
  color: #D1D5DB;
  font-size: 0.825rem;
  font-weight: 500;
  padding-block: 0.75rem;
  position: relative;
  transition: color 0.2s ease;
}

.subnav-item:hover,
.subnav-item.active {
  color: #FFFFFF;
}

.subnav-item.active::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 2px;
  background-color: var(--gpl-gold);
}

/* ==========================================================================
   Hero Banner Section (Matches media_1795093841503_d35198e2.png)
   ========================================================================== */
.godrej-hero-section {
  position: relative;
  min-height: clamp(380px, 60vh, 520px);
  background-color: var(--gpl-navy-dark);
  display: flex;
  align-items: flex-end;
  overflow: hidden;
}

.godrej-hero-bg {
  position: absolute;
  inset: 0;
  z-index: 1;
}

.godrej-hero-bg img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
}

.godrej-hero-gradient {
  position: absolute;
  inset: 0;
  z-index: 2;
  background: linear-gradient(
    180deg,
    rgba(0, 0, 0, 0.1) 0%,
    rgba(0, 0, 0, 0.3) 50%,
    rgba(7, 26, 48, 0.95) 100%
  );
}

.godrej-hero-container {
  position: relative;
  z-index: 3;
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  padding-bottom: clamp(1.5rem, 3.5vw, 2.5rem);
}

/* Floating Card at Bottom-Left of Hero */
.hero-project-card-box {
  background-color: rgba(7, 26, 48, 0.75);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 4px;
  padding: 1.15rem 1.35rem;
  color: #FFFFFF;
  max-width: 340px;
}

.hero-project-name {
  font-family: var(--font-serif);
  font-size: clamp(1.6rem, 3vw, 2.1rem);
  font-weight: 600;
  line-height: 1.15;
  color: #FFFFFF;
  margin-bottom: 0.25rem;
}

.hero-project-loc {
  font-size: 0.85rem;
  color: #CBD5E1;
  margin-bottom: 0.35rem;
}

.hero-project-price {
  font-size: 0.95rem;
  font-weight: 700;
  color: #FFFFFF;
  margin-bottom: 0.2rem;
}

.hero-project-possession {
  font-size: 0.8rem;
  color: #CBD5E1;
  margin-bottom: 0.2rem;
}

.hero-project-config {
  font-size: 0.825rem;
  font-weight: 600;
  color: var(--gpl-gold-light);
}

/* Bottom-Right Circular Button */
.hero-round-action-btn {
  width: 46px;
  height: 46px;
  border-radius: 50%;
  background-color: #FFFFFF;
  color: var(--gpl-navy);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);
  transition: transform 0.2s ease;
  flex-shrink: 0;
  margin-bottom: 0.5rem;
}

.hero-round-action-btn:hover {
  transform: scale(1.08);
}

/* ==========================================================================
   Breadcrumb Strip
   ========================================================================== */
.breadcrumb-strip {
  background-color: #FFFFFF;
  padding-block: 0.85rem;
  border-bottom: 1px solid var(--gpl-border);
}

.breadcrumb-nav {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  font-size: 0.775rem;
  color: #0B57D0;
  flex-wrap: wrap;
}

.breadcrumb-nav a {
  color: #0B57D0;
}

.bc-sep {
  color: #999999;
  font-size: 0.7rem;
}

.bc-current {
  color: #444444;
  font-weight: 600;
}

/* ==========================================================================
   Page Sections Standard Layout
   ========================================================================== */
.godrej-page-section {
  padding-block: clamp(2rem, 4vw, 3.5rem);
  background-color: #FFFFFF;
}

.bg-subtle-light {
  background-color: var(--gpl-bg-subtle);
}

.section-center-heading {
  font-family: var(--font-serif);
  font-size: clamp(1.6rem, 2.8vw, 2.2rem);
  font-weight: 600;
  color: var(--gpl-navy);
  text-align: center;
  margin-bottom: 1.5rem;
}

.section-center-heading-gold {
  font-family: var(--font-serif);
  font-size: clamp(1.6rem, 2.8vw, 2.2rem);
  font-weight: 600;
  color: var(--gpl-gold);
  text-align: center;
  margin-bottom: 0.5rem;
}

/* ==========================================================================
   Overview Section (Top Buttons: Enquire Now & Call Us)
   Matches media_1795093841503_d35198e2.png
   ========================================================================== */
.overview-top-actions-bar {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1.5rem;
  margin-bottom: 1.5rem;
}

.btn-action-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.9rem;
  font-weight: 600;
  color: #000000;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  transition: all 0.2s ease;
}

.btn-action-pill svg {
  color: #000000;
}

.btn-action-pill:hover {
  background-color: var(--gpl-bg-subtle);
  color: var(--gpl-navy);
}

.overview-main-text {
  font-size: 0.95rem;
  color: #333333;
  line-height: 1.7;
  text-align: left;
  margin-bottom: 1.5rem;
}

.overview-landscape-media {
  border-radius: 4px;
  overflow: hidden;
  margin-bottom: 1.5rem;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.06);
}

.overview-landscape-media img {
  width: 100%;
  height: auto;
  object-fit: cover;
}

.overview-spec-pills-row {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 0.75rem;
  margin-top: 1.25rem;
}

.spec-pill-box {
  background-color: var(--gpl-bg-subtle);
  border: 1px solid var(--gpl-border);
  border-radius: 4px;
  padding: 0.85rem 0.5rem;
  text-align: center;
}

.sp-val {
  display: block;
  font-weight: 700;
  font-size: 1.05rem;
  color: var(--gpl-navy);
}

.sp-lbl {
  font-size: 0.72rem;
  color: var(--gpl-text-muted);
  text-transform: uppercase;
}

/* ==========================================================================
   Neighbourhood Section
   Matches media_1795093841503_d35198e2.png
   ========================================================================== */
.neighbourhood-map-wrapper {
  border-radius: 6px;
  overflow: hidden;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
  border: 1px solid var(--gpl-border);
  margin-bottom: 1.5rem;
}

.transit-distances-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0.75rem;
}

.transit-item {
  background-color: var(--gpl-bg-subtle);
  border: 1px solid var(--gpl-border);
  border-radius: 4px;
  padding: 0.75rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.t-name {
  font-size: 0.825rem;
  font-weight: 500;
  color: var(--gpl-text);
}

.t-time {
  font-weight: 700;
  font-size: 0.85rem;
  color: var(--gpl-gold);
}

/* ==========================================================================
   Price Section (Gold Bar Table)
   Matches media_1795093841503_d35198e2.png
   ========================================================================== */
.official-price-table-card {
  border: 1px solid var(--gpl-border);
  border-radius: 4px;
  overflow: hidden;
  background-color: #FFFFFF;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.04);
  max-width: 600px;
  margin-inline: auto;
}

.price-table-gold-bar {
  background-color: var(--gpl-gold);
  color: #FFFFFF;
  padding: 0.65rem 1.25rem;
  font-weight: 600;
  font-size: 1.05rem;
}

.price-table-rows {
  display: flex;
  flex-direction: column;
}

.price-table-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 1.25rem;
  border-bottom: 1px solid var(--gpl-border);
}

.price-table-row:last-child {
  border-bottom: none;
}

.row-config-title {
  font-size: 1rem;
  font-weight: 600;
  color: #000000;
}

.row-config-price {
  display: flex;
  align-items: baseline;
  gap: 0.35rem;
}

.row-config-price .currency-symbol {
  font-size: 1.1rem;
  font-weight: 600;
  color: #000000;
}

.row-config-price .price-num {
  font-size: 1.15rem;
  font-weight: 700;
  color: #000000;
}

.row-config-price .onwards-text {
  font-size: 0.8rem;
  color: #666666;
}

.row-config-price .avail-req-text {
  font-size: 0.95rem;
  font-weight: 600;
  color: #444444;
}

.price-charges-disclaimer {
  font-size: 0.78rem;
  color: #777777;
  font-style: italic;
  margin-top: 0.85rem;
  text-align: center;
}

/* ==========================================================================
   EMI Calculator Section
   Matches media_1795093841503_d35198e2.png
   ========================================================================== */
.godrej-emi-card {
  background-color: #FFFFFF;
  border: 1px solid var(--gpl-border);
  border-radius: 6px;
  padding: clamp(1.5rem, 3vw, 2.25rem);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
  max-width: 600px;
  margin-inline: auto;
}

.emi-card-title {
  font-family: var(--font-serif);
  font-size: 1.4rem;
  font-weight: 600;
  color: #000000;
  margin-bottom: 1.25rem;
}

.emi-input-field-block {
  margin-bottom: 1.5rem;
}

.emi-field-lbl {
  display: block;
  font-size: 0.825rem;
  color: #666666;
  margin-bottom: 0.35rem;
}

.emi-input-currency-wrapper {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid #CCCCCC;
  padding-bottom: 0.35rem;
}

.emi-num-input {
  font-size: 1.4rem;
  font-weight: 700;
  color: #000000;
  border: none;
  outline: none;
  width: 100%;
  background: transparent;
}

.emi-input-rupee {
  font-size: 1.4rem;
  font-weight: 600;
  color: #000000;
  padding-left: 0.5rem;
}

.emi-slider-block {
  margin-bottom: 1.5rem;
}

.emi-slider-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.85rem;
  color: #333333;
  margin-bottom: 0.5rem;
}

.emi-pill-badge {
  border: 1px solid #CCCCCC;
  border-radius: 12px;
  padding: 0.15rem 0.65rem;
  font-size: 0.775rem;
  font-weight: 600;
  color: #000000;
}

.emi-range-track {
  width: 100%;
  height: 4px;
  background-color: #E0E0E0;
  border-radius: 2px;
  outline: none;
  -webkit-appearance: none;
  cursor: pointer;
}

.emi-range-track::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background-color: #333333;
  cursor: pointer;
}

.emi-slider-subtext,
.emi-slider-minmax {
  display: flex;
  justify-content: space-between;
  font-size: 0.75rem;
  color: #777777;
  margin-top: 0.35rem;
}

.emi-monthly-result-box {
  margin-top: 1.75rem;
  padding-top: 1.25rem;
  border-top: 1px dashed var(--gpl-border);
}

.emi-res-lbl {
  font-size: 0.85rem;
  color: #666666;
  display: block;
}

.emi-res-amount-line {
  display: flex;
  align-items: baseline;
  gap: 0.5rem;
  margin-top: 0.25rem;
}

.emi-res-amount-line strong {
  font-size: 1.65rem;
  font-weight: 700;
  color: #000000;
}

.per-mo-txt {
  font-size: 0.85rem;
  color: #888888;
}

/* ==========================================================================
   Gallery Section (Preview Cards + View Gallery Button)
   Matches media_1795093841503_d35198e2.png
   ========================================================================== */
.gallery-preview-cards-strip {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}

.gallery-preview-card {
  border-radius: 6px;
  overflow: hidden;
  height: clamp(200px, 30vw, 280px);
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
  cursor: pointer;
  transition: transform 0.2s ease;
}

.gallery-preview-card:hover {
  transform: translateY(-4px);
}

.gallery-preview-card img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.btn-view-gallery {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border: 1px solid #222222;
  border-radius: 4px;
  background-color: #FFFFFF;
  color: #222222;
  font-size: 0.875rem;
  font-weight: 600;
  padding: 0.65rem 1.75rem;
  transition: all 0.2s ease;
}

.btn-view-gallery:hover {
  background-color: #222222;
  color: #FFFFFF;
}

/* ==========================================================================
   Floor Plans Section
   ========================================================================== */
.floor-plan-pills-row {
  display: flex;
  justify-content: center;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
  flex-wrap: wrap;
}

.fp-pill-btn {
  padding: 0.5rem 1.25rem;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--gpl-text-muted);
  border: 1px solid var(--gpl-border);
  background-color: var(--gpl-bg-subtle);
  transition: all 0.2s ease;
}

.fp-pill-btn.active,
.fp-pill-btn:hover {
  background-color: var(--gpl-navy);
  color: #FFFFFF;
  border-color: var(--gpl-navy);
}

.fp-blueprint-card {
  background-color: var(--gpl-bg-subtle);
  border: 1px solid var(--gpl-border);
  border-radius: 6px;
  overflow: hidden;
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  align-items: center;
}

.fp-image-holder {
  background-color: #071A30;
  padding: 1.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.fp-image-holder img {
  max-height: 380px;
  width: auto;
  object-fit: contain;
  cursor: pointer;
}

.fp-info-panel {
  padding: 2rem;
  background-color: #FFFFFF;
}

.fp-info-panel h4 {
  font-family: var(--font-serif);
  font-size: 1.35rem;
  color: var(--gpl-navy);
  margin-bottom: 0.5rem;
}

.fp-info-panel p {
  font-size: 0.875rem;
  color: var(--gpl-text-muted);
  margin-bottom: 1.25rem;
  line-height: 1.6;
}

/* ==========================================================================
   Amenities Simple Grid
   ========================================================================== */
.amenities-simple-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.25rem;
}

.amenity-simple-card {
  background-color: #FFFFFF;
  border: 1px solid var(--gpl-border);
  border-radius: 4px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}

.amenity-simple-card img {
  width: 100%;
  height: 180px;
  object-fit: cover;
}

.amenity-simple-card h4 {
  font-size: 1rem;
  font-weight: 600;
  color: var(--gpl-navy);
  padding: 0.85rem 1rem 0.25rem;
}

.amenity-simple-card p {
  font-size: 0.8rem;
  color: var(--gpl-text-muted);
  padding: 0 1rem 1rem;
}

/* ==========================================================================
   MahaRERA Official Disclosure Box
   Matches media_1795093841503_d35198e2.png
   ========================================================================== */
.official-rera-disclosure-box {
  background-color: #FFFFFF;
  border: 1px solid var(--gpl-border);
  border-radius: 6px;
  padding: 1.5rem;
  box-shadow: 0 1px 6px rgba(0, 0, 0, 0.03);
}

.rera-qr-floating-box {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.25rem;
  padding-bottom: 1.25rem;
  border-bottom: 1px solid var(--gpl-border);
}

.rera-badge-labels {
  font-size: 0.85rem;
  line-height: 1.5;
}

.rera-badge-labels strong {
  color: var(--gpl-navy);
}

.rera-official-legal-text {
  font-size: 0.78rem;
  color: #444444;
  line-height: 1.65;
  margin-bottom: 0.85rem;
}

.rera-official-legal-text a {
  color: #0B57D0;
  text-decoration: underline;
}

/* ==========================================================================
   Get In Touch / Lead Form Section
   Matches media_1795093841503_d35198e2.png
   ========================================================================== */
.get-in-touch-subtext {
  font-size: 0.85rem;
  color: #666666;
  text-align: center;
  margin-bottom: 1.75rem;
  line-height: 1.6;
}

.get-in-touch-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.git-form-group {
  width: 100%;
}

.git-input {
  width: 100%;
  border: 1px solid var(--gpl-border);
  border-radius: 4px;
  padding: 0.85rem 1rem;
  font-size: 0.9rem;
  background-color: #FFFFFF;
  color: var(--gpl-text);
  outline: none;
}

.git-input:focus {
  border-color: var(--gpl-navy);
}

.git-phone-group {
  display: flex;
}

.git-phone-code {
  padding: 0.85rem 0.85rem;
  background-color: var(--gpl-bg-subtle);
  border: 1px solid var(--gpl-border);
  border-right: none;
  border-radius: 4px 0 0 4px;
  font-weight: 600;
  color: #555555;
  font-size: 0.9rem;
}

.git-phone-group .git-input {
  border-radius: 0 4px 4px 0;
}

.git-checkbox-line {
  display: flex;
  align-items: flex-start;
  gap: 0.5rem;
  font-size: 0.775rem;
  color: #555555;
  line-height: 1.4;
  margin-top: 0.25rem;
}

.git-checkbox-line input {
  margin-top: 2px;
}

.btn-git-submit {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background-color: #E0E0E0;
  color: #555555;
  font-weight: 600;
  font-size: 0.95rem;
  padding: 0.75rem 2.5rem;
  border-radius: 4px;
  transition: all 0.2s ease;
}

.btn-git-submit:hover {
  background-color: var(--gpl-navy);
  color: #FFFFFF;
}

/* ==========================================================================
   About Godrej Properties & Footer Accordions
   Matches media_1795093841503_d35198e2.png
   ========================================================================== */
.official-godrej-footer {
  background-color: #FFFFFF;
  border-top: 1px solid var(--gpl-border);
  padding-top: clamp(2rem, 4vw, 3rem);
  padding-bottom: 2rem;
}

.about-gpl-block {
  margin-bottom: 1.75rem;
}

.about-gpl-title {
  font-size: 1.05rem;
  font-weight: 700;
  color: #000000;
  margin-bottom: 0.5rem;
}

.about-gpl-desc {
  font-size: 0.8125rem;
  color: #555555;
  line-height: 1.65;
}

.footer-accordions-list {
  border-top: 1px solid var(--gpl-border);
  margin-bottom: 1.75rem;
}

.footer-acc-item {
  border-bottom: 1px solid var(--gpl-border);
}

.footer-acc-trigger {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.85rem 0;
  font-size: 0.95rem;
  font-weight: 500;
  color: #000000;
  text-align: left;
}

.acc-plus-icon {
  font-size: 1.25rem;
  color: #666666;
  transition: transform 0.2s ease;
}

.footer-acc-item.active .acc-plus-icon {
  transform: rotate(45deg);
}

.footer-acc-content {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.25s ease-out;
}

.footer-acc-inner {
  padding-bottom: 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
  font-size: 0.825rem;
  color: #555555;
}

.footer-acc-inner a:hover {
  color: var(--gpl-navy);
}

.footer-social-strip {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.5rem;
  padding-bottom: 1.5rem;
  border-bottom: 1px solid var(--gpl-border);
}

.follow-txt {
  font-size: 0.85rem;
  font-weight: 600;
  color: #333333;
}

.social-icons-row {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.social-icons-row a {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background-color: #333333;
  color: #FFFFFF;
  display: flex;
  align-items: center;
  justify-content: center;
}

.footer-legal-bar {
  flex-wrap: wrap;
  gap: 0.75rem;
  font-size: 0.75rem;
  color: #777777;
}

.footer-legal-links {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.sep-slash {
  color: #CCCCCC;
}

/* ==========================================================================
   Buttons
   ========================================================================== */
.btn-godrej-gold {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background-color: var(--gpl-gold);
  color: #FFFFFF;
  font-weight: 600;
  font-size: 0.875rem;
  padding: 0.65rem 1.35rem;
  border-radius: 4px;
  transition: background-color 0.2s ease;
}

.btn-godrej-gold:hover {
  background-color: var(--gpl-gold-dark);
}

.btn-godrej-navy {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background-color: var(--gpl-navy);
  color: #FFFFFF;
  font-weight: 600;
  font-size: 0.875rem;
  padding: 0.65rem 1.35rem;
  border-radius: 4px;
  transition: background-color 0.2s ease;
}

.btn-godrej-navy:hover {
  background-color: var(--gpl-navy-dark);
}

/* ==========================================================================
   Fixed Mobile Bottom Bar & Floating WhatsApp
   ========================================================================== */
.mobile-sticky-footer-bar {
  display: none;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  background-color: #FFFFFF;
  border-top: 1px solid var(--gpl-border);
  padding: 0.5rem 0.75rem;
  box-shadow: 0 -4px 16px rgba(0, 0, 0, 0.08);
}

.sticky-footer-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 0.5rem;
}

.btn-sticky-action {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.35rem;
  padding: 0.65rem 0.25rem;
  font-size: 0.8rem;
  font-weight: 600;
  border-radius: 4px;
}

.btn-sticky-action.btn-call {
  background-color: #FFFFFF;
  color: var(--gpl-navy);
  border: 1px solid var(--gpl-navy);
}

.btn-sticky-action.btn-wa {
  background-color: var(--wa-green);
  color: #FFFFFF;
}

.btn-sticky-action.btn-enquire {
  background-color: var(--gpl-gold);
  color: #FFFFFF;
}

.floating-whatsapp-pill {
  position: fixed;
  bottom: 2rem;
  right: 1.5rem;
  z-index: 990;
  width: 52px;
  height: 52px;
  border-radius: 50%;
  background-color: var(--wa-green);
  color: #FFFFFF;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 16px rgba(37, 211, 102, 0.4);
  transition: transform 0.2s ease;
}

.floating-whatsapp-pill:hover {
  transform: scale(1.1);
}

/* ==========================================================================
   Off-Canvas Mobile Drawer
   ========================================================================== */
.godrej-mobile-drawer {
  position: fixed;
  inset: 0;
  z-index: 2500;
  background-color: rgba(0, 0, 0, 0.6);
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.25s ease;
}

.godrej-mobile-drawer.open {
  opacity: 1;
  pointer-events: auto;
}

.drawer-inner-box {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  width: 82%;
  max-width: 320px;
  background-color: #FFFFFF;
  padding: 1.5rem 1.25rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transform: translateX(100%);
  transition: transform 0.25s ease;
  overflow-y: auto;
}

.godrej-mobile-drawer.open .drawer-inner-box {
  transform: translateX(0);
}

.drawer-header {
  padding-bottom: 1rem;
  border-bottom: 1px solid var(--gpl-border);
}

.drawer-close-btn {
  font-size: 1.75rem;
  color: #222222;
}

.drawer-nav-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  padding-block: 1.25rem;
}

.drawer-link {
  font-size: 0.95rem;
  font-weight: 500;
  color: #111111;
}

.drawer-contact-footer {
  padding-top: 1rem;
  border-top: 1px solid var(--gpl-border);
  font-size: 0.825rem;
  color: #555555;
}

/* ==========================================================================
   Modals & Lightbox
   ========================================================================== */
.modal-overlay {
  position: fixed;
  inset: 0;
  z-index: 3000;
  background-color: rgba(7, 26, 48, 0.7);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1rem;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s ease;
}

.modal-overlay.open {
  opacity: 1;
  pointer-events: auto;
}

.modal-card-box {
  background-color: #FFFFFF;
  width: 100%;
  max-width: 480px;
  border-radius: 6px;
  overflow: hidden;
  position: relative;
  box-shadow: 0 12px 36px rgba(0, 0, 0, 0.2);
}

.modal-close-icon {
  position: absolute;
  top: 1rem;
  right: 1rem;
  font-size: 1.5rem;
  color: #444444;
}

.modal-header-top {
  padding: 1.5rem 1.5rem 0.75rem;
  border-bottom: 1px solid var(--gpl-border);
}

.m-tag {
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  color: var(--gpl-gold);
}

.m-title {
  font-family: var(--font-serif);
  font-size: 1.35rem;
  color: var(--gpl-navy);
}

.modal-body-area {
  padding: 1.25rem 1.5rem 1.75rem;
}

.form-group-line {
  margin-bottom: 0.85rem;
}

.form-lbl {
  display: block;
  font-size: 0.78rem;
  font-weight: 600;
  margin-bottom: 0.25rem;
}

.form-ctrl {
  width: 100%;
  padding: 0.65rem 0.85rem;
  border: 1px solid var(--gpl-border);
  border-radius: 4px;
  font-size: 0.875rem;
  outline: none;
}

.phone-box-flex {
  display: flex;
}

.phone-tag {
  padding: 0.65rem 0.75rem;
  background-color: var(--gpl-bg-subtle);
  border: 1px solid var(--gpl-border);
  border-right: none;
  border-radius: 4px 0 0 4px;
  font-size: 0.85rem;
  font-weight: 600;
}

.phone-box-flex .form-ctrl {
  border-radius: 0 4px 4px 0;
}

/* Lightbox */
.lightbox-overlay {
  position: fixed;
  inset: 0;
  z-index: 4000;
  background-color: rgba(7, 26, 48, 0.95);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s ease;
  padding: 1rem;
}

.lightbox-overlay.open {
  opacity: 1;
  pointer-events: auto;
}

.lightbox-img-holder {
  max-width: 90vw;
  max-height: 80vh;
}

.lightbox-img-holder img {
  max-width: 100%;
  max-height: 80vh;
  object-fit: contain;
}

.lightbox-text-caption {
  color: #FFFFFF;
  margin-top: 1rem;
  font-size: 1.1rem;
  text-align: center;
}

.lightbox-nav-arrow {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.15);
  color: #FFFFFF;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.35rem;
}

.lightbox-prev-arrow { left: 1.25rem; }
.lightbox-next-arrow { right: 1.25rem; }

/* ==========================================================================
   RESPONSIVE BREAKPOINTS (Pixel-Perfect on All Screens)
   ========================================================================== */
@media (max-width: 768px) {
  body {
    padding-bottom: 60px; /* Space for sticky bar */
  }
  .desktop-only-flex {
    display: none;
  }
  .mobile-sticky-footer-bar {
    display: block;
  }
  .floating-whatsapp-pill {
    bottom: 4.8rem;
    right: 1.25rem;
    width: 48px;
    height: 48px;
  }
  .overview-spec-pills-row {
    grid-template-columns: repeat(2, 1fr);
  }
  .transit-distances-grid {
    grid-template-columns: 1fr;
  }
  .gallery-preview-cards-strip {
    grid-template-columns: 1fr;
    max-width: 340px;
    margin-inline: auto;
  }
  .fp-blueprint-card {
    grid-template-columns: 1fr;
  }
  .amenities-simple-grid {
    grid-template-columns: 1fr;
  }
}

@media (min-width: 769px) {
  .gallery-preview-cards-strip {
    grid-template-columns: repeat(3, 1fr);
  }
}
"""

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(STYLES_CSS)

print("Written pixel-perfect styles.css matching official Godrej mobile/desktop design!")
