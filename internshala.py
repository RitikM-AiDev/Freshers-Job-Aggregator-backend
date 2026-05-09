import re
from playwright.sync_api import sync_playwright

def internshala_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
        )
        
        page = browser.new_page()

        page.set_default_timeout(6000) 

        # URL for your job search
        url = "https://internshala.com/fresher-jobs/ai-agent-development,artificial-intelligence-ai,data-science,machine-learning-jobs/"

        page.goto(url, wait_until="domcontentloaded", timeout=6000)
    
        close_tab = page.locator("#close_popup")
        close_tab.click()

        # width = page.evaluate("window.innerWidth")
        # print(width)

        # if width < 768:
        #     Profile = page.locator("#category_mobile_wrapper .tag-input-field")
        # else:
        #     Profile = page.locator("#select_category_chosen.chosen-container.chosen-container-multi")

        # target_roles = [
        #     "Artificial Intelligence (AI)",
        #     "Machine Learning",
        #     "AI Agent Development",
        # ]

        # for i in target_roles:
        #     Profile.click()
        #     search_input = page.locator("#select_category_chosen input")
        #     search_input.fill(i)

        #     option = page.locator(".chosen-results li").filter(has_text=i).first
        #     option.wait_for()
        #     option.click()

        # Year = page.locator("#select_experience_chosen")
        # Year.click()

        # search_input = page.locator("#select_experience_chosen input")
        # option = page.locator(".chosen-results li").filter(has_text="Fresher").first
        # option.wait_for()
        # option.click()

        total_jobs = []

        while True:
            page.wait_for_selector(".individual_internship", state="visible")

            jobs = page.locator(".individual_internship")
            count = jobs.count()

            for i in range(count):
                job = jobs.nth(i)

                apply_link = job.get_attribute("data-href")
                if not apply_link:
                    continue

                loc_element = job.locator(".row-1-item:has(.ic-16-map-pin)")
                location = loc_element.inner_text() if loc_element.count() > 0 else "Remote"

                stipend_element = job.locator(".row-1-item:has(.ic-16-money) .desktop")
                stipend = stipend_element.inner_text() if stipend_element.count() > 0 else "Not Mentioned"

                intern_name_locator = job.locator(".job-internship-name")
                intern_name = intern_name_locator.inner_text() if intern_name_locator.count() > 0 else "Not Mentioned"

                company_locator = job.locator(".company-name")
                company = company_locator.inner_text() if company_locator.count() > 0 else "Not Mentioned"

                print(company)

                job_data = {
                    "apply_link": f"https://internshala.com{apply_link}",
                    "internship-name": intern_name,
                    "company": company,
                    "location": location,
                    "stipend": stipend,
                }

                total_jobs.append(job_data)

            next_button = page.locator("#navigation-forward")
            button_class = next_button.get_attribute("class") or ""

            if next_button.is_visible() and "disabled" not in button_class:
                next_button.click()
                page.wait_for_timeout(6000)
            else:
                break

        browser.close()
        return total_jobs

