/**
 * vv-effects.js — Viva Vendas shared effects
 * Lenis smooth scroll · Custom cursor · Image zoom on scroll
 * Page transitions · Marquee · GSAP integration
 */
(function () {
  'use strict';

  /* ─────────────────────────────────────────────
   * 1. PAGE TRANSITION — fade in on load
   * ───────────────────────────────────────────── */
  document.documentElement.style.cssText += 'opacity:0;transition:opacity .55s ease;';
  window.addEventListener('pageshow', function () {
    requestAnimationFrame(function () {
      document.documentElement.style.opacity = '1';
    });
  });

  /* ─────────────────────────────────────────────
   * 2. CUSTOM CURSOR
   * ───────────────────────────────────────────── */
  var isTouchDevice = window.matchMedia('(hover:none),(pointer:coarse)').matches;
  // Skip if page already has its own cursor implementation
  var hasOwnCursor = document.querySelector('.cursor-dot') !== null;
  if (!isTouchDevice && !hasOwnCursor) {
    var style = document.createElement('style');
    style.textContent = [
      'body{cursor:none!important}',
      '.vv-dot{position:fixed;width:8px;height:8px;border-radius:50%;background:#E8501E;pointer-events:none;z-index:99999;',
        'transform:translate(-50%,-50%);transition:width .2s,height .2s,background .2s,opacity .3s;will-change:transform;}',
      '.vv-ring{position:fixed;width:38px;height:38px;border-radius:50%;border:1.5px solid rgba(232,80,30,.45);pointer-events:none;z-index:99998;',
        'transform:translate(-50%,-50%);transition:width .35s cubic-bezier(0.16,1,0.3,1),height .35s cubic-bezier(0.16,1,0.3,1),',
        'border-color .25s,opacity .3s;will-change:transform;}',
      '.vv-dot.hovered{width:5px;height:5px;}',
      '.vv-ring.hovered{width:50px;height:50px;border-color:rgba(232,80,30,.7);background:rgba(232,80,30,.06);}',
      '.vv-dot.clicked{width:12px;height:12px;background:#FF6B35;}',
      '.vv-ring.clicked{width:28px;height:28px;}',
      'a,button,[onclick]{cursor:none!important}',
    ].join('');
    document.head.appendChild(style);

    var dot  = document.createElement('div'); dot.className  = 'vv-dot';
    var ring = document.createElement('div'); ring.className = 'vv-ring';
    document.body.appendChild(dot);
    document.body.appendChild(ring);

    var mx = window.innerWidth / 2, my = window.innerHeight / 2;
    var rx = mx, ry = my;
    var rafId;

    document.addEventListener('mousemove', function (e) {
      mx = e.clientX; my = e.clientY;
      dot.style.left = mx + 'px'; dot.style.top = my + 'px';
    });

    (function lerpRing() {
      rx += (mx - rx) * 0.12;
      ry += (my - ry) * 0.12;
      ring.style.left = rx + 'px';
      ring.style.top  = ry + 'px';
      rafId = requestAnimationFrame(lerpRing);
    })();

    document.addEventListener('mouseleave', function () {
      dot.style.opacity = '0'; ring.style.opacity = '0';
    });
    document.addEventListener('mouseenter', function () {
      dot.style.opacity = '1'; ring.style.opacity = '1';
    });

    document.addEventListener('mousedown', function () {
      dot.classList.add('clicked'); ring.classList.add('clicked');
    });
    document.addEventListener('mouseup', function () {
      dot.classList.remove('clicked'); ring.classList.remove('clicked');
    });

    document.addEventListener('mouseover', function (e) {
      var el = e.target.closest('a,button,[onclick],.g-item,.team-card,.imovel-card,.outro-card,.value-card,.faq-q');
      if (el) { dot.classList.add('hovered'); ring.classList.add('hovered'); }
      else     { dot.classList.remove('hovered'); ring.classList.remove('hovered'); }
    });
  }

  /* ─────────────────────────────────────────────
   * 3. LENIS SMOOTH SCROLL + GSAP TICKER
   *    (loads Lenis from CDN after DOM ready)
   * ───────────────────────────────────────────── */
  function initLenis() {
    if (typeof Lenis === 'undefined') return;
    var lenis = new Lenis({
      duration: 1.25,
      easing: function (t) { return Math.min(1, 1.001 - Math.pow(2, -10 * t)); },
      smooth: true,
      smoothTouch: false,
    });
    // Connect to GSAP ticker if available
    if (typeof gsap !== 'undefined') {
      gsap.ticker.add(function (time) { lenis.raf(time * 1000); });
      gsap.ticker.lagSmoothing(0);
      if (typeof ScrollTrigger !== 'undefined') {
        lenis.on('scroll', ScrollTrigger.update);
      }
    } else {
      (function raf(time) { lenis.raf(time); requestAnimationFrame(raf); })(0);
    }
    // Expose globally for other scripts
    window._lenis = lenis;
  }

  /* ─────────────────────────────────────────────
   * 4. IMAGE ZOOM ON SCROLL
   *    Add class "zoom-scroll" to any img wrapper
   *    The inner img scales from 1.15 → 1 as it scrolls into view
   * ───────────────────────────────────────────── */
  function initImageZoom() {
    if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') return;
    // Hero parallax already handled per-page; skip .hero-bg
    document.querySelectorAll('.about-img-wrap, .team-img-wrap, .imovel-img, .p-img').forEach(function (wrap) {
      var img = wrap.querySelector('img');
      if (!img) return;
      gsap.fromTo(img,
        { scale: 1.1 },
        { scale: 1, ease: 'none',
          scrollTrigger: { trigger: wrap, start: 'top bottom', end: 'bottom top', scrub: 1.2 }
        }
      );
    });
  }

  /* ─────────────────────────────────────────────
   * 5. PAGE EXIT TRANSITIONS
   * ───────────────────────────────────────────── */
  function initPageTransitions() {
    document.addEventListener('click', function (e) {
      var link = e.target.closest('a');
      if (!link) return;
      var href = link.getAttribute('href');
      if (!href || href.startsWith('#') || href.startsWith('mailto:') ||
          href.startsWith('tel:') || href.startsWith('https://api.whatsapp') ||
          link.target === '_blank' || e.ctrlKey || e.metaKey || e.shiftKey) return;
      e.preventDefault();
      var dest = href;
      document.documentElement.style.opacity = '0';
      setTimeout(function () { window.location.href = dest; }, 500);
    });
  }

  /* ─────────────────────────────────────────────
   * 6. MARQUEE INJECTION
   *    Looks for .vv-marquee-inject divs and fills them
   * ───────────────────────────────────────────── */
  function initMarquee() {
    if (typeof gsap === 'undefined') return;
    document.querySelectorAll('.vv-marquee').forEach(function (el) {
      var track = el.querySelector('.vv-marquee-track');
      if (!track) return;
      // Duplicate content for seamless loop
      track.innerHTML = track.innerHTML + track.innerHTML;
      var speed = parseFloat(el.dataset.speed) || 40;
      gsap.to(track, {
        xPercent: -50, ease: 'none', repeat: -1, duration: speed
      });
    });
  }

  /* ─────────────────────────────────────────────
   * INIT — wait for GSAP to be available
   * ───────────────────────────────────────────── */
  function waitForGsap(cb, tries) {
    tries = tries || 0;
    if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') { cb(); }
    else if (tries < 40) { setTimeout(function () { waitForGsap(cb, tries + 1); }, 100); }
  }

  // Lenis CDN script injection
  var lenisScript = document.createElement('script');
  lenisScript.src = 'https://cdn.jsdelivr.net/npm/@studio-freight/lenis@1.0.42/dist/lenis.min.js';
  lenisScript.onload = function () {
    waitForGsap(function () {
      initLenis();
      initImageZoom();
      initMarquee();
    });
  };
  document.head.appendChild(lenisScript);

  // Page transitions (no GSAP dep)
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initPageTransitions);
  } else {
    initPageTransitions();
  }

})();
