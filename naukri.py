from playwright.sync_api import sync_playwright, Page
def naukri_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
        )
        page = browser.new_page()
        page.set_default_timeout(6000) 

        # URL for your job search
        url = "https://www.naukri.com/artificial-intelligence-machine-learning-jobs-in-coimbatore-2?k=artificial+intelligence%2C+machine+learning&l=coimbatore%2C+chennai%2C+bengaluru&experience=0"

        page.goto(url, wait_until="domcontentloaded")
    #         page.locator("#expereinceDD").click()
    #         page.locator(".dropdown li").first.click()

    #         page.get_by_placeholder("Enter location").fill(
    #             "Coimbatore, Chennai, Bengaluru"
    #         )

    #         page.get_by_placeholder(
    #             "Enter skills / designations / companies"
    #         ).fill(
    #             "Artificial Intelligence, Machine learning"
    #         )

    #         page.locator(".qsbSubmit").click()
    #         page.wait_for_timeout(3000)

        all_jobs = []
        visited_links = set()

        max_pages = 8
        current_page = 0

        def handle_popups(page: Page):
            try:
                page.evaluate("""
                    () => {
                        document.querySelector('.ni-gnb-modal')?.remove();
                        document.querySelector('.ni-gnb-modal__backdrop')?.remove();
                        document.body.style.overflow = 'auto';
                    }
                """)
            except:
                pass

        while True:
            handle_popups(page)
            page.wait_for_load_state(timeout=6000,state="domcontentloaded")
            page.wait_for_selector(".srp-jobtuple-wrapper",timeout=60000)

            jobs = page.locator(".srp-jobtuple-wrapper")
            count = jobs.count()

            print(f"Page {current_page + 1} jobs: {count}")

            for i in range(count):
                job = jobs.nth(i)

                title_el = job.locator("a.title")
                company_el = job.locator(".comp-dtls-wrap")
                location_el = job.locator(".loc-wrap")
                salary_el = job.locator(".sal-wrap")

                apply_link = title_el.get_attribute("href")

                if not apply_link or apply_link in visited_links:
                    continue

                visited_links.add(apply_link)

                job_data = {
                    "company": company_el.inner_text() if company_el.count() else "NA",
                    "title": title_el.inner_text() if title_el.count() else "NA",
                    "location": location_el.inner_text() if location_el.count() else "NA",
                    "salary": salary_el.inner_text() if salary_el.count() else "NA",
                    "apply_link": apply_link
                }

                all_jobs.append(job_data)

            if current_page >= max_pages:
                break

            next_btn = page.locator(
                "a.styles_btn-secondary__2AsIP",
                has_text="Next"
            )

            if next_btn.count() > 0:
                handle_popups(page)

                next_btn.scroll_into_view_if_needed()
                next_btn.click()

                page.wait_for_timeout(6000)
                current_page += 1
            else:
                break

        browser.close()
        return all_jobs