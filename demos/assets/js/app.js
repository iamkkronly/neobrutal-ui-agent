(function () {
  const liveMessage = document.getElementById('liveMessage');
  const actionButton = document.getElementById('actionButton');
  const stateButton = document.getElementById('stateButton');
  let actionCount = 0;
  let active = false;

  if (actionButton && liveMessage) {
    actionButton.addEventListener('click', function () {
      actionCount += 1;
      liveMessage.textContent = 'Action received. This is feedback number ' + actionCount + '.';
    });
  }

  if (stateButton && liveMessage) {
    stateButton.addEventListener('click', function () {
      active = !active;
      stateButton.setAttribute('aria-pressed', String(active));
      stateButton.textContent = active ? 'Turn off state' : 'Toggle state';
      liveMessage.textContent = active ? 'State is active. The interface said what changed.' : 'State is resting. Ready for input.';
    });
  }

  function copyPrompt(button) {
    const prompt = 'Always use Neo-Brutalism as the primary visual language. Use Typography for hierarchy, Retro Pixel Art as a small purposeful accent, and Claymorphism or Glassmorphism only when the component specifically benefits from it. Reuse the design tokens, preserve accessibility, responsiveness, and all relevant interaction states.';
    const original = button.textContent;
    navigator.clipboard.writeText(prompt).then(function () {
      button.textContent = 'Prompt copied ✓';
      window.setTimeout(function () { button.textContent = original; }, 1800);
    }).catch(function () {
      button.textContent = 'Copy unavailable';
      window.setTimeout(function () { button.textContent = original; }, 1800);
    });
  }

  [document.getElementById('copyButton'), document.getElementById('copyButtonBottom')].forEach(function (button) {
    if (button) button.addEventListener('click', function () { copyPrompt(button); });
  });
}());
