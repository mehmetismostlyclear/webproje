def separete(linklists):
    bundlelinks=[]
    for link in linklists:
        if "bundle.app" in link:
            bundlelinks.append(link)
        #devam�n� burda bir ka� tane daha ay�ral�m
    return bundlelinks
