const init = () => {
  // 1. Accordions
  const faqItems = document.querySelectorAll('.group');
  faqItems.forEach(item => {
    const button = item.querySelector('button');
    if (button && item.parentElement && item.parentElement.classList.contains('max-w-4xl')) {
      const content = item.querySelector('div.overflow-hidden');
      const icon = item.querySelector('svg.lucide-plus');
      if (button && content) {
        button.addEventListener('click', () => {
          const isOpen = !content.classList.contains('hidden');
          if (isOpen) {
            content.classList.add('hidden');
            if (icon) icon.style.transform = 'rotate(0deg)';
          } else {
            content.classList.remove('hidden');
            if (icon) icon.style.transform = 'rotate(45deg)';
          }
        });
      }
    }
  });

  // 2. Search Toggle
  const searchButtons = document.querySelectorAll('button[data-search-toggle="true"]');
  const searchOverlay = document.querySelector('div[aria-label="Global site search"]');
  
  if (searchOverlay) {
    searchButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        const isOpen = searchOverlay.classList.contains('opacity-100');
        if (isOpen) {
          searchOverlay.classList.remove('opacity-100', 'translate-y-0');
          searchOverlay.classList.add('opacity-0', '-translate-y-2', 'pointer-events-none');
          
          // Switch icons in the button
          const searchIcon = btn.querySelector('.lucide-search');
          const closeIcon = btn.querySelector('.lucide-x');
          if (searchIcon) searchIcon.classList.replace('opacity-0', 'opacity-100');
          if (searchIcon) searchIcon.classList.replace('-rotate-90', 'rotate-0');
          if (searchIcon) searchIcon.classList.replace('scale-75', 'scale-100');
          if (closeIcon) closeIcon.classList.replace('opacity-100', 'opacity-0');
          if (closeIcon) closeIcon.classList.replace('rotate-0', '-rotate-90');
          if (closeIcon) closeIcon.classList.replace('scale-100', 'scale-75');
        } else {
          searchOverlay.classList.remove('opacity-0', '-translate-y-2', 'pointer-events-none');
          searchOverlay.classList.add('opacity-100', 'translate-y-0');
          
          // Switch icons in the button
          const searchIcon = btn.querySelector('.lucide-search');
          const closeIcon = btn.querySelector('.lucide-x');
          if (searchIcon) searchIcon.classList.replace('opacity-100', 'opacity-0');
          if (searchIcon) searchIcon.classList.replace('rotate-0', '-rotate-90');
          if (searchIcon) searchIcon.classList.replace('scale-100', 'scale-75');
          if (closeIcon) closeIcon.classList.replace('opacity-0', 'opacity-100');
          if (closeIcon) closeIcon.classList.replace('-rotate-90', 'rotate-0');
          if (closeIcon) closeIcon.classList.replace('scale-75', 'scale-100');
          
          setTimeout(() => {
            const input = searchOverlay.querySelector('input');
            if (input) input.focus();
          }, 100);
        }
      });
    });
  }

  // 3. Mobile Menu Toggle
  const mobileMenuButton = document.querySelector('button[aria-label="Toggle menu"]');
  if (mobileMenuButton) {
    let mobileNav = document.getElementById('mobile-nav-container');
    if (!mobileNav) {
      mobileNav = document.createElement('div');
      mobileNav.id = 'mobile-nav-container';
      mobileNav.className = 'fixed inset-0 z-[100] hidden bg-background flex-col';
      mobileNav.innerHTML = `
        <div class="flex items-center justify-between p-4 border-b border-border/50">
          <a class="flex items-center gap-2" href="/">
            <img alt="HealthCompiler" class="h-7 w-auto" src="images/image.png" />
          </a>
          <button id="close-mobile-menu" aria-label="Close menu" class="p-2 text-foreground">
            <svg class="lucide lucide-x" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
              <path d="M18 6 6 18"></path>
              <path d="m6 6 12 12"></path>
            </svg>
          </button>
        </div>
        <div class="flex-1 overflow-y-auto p-6 flex flex-col gap-6">
          <a class="text-xl font-medium" href="/platform">Platform</a>
          <a class="text-xl font-medium" href="/solutions">Solutions</a>
          <a class="text-xl font-medium" href="/who-we-serve">Who We Serve</a>
          <a class="text-xl font-medium" href="/resources">Resources</a>
          <a class="text-xl font-medium" href="/apex">APEX</a>
          <a class="mt-4 text-xl font-medium text-primary" href="https://insights.healthcompiler.com/onboarding/setup">Sign up</a>
          <a class="inline-flex w-full box-border items-center justify-center gap-2 font-medium transition-colors duration-200 bg-primary text-primary-foreground hover:bg-primary/80 h-12 text-base rounded-full px-4" href="/contact">
            Request a Demo
          </a>
        </div>
      `;
      document.body.appendChild(mobileNav);
      
      document.getElementById('close-mobile-menu').addEventListener('click', () => {
        mobileNav.classList.add('hidden');
        mobileNav.classList.remove('flex');
        document.body.style.overflow = '';
      });
    }

    mobileMenuButton.addEventListener('click', () => {
      mobileNav.classList.remove('hidden');
      mobileNav.classList.add('flex');
      document.body.style.overflow = 'hidden';
    });
  }
};

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}
