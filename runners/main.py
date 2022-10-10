import sys
sys.path.append(sys.path[0] + "/..")


from scrape.scraped import runner


scrape = runner()


scrape.scrapeRunner()