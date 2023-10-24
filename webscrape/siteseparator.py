def separete(linklists):
    bundlelinks=[]
    for link in linklists:
        if "bundle.app" in link:
            bundlelinks.append(link)
        #devamını burda bir kaç tane daha ayıralım
    return bundlelinks
