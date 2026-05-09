from playwright.sync_api import sync_playwright

def test_linkedin_navigation_ai():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.set_default_timeout(6000)
        page.goto(
            "https://www.linkedin.com/jobs/search?keywords=&location=Coimbatore%2C%20Tamil%20Nadu%2C%20India&geoId=101031506&position=1&pageNum=0",
            wait_until="domcontentloaded"
        )
        # try:
        #     dismiss = page.locator(
        #         '[data-tracking-control-name="public_jobs_contextual-sign-in-modal_modal_dismiss"]'
        #     )
        #     if dismiss.count() > 0:
        #         dismiss.click(force=True)
        # except:
        #     pass

        # # experience filter
        # page.get_by_label("Experience level filter.").click()

        # page.locator("label[for='f_E-0']").click(force=True)
        # page.locator("label[for='f_E-1']").click(force=True)

        # page.locator(
        #     'button[data-tracking-control-name="public_jobs_f_E"].filter__submit-button'
        # ).click()

   

        page.locator("#job-search-bar-keywords").fill("Artificial Intelligence (AI)")
        page.keyboard.press("Enter")

        page.wait_for_timeout(6000)

        jobs = page.locator(".jobs-search__results-list li")
        count = jobs.count()

        print("Jobs found:", count)

        total_jobs = []

        for i in range(count):
            job = jobs.nth(i)

            title_el = job.locator(".base-search-card__title")
            location_el = job.locator(".job-search-card__location")
            link_el = job.locator(
                'a[data-tracking-control-name="public_jobs_jserp-result_search-card"]'
            )

            title = title_el.inner_text() if title_el.count() else "NA"
            location = location_el.inner_text() if location_el.count() else "NA"
            apply_link = link_el.get_attribute("href") if link_el.count() else None

            total_jobs.append({
                "apply_link": apply_link,
                "location": location,
                "title": title,
                "experience": "Fresher"
            })

        browser.close()

        print(total_jobs)
        return total_jobs