import numpy as np
def separete(linklists):
    bundlelinks=[]
    bbclinks=[]
    hurriyetlinks=[]
    donanimlinks=[]
    ekonomimlinks=[]
    gazeteoksijenlinks=[]
    otherlinks=[]
    for link in linklists:
        if "bundle.app" in link:
            bundlelinks.append(link)
        elif 'bbc.com' in link:
            bbclinks.append(link)
        elif 'hurriyet.com'in link:
            hurriyetlinks.append(link)
        elif 'donanimhaber.com'in link:
            donanimlinks.append(link)
        elif 'ekonomim.com'in link:
            ekonomimlinks.append(link) 
        elif 'gazeteoksijen.com'in link:
            gazeteoksijenlinks.append(link)
        else:
            otherlinks.append(link)
            
    print(len(bundlelinks), "bundlelarin uzunlugu")
        #devam�n� burda bir ka� tane daha ay�ral�

    print(len(np.array(bbclinks)), "")
    print(len(np.array(ekonomimlinks)))
    print(len(np.array(hurriyetlinks)))
    print(len(np.array(donanimlinks)))
    print(len(np.array(gazeteoksijenlinks)))
    print(len(np.array(otherlinks)))
    return bundlelinks,bbclinks,hurriyetlinks,donanimlinks,ekonomimlinks,gazeteoksijenlinks