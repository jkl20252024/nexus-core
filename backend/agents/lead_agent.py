from backend.agents.scraper_agent import scrape_businesses

def find_leads():

    businesses = scrape_businesses()

    return businesses