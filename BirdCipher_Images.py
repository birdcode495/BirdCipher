

# -----------------------------------------------------------------------Image list creation --------------------------------------------------------------


#                            Biodiversidad de especies de aves presentes en el territorio del departamento de Cundinamarca en Colombia.


#                            Número de especies de la familia Accipitridae (halcones) incluidas en la lista: 22 taxones

#                            Número de especies de la familia Trochilidae (Colibríes) incluidas en la lista: 75 taxones



# -------------------------------------------------------------------------- Data sources -----------------------------------------------------------------


#                                   * Global Biodiversity Information Facility, GBIF. API 
#                                   * libro: Gobernación de Cundinamarca. Colibríes de Cundinamarca. Bogotá. 2018.
#                                   * Wikipedia


# ----------------------------------------------------------------------------------------------------------------------------------------------------------




BirdCipher_list = [["C:/BirdCipher/Bird_images/Struthioniformes1.png", "C:/BirdCipher/Bird_images/Struthioniformes2.png",
"C:/BirdCipher/Bird_images/Struthioniformes3.png", "C:/BirdCipher/Bird_images/Struthioniformes4.png",
"C:/BirdCipher/Bird_images/Struthioniformes5.png", "C:/BirdCipher/Bird_images/Struthioniformes6.png"], 
["C:/BirdCipher/Bird_images/Tinamiformes1.png", "C:/BirdCipher/Bird_images/Tinamiformes2.png", 
"C:/BirdCipher/Bird_images/Tinamiformes3.png", "C:/BirdCipher/Bird_images/Tinamiformes4.png", "C:/BirdCipher/Bird_images/Tinamiformes5.png",
"C:/BirdCipher/Bird_images/Tinamiformes6.png",], ["C:/BirdCipher/Bird_images/Rheiformes1.png", "C:/BirdCipher/Bird_images/Rheiformes2.png",
"C:/BirdCipher/Bird_images/Rheiformes3.png", "C:/BirdCipher/Bird_images/Rheiformes4.png", "C:/BirdCipher/Bird_images/Rheiformes5.png",
"C:/BirdCipher/Bird_images/Rheiformes6.png", "C:/BirdCipher/Bird_images/Rheiformes7.png"], ["C:/BirdCipher/Bird_images/Apterygiformes1.png",
"C:/BirdCipher/Bird_images/Apterygiformes2.png", "C:/BirdCipher/Bird_images/Apterygiformes3.png", "C:/BirdCipher/Bird_images/Apterygiformes4.png",
"C:/BirdCipher/Bird_images/Apterygiformes5.png", "C:/BirdCipher/Bird_images/Apterygiformes6.png", "C:/BirdCipher/Bird_images/Apterygiformes7.png"],
["C:/BirdCipher/Bird_images/Casuariiformes1.png", "C:/BirdCipher/Bird_images/Casuariiformes2.png", "C:/BirdCipher/Bird_images/Casuariiformes3.png",
"C:/BirdCipher/Bird_images/Casuariiformes4.png", "C:/BirdCipher/Bird_images/Casuariiformes5.png", "C:/BirdCipher/Bird_images/Casuariiformes6.png",
"C:/BirdCipher/Bird_images/Casuariiformes7.png"], ["C:/BirdCipher/Bird_images/Galliformes1.png", "C:/BirdCipher/Bird_images/Galliformes2.png",
"C:/BirdCipher/Bird_images/Galliformes3.png", "C:/BirdCipher/Bird_images/Galliformes4.png", "C:/BirdCipher/Bird_images/Galliformes5.png",
"C:/BirdCipher/Bird_images/Galliformes6.png", "C:/BirdCipher/Bird_images/Galliformes7.png", "C:/BirdCipher/Bird_images/Galliformes8.png",
"C:/BirdCipher/Bird_images/Galliformes9.png", "C:/BirdCipher/Bird_images/Galliformes10.png", "C:/BirdCipher/Bird_images/Galliformes11.png",
"C:/BirdCipher/Bird_images/Galliformes12.png", "C:/BirdCipher/Bird_images/Galliformes13.png", "C:/BirdCipher/Bird_images/Galliformes14.png",
"C:/BirdCipher/Bird_images/Galliformes15.png"], ["C:/BirdCipher/Bird_images/Anseriformes1.png", "C:/BirdCipher/Bird_images/Anseriformes2.png",
"C:/BirdCipher/Bird_images/Anseriformes3.png", "C:/BirdCipher/Bird_images/Anseriformes4.png", "C:/BirdCipher/Bird_images/Anseriformes5.png",
"C:/BirdCipher/Bird_images/Anseriformes6.png", "C:/BirdCipher/Bird_images/Anseriformes7.png", "C:/BirdCipher/Bird_images/Anseriformes8.png",
"C:/BirdCipher/Bird_images/Anseriformes9.png", "C:/BirdCipher/Bird_images/Anseriformes10.png", "C:/BirdCipher/Bird_images/Anseriformes11.png",
"C:/BirdCipher/Bird_images/Anseriformes12.png"], ["C:/BirdCipher/Bird_images/Phoenicopteriformes1.png", "C:/BirdCipher/Bird_images/Phoenicopteriformes2.png",
"C:/BirdCipher/Bird_images/Phoenicopteriformes3.png", "C:/BirdCipher/Bird_images/Phoenicopteriformes4.png", "C:/BirdCipher/Bird_images/Phoenicopteriformes5.png",
"C:/BirdCipher/Bird_images/Phoenicopteriformes6.png", "C:/BirdCipher/Bird_images/Phoenicopteriformes7.png", "C:/BirdCipher/Bird_images/Phoenicopteriformes8.png",
"C:/BirdCipher/Bird_images/Phoenicopteriformes9.png"], ["C:/BirdCipher/Bird_images/Podicipediformes1.png", "C:/BirdCipher/Bird_images/Podicipediformes2.png",
"C:/BirdCipher/Bird_images/Podicipediformes3.png", "C:/BirdCipher/Bird_images/Podicipediformes4.png", "C:/BirdCipher/Bird_images/Podicipediformes5.png",
"C:/BirdCipher/Bird_images/Podicipediformes6.png", "C:/BirdCipher/Bird_images/Podicipediformes7.png", "C:/BirdCipher/Bird_images/Podicipediformes8.png",
"C:/BirdCipher/Bird_images/Podicipediformes9.png", "C:/BirdCipher/Bird_images/Podicipediformes10.png", "C:/BirdCipher/Bird_images/Podicipediformes11.png",
"C:/BirdCipher/Bird_images/Podicipediformes12.png"], ["C:/BirdCipher/Bird_images/Columbiformes1.png", "C:/BirdCipher/Bird_images/Columbiformes2.png",
"C:/BirdCipher/Bird_images/Columbiformes3.png", "C:/BirdCipher/Bird_images/Columbiformes4.png", "C:/BirdCipher/Bird_images/Columbiformes5.png",
"C:/BirdCipher/Bird_images/Columbiformes6.png", "C:/BirdCipher/Bird_images/Columbiformes7.png", "C:/BirdCipher/Bird_images/Columbiformes8.png",
"C:/BirdCipher/Bird_images/Columbiformes9.png", "C:/BirdCipher/Bird_images/Columbiformes10.png", "C:/BirdCipher/Bird_images/Columbiformes11.png",
"C:/BirdCipher/Bird_images/Columbiformes12.png", "C:/BirdCipher/Bird_images/Columbiformes13.png", "C:/BirdCipher/Bird_images/Columbiformes14.png",
"C:/BirdCipher/Bird_images/Columbiformes15.png", "C:/BirdCipher/Bird_images/Columbiformes16.png"], ["C:/BirdCipher/Bird_images/Mesitornithidae1.png",
"C:/BirdCipher/Bird_images/Mesitornithidae2.png", "C:/BirdCipher/Bird_images/Mesitornithidae3.png", "C:/BirdCipher/Bird_images/Mesitornithidae4.png",
"C:/BirdCipher/Bird_images/Mesitornithidae5.png", "C:/BirdCipher/Bird_images/Mesitornithidae6.png", "C:/BirdCipher/Bird_images/Mesitornithidae7.png",
"C:/BirdCipher/Bird_images/Mesitornithidae8.png", "C:/BirdCipher/Bird_images/Mesitornithidae9.png", "C:/BirdCipher/Bird_images/Mesitornithidae10.png",
"C:/BirdCipher/Bird_images/Mesitornithidae11.png"], ["C:/BirdCipher/Bird_images/Pterocliformes1.png", "C:/BirdCipher/Bird_images/Pterocliformes2.png",
"C:/BirdCipher/Bird_images/Pterocliformes3.png", "C:/BirdCipher/Bird_images/Pterocliformes4.png", "C:/BirdCipher/Bird_images/Pterocliformes5.png",
"C:/BirdCipher/Bird_images/Pterocliformes6.png", "C:/BirdCipher/Bird_images/Pterocliformes7.png", "C:/BirdCipher/Bird_images/Pterocliformes8.png",
"C:/BirdCipher/Bird_images/Pterocliformes9.png", "C:/BirdCipher/Bird_images/Pterocliformes10.png", "C:/BirdCipher/Bird_images/Pterocliformes11.png",
"C:/BirdCipher/Bird_images/Pterocliformes12.png", "C:/BirdCipher/Bird_images/Pterocliformes13.png", "C:/BirdCipher/Bird_images/Pterocliformes14.png",
"C:/BirdCipher/Bird_images/Pterocliformes15.png", "C:/BirdCipher/Bird_images/Pterocliformes16.png", "C:/BirdCipher/Bird_images/Pterocliformes17.png",
"C:/BirdCipher/Bird_images/Pterocliformes18.png"], ["C:/BirdCipher/Bird_images/Cuculiformes1.png", "C:/BirdCipher/Bird_images/Cuculiformes2.png",
"C:/BirdCipher/Bird_images/Cuculiformes3.png", "C:/BirdCipher/Bird_images/Cuculiformes4.png", "C:/BirdCipher/Bird_images/Cuculiformes5.png",
"C:/BirdCipher/Bird_images/Cuculiformes6.png", "C:/BirdCipher/Bird_images/Cuculiformes7.png", "C:/BirdCipher/Bird_images/Cuculiformes8.png",
"C:/BirdCipher/Bird_images/Cuculiformes9.png", "C:/BirdCipher/Bird_images/Cuculiformes10.png", "C:/BirdCipher/Bird_images/Cuculiformes11.png",
"C:/BirdCipher/Bird_images/Cuculiformes12.png", "C:/BirdCipher/Bird_images/Cuculiformes13.png", "C:/BirdCipher/Bird_images/Cuculiformes14.png",
"C:/BirdCipher/Bird_images/Cuculiformes15.png", "C:/BirdCipher/Bird_images/Cuculiformes16.png", "C:/BirdCipher/Bird_images/Cuculiformes17.png",
"C:/BirdCipher/Bird_images/Cuculiformes18.png", "C:/BirdCipher/Bird_images/Cuculiformes19.png", "C:/BirdCipher/Bird_images/Cuculiformes20.png",
"C:/BirdCipher/Bird_images/Cuculiformes21.png"]]

number_species = [38, 55, 13, 8, 10, 457, 442, 23, 42, 441, 3, 20, 188]


#print(len(BirdCipher_list))