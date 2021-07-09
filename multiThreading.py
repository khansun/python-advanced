from concurrent.futures import ThreadPoolExecutor, wait

def scrape_page(url):
    # ... scraping logic

    # remove the following line when you have written the logic
    raise NotImplementedError

def batch_scrape(urls):
    tasks = []

    with ThreadPoolExecutor(max_workers=8) as executor:
        for url in urls:
            # for executor.submit, the first argument will be the name of the function to execute. All the argument after that will be passed as the executing function's argument
            tasks.append(executor.submit(scrape_page, url))

    wait(tasks)


if __name__ == "__main__":
    urls = ['https://google.com', 'htpps://facebook.com']
    batch_scrape(urls)
