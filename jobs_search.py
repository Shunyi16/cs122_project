#jobs_search.py
import csv
import requests
from bs4 import BeautifulSoup


def linkedin_scraper(webpage, page_number, writer):
    """
    Get data from Linked In and save into a csv file
    """

    next_page = webpage + str(page_number)
    print(str(next_page))
    response = requests.get(str(next_page))
    soup = BeautifulSoup(response.content,'html.parser')

    jobs = soup.find_all('div', {'class':'base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card'})
    for job in jobs:
        job_title = job.find('h3', {'class':'base-search-card__title'}).text.strip()
        job_title = job_title.replace(",", ".")
        job_company = job.find('h4', class_='base-search-card__subtitle').text.strip()
        job_location = job.find('span', class_='job-search-card__location').text.strip()
        job_link = job.find('a', class_='base-card__full-link')['href']
        try:
            job_time = job.find('time', class_='job-search-card__listdate')['datetime']
        except:
            job_time = job.find('time', class_='job-search-card__listdate--new')['datetime']
        
        writer.writerow([job_title, job_time, job_company, job_location, job_link])

    if page_number < 25:
        page_number = page_number + 25
        linkedin_scraper(webpage, page_number, writer)   

def new_search(input_position):
    """
    Take the position from input and pass the linkedin_scraper
    """
    position = '%20'.join(input_position.split())
    print(position)
    url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=' + position + '&location=United%20States&geoId=103644278&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0&start='
    with open('linkedin-jobs.csv', "w", encoding="utf-8") as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(['Title', 'Time', 'Company', 'Location', 'Link'])
        linkedin_scraper(url, 0, writer)


