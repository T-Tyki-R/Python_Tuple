# Advanced Tuple Techniques: Joining and Nesting in Python

catalog1 = (("Laptop", 1000), ("Camera", 500))
catalog2 = (("Smartphone", 800), ("Tablet", 450))
catalog3 = (("Game Console", 200), ("TV", 300)) # <- tester


def combined_tech_catalog(*catalog_list):
    tech = ()
    for i in catalog_list:
         for x in i:           
            tech += x
    return tech
           

print(combined_tech_catalog(catalog1, catalog2, catalog3))