import _elementtree
import xml.etree.ElementTree as ET

def search_by_food(foodname):
    result = 0
    for canteen in root:
        count = 0
        for food in canteen:
            if foodname.lower() in food[0].text:
                name = food[0].text
                price = food[1].text
                if count == 0:
                    print(canteen.attrib)
                    print('-',name.title(),'($'+price+')')
                    count=1
                    result += 1
                else:
                    print('-',name.title(),'($'+price+')')
                    result += 1
    print("=> Total:",result,"results")
            

def search_by_price(max_price):
    result = 0
    for canteen in root:
        count = 0
        for food in canteen:
            if float(food[1].text) <= float(max_price):
                name = food[0].text
                price = food[1].text
                if count == 0:
                    print(canteen.attrib)
                    print('-',name.title(),'($'+price+')')
                    count=1
                    result += 1
                else:
                    print('-',name.title(),'($'+price+')')
                    result += 1
    print("=> Total:",result,"results")
                    
                
foodlist = ET.parse('foodlist_data.xml')
root = foodlist.getroot()
foodname = input("Enter the food you want: ")
search_by_food(foodname)
print()
max_price = input("Enter maximum price you want to pay: $")
search_by_price(max_price)
 

