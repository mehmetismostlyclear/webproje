def separete(linklists):
    for link in linklists:
        if "bundle.app" in link:
            bundlelinks.np(append(link))
        #devam�n� burda bir ka� tane daha ay�ral�m
    return bundlelinks
