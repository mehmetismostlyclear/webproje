def separete(linklists):
    for link in linklists:
        if "bundle.app" in link:
            bundlelinks.np(append(link))
        #devamını burda bir kaç tane daha ayıralım
    return bundlelinks
