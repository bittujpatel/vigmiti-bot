"use strict";

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', e => {
    e.preventDefault();
    document.querySelector(anchor.getAttribute('href')).scrollIntoView({
      behavior: 'smooth'
    });
  });
});

// Animation on scroll
const animateOnScroll = () => {
  const elements = document.querySelectorAll('.animate');
  elements.forEach(element => {
    if (isVisible(element)) {
      element.classList.add('fade-up');
    }
  });
};

const isVisible = element => {
  const rect = element.getBoundingClientRect();
  return (
    rect.top >= 0 &&
    rect.left >= 0 &&
    rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
    rect.right <= (window.innerWidth || document.documentElement.clientWidth)
  );
};

// Add event listeners for scroll and load events
window.addEventListener('scroll', animateOnScroll);
window.addEventListener('load', animateOnScroll);

// Hover effects on buttons
const buttons = document.querySelectorAll('.btn');
buttons.forEach(button => {
  button.addEventListener('mouseenter', e => {
    button.classList.add('btn-hover');
  });
  button.addEventListener('mouseleave', e => {
    button.classList.remove('btn-hover');
  });
});
