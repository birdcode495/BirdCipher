

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
"C:/BirdCipher/Bird_images/Cuculiformes21.png"], ["C:/BirdCipher/Bird_images/Otidiformes1.png", "C:/BirdCipher/Bird_images/Otidiformes2.png",
"C:/BirdCipher/Bird_images/Otidiformes3.png", "C:/BirdCipher/Bird_images/Otidiformes4.png", "C:/BirdCipher/Bird_images/Otidiformes5.png",
"C:/BirdCipher/Bird_images/Otidiformes6.png", "C:/BirdCipher/Bird_images/Otidiformes7.png", "C:/BirdCipher/Bird_images/Otidiformes8.png",
"C:/BirdCipher/Bird_images/Otidiformes9.png", "C:/BirdCipher/Bird_images/Otidiformes10.png", "C:/BirdCipher/Bird_images/Otidiformes11.png",
"C:/BirdCipher/Bird_images/Otidiformes12.png", "C:/BirdCipher/Bird_images/Otidiformes13.png", "C:/BirdCipher/Bird_images/Otidiformes14.png",
"C:/BirdCipher/Bird_images/Otidiformes15.png", "C:/BirdCipher/Bird_images/Otidiformes16.png", "C:/BirdCipher/Bird_images/Otidiformes17.png"],
["C:/BirdCipher/Bird_images/Musophagiformes1.png", "C:/BirdCipher/Bird_images/Musophagiformes2.png", "C:/BirdCipher/Bird_images/Musophagiformes3.png",
"C:/BirdCipher/Bird_images/Musophagiformes4.png", "C:/BirdCipher/Bird_images/Musophagiformes5.png", "C:/BirdCipher/Bird_images/Musophagiformes6.png",
"C:/BirdCipher/Bird_images/Musophagiformes7.png", "C:/BirdCipher/Bird_images/Musophagiformes8.png", "C:/BirdCipher/Bird_images/Musophagiformes9.png",
"C:/BirdCipher/Bird_images/Musophagiformes10.png", "C:/BirdCipher/Bird_images/Musophagiformes11.png", "C:/BirdCipher/Bird_images/Musophagiformes12.png",
"C:/BirdCipher/Bird_images/Musophagiformes13.png", "C:/BirdCipher/Bird_images/Musophagiformes14.png", "C:/BirdCipher/Bird_images/Musophagiformes15.png",
"C:/BirdCipher/Bird_images/Musophagiformes16.png", "C:/BirdCipher/Bird_images/Musophagiformes17.png", "C:/BirdCipher/Bird_images/Musophagiformes18.png"],
["C:/BirdCipher/Bird_images/Opisthocomiformes1.png", "C:/BirdCipher/Bird_images/Opisthocomiformes2.png", "C:/BirdCipher/Bird_images/Opisthocomiformes3.png",
"C:/BirdCipher/Bird_images/Opisthocomiformes4.png", "C:/BirdCipher/Bird_images/Opisthocomiformes5.png", "C:/BirdCipher/Bird_images/Opisthocomiformes6.png",
"C:/BirdCipher/Bird_images/Opisthocomiformes7.png", "C:/BirdCipher/Bird_images/Opisthocomiformes8.png", "C:/BirdCipher/Bird_images/Opisthocomiformes9.png",
"C:/BirdCipher/Bird_images/Opisthocomiformes10.png"], ["C:/BirdCipher/Bird_images/Gruiformes1.png", "C:/BirdCipher/Bird_images/Gruiformes2.png",
"C:/BirdCipher/Bird_images/Gruiformes3.png", "C:/BirdCipher/Bird_images/Gruiformes4.png", "C:/BirdCipher/Bird_images/Gruiformes5.png",
"C:/BirdCipher/Bird_images/Gruiformes6.png", "C:/BirdCipher/Bird_images/Gruiformes7.png", "C:/BirdCipher/Bird_images/Gruiformes8.png",
"C:/BirdCipher/Bird_images/Gruiformes9.png", "C:/BirdCipher/Bird_images/Gruiformes10.png", "C:/BirdCipher/Bird_images/Gruiformes11.png",
"C:/BirdCipher/Bird_images/Gruiformes12.png", "C:/BirdCipher/Bird_images/Gruiformes13.png", "C:/BirdCipher/Bird_images/Gruiformes14.png",
"C:/BirdCipher/Bird_images/Gruiformes15.png", "C:/BirdCipher/Bird_images/Gruiformes16.png", "C:/BirdCipher/Bird_images/Gruiformes17.png",
"C:/BirdCipher/Bird_images/Gruiformes18.png", "C:/BirdCipher/Bird_images/Gruiformes19.png", "C:/BirdCipher/Bird_images/Gruiformes20.png"],
["C:/BirdCipher/Bird_images/Charadriiformes1.png", "C:/BirdCipher/Bird_images/Charadriiformes2.png", "C:/BirdCipher/Bird_images/Charadriiformes3.png",
"C:/BirdCipher/Bird_images/Charadriiformes4.png", "C:/BirdCipher/Bird_images/Charadriiformes5.png", "C:/BirdCipher/Bird_images/Charadriiformes6.png",
"C:/BirdCipher/Bird_images/Charadriiformes7.png", "C:/BirdCipher/Bird_images/Charadriiformes8.png", "C:/BirdCipher/Bird_images/Charadriiformes9.png",
"C:/BirdCipher/Bird_images/Charadriiformes10.png", "C:/BirdCipher/Bird_images/Charadriiformes11.png", "C:/BirdCipher/Bird_images/Charadriiformes12.png",
"C:/BirdCipher/Bird_images/Charadriiformes13.png", "C:/BirdCipher/Bird_images/Charadriiformes14.png", "C:/BirdCipher/Bird_images/Charadriiformes15.png",
"C:/BirdCipher/Bird_images/Charadriiformes16.png", "C:/BirdCipher/Bird_images/Charadriiformes17.png", "C:/BirdCipher/Bird_images/Charadriiformes18.png",
"C:/BirdCipher/Bird_images/Charadriiformes19.png", "C:/BirdCipher/Bird_images/Charadriiformes20.png"], ["C:/BirdCipher/Bird_images/Caprimulgiformes1.png",
"C:/BirdCipher/Bird_images/Caprimulgiformes2.png", "C:/BirdCipher/Bird_images/Caprimulgiformes3.png", "C:/BirdCipher/Bird_images/Caprimulgiformes4.png",
"C:/BirdCipher/Bird_images/Caprimulgiformes5.png", "C:/BirdCipher/Bird_images/Caprimulgiformes6.png", "C:/BirdCipher/Bird_images/Caprimulgiformes7.png",
"C:/BirdCipher/Bird_images/Caprimulgiformes8.png", "C:/BirdCipher/Bird_images/Caprimulgiformes9.png", "C:/BirdCipher/Bird_images/Caprimulgiformes10.png",
"C:/BirdCipher/Bird_images/Caprimulgiformes11.png", "C:/BirdCipher/Bird_images/Caprimulgiformes12.png", "C:/BirdCipher/Bird_images/Caprimulgiformes13.png",
"C:/BirdCipher/Bird_images/Caprimulgiformes14.png", "C:/BirdCipher/Bird_images/Caprimulgiformes15.png", "C:/BirdCipher/Bird_images/Caprimulgiformes16.png",
"C:/BirdCipher/Bird_images/Caprimulgiformes17.png", "C:/BirdCipher/Bird_images/Caprimulgiformes18.png", "C:/BirdCipher/Bird_images/Caprimulgiformes19.png",
"C:/BirdCipher/Bird_images/Caprimulgiformes20.png", "C:/BirdCipher/Bird_images/Caprimulgiformes21.png"], ["C:/BirdCipher/Bird_images/Nyctibiiformes1.png",
"C:/BirdCipher/Bird_images/Nyctibiiformes2.png", "C:/BirdCipher/Bird_images/Nyctibiiformes3.png", "C:/BirdCipher/Bird_images/Nyctibiiformes4.png",
"C:/BirdCipher/Bird_images/Nyctibiiformes5.png", "C:/BirdCipher/Bird_images/Nyctibiiformes6.png", "C:/BirdCipher/Bird_images/Nyctibiiformes7.png",
"C:/BirdCipher/Bird_images/Nyctibiiformes8.png", "C:/BirdCipher/Bird_images/Nyctibiiformes9.png", "C:/BirdCipher/Bird_images/Nyctibiiformes10.png",
"C:/BirdCipher/Bird_images/Nyctibiiformes11.png", "C:/BirdCipher/Bird_images/Nyctibiiformes12.png"], ["C:/BirdCipher/Bird_images/Steatornithiformes1.png",
"C:/BirdCipher/Bird_images/Steatornithiformes2.png", "C:/BirdCipher/Bird_images/Steatornithiformes3.png", "C:/BirdCipher/Bird_images/Steatornithiformes4.png",
"C:/BirdCipher/Bird_images/Steatornithiformes5.png", "C:/BirdCipher/Bird_images/Steatornithiformes6.png", "C:/BirdCipher/Bird_images/Steatornithiformes7.png",
"C:/BirdCipher/Bird_images/Steatornithiformes8.png", "C:/BirdCipher/Bird_images/Steatornithiformes9.png", "C:/BirdCipher/Bird_images/Steatornithiformes10.png"],
["C:/BirdCipher/Bird_images/Podargiformes1.png", "C:/BirdCipher/Bird_images/Podargiformes2.png", "C:/BirdCipher/Bird_images/Podargiformes3.png",
"C:/BirdCipher/Bird_images/Podargiformes4.png", "C:/BirdCipher/Bird_images/Podargiformes5.png", "C:/BirdCipher/Bird_images/Podargiformes6.png",
"C:/BirdCipher/Bird_images/Podargiformes7.png", "C:/BirdCipher/Bird_images/Podargiformes8.png", "C:/BirdCipher/Bird_images/Podargiformes9.png",
"C:/BirdCipher/Bird_images/Podargiformes10.png", "C:/BirdCipher/Bird_images/Podargiformes11.png", "C:/BirdCipher/Bird_images/Podargiformes12.png",
"C:/BirdCipher/Bird_images/Podargiformes13.png", "C:/BirdCipher/Bird_images/Podargiformes14.png", "C:/BirdCipher/Bird_images/Podargiformes15.png",
"C:/BirdCipher/Bird_images/Podargiformes16.png", "C:/BirdCipher/Bird_images/Podargiformes17.png", "C:/BirdCipher/Bird_images/Podargiformes18.png",
"C:/BirdCipher/Bird_images/Podargiformes19.png", "C:/BirdCipher/Bird_images/Podargiformes20.png"], ["C:/BirdCipher/Bird_images/Aegotheliformes1.png",
"C:/BirdCipher/Bird_images/Aegotheliformes2.png", "C:/BirdCipher/Bird_images/Aegotheliformes3.png", "C:/BirdCipher/Bird_images/Aegotheliformes4.png",
"C:/BirdCipher/Bird_images/Aegotheliformes5.png", "C:/BirdCipher/Bird_images/Aegotheliformes6.png", "C:/BirdCipher/Bird_images/Aegotheliformes7.png",
"C:/BirdCipher/Bird_images/Aegotheliformes8.png", "C:/BirdCipher/Bird_images/Aegotheliformes9.png", "C:/BirdCipher/Bird_images/Aegotheliformes10.png"],
["C:/BirdCipher/Bird_images/Apodiformes1.png", "C:/BirdCipher/Bird_images/Apodiformes2.png", "C:/BirdCipher/Bird_images/Apodiformes3.png",
"C:/BirdCipher/Bird_images/Apodiformes4.png", "C:/BirdCipher/Bird_images/Apodiformes5.png", "C:/BirdCipher/Bird_images/Apodiformes6.png",
"C:/BirdCipher/Bird_images/Apodiformes7.png", "C:/BirdCipher/Bird_images/Apodiformes8.png", "C:/BirdCipher/Bird_images/Apodiformes9.png",
"C:/BirdCipher/Bird_images/Apodiformes10.png", "C:/BirdCipher/Bird_images/Apodiformes11.png", "C:/BirdCipher/Bird_images/Apodiformes12.png",
"C:/BirdCipher/Bird_images/Apodiformes13.png", "C:/BirdCipher/Bird_images/Apodiformes14.png", "C:/BirdCipher/Bird_images/Apodiformes15.png",
"C:/BirdCipher/Bird_images/Apodiformes16.png", "C:/BirdCipher/Bird_images/Apodiformes17.png", "C:/BirdCipher/Bird_images/Apodiformes18.png",
"C:/BirdCipher/Bird_images/Apodiformes19.png", "C:/BirdCipher/Bird_images/Apodiformes20.png", "C:/BirdCipher/Bird_images/Apodiformes21.png",
"C:/BirdCipher/Bird_images/Apodiformes22.png", "C:/BirdCipher/Bird_images/Apodiformes23.png", "C:/BirdCipher/Bird_images/Apodiformes24.png",
"C:/BirdCipher/Bird_images/Apodiformes25.png", "C:/BirdCipher/Bird_images/Apodiformes26.png", "C:/BirdCipher/Bird_images/Apodiformes27.png",
"C:/BirdCipher/Bird_images/Apodiformes28.png", "C:/BirdCipher/Bird_images/Apodiformes29.png", "C:/BirdCipher/Bird_images/Apodiformes30.png",
"C:/BirdCipher/Bird_images/Apodiformes31.png", "C:/BirdCipher/Bird_images/Apodiformes32.png", "C:/BirdCipher/Bird_images/Apodiformes33.png",
"C:/BirdCipher/Bird_images/Apodiformes34.png", "C:/BirdCipher/Bird_images/Apodiformes35.png", "C:/BirdCipher/Bird_images/Apodiformes36.png"],
["C:/BirdCipher/Bird_images/Phaethontiformes1.png", "C:/BirdCipher/Bird_images/Phaethontiformes2.png", "C:/BirdCipher/Bird_images/Phaethontiformes3.png",
"C:/BirdCipher/Bird_images/Phaethontiformes4.png", "C:/BirdCipher/Bird_images/Phaethontiformes5.png", "C:/BirdCipher/Bird_images/Phaethontiformes6.png",
"C:/BirdCipher/Bird_images/Phaethontiformes7.png", "C:/BirdCipher/Bird_images/Phaethontiformes8.png", "C:/BirdCipher/Bird_images/Phaethontiformes9.png",
"C:/BirdCipher/Bird_images/Phaethontiformes10.png", "C:/BirdCipher/Bird_images/Phaethontiformes11.png", "C:/BirdCipher/Bird_images/Phaethontiformes12.png",
"C:/BirdCipher/Bird_images/Phaethontiformes13.png", "C:/BirdCipher/Bird_images/Phaethontiformes14.png", "C:/BirdCipher/Bird_images/Phaethontiformes15.png",
"C:/BirdCipher/Bird_images/Phaethontiformes16.png", "C:/BirdCipher/Bird_images/Phaethontiformes17.png", "C:/BirdCipher/Bird_images/Phaethontiformes18.png",
"C:/BirdCipher/Bird_images/Phaethontiformes19.png", "C:/BirdCipher/Bird_images/Phaethontiformes20.png"], ["C:/BirdCipher/Bird_images/Eurypygiformes1.png",
"C:/BirdCipher/Bird_images/Eurypygiformes2.png", "C:/BirdCipher/Bird_images/Eurypygiformes3.png", "C:/BirdCipher/Bird_images/Eurypygiformes4.png",
"C:/BirdCipher/Bird_images/Eurypygiformes5.png", "C:/BirdCipher/Bird_images/Eurypygiformes6.png", "C:/BirdCipher/Bird_images/Eurypygiformes7.png",
"C:/BirdCipher/Bird_images/Eurypygiformes8.png", "C:/BirdCipher/Bird_images/Eurypygiformes9.png", "C:/BirdCipher/Bird_images/Eurypygiformes10.png",
"C:/BirdCipher/Bird_images/Eurypygiformes11.png", "C:/BirdCipher/Bird_images/Eurypygiformes12.png", "C:/BirdCipher/Bird_images/Eurypygiformes13.png"],
["C:/BirdCipher/Bird_images/Gaviiformes1.png", "C:/BirdCipher/Bird_images/Gaviiformes2.png", "C:/BirdCipher/Bird_images/Gaviiformes3.png",
"C:/BirdCipher/Bird_images/Gaviiformes4.png", "C:/BirdCipher/Bird_images/Gaviiformes5.png", "C:/BirdCipher/Bird_images/Gaviiformes6.png",
"C:/BirdCipher/Bird_images/Gaviiformes7.png", "C:/BirdCipher/Bird_images/Gaviiformes8.png", "C:/BirdCipher/Bird_images/Gaviiformes9.png",
"C:/BirdCipher/Bird_images/Gaviiformes10.png", "C:/BirdCipher/Bird_images/Gaviiformes11.png", "C:/BirdCipher/Bird_images/Gaviiformes12.png",
"C:/BirdCipher/Bird_images/Gaviiformes13.png", "C:/BirdCipher/Bird_images/Gaviiformes14.png", "C:/BirdCipher/Bird_images/Gaviiformes15.png",
"C:/BirdCipher/Bird_images/Gaviiformes16.png", "C:/BirdCipher/Bird_images/Gaviiformes17.png", "C:/BirdCipher/Bird_images/Gaviiformes18.png",
"C:/BirdCipher/Bird_images/Gaviiformes19.png", "C:/BirdCipher/Bird_images/Gaviiformes20.png"]]

number_species = [38, 55, 13, 8, 10, 457, 442, 23, 42, 441, 3, 20, 188, 39, 23, 4, 443, 622, 130, 8, 4, 20, 13, 541, 7, 3, 23]


#print(len(BirdCipher_list))