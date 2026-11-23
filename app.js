/**
 * GODREJ ELANOR MAHALUNGE — MASTER CONTROLLER
 * Zero-dependency Vanilla JavaScript matching official Godrej UX
 */

document.addEventListener('DOMContentLoaded', () => {
  initSubNavScroll();
  initMobileDrawer();
  initFloorPlanTabs();
  initEmiCalculator();
  initGalleryLightbox();
  initFooterAccordion();
  initModals();
  initLeadForms();
});

/* ==========================================================================
   1. Sub-Navigation Sticky & Smooth Scroll & Active Indicator
   ========================================================================== */
function initSubNavScroll() {
  const subNav = document.getElementById('subNav');
  const navLinks = document.querySelectorAll('.subnav-links-list a[href^="#"], .drawer-link[href^="#"], .breadcrumb-trail a[href^="#"]');
  const sections = Array.from(document.querySelectorAll('section[id]'));
  const topLinks = document.querySelectorAll('.header-brand-link, .header-script-link, a[href="#hero"]');

  // Smooth scroll to top when clicking logos or Home
  topLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
      // Close mobile drawer if open
      const drawer = document.getElementById('mobileDrawer');
      if (drawer && drawer.classList.contains('open')) {
        drawer.classList.remove('open');
        document.body.style.overflow = '';
      }
    });
  });

  // Smooth scroll for in-page anchors
  navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      const targetId = link.getAttribute('href');
      if (!targetId || targetId === '#') return;
      if (targetId === '#hero') {
        e.preventDefault();
        window.scrollTo({ top: 0, behavior: 'smooth' });
        return;
      }
      
      const targetEl = document.querySelector(targetId);
      if (targetEl) {
        e.preventDefault();
        const headerHeight = 114;
        const targetTop = targetEl.getBoundingClientRect().top + window.scrollY - headerHeight + 5;
        
        window.scrollTo({
          top: targetTop,
          behavior: 'smooth'
        });

        // Close mobile drawer if open
        const drawer = document.getElementById('mobileDrawer');
        if (drawer && drawer.classList.contains('open')) {
          drawer.classList.remove('open');
          document.body.style.overflow = '';
        }
      }
    });
  });

  // Active section indicator on scroll
  window.addEventListener('scroll', () => {
    const scrollPos = window.scrollY + 140;
    
    sections.forEach(sec => {
      const top = sec.offsetTop;
      const height = sec.offsetHeight;
      const id = sec.getAttribute('id');
      
      if (scrollPos >= top && scrollPos < top + height) {
        document.querySelectorAll('.subnav-links-list a').forEach(a => {
          if (a.getAttribute('href') === `#${id}`) {
            a.classList.add('active');
          } else {
            a.classList.remove('active');
          }
        });
      }
    });
  }, { passive: true });
}

/* ==========================================================================
   2. Mobile Drawer Navigation
   ========================================================================== */
function initMobileDrawer() {
  const toggleBtn = document.getElementById('navToggleBtn');
  const drawer = document.getElementById('mobileDrawer');
  const closeBtn = document.getElementById('drawerCloseBtn');

  function openDrawer() {
    if (drawer) {
      drawer.classList.add('open');
      document.body.style.overflow = 'hidden';
    }
  }

  function closeDrawer() {
    if (drawer) {
      drawer.classList.remove('open');
      document.body.style.overflow = '';
    }
  }

  toggleBtn?.addEventListener('click', openDrawer);
  closeBtn?.addEventListener('click', closeDrawer);

  drawer?.addEventListener('click', (e) => {
    if (e.target === drawer) {
      closeDrawer();
    }
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && drawer?.classList.contains('open')) {
      closeDrawer();
    }
  });
}

/* ==========================================================================
   3. Floor Plan Tabs
   ========================================================================== */
function initFloorPlanTabs() {
  const tabBtns = document.querySelectorAll('.fp-pill-btn[data-tab]');
  const tabPanes = document.querySelectorAll('.fp-tab-pane');

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetId = btn.getAttribute('data-tab');

      tabBtns.forEach(b => b.classList.remove('active'));
      tabPanes.forEach(pane => {
        pane.classList.remove('active');
        pane.style.display = 'none';
      });

      btn.classList.add('active');
      const targetPane = document.getElementById(targetId);
      if (targetPane) {
        targetPane.classList.add('active');
        targetPane.style.display = 'block';
      }
    });
  });
}

/* ==========================================================================
   4. Live EMI Calculator (Exact Godrej Math & Sliders)
   ========================================================================== */
function initEmiCalculator() {
  const loanInput = document.getElementById('calcLoanAmt');
  const sliderAdv = document.getElementById('sliderAdvance');
  const sliderDur = document.getElementById('sliderDuration');
  const sliderRate = document.getElementById('sliderRate');

  const advValSpan = document.getElementById('advPayVal');
  const downPaySpan = document.getElementById('downPayAmt');
  const durValSpan = document.getElementById('tenorYearsVal');
  const rateValSpan = document.getElementById('ratePctVal');
  const emiValSpan = document.getElementById('finalMonthlyEmi');

  function formatIndianCurrency(num) {
    if (isNaN(num)) return '0';
    return Math.round(num).toLocaleString('en-IN');
  }

  function formatLacsOrCr(amount) {
    if (amount >= 10000000) {
      return `₹ ${(amount / 10000000).toFixed(2)} Cr`;
    } else if (amount >= 100000) {
      return `₹ ${(amount / 100000).toFixed(2)} Lacs`;
    }
    return `₹ ${formatIndianCurrency(amount)}`;
  }

  function calculateEmi() {
    let basePrice = parseFloat(loanInput?.value) || 18900000;
    if (basePrice < 100000) basePrice = 18900000;

    const advPct = parseFloat(sliderAdv?.value) || 20;
    const years = parseFloat(sliderDur?.value) || 20;
    const rateAnnual = parseFloat(sliderRate?.value) || 8.5;

    const downPayment = (basePrice * advPct) / 100;
    const principal = basePrice - downPayment;
    const months = years * 12;
    const monthlyRate = (rateAnnual / 12) / 100;

    let emi = 0;
    if (monthlyRate > 0 && months > 0 && principal > 0) {
      emi = (principal * monthlyRate * Math.pow(1 + monthlyRate, months)) / (Math.pow(1 + monthlyRate, months) - 1);
    }

    if (advValSpan) advValSpan.textContent = `${advPct}%`;
    if (downPaySpan) downPaySpan.textContent = formatLacsOrCr(downPayment);
    if (durValSpan) durValSpan.textContent = `${years} Years`;
    if (rateValSpan) rateValSpan.textContent = `${rateAnnual.toFixed(1)}%`;
    if (emiValSpan) emiValSpan.textContent = `₹ ${formatIndianCurrency(emi)} / month`;
  }

  sliderAdv?.addEventListener('input', calculateEmi);
  sliderDur?.addEventListener('input', calculateEmi);
  sliderRate?.addEventListener('input', calculateEmi);
  loanInput?.addEventListener('input', calculateEmi);

  // Initial calculation
  calculateEmi();
}

/* ==========================================================================
   5. Full Gallery Lightbox System (All 24 Official Images)
   ========================================================================== */
function initGalleryLightbox() {
  const galleryItems = [];
  for (let i = 1; i <= 24; i++) {
    galleryItems.push({
      src: `assets/images/godrej-cdn/gallery/official-gal-${i}.webp`,
      title: `Godrej Elanor Mahalunge - Official Gallery View ${i}`
    });
  }

  const lightbox = document.getElementById('lightboxModal');
  const lightboxImg = document.getElementById('lightboxImg');
  const lightboxCaption = document.getElementById('lightboxCaption');
  const closeBtn = document.getElementById('lightboxCloseBtn');
  const prevBtn = document.querySelector('.lightbox-prev');
  const nextBtn = document.querySelector('.lightbox-next');
  const openGalleryBtn = document.getElementById('openFullGalleryBtn');
  const previewCards = document.querySelectorAll('.gallery-preview-card');

  let currentIndex = 0;

  function showImage(index) {
    if (!galleryItems[index] || !lightboxImg) return;
    currentIndex = index;
    const item = galleryItems[currentIndex];
    
    lightboxImg.style.opacity = '0';
    lightboxImg.src = item.src;
    lightboxImg.onload = () => {
      lightboxImg.style.transition = 'opacity 0.2s ease';
      lightboxImg.style.opacity = '1';
    };
    
    if (lightboxCaption) {
      lightboxCaption.innerHTML = `<strong>${item.title}</strong> <span style="opacity: 0.7; margin-left: 0.5rem;">(${currentIndex + 1} / ${galleryItems.length})</span>`;
    }

    lightbox?.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    lightbox?.classList.remove('open');
    document.body.style.overflow = '';
  }

  function nextImage() {
    currentIndex = (currentIndex + 1) % galleryItems.length;
    showImage(currentIndex);
  }

  function prevImage() {
    currentIndex = (currentIndex - 1 + galleryItems.length) % galleryItems.length;
    showImage(currentIndex);
  }

  openGalleryBtn?.addEventListener('click', () => {
    showImage(0);
  });

  previewCards.forEach((card) => {
    card.addEventListener('click', () => {
      const idx = parseInt(card.getAttribute('data-lightbox-idx'), 10) || 0;
      showImage(idx);
    });
  });

  closeBtn?.addEventListener('click', closeLightbox);
  nextBtn?.addEventListener('click', (e) => { e.stopPropagation(); nextImage(); });
  prevBtn?.addEventListener('click', (e) => { e.stopPropagation(); prevImage(); });

  lightbox?.addEventListener('click', (e) => {
    if (e.target === lightbox || e.target.classList.contains('lightbox-body')) {
      closeLightbox();
    }
  });

  document.addEventListener('keydown', (e) => {
    if (!lightbox?.classList.contains('open')) return;
    if (e.key === 'Escape') closeLightbox();
    if (e.key === 'ArrowRight') nextImage();
    if (e.key === 'ArrowLeft') prevImage();
  });
}

/* ==========================================================================
   6. Footer Accordions
   ========================================================================== */
function initFooterAccordion() {
  const triggers = document.querySelectorAll('.footer-acc-trigger');

  triggers.forEach(trigger => {
    trigger.addEventListener('click', () => {
      const item = trigger.closest('.footer-acc-item');
      if (!item) return;

      const isOpen = item.classList.contains('open');

      document.querySelectorAll('.footer-acc-item.open').forEach(other => {
        if (other !== item) {
          other.classList.remove('open');
        }
      });

      if (isOpen) {
        item.classList.remove('open');
      } else {
        item.classList.add('open');
      }
    });
  });
}

/* ==========================================================================
   7. Modals Management (Enquiry & Success)
   ========================================================================== */
function initModals() {
  window.openModal = function(modalId, prefill = '') {
    const modal = document.getElementById(modalId);
    if (!modal) return;

    if (prefill) {
      const noteInput = modal.querySelector('input[name="enquiry_type"]') || modal.querySelector('select[name="configuration"]');
      if (noteInput) {
        if (noteInput.tagName === 'SELECT') {
          if (prefill.includes('4 BHK')) noteInput.value = '4 BHK Duplex';
          else if (prefill.includes('3 BHK')) noteInput.value = '3 BHK Premium';
        } else {
          noteInput.value = prefill;
        }
      }
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

  // Auto popup enquiry form 3.5 seconds after page load
  let hasAutoOpened = false;
  setTimeout(() => {
    if (hasAutoOpened) return;
    const enquiryModal = document.getElementById('enquiryModal');
    const lightboxModal = document.getElementById('lightboxModal');
    const successModal = document.getElementById('successModal');

    const isAnyModalOpen = (enquiryModal && enquiryModal.classList.contains('open')) ||
                           (lightboxModal && lightboxModal.classList.contains('open')) ||
                           (successModal && successModal.classList.contains('open'));

    if (!isAnyModalOpen) {
      hasAutoOpened = true;
      window.openModal('enquiryModal', 'Priority Project Details & Price Sheet');
    }
  }, 3500);

  document.querySelectorAll('[data-open-modal]').forEach(btn => {
    btn.addEventListener('click', (e) => {
      hasAutoOpened = true;
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
   8. Form Submission & Direct WhatsApp Lead Routing
   ========================================================================== */
function initLeadForms() {
  const forms = document.querySelectorAll('form[data-lead-form]');
  const TARGET_PHONE = '8459396466';
  const TARGET_EMAIL = 'enquiryinfinitee@gmail.com';
  const SECONDARY_EMAIL = 'abhijitsarvade39@gmail.com';

  forms.forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();

      const nameInput = form.querySelector('input[name="name"]');
      const phoneInput = form.querySelector('input[name="phone"]');
      const emailInput = form.querySelector('input[name="email"]');
      const configInput = form.querySelector('select[name="configuration"]') || form.querySelector('input[name="configuration"]');

      const name = nameInput ? nameInput.value.trim() : '';
      const phone = phoneInput ? phoneInput.value.trim() : '';
      const email = emailInput ? emailInput.value.trim() : '';
      const config = configInput ? configInput.value : '3 BHK Premium';

      if (!name || name.length < 2) {
        alert('Please enter your full name.');
        nameInput?.focus();
        return;
      }

      const cleanPhone = phone.replace(/[^0-9]/g, '');
      if (cleanPhone.length < 10) {
        alert('Please enter a valid 10-digit mobile number.');
        phoneInput?.focus();
        return;
      }

      const submitBtn = form.querySelector('button[type="submit"]');
      const origText = submitBtn ? submitBtn.innerHTML : '';
      if (submitBtn) {
        submitBtn.innerHTML = 'Submitting Request...';
        submitBtn.disabled = true;
      }

      const leadPayload = {
        name,
        phone: cleanPhone,
        email,
        configuration: config,
        timestamp: new Date().toISOString(),
        project: 'Godrej Elanor Mahalunge, Pune',
        targetEmails: [TARGET_EMAIL, SECONDARY_EMAIL],
        targetPhone: TARGET_PHONE
      };

      try {
        const stored = JSON.parse(localStorage.getItem('godrej_elanor_leads') || '[]');
        stored.push(leadPayload);
        localStorage.setItem('godrej_elanor_leads', JSON.stringify(stored));
      } catch (err) {
        console.warn('LocalStorage error', err);
      }

      // Send Instant Lead Notification Email to Both Emails (Client & Abhijit)
      try {
        fetch(`https://formsubmit.co/ajax/${TARGET_EMAIL}`, {
          method: 'POST',
          headers: { 
            'Content-Type': 'application/json',
            'Accept': 'application/json' 
          },
          body: JSON.stringify({
            _subject: `New Lead: Godrej Elanor Mahalunge - ${name} (${cleanPhone})`,
            _cc: SECONDARY_EMAIL,
            _template: 'table',
            _captcha: 'false',
            'Project': 'Godrej Elanor Mahalunge Township, Pune',
            'Customer Name': name,
            'Mobile Number': cleanPhone,
            'Email Address': email || 'Not provided',
            'Preferred Configuration': config,
            'Submission Time': new Date().toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' })
          })
        }).catch(err => console.log('Lead email notification status:', err));
      } catch (err) {}

      const waMsg = `Hi Godrej Sales Team, I am interested in Godrej Elanor Mahalunge.%0A*Name:* ${encodeURIComponent(name)}%0A*Phone:* ${cleanPhone}%0A*Email:* ${encodeURIComponent(email || 'N/A')}%0A*Configuration:* ${encodeURIComponent(config)}%0APlease share the official price sheet, brochure and floor plans.`;
      const waUrl = `https://wa.me/91${TARGET_PHONE}?text=${waMsg}`;

      setTimeout(() => {
        if (submitBtn) {
          submitBtn.innerHTML = origText;
          submitBtn.disabled = false;
        }

        form.reset();

        document.querySelectorAll('.modal-overlay').forEach(m => m.classList.remove('open'));
        document.body.style.overflow = '';

        const successModal = document.getElementById('successModal');
        const nameEl = document.getElementById('successLeadName');
        const phoneEl = document.getElementById('successLeadPhone');
        const refEl = document.getElementById('successRefId');

        if (nameEl) nameEl.textContent = name;
        if (phoneEl) phoneEl.textContent = `+91 ${cleanPhone}`;
        if (refEl) refEl.textContent = 'GE-' + Math.floor(10000 + Math.random() * 90000);

        const successWaBtn = successModal?.querySelector('.btn-success-whatsapp') || successModal?.querySelector('a[href*="wa.me"]');
        if (successWaBtn) {
          successWaBtn.setAttribute('href', waUrl);
        }

        if (successModal) {
          successModal.classList.add('open');
          document.body.style.overflow = 'hidden';
        } else {
          window.open(waUrl, '_blank');
        }
      }, 500);
    });
  });
}
