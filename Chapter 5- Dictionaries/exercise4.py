rivers = {'Rio Grande':'Mexico and United States',
          'Missouri River':'United States',
          'yangtze':'china'
    }
i=0
for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".")

print("\nThe following rivers are included in the dictionary:","\n")
for river in rivers.keys():
    i=i+1
    print(i,"-",river.title())

print("\nThe following countries are included in the dictionary:","\n")
i=0
for country in rivers.values():
    i=i+1
    print(i,"-",country.title())