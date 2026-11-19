/**
 * GODREJ ELANOR MAHALUNGE — EDITORIAL ARCHITECTURE CONTROLLER
 * Zero-dependency Vanilla JavaScript
 */

document.addEventListener('DOMContentLoaded', () => {
  initHeader();
  initMobileDrawer();
  initFloorPlanTabs();
  initGalleryLightbox();
  initFaqAccordion();
  initEmiCalculator();
  initModals();
  initForms();
  initSmoothScroll();
});

/* ==========================================================================
   Header Transformation on Scroll
   ========================================================================== */
function initHeader() {
  const header = document.querySelector('.site-header');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 30) {
      header?.classList.add('scrolled');
    } else {
      header?.classList.remove('scrolled');
    }
  }, { passive: true });
}

/* ==========================================================================
   Mobile Navigation Drawer
   ========================================================================== */
function initMobileDrawer() {
  const toggleBtn = document.querySelector('.mobile-nav-toggle');
  const drawer = document.getElementById('mobileDrawer');
  const closeBtn = document.getElementById('mobileCloseBtn');
  const navLinks = drawer?.querySelectorAll('a');

  function openDrawer() {
    drawer?.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeDrawer() {
    drawer?.classList.remove('open');
    document.body.style.overflow = '';
  }

  toggleBtn?.addEventListener('click', openDrawer);
  closeBtn?.addEventListener('click', closeDrawer);

  drawer?.addEventListener('click', (e) => {
    if (e.target === drawer) closeDrawer();
  });

  navLinks?.forEach(link => {
    link.addEventListener('click', closeDrawer);
  });
}

/* ==========================================================================
   Blueprint & Floor Plan Tabs
   ========================================================================== */
function initFloorPlanTabs() {
  const tabBtns = document.querySelectorAll('.plan-pill-btn[data-tab]');
  const tabPanes = document.querySelectorAll('.plan-tab-pane');

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetId = btn.getAttribute('data-tab');

      tabBtns.forEach(b => b.classList.remove('active'));
      tabPanes.forEach(p => {
        p.style.display = 'none';
        p.classList.remove('active');
      });

      btn.classList.add('active');
      const targetPane = document.getElementById(targetId);
      if (targetPane) {
        targetPane.style.display = 'block';
        targetPane.classList.add('active');
      }
    });
  });
}

/* ==========================================================================
   Gallery Lightbox System
   ========================================================================== */
function initGalleryLightbox() {
  const lightbox = document.getElementById('lightboxModal');
  const lightboxImg = document.getElementById('lightboxImg');
  const lightboxCaption = document.getElementById('lightboxCaption');
  const closeBtn = document.getElementById('lightboxCloseBtn');
  const prevBtn = document.querySelector('.lightbox-prev');
  const nextBtn = document.querySelector('.lightbox-next');

  let triggers = Array.from(document.querySelectorAll('[data-lightbox-src]'));
  let currentIndex = 0;

  triggers.forEach((trigger, idx) => {
    trigger.addEventListener('click', () => {
      currentIndex = idx;
      showItem(currentIndex);
    });
  });

  function showItem(index) {
    if (!triggers[index] || !lightbox || !lightboxImg) return;
    const item = triggers[index];
    const src = item.getAttribute('data-lightbox-src') || item.querySelector('img')?.src;
    const caption = item.getAttribute('data-title') || 'Godrej Elanor Mahalunge';

    lightboxImg.src = src;
    if (lightboxCaption) lightboxCaption.textContent = caption;
    lightbox.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    lightbox?.classList.remove('open');
    document.body.style.overflow = '';
  }

  function showNext() {
    currentIndex = (currentIndex + 1) % triggers.length;
    showItem(currentIndex);
  }

  function showPrev() {
    currentIndex = (currentIndex - 1 + triggers.length) % triggers.length;
    showItem(currentIndex);
  }

  closeBtn?.addEventListener('click', closeLightbox);
  nextBtn?.addEventListener('click', (e) => { e.stopPropagation(); showNext(); });
  prevBtn?.addEventListener('click', (e) => { e.stopPropagation(); showPrev(); });

  lightbox?.addEventListener('click', (e) => {
    if (e.target === lightbox || e.target.classList.contains('lightbox-img-wrap')) {
      closeLightbox();
    }
  });

  document.addEventListener('keydown', (e) => {
    if (!lightbox?.classList.contains('open')) return;
    if (e.key === 'Escape') closeLightbox();
    if (e.key === 'ArrowRight') showNext();
    if (e.key === 'ArrowLeft') showPrev();
  });
}

/* ==========================================================================
   Editorial FAQ Accordion
   ========================================================================== */
function initFaqAccordion() {
  const items = document.querySelectorAll('.faq-item-editorial');

  items.forEach(item => {
    const trigger = item.querySelector('.faq-trigger-editorial');
    const answer = item.querySelector('.faq-answer-editorial');

    trigger?.addEventListener('click', () => {
      const isOpen = item.classList.contains('active');

      // Close all
      items.forEach(other => {
        other.classList.remove('active');
        const otherAns = other.querySelector('.faq-answer-editorial');
        if (otherAns) otherAns.style.maxHeight = null;
      });

      if (!isOpen && answer) {
        item.classList.add('active');
        answer.style.maxHeight = answer.scrollHeight + 'px';
      }
    });
  });

  // Open first by default
  if (items[0]) {
    items[0].classList.add('active');
    const firstAns = items[0].querySelector('.faq-answer-editorial');
    if (firstAns) firstAns.style.maxHeight = firstAns.scrollHeight + 'px';
  }
}

/* ==========================================================================
   Home Loan & EMI Estimator
   ========================================================================== */
function initEmiCalculator() {
  const loanSlider = document.getElementById('calcLoan');
  const loanVal = document.getElementById('calcLoanVal');
  const tenorSlider = document.getElementById('calcTenor');
  const tenorVal = document.getElementById('calcTenorVal');
  const rateSlider = document.getElementById('calcRate');
  const rateVal = document.getElementById('calcRateVal');

  const emiDisplay = document.getElementById('calcMonthlyEmi');
  const principalDisplay = document.getElementById('calcPrincipal');
  const interestDisplay = document.getElementById('calcInterest');
  const totalDisplay = document.getElementById('calcTotal');

  function calculate() {
    if (!loanSlider || !tenorSlider || !rateSlider) return;

    const P = parseFloat(loanSlider.value) * 100000;
    const N = parseFloat(tenorSlider.value) * 12;
    const annualRate = parseFloat(rateSlider.value);
    const R = (annualRate / 12) / 100;

    const emi = (P * R * Math.pow(1 + R, N)) / (Math.pow(1 + R, N) - 1);
    const totalPayable = emi * N;
    const totalInterest = totalPayable - P;

    if (loanVal) loanVal.textContent = `₹ ${parseFloat(loanSlider.value) >= 100 ? (parseFloat(loanSlider.value)/100).toFixed(2) + ' Cr' : loanSlider.value + ' Lacs'}`;
    if (tenorVal) tenorVal.textContent = `${tenorSlider.value} Years`;
    if (rateVal) rateVal.textContent = `${annualRate.toFixed(1)}% p.a.`;

    if (emiDisplay) emiDisplay.textContent = `₹ ${Math.round(emi).toLocaleString('en-IN')}`;
    if (principalDisplay) principalDisplay.textContent = `₹ ${Math.round(P).toLocaleString('en-IN')}`;
    if (interestDisplay) interestDisplay.textContent = `₹ ${Math.round(totalInterest).toLocaleString('en-IN')}`;
    if (totalDisplay) totalDisplay.textContent = `₹ ${Math.round(totalPayable).toLocaleString('en-IN')}`;
  }

  [loanSlider, tenorSlider, rateSlider].forEach(s => s?.addEventListener('input', calculate));
  calculate();
}

/* ==========================================================================
   Modals Management
   ========================================================================== */
function initModals() {
  window.openModal = function(modalId, configPrefill = '') {
    const modal = document.getElementById(modalId);
    if (!modal) return;

    if (configPrefill) {
      const select = modal.querySelector('select[name="configuration"]');
      if (select) select.value = configPrefill;
    }

    modal.classList.add('open');
    document.body.style.overflow = 'hidden';
  };

  window.closeModal = function(modalId) {
    const modal = document.getElementById(modalId);
    if (!modal) return;
    modal.classList.remove('open');
    document.body.style.overflow = '';
  };

  document.querySelectorAll('[data-open-modal]').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const modalId = btn.getAttribute('data-open-modal');
      const prefill = btn.getAttribute('data-prefill') || '';
      window.openModal(modalId, prefill);
    });
  });

  document.querySelectorAll('.modal-close-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const modal = btn.closest('.modal-overlay');
      if (modal) {
        modal.classList.remove('open');
        document.body.style.overflow = '';
      }
    });
  });

  document.querySelectorAll('.modal-overlay').forEach(overlay => {
    overlay.addEventListener('click', (e) => {
      if (e.target === overlay) {
        overlay.classList.remove('open');
        document.body.style.overflow = '';
      }
    });
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      document.querySelectorAll('.modal-overlay').forEach(m => m.classList.remove('open'));
      document.body.style.overflow = '';
    }
  });
}

/* ==========================================================================
   Form Handling & Lead Confirmation
   ========================================================================== */
function initForms() {
  const forms = document.querySelectorAll('form[data-lead-form]');

  forms.forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();

      const nameInput = form.querySelector('input[name="name"]');
      const phoneInput = form.querySelector('input[name="phone"]');
      const configInput = form.querySelector('select[name="configuration"]');
      const dateInput = form.querySelector('input[name="visit_date"]');

      const name = nameInput ? nameInput.value.trim() : '';
      const phone = phoneInput ? phoneInput.value.trim() : '';
      const config = configInput ? configInput.value : '3 BHK Premium';
      const visitDate = dateInput ? dateInput.value : '';

      const cleanPhone = phone.replace(/[^0-9]/g, '');
      if (cleanPhone.length < 10) {
        showToast('Please enter a valid 10-digit mobile number.', 'error');
        phoneInput?.focus();
        return;
      }

      if (!name) {
        showToast('Please enter your full name.', 'error');
        nameInput?.focus();
        return;
      }

      const submitBtn = form.querySelector('button[type="submit"]');
      const originalText = submitBtn ? submitBtn.innerHTML : '';
      if (submitBtn) {
        submitBtn.innerHTML = 'Securing Priority...';
        submitBtn.disabled = true;
      }

      const leadData = {
        name,
        phone: cleanPhone,
        configuration: config,
        visitDate,
        timestamp: new Date().toISOString(),
        project: 'Godrej Elanor Mahalunge, Pune'
      };

      try {
        const stored = JSON.parse(localStorage.getItem('godrej_elanor_leads') || '[]');
        stored.push(leadData);
        localStorage.setItem('godrej_elanor_leads', JSON.stringify(stored));
      } catch (err) {
        console.warn('LocalStorage unavailable', err);
      }

      setTimeout(() => {
        if (submitBtn) {
          submitBtn.innerHTML = originalText;
          submitBtn.disabled = false;
        }

        form.reset();

        document.querySelectorAll('.modal-overlay').forEach(m => m.classList.remove('open'));
        document.body.style.overflow = '';

        const successModal = document.getElementById('successModal');
        if (successModal) {
          document.getElementById('successLeadName').textContent = name;
          document.getElementById('successLeadPhone').textContent = `+91 ${cleanPhone}`;
          document.getElementById('successRefId').textContent = 'GE-' + Math.floor(10000 + Math.random() * 90000);
          successModal.classList.add('open');
          document.body.style.overflow = 'hidden';
        } else {
          showToast(`Thank you, ${name}! Your request has been acknowledged.`);
        }
      }, 600);
    });
  });
}

/* ==========================================================================
   Toast Notification System
   ========================================================================== */
function showToast(message, type = 'success') {
  let container = document.querySelector('.toast-container');
  if (!container) {
    container = document.createElement('div');
    container.className = 'toast-container';
    document.body.appendChild(container);
  }

  const toast = document.createElement('div');
  toast.className = 'toast';
  if (type === 'error') toast.style.borderColor = '#E57373';

  toast.innerHTML = `
    <span style="font-weight: 700; color: ${type === 'error' ? '#E57373' : 'var(--accent-terracotta)'}">•</span>
    <span>${message}</span>
  `;

  container.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transition = 'opacity 0.3s ease';
    setTimeout(() => toast.remove(), 300);
  }, 4000);
}

/* ==========================================================================
   Smooth Scrolling
   ========================================================================== */
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#' || targetId === '') return;

      const target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        const headerHeight = document.querySelector('.site-header')?.offsetHeight || 75;
        const top = target.getBoundingClientRect().top + window.scrollY - headerHeight + 5;
        window.scrollTo({
          top: top,
          behavior: 'smooth'
        });
      }
    });
  });
}

/* ==========================================================================
   Brochure Download Helper
   ========================================================================== */
window.downloadBrochureFile = function() {
  showToast('Downloading Godrej Elanor Project Factsheet...');
  
  setTimeout(() => {
    const factsheetContent = `
================================================================================
                    GODREJ ELANOR MAHALUNGE, PUNE
                    French Riverside Living by Godrej Properties
================================================================================

PROJECT OVERVIEW:
• Developer: Godrej Properties Ltd. (127+ Years of Trust)
• Location: Mahalunge, Baner-Hinjawadi IT Corridor, Pune - 411045
• MahaRERA Registration: PR1260002602617
• Channel Partner RERA: A51900029955 (PropSolutions4U Pvt. Ltd.)
• Land Parcel: 8.5 Acres (French-inspired architecture)
• Open Green Spaces: Approx. 5 Acres
• Structure: Basement + Ground + 3 Podiums + 35 Residential Floors
• Towers: 5 Residential Towers (Phase 1 launch: 2 Towers)
• Density: Low-density design with 8 residences per floor & 7 high-speed lifts

CONFIGURATIONS & PRICING:
1. 3 BHK Premium:
   - Carpet Area: 1,270 – 1,280 Sq. Ft.
   - Price: ₹ 1.90 – 2.03 Cr* (All Inclusive)
   - Features: Expansive running decks, cross-ventilation, French river views.

2. 3 BHK Luxe:
   - Carpet Area: 1,310 Sq. Ft.
   - Price: ₹ 1.96 – 2.09 Cr* (All Inclusive)
   - Features: Ultra-spacious master suite with private deck, panoramic river vistas.

3. 4 BHK Duplex Residences:
   - Carpet Area: On Request (Floors 32 to 35)
   - Price: ₹ On Request*
   - Features: Crowning top 4 floors, double-height living, grand riverside decks.

KEY HIGHLIGHTS & RIVERFRONT AMENITIES:
• Nearly 1,00,000 Sq. Ft. of Curated Riverfront Amenities
• Twin Designer Clubhouses: 18,000 Sq. Ft. and 12,000 Sq. Ft. (30,000 Sq. Ft. total)
• Grand Infinity-Edge Swimming Pool & Sun Deck
• Riverfront Promenade & Nature Boardwalk
• Professional Badminton & Squash Courts
• High-Tech Fitness Studio & Crossfit Zone
• 36-metre Main & 15-metre Internal Arterial Roads
• Expression of Interest (EOI) starting at ₹ 1 Lakh*

LOCATION & TRANSIT ADVANTAGES:
• Hinjewadi IT Park: 9 Mins
• Mumbai-Pune Expressway / NH 48: 12 Mins
• Balewadi Metro Station: 14 Mins
• Baner / Wakad: 16 Mins
• Symbiosis University: 14 Mins
• Ruby Hall Clinic: 11 Mins
• Pune Airport: 35 Mins

SALES & SITE VISIT DESK:
• Phone: +91 91755 51405
• Address: Godrej Elanor, Riverfront Road, Mahalunge, Pune - 411045
================================================================================
    `;

    const blob = new Blob([factsheetContent], { type: 'text/plain;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'Godrej-Elanor-Mahalunge-Factsheet.txt';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);

    showToast('Factsheet downloaded successfully!');
  }, 800);
};
