from random import sample, seed, random

def lambda_handler(event, context):
    weighted_places = [
      ("Pivobar", 15),
      ("FatGoosePub", 20),
      ("Sova", 20),
      ("Sherlok", 10),
      ("Shoti", 10),
      ("Kitchen", 10),
      ("FrauMuller", 10),
      ("BigBen", 20)
    ]
    
    place, weight = zip(*weighted_places)
    weight_index = 1.0 / sum(weight)
    probability = map(lambda x: x * weight_index, weight)
    multinomial = map(lambda x: int(round(x * 1000)), probability)
    
    places = []
    for i, count in enumerate(multinomial):
      places.extend([place[i]]*count)
    
    seed()
    seed(random())
    
    sample_place = sample(places, 1)[0]
    
    return "Selected place: %s" % sample_place

if __name__ == "__main__":
    print lambda_handler(None, None)
