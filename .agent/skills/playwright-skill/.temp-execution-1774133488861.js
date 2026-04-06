const { chromium } = require('playwright');

const TARGET_URL = 'http://localhost:3000';

(async () => {
  const browser = await chromium.launch({ headless: false });
  const page = await browser.newPage();

  await page.setViewportSize({ width: 1440, height: 900 });

  await page.goto(TARGET_URL, { waitUntil: 'networkidle', timeout: 10000 });

  await page.screenshot({
    path: '/tmp/bigtex-final-complete.png',
    fullPage: true,
  });

  console.log('📸 Final complete screenshot saved to /tmp/bigtex-final-complete.png');

  await browser.close();
})();
