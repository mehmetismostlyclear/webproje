def separete(linklists):
    bundlelinks=[]
    otherlinks=[]
    for link in linklists:
        if "bundle.app" in link:
            bundlelinks.append(link)
        #elif 'bbc.com' in link:
         #   bbclinks.append(link)
        else:
            otherlinks.append(link)
            
    print(len(bundlelinks), "bundlelarin uzunlugu")
        #devamını burda bir kaç tane daha ayıralım
    return bundlelinks, otherlinks
