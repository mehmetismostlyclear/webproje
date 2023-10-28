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
        #devam�n� burda bir ka� tane daha ay�ral�m
    return bundlelinks, otherlinks
