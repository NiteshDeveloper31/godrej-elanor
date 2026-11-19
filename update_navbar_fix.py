# -*- coding: utf-8 -*-
"""
Perfect fixed Header & Subnav matching media_1795095536336_5ec03fb4.png
"""

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace header and subnav CSS completely with fixed, rock-solid layout
old_hdr_section = css[css.find('/* ==========================================================================\n   1. TOP HEADER'):css.find('/* ==========================================================================\n   3. BREADCRUMBS')]

new_hdr_section = r'''/* ==========================================================================
   1. TOP HEADER & SUB-NAVIGATION (Fixed, Zero-Jump, Exact Godrej Architecture)
   ========================================================================== */
.godrej-site-header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  width: 100%;
  height: 64px;
  background-color: #FFFFFF;
  border-bottom: 1px solid #E7E7E7;
  z-index: 1000;
  display: flex;
  align-items: center;
}

.header-inner-container {
  width: 100%;
  max-width: 1320px;
  margin: 0 auto;
  padding: 0 1.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.header-brand-link {
  display: flex;
  align-items: center;
  text-decoration: none;
  flex-shrink: 0;
}

.header-logo-gpl {
  height: 32px;
  width: auto;
  max-width: 150px;
  display: block;
}

.header-right-group {
  display: flex;
  align-items: center;
  gap: 0.85rem;
  flex-shrink: 0;
}

.hdr-icon-circle {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  background: #F4F4F4;
  border: none;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: background 0.2s ease, transform 0.2s ease;
}

.hdr-icon-circle:hover {
  background: #EAEAEA;
  transform: scale(1.05);
}

.header-script-link {
  display: flex;
  align-items: center;
  text-decoration: none;
  margin-left: 0.5rem;
  flex-shrink: 0;
}

.header-logo-script {
  height: 28px;
  width: auto;
  max-width: 65px;
  display: block;
}

@media (max-width: 768px) {
  .godrej-site-header {
    height: 56px;
  }
  .header-inner-container {
    padding: 0 0.85rem;
  }
  .header-logo-gpl {
    height: 24px;
    max-width: 110px;
  }
  .header-right-group {
    gap: 0.45rem;
  }
  .hdr-icon-circle {
    width: 32px;
    height: 32px;
  }
  .hdr-icon-circle svg {
    width: 16px;
    height: 16px;
  }
  .header-logo-script {
    height: 22px;
    max-width: 45px;
    margin-left: 0.2rem;
  }
}

/* Sub-Navigation Bar: Fixed directly under the white header */
.hero-subnav-bar {
  position: fixed;
  top: 64px;
  left: 0;
  right: 0;
  width: 100%;
  height: 48px;
  z-index: 990;
  background-color: var(--gpl-navy-dark);
  border-bottom: 1px solid rgba(255, 255, 255, 0.12);
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.15);
}

@media (max-width: 768px) {
  .hero-subnav-bar {
    top: 56px;
    height: 44px;
    overflow-x: auto;
    overflow-y: hidden;
    -webkit-overflow-scrolling: touch;
  }
}

.subnav-inner-container {
  width: 100%;
  max-width: 1320px;
  margin: 0 auto;
  padding: 0 1.5rem;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

@media (max-width: 768px) {
  .subnav-inner-container {
    padding: 0 0.85rem;
    width: max-content;
    min-width: 100%;
    justify-content: flex-start;
    gap: 1.25rem;
  }
}

.subnav-back-link {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #FFFFFF;
  text-decoration: none;
  font-size: 15px;
  font-weight: 500;
  flex-shrink: 0;
  transition: opacity 0.2s ease;
}

.subnav-back-link:hover {
  opacity: 0.85;
}

.subnav-links-list {
  display: flex;
  align-items: center;
  gap: 2.25rem;
  list-style: none;
  margin: 0;
  padding: 0;
  flex-shrink: 0;
}

@media (max-width: 768px) {
  .subnav-links-list {
    gap: 1.25rem;
  }
}

.subnav-links-list a {
  color: #FFFFFF;
  text-decoration: none;
  font-size: 15px;
  font-weight: 500;
  padding: 4px 0;
  border-bottom: 2px solid transparent;
  transition: border-color 0.2s ease, opacity 0.2s ease;
  white-space: nowrap;
}

.subnav-links-list a.active,
.subnav-links-list a:hover {
  border-bottom-color: var(--gpl-gold);
  color: #FFFFFF;
}

/* ==========================================================================
   2. HERO BANNER SECTION (Starts below fixed 112px headers)
   ========================================================================== */
.godrej-hero-section {
  position: relative;
  width: 100%;
  margin-top: 112px; /* 64px header + 48px subnav */
  height: calc(85vh - 112px);
  min-height: 540px;
  max-height: 780px;
  background-color: var(--gpl-navy-dark);
  overflow: hidden;
}

@media (max-width: 768px) {
  .godrej-hero-section {
    margin-top: 100px; /* 56px + 44px */
    height: calc(75vh - 100px);
    min-height: 440px;
  }
}

.hero-picture-bg,
.hero-bg-media {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
}

/* Subtle lighting overlay leaving building sharp & bright */
.hero-lighting-overlay {
  position: absolute;
  inset: 0;
  z-index: 2;
  pointer-events: none;
  background: linear-gradient(
    180deg,
    rgba(0, 0, 0, 0.25) 0%,
    rgba(0, 0, 0, 0) 30%,
    rgba(0, 0, 0, 0.2) 100%
  );
}

/* Floating Card at Bottom-Left */
.hero-floating-card-wrapper {
  position: absolute;
  bottom: 2.5rem;
  left: 2.5rem;
  z-index: 5;
  max-width: 680px;
}

@media (max-width: 768px) {
  .hero-floating-card-wrapper {
    bottom: 1.5rem;
    left: 1rem;
    right: 4.5rem;
    max-width: none;
  }
}

.property-details-info {
  background: rgba(0, 0, 0, 0.40);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.18);
  border-radius: 4px;
  padding: 1.35rem 1.85rem;
  color: #FFFFFF;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.25);
}

@media (max-width: 768px) {
  .property-details-info {
    padding: 0.85rem 1rem;
  }
}

.hero-project-title {
  font-family: var(--gpl-font-sans);
  font-size: clamp(1.6rem, 3.2vw, 2.3rem);
  font-weight: 600;
  line-height: 1.15;
  color: #FFFFFF;
  margin: 0 0 0.25rem 0;
  text-shadow: 0 2px 6px rgba(0, 0, 0, 0.6);
}

.hero-project-sub {
  font-family: var(--gpl-font-sans);
  font-size: 0.95rem;
  color: rgba(255, 255, 255, 0.95);
  margin-bottom: 0.75rem;
  text-shadow: 0 1px 4px rgba(0, 0, 0, 0.6);
}

.hero-specs-row {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 0.4rem 0.85rem;
  font-size: 14.5px;
  color: #FFFFFF;
  text-shadow: 0 1px 4px rgba(0, 0, 0, 0.6);
}

.hero-spec-item b {
  font-weight: 600;
  margin-right: 4px;
}

.hero-spec-sep {
  opacity: 0.6;
}

/* Bottom-Right Circular Action Button */
.hero-action-circle-wrap {
  position: absolute;
  bottom: 2.5rem;
  right: 2.5rem;
  z-index: 5;
}

@media (max-width: 768px) {
  .hero-action-circle-wrap {
    bottom: 1.5rem;
    right: 1rem;
  }
}

.hero-circle-plus-btn {
  width: 52px;
  height: 52px;
  border-radius: 50%;
  background: #FFFFFF;
  border: 3.5px solid #6BA4D9;
  box-shadow: 0 4px 18px rgba(0, 0, 0, 0.35);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.hero-circle-plus-btn:hover {
  transform: scale(1.08);
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.45);
}

'''

css = css.replace(old_hdr_section, new_hdr_section)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("styles.css updated with rock-solid fixed header & subnav!")
