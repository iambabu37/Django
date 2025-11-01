import re
array ="""3,4-Dihydroxybenzoic acid    IMPHY011883
Benzyl Alcohol    IMPHY002915
Coumarin    IMPHY003490
4-Isopropylbenzaldehyde    IMPHY003545
Hydroquinone    IMPHY006959
Benzyl isothiocyanate    IMPHY005071
Camphor    IMPHY012036
Eucalyptol    IMPHY010072
Hinokitiol    IMPHY017282
Lapachol    IMPHY003002
Menadione    IMPHY002992
Phloretin    IMPHY000813
Protopine    IMPHY000870
Sanguinarine    IMPHY004539
Sulforaphane    IMPHY010559
Reserpine    IMPHY012049
Allyl isothiocyanate    IMPHY006321
alpha-Pinene    IMPHY012061
Methyleugenol    IMPHY006696
Furfural    IMPHY007041
gamma-Terpinene    IMPHY003982
alpha-Terpinene    IMPHY011643
Citronellal    IMPHY012086
1-Dodecanol    IMPHY007100
1,4-Naphthoquinone    IMPHY007073
Estragole    IMPHY006944
Cianidanol    IMPHY014854
Jervine    IMPHY000366
Islandicin    IMPHY004243
Rhein    IMPHY002157
Plumbagin    IMPHY001191
Aloe emodin    IMPHY000333
Emetine    IMPHY000198
Cadalene    IMPHY000070
Osthole    IMPHY001134
Arachidic acid    IMPHY011394
Oleanolic acid    IMPHY011826
Anemonin    IMPHY000163
beta-Cadinene    IMPHY010603
Paeonol    IMPHY000295
3-Hydroxyflavone    IMPHY000011
Terpinolene    IMPHY011599
Diallyl sulfide    IMPHY001879
Dimethyl disulfide    IMPHY001846
Pentadecanoic acid    IMPHY002667
beta-Pinene    IMPHY012147
Lysergol    IMPHY003786
Diallyl trisulfide    IMPHY005399
N-Methyllaurotetanine    IMPHY005387
Diallyl disulfide    IMPHY011480
Phenethyl isothiocyanate    IMPHY005144
Dimethyl trisulfide    IMPHY005804
Thalicarpine    IMPHY005773
Limonene    IMPHY014988
Helenalin    IMPHY005192
3-Carene    IMPHY011392
Myrcene    IMPHY003485
Silibinin    IMPHY011703
Dmask    IMPHY003585
d-Borneol    IMPHY011590
Betulinic acid    IMPHY012003
Baicalin    IMPHY004115
Carnosic acid    IMPHY006653
Pentagalloylglucose    IMPHY006658
Tomatidine    IMPHY004110
beta-Terpinene    IMPHY007267
Pinocembrin    IMPHY007196
3,3,6-Trimethylhepta-1,5-dien-4-one    IMPHY007113
Artemisinin    IMPHY007168
Alloimperatorin    IMPHY006581
Epigallocatechin    IMPHY011737
Chebulinic acid    IMPHY010827
Magnolol    IMPHY006690
Honokiol    IMPHY006683
Chelerythrine chloride    IMPHY012217
Jatrorrhizine    IMPHY007190
Polygodial    IMPHY004272
Alkannin    IMPHY003697
Alantolactone    IMPHY006053
alpha-Amyrin    IMPHY011619
Sigmoidin A    IMPHY006079
Isoalantolactone    IMPHY011463
Solanocapsine    IMPHY007015
Taxodione    IMPHY010854
Arjunolic acid    IMPHY011627
Isoneorautenol    IMPHY012234
Maslinic acid    IMPHY011970
Eucalyptin    IMPHY010980
Cryptolepine    IMPHY007232
Primin    IMPHY007018
Aucubin    IMPHY011516
Matrine    IMPHY004247
Lupanine    IMPHY007309
Irehdiamine A    IMPHY012282
Cryptopleurine    IMPHY007424
Xanthorrhizol    IMPHY007427
(-)-trans-Carveol    IMPHY011988
Thymohydroquinone    IMPHY007606
Aristololactam    IMPHY007632"""
filter1= re.split(r'\t|\n|  ', array)
print(filter1)
babu = [[filter1[i],filter1[i+2]]for i in range(0,len(filter1),3)]
print(babu)
print(len(babu))
import requests
def image_downloader(array):
  for i in range(len(array)):
    url = f"https://cb.imsc.res.in/imppat/images/2D_IMAGE/PNG/{array[i][1]}.png"
    print(array[i][0],array[i][1])
  

    # Send an HTTP GET request to the image URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Save the image to a local file
        with open(f"{array[i][0]}.png", 'wb') as f:
            f.write(response.content)
        print(f"{array[i][1]} Image downloaded successfully.")
    else:
        print(f"Failed to download image. Status code: {response.status_code}")
        with open("notdownloaded.txt","wb") as f:
          f.write(f"{array[i][1]}")
image_downloader(babu)

