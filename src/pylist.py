#Pylist V1
#Axel INGRAO
#GPL Licence

#Déclaration des imports
from controler.MenuControler import MenuControler
from interface.Terminal import Terminal

#Déclaration des variables globales
m_interface = Terminal()
m_menu = MenuControler(m_interface)

m_menu.__run__()