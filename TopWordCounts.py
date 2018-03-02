sample_str = '''
Agriculture is the cultivation and breeding of animals, plants and fungi for food, fiber, biofuel, medicinal plants and other products used to sustain and enhance life.[1] Agriculture was the key development in the rise of sedentary human civilization, whereby farming of domesticated species created food surpluses that nurtured the development of civilization. The study of agriculture is known as agricultural science. The history of agriculture by humans dates back thousands of years, and its development has been driven and defined by greatly different climates, cultures, and technologies; industrial agriculture based on large-scale monoculture farming has become the dominant agricultural method. Although generally understood to denote the practices of humans, other animals?for example, fungus-growing ants?have also been found to engage in agriculture.
Modern agronomy, plant breeding, agrochemicals such as pesticides and fertilizers, and technological developments have in many cases sharply increased yields from cultivation, but at the same time have caused widespread ecological damage and negative human health effects. Selective breeding and modern practices in animal husbandry have similarly increased the output of meat, but have raised concerns about animal welfare, environmental damage (such as massive drainage of resources such as water and feed fed to the animals, global warming, rainforest destruction, leftover waste products that are littered), and the health effects of the antibiotics, growth hormones, artificial additives and other chemicals commonly used in industrial meat production. Genetically modified organisms are an increasing component of agriculture, although they are banned in several countries. Agricultural food production and water management are increasingly becoming global issues that are fostering debate on a number of fronts. Significant degradation of land and water resources, including the depletion of aquifers, has been observed in recent decades, and the effects of global warming on agriculture and of agriculture on global warming are still not fully understood. However, entomophagy would solve most of the former problems, and may start to gain popularity among society in the West.[2]
The major agricultural products can be broadly grouped into foods, fibers, fuels, and raw materials. Specific foods include cereals (grains), vegetables, fruits, oils, meats and spices. Fibers include cotton, wool, hemp, silk and flax. Raw materials include lumber and bamboo. Other useful materials are also produced by plants, such as resins, dyes, drugs, perfumes, biofuels and ornamental products such as cut flowers and nursery plants. Over one third of the world's workers are employed in agriculture, second only to the service sector, although the percentages of agricultural workers in developed countries has decreased significantly over the past several centuries.
'''


def get_word_count(my_str):
    """
    Get Map of each word count in a string
    param: my_str String
    return: Map
    """
    my_list = my_str.split(" ")
    my_map = {}
    for word in my_list:
        # Strip the word from any character
        word = word.strip(".")
        word = word.strip(",")
        # Convert word to all lowercase
        word = word.lower()
        if word not in my_map:
            my_map[word] = 1
        else:
            my_map[word] += 1

    return my_map


def get_topper(my_map):
    """
    Get the word with highest count in map
    :param my_map:
    :return:
    """
    current_max = 0
    topper = ""
    for key, value in my_map.iteritems():
        if value > current_max:
            current_max = value
            topper = key
    return topper, current_max


def get_all_toppers(my_map, n):
    """
    Get the Top n words in decreasing count of their occurences in the map
    :param my_map:
    :param n:
    :return:
    """
    toppers = []
    for n in xrange(n):
        t, c = get_topper(my_map)
        toppers.append(t+str(c))
        my_map[t] = 0
    return toppers


my_map = get_word_count(sample_str)
# Get the Top 100 words in decreasing count of their occurences in the map
toppers = get_all_toppers(my_map, n=100)
print toppers
